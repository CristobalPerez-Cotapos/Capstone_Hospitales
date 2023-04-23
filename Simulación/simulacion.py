import parametros_simulacion as ps
from hospital import Hospital

class Simulacion:
    def __init__(self, estrategia):
        self.estrategia = estrategia
        self.hospitales = []
        self.dias_transcurridos = 0
        self.dias_de_simulacion = ps.DIAS_DE_SIMULACION
        self.agregar_hospitales()

    def agregar_hospitales(self):
        for i in range(ps.NUMERO_HOSPITALES):
            hospital = Hospital(f"H_{i+1}")
            self.hospitales.append(hospital)

    def simular(self):
        for i in range(self.dias_de_simulacion):
            for j in range(ps.JORNADAS_POR_DIAS):
                for hospital in self.hospitales:
                    hospital.simular_jornada()
                print(f"Jornada {j+1} del dia {i+1}")
                print("------------------------------------------------")
                self.imprimir_estado()
            self.dias_transcurridos += 1

    def imprimir_estado(self):
        for hospital in self.hospitales:
            print(hospital)

    def aplicar_estrategia(self):
        pass