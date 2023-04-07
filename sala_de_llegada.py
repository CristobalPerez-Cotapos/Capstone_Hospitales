from abc import ABC, abstractmethod

class SalaDeLLegada(ABC):

    def __init__(self):
        super().__init__()
        self.pacientes = []

    @abstractmethod
    def agregar_paciente(self, paciente):
        pass

    @abstractmethod
    def __str__(self):
        pass

class AdmisionGeneral(SalaDeLLegada):

    def __init__(self):
        super().__init__()

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    
class Urgencias(SalaDeLLegada):

    def __init__(self):
        super().__init__()

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)