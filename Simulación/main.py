from simulacion import Simulacion
import parametros_simulacion as ps
import random 

random.seed(ps.SEED)


simulacion = Simulacion(estrategia="estrategia")
simulacion.simular()