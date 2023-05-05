from abc import ABC, abstractmethod
from numpy import random
from paciente import Paciente
import parametros_hospitales as ph
import parametros_simulacion as ps
random.seed(ps.SEED)

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

    def __init__(self, tiempo_espera=ph.TIEMPOS_ESPERA_POR_UNIDAD["WL"]):
        super().__init__()
        self.pacientes_en_atencion = {i: [] for i in range(1, 9)}
        self.pacientes_atendidos = []
        self.tiempos_espera = tiempo_espera
        self.total_de_pacientes_en_espera = 0
        self.total_de_pacientes_para_ingresar = 0
        self.cantidad_de_pacientes_por_grupo_en_atencion = {i: 0 for i in range(1, 9)}
        self.cantidad_de_pacientes_por_grupo_atendidos = {i: 0 for i in range(1, 9)}

    def simular_jornada(self):
        for grupo in self.pacientes_en_atencion:
            for paciente in self.pacientes_en_atencion[grupo]:
                paciente.tiempo_atencion_unidad_actual += 0.5  # Se mide en días
                if paciente.tiempo_atencion_unidad_actual >= self.tiempos_espera[grupo]:
                    self.pacientes_atendidos.append(paciente)
                    self.pacientes_en_atencion[grupo].remove(paciente)
                    self.cantidad_de_pacientes_por_grupo_en_atencion[grupo] -= 1
                    self.cantidad_de_pacientes_por_grupo_atendidos[grupo] += 1
                    self.total_de_pacientes_en_espera -= 1
                    self.total_de_pacientes_para_ingresar += 1
        self.llegada_de_pacientes()

    def pacientes_listos_para_trasladar(self, unidad):
        pacientes_listos = []
        for i in self.pacientes_atendidos:
            if i.ruta_paciente[0] == unidad:
                pacientes_listos.append(i)
        return pacientes_listos
    
    def retirar_paciente(self, paciente):
        self.pacientes_atendidos.remove(paciente)
        self.total_de_pacientes_para_ingresar -= 1
        self.cantidad_de_pacientes_por_grupo_atendidos[paciente.grupo_diagnostico] -= 1

    def llegada_de_pacientes(self):
        for grupo_diagnostico in ph.TASA_LLEGADA_HOSPITAL["WL"]:
            cantidad_de_llegadas = random.poisson(ph.TASA_LLEGADA_HOSPITAL["WL"][grupo_diagnostico])
            self.total_de_pacientes += cantidad_de_llegadas
            self.cantidad_de_pacientes_por_grupo[grupo_diagnostico] += cantidad_de_llegadas
            for i in range(cantidad_de_llegadas):
                paciente = Paciente(grupo_diagnostico)
                paciente.ruta_paciente.pop(0)
                paciente.tiempo_atencion_unidad_actual = 0
                self.pacientes_en_atencion[paciente.grupo_diagnostico].append(paciente)
                self.cantidad_de_pacientes_por_grupo_en_atencion[paciente.grupo_diagnostico] += 1
                self.total_de_pacientes_en_espera += 1
                self.pacientes.append(paciente)

    def recopilar_informacion(self):
        return {"WL":(self.cantidad_de_pacientes_por_grupo_en_atencion,
                self.cantidad_de_pacientes_por_grupo_atendidos,
                0)}

    def __str__(self):
        text = "Lista de espera \n"
        text += super().__str__()
        return text

class Urgencias(SalaDeLLegada):

    def __init__(self, hospital:str, costo, capacidad, tiempo_espera, simulacion, codigo="ED"):
        super().__init__()
        self.hospital = hospital
        self.costo = costo
        self.capacidad = capacidad
        self.tiempo_de_espera = tiempo_espera
        self.codigo = codigo
        self.cantidad_de_pacientes_por_grupo_en_atencion = {i: 0 for i in range(1, 9)}
        self.cantidad_de_pacientes_por_grupo_atendidos = {i: 0 for i in range(1, 9)}
        self.simuacion = simulacion

    @property
    def camas_disponibles(self):
        return self.capacidad - self.total_de_pacientes
    
    def pacientes_listos_para_trasladar(self, destino):
        pacientes_listos = []
        for paciente in self.pacientes:
            if paciente.ruta_paciente[0] == destino:
                pacientes_listos.append(paciente)
        return pacientes_listos
    
    def llegada_de_pacientes(self):
        nuevos_pacientes = []
        for grupo_diagnostico in ph.TASA_LLEGADA_HOSPITAL[self.hospital]:
            cantidad_de_llegadas = random.poisson(ph.TASA_LLEGADA_HOSPITAL[self.hospital][grupo_diagnostico])
            for i in range(cantidad_de_llegadas):
                paciente = Paciente(grupo_diagnostico)
                if paciente.ruta_paciente[0] == self.codigo:
                    paciente.ruta_paciente.pop(0)
                else:
                    raise ValueError(f"El paciente con grupo {grupo_diagnostico} no llega a esta sala de llegada")
                nuevos_pacientes.append(paciente)
            
        # Ordenar pacientes por costo de derivación
        nuevos_pacientes = sorted(nuevos_pacientes, key=lambda x: ph.COSTOS_DERIVACION[paciente.ruta_paciente[0]][grupo_diagnostico], reverse=True)
        for paciente in nuevos_pacientes:
            ############ Falta que el paciente sepa a que hospital va #################
            puntaje, hospital = self.simuacion.generar_puntaje_paciente(paciente)
            #print(f"El paciente tiene un puntaje de {puntaje} y las camas disponibles son {self.camas_disponibles}")
            if self.camas_disponibles > 0 and puntaje > 0:
                self.pacientes.append(paciente)
                self.cantidad_de_pacientes_por_grupo_en_atencion[grupo_diagnostico] += 1
                self.total_de_pacientes += 1
            else:
                self.simuacion.derivar_paciente(paciente, ED=True)

    def retirar_paciente(self, paciente):
        self.pacientes.remove(paciente)
        self.total_de_pacientes -= 1
        self.cantidad_de_pacientes_por_grupo_atendidos[paciente.grupo_diagnostico] -= 1

    def calcular_costos_jornada(self):
        # Como la atención en urgencias es inmediata, todo el costo por espera es inutil
        costos_totales = 0
        costos_muertos = 0
        for i in self.pacientes:
            costos_muertos += self.costo[i.grupo_diagnostico]
        costos_totales += costos_muertos
        return costos_totales, costos_muertos 
    
    def recopilar_informacion(self):
        return (self.cantidad_de_pacientes_por_grupo_en_atencion,
               self.cantidad_de_pacientes_por_grupo_atendidos,
               self.camas_disponibles)

    def __str__(self):
        text = f"Urgencias Hospital {self.hospital[-1]}, total de pacientes: {self.total_de_pacientes} \n"
        return text

if __name__ == "__main__":
    lista_espera = ListaDeEspera(ph.TIEMPOS_ESPERA_POR_UNIDAD["WL"])
    for i in range(100):
        lista_espera.simular_jornada()
        print(f"Jornada {i} \n")
        print(lista_espera)
        print(f"Pacientes atendidos: {lista_espera.total_de_pacientes_para_ingresar}")
        print(f"Pacientes en espera: {lista_espera.total_de_pacientes_en_espera}")
        print("\n")
        print("\n")



