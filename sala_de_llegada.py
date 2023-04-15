from abc import ABC, abstractmethod
from numpy import random
from paciente import Paciente
import parametros_hospitales as ph

class SalaDeLLegada(ABC):

    def __init__(self):
        super().__init__()
        self.pacientes = []
        self.cantidad_de_pacientes_por_grupo = {i: 0 for i in range(1, 9)}
        self.total_de_pacientes = 0

    @abstractmethod
    def llegada_de_pacientes(self, paciente):
        pass

    @abstractmethod
    def __str__(self):
        text = f"Total de pacientes: {self.total_de_pacientes}"
        for grupo_diagnostico in self.cantidad_de_pacientes_por_grupo:
            if self.cantidad_de_pacientes_por_grupo[grupo_diagnostico] != 0:
                text += "\n" + f"Grupo {grupo_diagnostico}: {self.cantidad_de_pacientes_por_grupo[grupo_diagnostico]}"
        return text
    
    def simular_jornada(self):
        self.llegada_de_pacientes()

   

class ListaDeEspera(SalaDeLLegada):

    def __init__(self):
        super().__init__()

    def llegada_de_pacientes(self):
        for grupo_diagnostico in ph.TASA_LLEGADA_HOSPITAL["WL"]:
            cantidad_de_llegadas = random.poisson(ph.TASA_LLEGADA_HOSPITAL["WL"][grupo_diagnostico])
            self.total_de_pacientes += cantidad_de_llegadas
            self.cantidad_de_pacientes_por_grupo[grupo_diagnostico] += cantidad_de_llegadas
            for i in range(cantidad_de_llegadas):
                self.pacientes.append(Paciente(grupo_diagnostico))

    def __str__(self):
        text = "Lista de espera \n"
        text += super().__str__()
        return text

class Urgencias(SalaDeLLegada):

    def __init__(self, hospital:str, costo, capacidad, tiempo_espera):
        super().__init__()
        self.hospital = hospital
        self.costo = costo
        self.capacidad = capacidad
        self.tiempo_de_espera = tiempo_espera


    def llegada_de_pacientes(self):
        for grupo_diagnostico in ph.TASA_LLEGADA_HOSPITAL[self.hospital]:
            cantidad_de_llegadas = random.poisson(ph.TASA_LLEGADA_HOSPITAL[self.hospital][grupo_diagnostico])
            self.total_de_pacientes += cantidad_de_llegadas
            self.cantidad_de_pacientes_por_grupo[grupo_diagnostico] += cantidad_de_llegadas
            for i in range(cantidad_de_llegadas):
                self.pacientes.append(Paciente(grupo_diagnostico))

    def __str__(self):
        text = f"Urgencias Hospital {self.hospital[-1]}, total de pacientes: {self.total_de_pacientes} \n"
        return text

if __name__ == "__main__":
    urgencias = Urgencias("H_1")
    for i in range(10):
        print(f"Simulación {i}")
        urgencias.llegada_de_pacientes()
        print(urgencias)
