from random import uniform, randint, seed
from parametros_hospitales import PROBABILIDADES_DE_TRANSICION
import parametros_simulacion as ps

seed(ps.SEED)

class Paciente():

    id = 0

    def __init__(self, grupo_diagnostico: int):
        super().__init__()
        self.id = Paciente.id
        Paciente.id += 1
        self.grupo_diagnostico = grupo_diagnostico
        self.tiempo_esperado = 0
        self.ruta_paciente = []
        self.definir_ruta_paciente()
        self.tiempo_antencion_unidad_actual = 0

    def definir_ruta_paciente(self):
        if self.grupo_diagnostico >= 5:
            self.ruta_paciente = ["WL", "GA"]
        else:
            self.ruta_paciente = ["ED"]
        while self.ruta_paciente[-1] != "FIN":
            self.agregar_elemento_ruta()
        
    def agregar_elemento_ruta(self):
        azar = uniform(0, 100)
        probabilidades = PROBABILIDADES_DE_TRANSICION[self.grupo_diagnostico][self.ruta_paciente[-1]]
        probabilidad_acumulada = 0
        for i in probabilidades:
            probabilidad_acumulada += probabilidades[i]
            if azar <= probabilidad_acumulada:
                self.ruta_paciente.append(i)
                break

    def __str__(self):
        return f"Paciente {self.id} (grupo {self.grupo_diagnostico})"
    
if __name__ == "__main__":
    for i in range(101):
        grupo = randint(1, 8)
        paciente = Paciente(grupo)
        print(paciente, paciente.ruta_paciente)
