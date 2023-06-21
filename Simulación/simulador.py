from simulacion import Simulacion
from estrategia import Estrategia
import parametros_simulacion as ps
import parametros_hospitales as ph
import random
from abrir_json import Archivos as ar
from threading import Thread
random.seed(ps.SEED)
from copy import deepcopy
import multiprocessing as mp
import pickle
import psutil

class Simulador:

    def __init__(self, estrategia_inicial):
        self.estrategia = estrategia_inicial
        self.simulaciones = []
        self.resultados_estrategias = {}
        self.estrategia_base = estrategia_inicial
        self.mejor_estrategia = estrategia_inicial
        self.simulacion_base = None
    def crear_simulacion(self):
        simulacion = Simulacion(self.estrategia)
        simulacion.simular_miltiples_veces()
        return simulacion

    def funcion_objetivo(self, simulacion):
        return simulacion.calcular_funcion_objetivo()
    
    def generar_nueva_estrategia(self, numero_iteraciones):
        aleatorio_mutacion_fuerte = random.random()
        if aleatorio_mutacion_fuerte < max(1/numero_iteraciones, 0.05):
            return (self.estrategia.mutar_estrategia_fuerte(), deepcopy(self.estrategia.parametros_secundarios))
        
        else:
            aleatorio = random.random()
            if aleatorio < 0.1:
                return (deepcopy(self.estrategia.parametros_estrategia), self.estrategia.mutar_parametros_secundarios())
            elif aleatorio < 0.2:
                return (self.estrategia.mutar_estrategia_debil(), deepcopy(self.estrategia.parametros_secundarios))
            elif aleatorio < 0.5:
                return (self.estrategia.mutar_estrategia_media_tipo_paciente(), deepcopy(self.estrategia.parametros_secundarios))
            elif aleatorio < 0.8:
                return (self.estrategia.mutar_estrategia_media_unidad(), deepcopy(self.estrategia.parametros_secundarios))
            else:
                return (self.estrategia.mutar_estrategia_media(), deepcopy(self.estrategia.parametros_secundarios))
        
    def simular(self):
        estrategias = []
        estrategias.append(self.estrategia)
        for i in range(ps.NUMERO_SIMULACIONES_PARALELAS - 1):
            estrtegia = self.generar_nueva_estrategia(numero_iteraciones = 1)
            estrtegia = Estrategia(estrtegia[0], estrtegia[1])
            estrategias.append(estrtegia)
        
        manager = mp.Manager()
        resultados_simulaciones = manager.list()
        simulaciones = [Simulacion(estrategia, resultados_simulaciones) for estrategia in estrategias]
        pool = mp.Pool(processes = ps.NUMERO_CORAZONES)
        

        pool.map(Simulacion.simular_miltiples_veces, simulaciones)
        resultados = list(resultados_simulaciones)
        for simulacion in resultados:
            if simulacion.estrategia.id == self.estrategia.id:
                self.simulacion_base = simulacion
            self.simulaciones.append(simulacion)
        

        self.simulaciones = sorted(self.simulaciones, key=lambda x: x.promedio_resultados())
        print(f"Funcion objetivo: {self.simulaciones[0].promedio_resultados()} iteracion 0")
        self.mejor_estrategia = self.simulaciones[0]
        mejor_valor = self.simulaciones[0].promedio_resultados()
        
        for i in range(ps.NUMERO_ITERACIONES):
            lista_estrategias = []
            random.seed(ps.SEED * (i + 1))
            for j in range(ps.NUMERO_SIMULACIONES_MEZCLA):
                nuva_estrategia = self.mezclar_estrategias(self.simulaciones[j].estrategia.parametros_estrategia, self.simulaciones[j+1].estrategia.parametros_estrategia)
                parametros_secundarios = self.simulaciones[j].estrategia.parametros_secundarios if random.random() < 0.5 else self.simulaciones[j+1].estrategia.parametros_secundarios
                nuva_estrategia = Estrategia(nuva_estrategia, parametros_secundarios)
                lista_estrategias.append(nuva_estrategia)
            
            for j in range(ps.NUMERO_SIMULACIONES_MEZCLA, ps.NUMERO_SIMULACIONES_PARALELAS):
                if i != 0:
                    if j <= 3:
                        estrtegia = self.generar_nueva_estrategia(numero_iteraciones = i + 1)
                    elif j <= 5:
                        self.estrategia = estrategia2
                        estrtegia = self.generar_nueva_estrategia(numero_iteraciones = i + 1)
                    else:
                        self.estrategia = estrategia3
                        estrtegia = self.generar_nueva_estrategia(numero_iteraciones = i + 1)
                else:
                    estrtegia = self.generar_nueva_estrategia(numero_iteraciones = i + 1)
                estrtegia = Estrategia(estrtegia[0], estrtegia[1])
                lista_estrategias.append(estrtegia)
            
            manager = mp.Manager()
            resultados_simulaciones = manager.list()
            simulaciones = [Simulacion(estrategia, resultados_simulaciones) for estrategia in lista_estrategias]
            pool = mp.Pool(processes = ps.NUMERO_CORAZONES)
            pool.map(Simulacion.simular_miltiples_veces, simulaciones)
            resultados = list(resultados_simulaciones)
            lista_simulaciones = []
            for simulacion in resultados:
                self.simulaciones.append(simulacion)
                lista_simulaciones.append(simulacion)

            self.simulaciones = sorted(self.simulaciones, key=lambda x: x.promedio_resultados())
            lista_simulaciones = sorted(lista_simulaciones, key=lambda x: x.promedio_resultados())
            self.estrategia = lista_simulaciones[0].estrategia
            num1 = random.randint(0,5)
            num2 = random.randint(0,5)
            estrategia2 = lista_simulaciones[num1].estrategia
            estrategia3 = lista_simulaciones[num2].estrategia
            #for i in self.estrategia.parametros_estrategia: 
            #    print(self.estrategia.parametros_estrategia[i])
            if self.simulaciones[0].promedio_resultados() < mejor_valor:
                print("Mejor estrategia encontrada")
                print(f"id: {self.simulaciones[0].estrategia.id}")
                mejor_valor = self.simulaciones[0].promedio_resultados()
                self.mejor_diccionario_estrategia = deepcopy(self.simulaciones[0].estrategia.parametros_estrategia)
                self.mejores_parametros_secundarios = deepcopy(self.simulaciones[0].estrategia.parametros_secundarios)
                self.estrategia = Estrategia(self.mejor_diccionario_estrategia, self.mejores_parametros_secundarios)
                self.mejor_estrategia = self.simulaciones[0]
            print(f"Funcion objetivo: {mejor_valor} iteracion {i + 1} id estrategia {self.estrategia.id}\n")
            if i % 10 == 0:
                lista_KPIs = ["Costos jornada", "Costos muertos", "Costos derivaciones", "Costos espera WL", "Costos traslados" ,"Derivaciones", "Espera WL", "Pacientes esperando", "Tasas ocupación"]
                self.resultados_estrategias = {}
                mejores_resultados = []
                mejores_estrategias = []
                i = 0
                while len(mejores_resultados) < 10 and i < len(self.simulaciones):
                    if self.simulaciones[i].promedio_resultados() not in mejores_resultados:
                        mejores_resultados.append(self.simulaciones[i].promedio_resultados())
                        mejores_estrategias.append(self.simulaciones[i])
                    i += 1

                for j in range(len(mejores_estrategias)):
                    diccionario_auxiliar = {kpi : {f"Simulación {n+1}" : 0 for n in range(ps.SIMULACIONES_POR_ESTRATEGIA)} for kpi in lista_KPIs}
                    for i in range (1, ps.SIMULACIONES_POR_ESTRATEGIA + 1):
                        for kpi in lista_KPIs:
                            diccionario_auxiliar[kpi][f"Simulación {i}"] = mejores_estrategias[j].diccionario_resultados[f"Simulación {i}"][kpi]

                    self.resultados_estrategias[f"Estrategia {mejores_estrategias[j].estrategia.id}"] = {kpi : diccionario_auxiliar[kpi] for kpi in lista_KPIs}
                diccionario_auxiliar = {kpi : {f"Simulación {n+1}" : 0 for n in range(ps.SIMULACIONES_POR_ESTRATEGIA)} for kpi in lista_KPIs}
                for i in range (1, ps.SIMULACIONES_POR_ESTRATEGIA + 1):
                    for kpi in lista_KPIs:
                        diccionario_auxiliar[kpi][f"Simulación {i}"] = self.simulacion_base.diccionario_resultados[f"Simulación {i}"][kpi]
                diccionario_estrategias = {}
                diccionario_estrategias[f"Estrategia Inicial"] = {"Parametros principales" : ph.PARAMETROS_ESTRATEGIA_PRINCIPALES, "Parametros secundarios" : ps.PARAMETROS_ESTRATEGIA_SECUNDARIOS}
                for simulacion_e in mejores_estrategias:
                    diccionario_estrategias[f"Estrategia {simulacion_e.estrategia.id}"] = {"Parametros principales" : simulacion_e.estrategia.parametros_estrategia, "Parametros secundarios" : simulacion_e.estrategia.parametros_secundarios} 
                
                ar("None").guardar_resultados(self.resultados_estrategias, "anda.json")   # guarda los resultados de las mejores estrategias
                ar("None").guardar_resultados(diccionario_estrategias, "anda2.json")   # guarda las mejores estrategias en un diccionario
                print(f"Funcion objetivo: {mejor_valor}")
                
        lista_KPIs = ["Costos jornada", "Costos muertos", "Costos derivaciones", "Costos espera WL", "Costos traslados" ,"Derivaciones", "Espera WL", "Pacientes esperando", "Tasas ocupación"]
        self.resultados_estrategias = {}
        mejores_resultados = []
        mejores_estrategias = []
        i = 0
        while len(mejores_resultados) < 10 and i < len(self.simulaciones):
            if self.simulaciones[i].promedio_resultados() not in mejores_resultados:
                mejores_resultados.append(self.simulaciones[i].promedio_resultados())
                mejores_estrategias.append(self.simulaciones[i])
            i += 1

        for j in range(len(mejores_estrategias)):
            diccionario_auxiliar = {kpi : {f"Simulación {n+1}" : 0 for n in range(ps.SIMULACIONES_POR_ESTRATEGIA)} for kpi in lista_KPIs}
            for i in range (1, ps.SIMULACIONES_POR_ESTRATEGIA + 1):
                for kpi in lista_KPIs:
                    diccionario_auxiliar[kpi][f"Simulación {i}"] = mejores_estrategias[j].diccionario_resultados[f"Simulación {i}"][kpi]

            self.resultados_estrategias[f"Estrategia {mejores_estrategias[j].estrategia.id}"] = {kpi : diccionario_auxiliar[kpi] for kpi in lista_KPIs}
        diccionario_auxiliar = {kpi : {f"Simulación {n+1}" : 0 for n in range(ps.SIMULACIONES_POR_ESTRATEGIA)} for kpi in lista_KPIs}
        for i in range (1, ps.SIMULACIONES_POR_ESTRATEGIA + 1):
            for kpi in lista_KPIs:
                diccionario_auxiliar[kpi][f"Simulación {i}"] = self.simulacion_base.diccionario_resultados[f"Simulación {i}"][kpi]
        diccionario_estrategias = {}
        diccionario_estrategias[f"Estrategia Inicial"] = {"Parametros principales" : ph.PARAMETROS_ESTRATEGIA_PRINCIPALES, "Parametros secundarios" : ps.PARAMETROS_ESTRATEGIA_SECUNDARIOS}
        for simulacion_e in mejores_estrategias:
            diccionario_estrategias[f"Estrategia {simulacion_e.estrategia.id}"] = {"Parametros principales" : simulacion_e.estrategia.parametros_estrategia, "Parametros secundarios" : simulacion_e.estrategia.parametros_secundarios} 
        
        ar("None").guardar_resultados(self.resultados_estrategias, "anda.json")   # guarda los resultados de las mejores estrategias
        ar("None").guardar_resultados(diccionario_estrategias, "anda2.json")   # guarda las mejores estrategias en un diccionario
        print(f"Funcion objetivo: {mejor_valor}")
        

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

        




