from simulacion import Simulacion
import parametros_simulacion as ps
import random 
from paciente import Paciente
from estrategia import Estrategia
from simulador import Simulador
#import respaldo as r
from abrir_json import Archivos as ar
from analisis_resultados import Analisis
import scipy.stats as st
import numpy as np
random.seed(ps.SEED)

# estrategia = Estrategia(ps.PARAMETROS_ESTRATEGIA_PROVISORIOS)
# simulacion = Simulador(estrategia)
# simulacion.simular_mejores_estrategias()
if __name__ == "__main__":
    estrategia = Estrategia(ps.PARAMETROS_ESTRATEGIA_PRINCIPALES, ps.PARAMETROS_ESTRATEGIA_SECUNDARIOS)
    simulacion = Simulador(estrategia)
    simulacion.simular()
# print(simulacion.capacidad_cama_por_simulacion)
# print(simulacion.costos_derivacion_simulacion)
# print(simulacion.costos_espera_WL_simulacion)
# print(simulacion.costos_muertos_hospitales_simulacion)

#simulacion = Simulacion(estrategia)
#simulacion.simular_miltiples_veces()

#print("Costo total: ", simulacion.promedio_resultados())

# estrategia_inicial = simulacion.estrategia_base
# mejor_estrategia = simulacion.mejor_estrategia
# analisis = Analisis(estrategia_inicial, mejor_estrategia)
# analisis.chequear_intervalo()
