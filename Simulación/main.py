from simulacion import Simulacion
import parametros_simulacion as ps
import random 
from paciente import Paciente
from estrategia import Estrategia
from simulador import Simulador
import respaldo as r
from cargar_datos import leer_parametros
from funciones import Archivos as ar
from analisis_resultados import Analisis
import scipy.stats as st
import numpy as np
import multiprocessing as mp
random.seed(ps.SEED)

# estrategia = Estrategia(ps.PARAMETROS_ESTRATEGIA_PROVISORIOS)
# simulacion = Simulador(estrategia)
# simulacion.simular_mejores_estrategias()


if __name__ == "__main__":
    estrategia = Estrategia(ps.PARAMETROS_ESTRATEGIA_PROVISORIOS)
    simulacion = Simulador(estrategia)
    simulacion.simular()
















    # lista_estrategias = []
    # estrategia = Estrategia(ps.PARAMETROS_ESTRATEGIA_PROVISORIOS)
    # simulador = Simulador(estrategia)
    # lista_estrategias.append(estrategia)
    # for i in range(15):
    #     estrategia = simulador.generar_nueva_estrategia()
    #     estrategia = Estrategia(estrategia)
    #     lista_estrategias.append(estrategia)
    # manager = mp.Manager()
    # resultados_compartidos = manager.list()
    # simulaciones = [Simulacion(estrategia, resultados_compartidos) for estrategia in lista_estrategias]
    # pool = mp.Pool(processes=16)
    # pool.map(Simulacion.simular_miltiples_veces, simulaciones)
    # resltados = list(resultados_compartidos)
    # simulaciones = sorted(resltados, key=lambda x: x.promedio_resultados())
    # for simulacion in simulaciones:
    #     print(simulacion.promedio_resultados())
    # pool.close()
    # pool.join()


# simulacion = Simulador(estrategia)
# simulacion.simular()
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
