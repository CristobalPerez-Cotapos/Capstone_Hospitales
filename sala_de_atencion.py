from abc import ABC, abstractmethod

class SalaDeAtencion(ABC):

    def __init__(self):
        super().__init__()
        self.pacientes = []
        self.pacientes_atendidos = []

    @abstractmethod
    def agregar_paciente(self, paciente):
        pass

    @abstractmethod
    def atender_paciente(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Operatoria(SalaDeAtencion):
    def __init__(self):
        super().__init__()

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def atender_paciente(self):
        paciente = self.pacientes.pop(0)
        self.pacientes_atendidos.append(paciente)
        return paciente

    def __str__(self):
        return f"Operatoria: {len(self.pacientes)} pacientes en espera"
    
class CuidadosIntensivos(SalaDeAtencion):
    def __init__(self):
        super().__init__()

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def atender_paciente(self):
        paciente = self.pacientes.pop(0)
        self.pacientes_atendidos.append(paciente)
        return paciente

    def __str__(self):
        return f"Cuidados Intensivos: {len(self.pacientes)} pacientes en espera"
    
class CuidadosIntermedios(SalaDeAtencion):
    def __init__(self):
        super().__init__()

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def atender_paciente(self):
        paciente = self.pacientes.pop(0)
        self.pacientes_atendidos.append(paciente)
        return paciente

    def __str__(self):
        return f"Cuidados Intermedios: {len(self.pacientes)} pacientes en espera"