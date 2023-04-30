from simulacion import Simulacion
import parametros_simulacion as ps
import random 
from paciente import Paciente
from estrategia import Estrategia

random.seed(ps.SEED)


simulacion = Simulacion(estrategia="estrategia")
simulacion.simular()

paciente = Paciente(1)
estrategia = Estrategia(ps.PARAMETROS_ESTRATEGIA_PROVISORIOS)
datos = simulacion.recopilar_informacion()["H_1"]
puntaje = estrategia.generar_punteje_paciente(paciente, datos, "H_1")
print(puntaje)