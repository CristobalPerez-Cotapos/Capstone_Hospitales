from simulacion import Simulacion
from estrategia import Estrategia
import parametros_simulacion as ps
import random
random.seed(ps.SEED)

class Simulador:

    def __init__(self, estrategia_inicial):
        self.estrategia = estrategia_inicial

    def crear_simulacion(self):
        simulacion = Simulacion(self.estrategia)
        simulacion.simular()
        return simulacion

    def funcion_objetivo(self, simulacion):
        return simulacion.calcular_funcion_objetivo()
    
    def generar_nueva_estrategia(self, simulacion):
        return simulacion.estrategia.mutar_estrategia()
    
    def simular(self):
        simulacion = self.crear_simulacion()
        funcion_objetivo = self.funcion_objetivo(simulacion)
        for i in range(10000):
            nueva_estrategia = self.generar_nueva_estrategia(simulacion)
            nueva_estrategia = Estrategia(nueva_estrategia)
            nueva_simulacion = Simulacion(nueva_estrategia)
            nueva_simulacion.simular()
            nueva_funcion_objetivo = self.funcion_objetivo(nueva_simulacion)
            if nueva_funcion_objetivo < funcion_objetivo:
                simulacion = nueva_simulacion
                funcion_objetivo = nueva_funcion_objetivo
            
            print(f"Simulacion {i+1} de 100")
            print(f"Funcion objetivo: {funcion_objetivo}")


