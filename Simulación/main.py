from simulacion import Simulacion
import parametros_simulacion as ps
import random 
from paciente import Paciente
from estrategia import Estrategia
from simulador import Simulador
from cargar_datos import leer_parametros
from funciones import Archivos as ar
from analisis_resultados import Analisis
random.seed(ps.SEED)

# estrategia = Estrategia(ps.PARAMETROS_ESTRATEGIA_PROVISORIOS)
# simulacion = Simulador(estrategia)
# simulacion.simular_mejores_estrategias()


estrategia = Estrategia(ar('None').leer_estrategias()["Estrategia 243"])
simulacion = Simulacion(estrategia)
simulacion.simular()
print(simulacion.costos_muertos_hospitales)
#simulacion = Simulacion(estrategia)
#simulacion.simular_miltiples_veces()

#print("Costo total: ", simulacion.promedio_resultados())



# estrategia_inicial = simulacion.estrategia_base
# mejor_estrategia = simulacion.mejor_estrategia
# analisis = Analisis(estrategia_inicial, mejor_estrategia)
# analisis.chequear_intervalo()
