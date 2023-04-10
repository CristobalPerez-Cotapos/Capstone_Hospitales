from abc import ABC, abstractmethod

class SalaDeAtencion(ABC):

    def __init__(self, hospital:str, costo:int, tiempos_espera:dict, capacidad:int):
        super().__init__()
        self.pacientes_en_atencion = {i: [] for i in range(1, 9)}
        self.pacientes_atendidos = {i: [] for i in range(1 ,9)} # pacientes que ya fueron atendidos y siguen en la sala de atencion
        self.costo = costo
        self.tiempos_espera = tiempos_espera  # {grupo_diagnostico: tiempo_espera}
        self.capacidad = capacidad
        self.cantidad_de_pacientes_por_grupo_en_atencion = {i: 0 for i in range(1, 9)}
        self.cantidad_de_pacientes_por_grupo_atendidos = {i: 0 for i in range(1, 9)}
        self.total_de_pacientes_en_atencion = 0
        self.total_de_pacientes_atendidos = 0

    @property
    def total_de_pacientes(self):
        return self.total_de_pacientes_en_atencion + self.total_de_pacientes_atendidos

    def agregar_paciente(self, paciente):
        paciente.tiempo_atencion_unidad_actual = 0
        self.pacientes_en_atencion[paciente.grupo_diagnostico].append(paciente)
        self.cantidad_de_pacientes_por_grupo[paciente.grupo_diagnostico] += 1
        self.total_de_pacientes += 1


    def simular_modulo(self):
        for grupo in self.pacientes_en_atencion:
            for paciente in self.pacientes_en_atencion[grupo]:
                paciente.tiempo_atencion_unidad_actual += 1
                if paciente.tiempo_atencion_unidad_actual == self.tiempos_espera[grupo]:
                    self.pacientes_atendidos[grupo].append(paciente)
                    self.pacientes_en_atencion[grupo].remove(paciente)
                    self.cantidad_de_pacientes_por_grupo_en_atencion[grupo] -= 1
                    self.cantidad_de_pacientes_por_grupo_atendidos[grupo] += 1
                    self.total_de_pacientes_en_atencion -= 1
                    self.total_de_pacientes_atendidos += 1

    def retirar_paciente(self, estrategia):
        raise NotImplementedError("No implementado, falta desarrollar la estrategia de retiro de pacientes")
        self.cantidad_de_pacientes_por_grupo_en_atencion[paciente.grupo_diagnostico] -= 1
        self.total_de_pacientes_en_atencion -= 1



class Operatoria(SalaDeAtencion):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Operatoria: {len(self.pacientes)} pacientes en espera"
    
class CuidadosIntensivos(SalaDeAtencion):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Cuidados Intensivos: {len(self.pacientes)} pacientes en espera"
    
class CuidadosIntermedios(SalaDeAtencion):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"Cuidados Intermedios: {len(self.pacientes)} pacientes en espera"