from simulacion import Simulacion
from estrategia import Estrategia
import parametros_simulacion as ps
import random
from threading import Thread
random.seed(ps.SEED)
from copy import deepcopy

class Simulador:

    def __init__(self, estrategia_inicial):
        self.estrategia = estrategia_inicial
        self.simulaciones = []
        self.capacidades_camas_iteraciones = {}
        self.funciones_objetivos_estrategias = {}
        self.capacidades_promedio_camas = {}
        self.costos_muertos_hospitales_estrategias = {}
        self.costos_muertos_WL_estrategias = {}
        self.costos_derivaciones_estrategias = {}
        self.estrategia_base = estrategia_inicial
        self.mejor_estrategia = estrategia_inicial

    def crear_simulacion(self):
        simulacion = Simulacion(self.estrategia)
        simulacion.simular_miltiples_veces()
        return simulacion

    def funcion_objetivo(self, simulacion):
        return simulacion.calcular_funcion_objetivo()
    
    def generar_nueva_estrategia(self):
        aleatorio = random.random()
        if aleatorio < 0.15:
            return self.estrategia.mutar_estrategia_fuerte()
        elif aleatorio < 0.4:
            return self.estrategia.mutar_estrategia_muy_debil()
        elif aleatorio < 0.8:
            return self.estrategia.mutar_estrategia_media()
        return self.estrategia.mutar_estrategia_debil()
    
    def simular(self):
        lista_threads = []
        simulacion = self.crear_simulacion()
        #print(f"Funcion objetivo: {simulacion.promedio_resultados()} solucion original")
        self.estrategia_base = simulacion
        self.simulaciones.append(simulacion)
        for i in range(ps.NUMERO_SIMULACIONES_PARALELAS):
            estrtegia = self.generar_nueva_estrategia()
            estrtegia = Estrategia(estrtegia)
            simulacion = Simulacion(estrtegia)
            self.simulaciones.append(simulacion)
            thread = Thread(target=simulacion.simular_miltiples_veces)
            thread.start()
            lista_threads.append(thread)
        for thread in lista_threads:
            thread.join()
        for i in range (len(self.simulaciones)):
            self.capacidades_camas_iteraciones[f"Estrategia {i}"] = self.simulaciones[i].capacidades_camas
            self.funciones_objetivos_estrategias[f"Estrategia {i}"] = self.simulaciones[i].funciones_objetivos
            self.capacidades_promedio_camas[f"Estrategia {i}"] = self.simulaciones[i].promedio_capacidades
            self.costos_muertos_hospitales_estrategias[f"Estrategia {i}"] = self.simulaciones[i].costos_muertos_hospitales_simulacion
            self.costos_muertos_WL_estrategias[f"Estrategia {i}"] = self.simulaciones[i].costos_espera_WL_simulacion
            self.costos_derivaciones_estrategias[f"Estrategia {i}"] = self.simulaciones[i].costos_derivacion_simulacion

            
        self.simulaciones = sorted(self.simulaciones, key=lambda x: x.promedio_resultados())
        print(f"Funcion objetivo: {self.simulaciones[0].promedio_resultados()} iteracion 0")
        self.mejor_estrategia = self.simulaciones[0]
        mejor_valor = self.simulaciones[0].promedio_resultados()

        for i in range(0):
            lista_threads = []
            for j in range(3):
                nuva_estrategia = self.mezclar_estrategias(self.simulaciones[j].estrategia.parametros_estrategia, self.simulaciones[j+1].estrategia.parametros_estrategia)
                nuva_estrategia = Estrategia(nuva_estrategia)
                simulacion = Simulacion(nuva_estrategia)
                self.simulaciones[j] = simulacion
                thread = Thread(target=simulacion.simular_miltiples_veces)
                thread.start()
                lista_threads.append(thread)
            for j in range(3, ps.NUMERO_SIMULACIONES_PARALELAS):
                estrtegia = self.generar_nueva_estrategia()
                estrtegia = Estrategia(estrtegia)
                simulacion = Simulacion(estrtegia)
                self.simulaciones[j] = simulacion
                thread = Thread(target=simulacion.simular_miltiples_veces)
                thread.start()
                lista_threads.append(thread)
            for thread in lista_threads:
                thread.join()

            self.simulaciones = sorted(self.simulaciones, key=lambda x: x.promedio_resultados())
            print(f"Funcion objetivo: {mejor_valor} iteracion {i + 1} id estrategia {self.estrategia.id}\n")
            #for i in self.estrategia.parametros_estrategia:
            #    print(self.estrategia.parametros_estrategia[i])
            if self.simulaciones[0].promedio_resultados() < mejor_valor:
                mejor_valor = self.simulaciones[0].promedio_resultados()
                self.mejor_diccionario_estrategia = deepcopy(self.simulaciones[0].estrategia.parametros_estrategia)
                self.estrategia = Estrategia(self.mejor_diccionario_estrategia)

        # print(f"Funcion objetivo: {mejor_valor}")
        # print(self.estrategia.parametros_estrategia)

    def mezclar_estrategias(self, estrategia1, estrategia2):
        nueva_estrategia = {}
        for key in estrategia1:
            if random.random() <= 0.5:
                nueva_estrategia[key] = deepcopy(estrategia1[key])
            else:
                nueva_estrategia[key] = deepcopy(estrategia2[key])
        return nueva_estrategia




