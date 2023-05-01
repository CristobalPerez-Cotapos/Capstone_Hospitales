from simulacion import Simulacion
import parametros_simulacion as ps
import random 
from paciente import Paciente
from estrategia import Estrategia
from simulador import Simulador

random.seed(ps.SEED)

estrategia = Estrategia(ps.PARAMETROS_ESTRATEGIA_PROVISORIOS)
simulacion = Simulador(estrategia)
simulacion.simular()

