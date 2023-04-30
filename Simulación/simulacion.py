import parametros_simulacion as ps
import parametros_hospitales as ph
from hospital import Hospital
from sala_de_llegada import ListaDeEspera
import random 
random.seed(ps.SEED)

class Simulacion:
    def __init__(self, estrategia):
        self.estrategia = estrategia
        self.hospitales = []
        self.dias_transcurridos = 0
        self.dias_de_simulacion = ps.DIAS_DE_SIMULACION
        self.lista_de_espera = ListaDeEspera()
        self.agregar_hospitales()

    def agregar_hospitales(self):
        for i in range(ps.NUMERO_HOSPITALES):
            hospital = Hospital(f"H_{i+1}")
            self.hospitales.append(hospital)

    def simular(self):
        for dia in range(self.dias_de_simulacion):
            for jornada in range(ps.JORNADAS_POR_DIAS):
                self.lista_de_espera.simular_jornada()
                self.trasladar_pacientes_lista_de_espera()
                for hospital in self.hospitales:
                    hospital.simular_jornada()
                print(f"Jornada {jornada+1} del dia {dia+1}")
                print("------------------------------------------------")
                self.imprimir_estado()
            self.dias_transcurridos += 1

    def trasladar_pacientes_lista_de_espera(self):
        for hospital in self.hospitales:
            pacientes_listos = self.lista_de_espera.pacientes_listos_para_trasladar("GA")
            for paciente in pacientes_listos:
                if hospital.admision.camas_disponibles > 0:
                    hospital.admision.agregar_paciente(paciente)
                    self.lista_de_espera.retirar_paciente(paciente)

    def imprimir_estado(self):
        for hospital in self.hospitales:
            print(hospital)

    def aplicar_estrategia(self):
        pass