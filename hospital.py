from sala_de_atencion import Operatorio, CuidadosIntensivos, CuidadosIntermedios, Admision
from sala_de_llegada import Urgencias
import parametros_hospitales as ph

class Hospital:
    def __init__(self, nombre):
        self.nombre = nombre
        self.crear_unidades()

    def crear_unidades(self):
        self.urgencias = Urgencias(self.nombre, 
                                   costo=ph.COSTOS_POR_UNIDAD[self.nombre]["ED"],
                                   capacidad=ph.CAMAS_POR_UNIDAD[self.nombre]["ED"],
                                   tiempo_espera=ph.TIEMPOS_ESPERA_POR_UNIDAD[self.nombre]["ED"])

        self.operatorio = Operatorio(self.nombre,
                                    costo=ph.COSTOS_POR_UNIDAD[self.nombre]["OR"],
                                    capacidad=ph.CAMAS_POR_UNIDAD[self.nombre]["OR"],
                                    tiempo_espera=ph.TIEMPOS_ESPERA_POR_UNIDAD[self.nombre]["OR"])
        
        self.cuidados_intensivos = CuidadosIntensivos(self.nombre,
                                                    costo=ph.COSTOS_POR_UNIDAD[self.nombre]["ICU"],
                                                    capacidad=ph.CAMAS_POR_UNIDAD[self.nombre]["ICU"],
                                                    tiempo_espera=ph.TIEMPOS_ESPERA_POR_UNIDAD[self.nombre]["ICU"])
        
        self.cuidados_intermedios = CuidadosIntermedios(self.nombre,
                                                    costo=ph.COSTOS_POR_UNIDAD[self.nombre]["SDU_WARD"],
                                                    capacidad=ph.CAMAS_POR_UNIDAD[self.nombre]["SDU_WARD"],
                                                    tiempo_espera=ph.TIEMPOS_ESPERA_POR_UNIDAD[self.nombre]["SDU_WARD"])
        
        self.admision = Admision(self.nombre,
                                costo=ph.COSTOS_POR_UNIDAD[self.nombre]["GA"],
                                capacidad=ph.CAMAS_POR_UNIDAD[self.nombre]["GA"],
                                tiempo_espera=ph.TIEMPOS_ESPERA_POR_UNIDAD[self.nombre]["GA"])


    def simular_jornada(self):
        self.urgencias.simular_jornada()
        self.operatorio.simular_jornada()
        self.cuidados_intensivos.simular_jornada()
        self.cuidados_intermedios.simular_jornada()
        self.admision.simular_jornada()

    def __str__(self):
        return  f"Hospital: {self.nombre}\n" + \
                f"{self.urgencias}\n" + \
                f"{self.operatorio}\n" + \
                f"{self.cuidados_intensivos}\n" + \
                f"{self.cuidados_intermedios}\n" + \
                f"{self.admision}\n"
    