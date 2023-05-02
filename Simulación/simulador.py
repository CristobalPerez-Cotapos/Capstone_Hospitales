from simulacion import Simulacion
from estrategia import Estrategia
import parametros_simulacion as ps
import random
from threading import Thread
random.seed(ps.SEED)

class Simulador:

    def __init__(self, estrategia_inicial):
        self.estrategia = estrategia_inicial
        self.simulaciones = []

    def crear_simulacion(self):
        simulacion = Simulacion(self.estrategia)
        simulacion.simular()
        return simulacion

    def funcion_objetivo(self, simulacion):
        return simulacion.calcular_funcion_objetivo()
    
    def generar_nueva_estrategia(self, simulacion):
        if random.random() < 0.1:
            return simulacion.estrategia.mutar_estrategia_fuerte()
        return simulacion.estrategia.mutar_estrategia_debil()
    
    def simular(self):
        lista_threads = []
        simulacion = self.crear_simulacion()
        self.simulaciones.append(simulacion)
        for i in range(ps.NUMERO_SIMULACIONES_PARALELAS):
            estrtegia = self.generar_nueva_estrategia(simulacion)
            estrtegia = Estrategia(estrtegia)
            simulacion = Simulacion(estrtegia)
            self.simulaciones.append(simulacion)
            thread = Thread(target=simulacion.simular)
            thread.start()
            lista_threads.append(thread)
        for thread in lista_threads:
            thread.join()
        sorted(self.simulaciones, key=lambda x: x.calcular_funcion_objetivo(), reverse=True)
        print(f"Funcion objetivo: {self.simulaciones[0].calcular_funcion_objetivo()}")
        mejor_valor = self.simulaciones[0].calcular_funcion_objetivo()

        for i in range(1000):
            lista_threads = []
            for j in range(5):
                nuva_estrategia = self.mezclar_estrategias(self.simulaciones[j].estrategia.parametros_estrategia, self.simulaciones[j+1].estrategia.parametros_estrategia)
                nuva_estrategia = Estrategia(nuva_estrategia)
                simulacion = Simulacion(nuva_estrategia)
                self.simulaciones[j] = simulacion
                thread = Thread(target=simulacion.simular)
                thread.start()
                lista_threads.append(thread)
            for j in range(5, ps.NUMERO_SIMULACIONES_PARALELAS):
                estrtegia = self.generar_nueva_estrategia(simulacion)
                estrtegia = Estrategia(estrtegia)
                simulacion = Simulacion(estrtegia)
                self.simulaciones[j] = simulacion
                thread = Thread(target=simulacion.simular)
                thread.start()
                lista_threads.append(thread)
            for thread in lista_threads:
                thread.join()

            sorted(self.simulaciones, key=lambda x: x.calcular_funcion_objetivo())
            print(f"Funcion objetivo: {mejor_valor} iteracion {i}")
            if self.simulaciones[0].calcular_funcion_objetivo() < mejor_valor:
                mejor_valor = self.simulaciones[0].calcular_funcion_objetivo()
                self.estrategia = self.simulaciones[0].estrategia

        print(f"Funcion objetivo: {mejor_valor}")
        print(self.estrategia.parametros_estrategia)

    def mezclar_estrategias(self, estrategia1, estrategia2):
        nueva_estrategia = {}
        for key in estrategia1:
            if random.random() <= 0.5:
                nueva_estrategia[key] = estrategia1[key]
            else:
                nueva_estrategia[key] = estrategia2[key]
        return nueva_estrategia




