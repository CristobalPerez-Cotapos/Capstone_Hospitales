from simulacion import Simulacion
from estrategia import Estrategia
import parametros_simulacion as ps
import random
from funciones import Archivos as ar
from threading import Thread
random.seed(ps.SEED)
from copy import deepcopy
import multiprocessing as mp
import pickle
import dill as pickle


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
        self.derivaciones_estrategias = {}
        self.espera_WL_estrategias = {}
        self.costos_muertos_hospitales_diarios_estrategias = {}
        self.pacientes_atendidos_estrategias = {}
        self.estrategia_base = estrategia_inicial
        self.mejor_estrategia = estrategia_inicial
        self.resultados = []
    def crear_simulacion(self):
        simulacion = Simulacion(self.estrategia)
        simulacion.simular_miltiples_veces()
        return simulacion

    def funcion_objetivo(self, simulacion):
        return simulacion.calcular_funcion_objetivo()
    
    def generar_nueva_estrategia(self):
        aleatorio = random.random()
        if aleatorio < 0.95:
            return self.estrategia.mutar_estrategia_fuerte()
        elif aleatorio < 0.98:
            return self.estrategia.mutar_estrategia_muy_debil()
        elif aleatorio < 0.99:
            return self.estrategia.mutar_estrategia_media()
        return self.estrategia.mutar_estrategia_debil()
    
    def simular(self):
        lista_threads = []
        #simulacion = self.crear_simulacion()
        #print(f"Funcion objetivo: {simulacion.promedio_resultados()} solucion original")
        #self.estrategia_base = simulacion
        #self.simulaciones.append(simulacion)
        estrategias = []
        estrategias.append(self.estrategia)
        procesos = []
        for i in range(ps.NUMERO_SIMULACIONES_PARALELAS - 1):
            estrtegia = self.generar_nueva_estrategia()
            estrtegia = Estrategia(estrtegia)
            estrategias.append(estrtegia)
            # simulacion = Simulacion(estrtegia)
            # self.simulaciones.append(simulacion)
        manager = mp.Manager()
        resultados_compartidos = manager.list()
        simulaciones = [Simulacion(estrategia, resultados_compartidos) for estrategia in estrategias]
        pool = mp.Pool(processes = ps.NUMERO_SIMULACIONES_PARALELAS)
        self.simulaciones = pool.map(Simulacion.simular_miltiples_veces, simulaciones)
        resultados = list(resultados_compartidos)
        self.simulaciones = sorted(resultados, key=lambda x: x.promedio_resultados())
        for simulacion in self.simulaciones:
            print(simulacion.promedio_resultados())
        pool.close()
        pool.join()
                       
        #     thread = Thread(target=simulacion.simular_miltiples_veces)
        #     thread.start()
        #     lista_threads.append(thread)
        # for thread in lista_threads:
        #     thread.join()

        self.simulaciones = sorted(self.simulaciones, key=lambda x: x.promedio_resultados())
        print(f"Funcion objetivo: {self.simulaciones[0].promedio_resultados()} iteracion 0")
        self.mejor_estrategia = self.simulaciones[0]
        mejor_valor = self.simulaciones[0].promedio_resultados()

        # for i in range(15):
        #     lista_threads = []
        #     for j in range(3):
        #         nuva_estrategia = self.mezclar_estrategias(self.simulaciones[j].estrategia.parametros_estrategia, self.simulaciones[j+1].estrategia.parametros_estrategia)
        #         nuva_estrategia = Estrategia(nuva_estrategia)
        #         simulacion = Simulacion(nuva_estrategia)
        #         self.simulaciones[j] = simulacion
        #         thread = Thread(target=simulacion.simular_miltiples_veces)
        #         thread.start()
        #         lista_threads.append(thread)
        #     for j in range(3, ps.NUMERO_SIMULACIONES_PARALELAS):
        #         estrtegia = self.generar_nueva_estrategia()
        #         estrtegia = Estrategia(estrtegia)
        #         simulacion = Simulacion(estrtegia)
        #         self.simulaciones[j] = simulacion
        #         thread = Thread(target=simulacion.simular_miltiples_veces)
        #         thread.start()
        #         lista_threads.append(thread)
        #     for thread in lista_threads:
        #         thread.join()

        #     self.simulaciones = sorted(self.simulaciones, key=lambda x: x.promedio_resultados())
        #     print(f"Funcion objetivo: {mejor_valor} iteracion {i + 1} id estrategia {self.estrategia.id}\n")
        #     #for i in self.estrategia.parametros_estrategia:
        #     #    print(self.estrategia.parametros_estrategia[i])
        #     if self.simulaciones[0].promedio_resultados() < mejor_valor:
        #         mejor_valor = self.simulaciones[0].promedio_resultados()
        #         self.mejor_diccionario_estrategia = deepcopy(self.simulaciones[0].estrategia.parametros_estrategia)
        #         self.estrategia = Estrategia(self.mejor_diccionario_estrategia)
    

        # for i in range (len(self.simulaciones)):
        #     self.capacidades_camas_iteraciones[f"Estrategia {self.simulaciones[i].estrategia.id}"] = self.simulaciones[i].capacidades_camas
        #     self.funciones_objetivos_estrategias[f"Estrategia {self.simulaciones[i].estrategia.id}"] = self.simulaciones[i].funciones_objetivos
        #     self.capacidades_promedio_camas[f"Estrategia {self.simulaciones[i].estrategia.id}"] = self.simulaciones[i].promedio_capacidades
        #     self.costos_muertos_hospitales_estrategias[f"Estrategia {self.simulaciones[i].estrategia.id}"] = self.simulaciones[i].costos_muertos_hospitales_simulacion
        #     self.costos_muertos_WL_estrategias[f"Estrategia {self.simulaciones[i].estrategia.id}"] = self.simulaciones[i].costos_espera_WL_simulacion
        #     self.costos_derivaciones_estrategias[f"Estrategia {self.simulaciones[i].estrategia.id}"] = self.simulaciones[i].costos_derivacion_simulacion
        # diccionario_estrategias = {}
        # diccionario_estrategias[f"Estrategia Inicial"] = ps.PARAMETROS_ESTRATEGIA_PROVISORIOS
        # for simulacion_e in self.simulaciones[:5]:
        #     diccionario_estrategias[f"Estrategia {simulacion_e.estrategia.id}"] = simulacion_e.estrategia.parametros_estrategia
        
        # ar("None").guardar_resultados(diccionario_estrategias, "estrategias.json")   # guarda las mejores estrategias en un diccionario
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

    def simular_mejores_estrategias(self):
        diccionario_estrategias = ar("None").leer_estrategias()
        lista_threads = []
        simulaciones = []
        for key in diccionario_estrategias.keys():
            estrategia = Estrategia(diccionario_estrategias[key])
            simulacion = Simulacion(estrategia)
            simulaciones.append(simulacion)
            thread = Thread(target=simulacion.simular_mejores_estrategias_multiples_veces)
            thread.start()
            lista_threads.append(thread)
        for thread in lista_threads:
            thread.join()

        for i in range (len(simulaciones)):
            self.costos_muertos_hospitales_diarios_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].costos_muertos_hospitales_diarios_simulacion
            self.espera_WL_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].espera_WL
            self.derivaciones_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].derivaciones
            self.pacientes_atendidos_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].pacientes_esperando

        
        diccionario = {}
        diccionario['Costos muertos diarios'] = self.costos_muertos_hospitales_diarios_estrategias
        diccionario['Espera WL'] = self.espera_WL_estrategias
        diccionario['Derivaciones'] = self.derivaciones_estrategias
        diccionario['Pacientes esperando'] = self.pacientes_atendidos_estrategias


        diccionario_resultados = {}

        for i in range (len(simulaciones)):
            self.capacidades_camas_iteraciones[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].capacidades_camas
            self.funciones_objetivos_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].funciones_objetivos
            self.capacidades_promedio_camas[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].promedio_capacidades
            self.costos_muertos_hospitales_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].costos_muertos_hospitales_simulacion
            self.costos_muertos_WL_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].costos_espera_WL_simulacion
            self.costos_derivaciones_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].costos_derivacion_simulacion

        diccionario_resultados['Capacidades promedio camas'] = self.capacidades_promedio_camas
        diccionario_resultados['Función objetivo'] = self.funciones_objetivos_estrategias
        diccionario_resultados['Costos muertos WL'] = self.costos_muertos_WL_estrategias
        diccionario_resultados['Costos muertos hospitales'] = self.costos_muertos_hospitales_estrategias
        diccionario_resultados['Costos derivaciones'] = self.costos_derivaciones_estrategias


        cambio_politica = True             # IMPORTANTE: Este valor lo cambiamos entre True y False dependiendo de si estamos simulando las mejores estrategias o estamos viendo el cambio de política con estas

        if not cambio_politica:
            ar('None').guardar_resultados(diccionario, "resultados_diarios_estrategias.json")
            ar('None').guardar_resultados(diccionario_resultados, "resultados_estrategias.json")
        
        else:
            ar('None').guardar_resultados(diccionario, "resultados_cambio_politica_diarios.json")
            ar('None').guardar_resultados(diccionario_resultados, "resultados_cambio_politica.json")
            
        # ar('None').guardar_resultados(diccionario, "resultados_estrategias.json")   #### guarda los resultados de las mejores estrategias

    # def simular_cambio_politicas(self):
    #     diccionario_estrategias = ar("None").leer_estrategias()
    #     lista_threads = []
    #     simulaciones = []
    #     for key in diccionario_estrategias.keys():
    #         estrategia = Estrategia(diccionario_estrategias[key])
    #         simulacion = Simulacion(estrategia)
    #         simulaciones.append(simulacion)
    #         thread = Thread(target=simulacion.simular_mejores_estrategias_multiples_veces)
    #         thread.start()
    #         lista_threads.append(thread)
    #     for thread in lista_threads:
    #         thread.join()

    #     for i in range (len(simulaciones)):
    #         self.costos_muertos_hospitales_diarios_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].costos_muertos_hospitales_diarios_simulacion
    #         self.espera_WL_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].espera_WL
    #         self.derivaciones_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].derivaciones
    #         self.pacientes_atendidos_estrategias[f"Estrategia {simulaciones[i].estrategia.id}"] = simulaciones[i].pacientes_esperando

        
    #     diccionario = {}
    #     diccionario['Costos muertos diarios'] = self.costos_muertos_hospitales_diarios_estrategias
    #     diccionario['Espera WL'] = self.espera_WL_estrategias
    #     diccionario['Derivaciones'] = self.derivaciones_estrategias
    #     diccionario['Pacientes esperando'] = self.pacientes_atendidos_estrategias
    #     ar('None').guardar_resultados(diccionario, 'resultados_cambio_politica_diarios.json')

        




