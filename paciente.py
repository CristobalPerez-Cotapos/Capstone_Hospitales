from abc import ABC, abstractmethod
from random import uniform
from probabilidades_transicion import PROBABILIDADES_DE_TRANSICION

class Paciente(ABC):

    id = 0

    def __init__(self, grupo_diagnostico: int):
        super().__init__()
        self.id = Paciente.id
        Paciente.id += 1
        self.grupo_diagnostico = grupo_diagnostico
        self.tiempo_esperado = 0
        self.ruta_paciente = []
        self.definir_ruta_paciente()

    @abstractmethod
    def definir_ruta_paciente(self):
        pass

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

class PacienteWL(Paciente):

    def __init__(self, grupo_diagnostico: str):
        super().__init__(grupo_diagnostico)

    def definir_ruta_paciente(self):
        self.ruta_paciente = ["GA"]
        while self.ruta_paciente[-1] != "FIN":
            self.agregar_elemento_ruta()

class PacienteED(Paciente):

    def __init__(self, grupo_diagnostico: str):
        super().__init__(grupo_diagnostico)

    def definir_ruta_paciente(self):
        self.ruta_paciente = ["ED"]
        while self.ruta_paciente[-1] != "FIN":
            self.agregar_elemento_ruta()

if __name__ == "__main__":
    for i in range(100):
        paciente = PacienteED(4)
        print(paciente.id, paciente.ruta_paciente)
