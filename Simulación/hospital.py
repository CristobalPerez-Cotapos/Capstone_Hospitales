from sala_de_atencion import Operatorio, CuidadosIntensivos, CuidadosIntermedios, Admision
from sala_de_llegada import Urgencias
import parametros_hospitales as ph
import parametros_simulacion as ps
import random 
random.seed(ps.SEED)

class Hospital:
    def __init__(self, nombre, simulacion):
        self.costos_total = 0
        self.costos_muertos = 0
        self.nombre = nombre
        self.simulacion = simulacion
        self.crear_unidades()
        self.lista_de_unidades = [self.urgencias, self.operatorio, self.cuidados_intensivos, self.cuidados_intermedios, self.admision]
        self.capacidades = {}

    def crear_unidades(self):
        self.urgencias = Urgencias(hospital=self.nombre, 
                                   costo=ph.COSTOS_POR_UNIDAD[self.nombre]["ED"],
                                   capacidad=ph.CAMAS_POR_UNIDAD[self.nombre]["ED"],
                                   simulacion=self.simulacion)

        self.operatorio = Operatorio(hospital=self.nombre,
                                    costo=ph.COSTOS_POR_UNIDAD[self.nombre]["OR"],
                                    capacidad=ph.CAMAS_POR_UNIDAD[self.nombre]["OR"],)
        
        self.cuidados_intensivos = CuidadosIntensivos(hospital=self.nombre,
                                                    costo=ph.COSTOS_POR_UNIDAD[self.nombre]["ICU"],
                                                    capacidad=ph.CAMAS_POR_UNIDAD[self.nombre]["ICU"],)
        
        self.cuidados_intermedios = CuidadosIntermedios(hospital=self.nombre,
                                                    costo=ph.COSTOS_POR_UNIDAD[self.nombre]["SDU_WARD"],
                                                    capacidad=ph.CAMAS_POR_UNIDAD[self.nombre]["SDU_WARD"],)
        
        self.admision = Admision(hospital=self.nombre,
                                costo=ph.COSTOS_POR_UNIDAD[self.nombre]["GA"],
                                capacidad=ph.CAMAS_POR_UNIDAD[self.nombre]["GA"],)
        
    def revisar_capacidades_camas(self):
        lista_unidades_medicas = ["OR", "ICU", "SDU_WARD"]
        dicc = {i : { j : 0 for j in lista_unidades_medicas} for i in range(1, 9)}
        for unidad in self.lista_de_unidades:
            codigo = unidad.codigo
            if codigo in lista_unidades_medicas:
                for grupo_diagnostico in unidad.cantidad_de_pacientes_por_grupo_en_atencion.keys():
                    cantidad = 0
                    cantidad += unidad.cantidad_de_pacientes_por_grupo_en_atencion[grupo_diagnostico]
                    cantidad += unidad.cantidad_de_pacientes_por_grupo_atendidos[grupo_diagnostico]
                    tasa_ocupacion = cantidad / ph.CAMAS_POR_UNIDAD[self.nombre][codigo] * 100
                    dicc[grupo_diagnostico][codigo] = tasa_ocupacion
        return dicc


    def simular_jornada(self):
        self.operatorio.simular_jornada()
        self.cuidados_intensivos.simular_jornada()
        self.cuidados_intermedios.simular_jornada()
        self.admision.simular_jornada()
        
        for i in range(20):
            self.desplazamiento_entre_unidades()   # Lo hacemos 5 veces por las 5 unidades

        self.urgencias.simular_jornada()

        for i in range(20):
            self.desplazamiento_entre_unidades()   # Lo hacemos 5 veces por las 5 unidades
        
    def desplazamiento_entre_unidades(self):
        camas_disponibles = {}
        for i in self.lista_de_unidades:
            camas_disponibles[i.codigo] = i.camas_disponibles

        for inicio in self.lista_de_unidades:
            for destino in self.lista_de_unidades:
                if inicio != destino:
                    pacientes_listos = inicio.pacientes_listos_para_trasladar(destino.codigo)
                    for paciente in pacientes_listos:
                        if camas_disponibles[destino.codigo] > 0:
                            camas_disponibles[destino.codigo] -= 1
                            self.desplazar_paciente(paciente, inicio, destino)
                        else:
                            break
            for paciente in inicio.pacientes_listos_para_trasladar("FIN"):
                inicio.retirar_paciente(paciente)

    def desplazar_paciente(self, paciente, inicio, destino):
        inicio.retirar_paciente(paciente)
        destino.agregar_paciente(paciente)

    def calcular_costos_jornada(self):
        costo_total_diario= 0
        costo_muerto_diario = 0
        for unidad in self.lista_de_unidades:
            costo_total, costo_muerto = unidad.calcular_costos_jornada()

            costo_total_diario += costo_total
            costo_muerto_diario += costo_muerto

            self.costos_total += costo_total
            self.costos_muertos += costo_muerto
        return costo_total_diario, costo_muerto_diario

    def recopilar_informacion(self):
        datos = {}
        for unidad in self.lista_de_unidades:
            datos[unidad.codigo] = unidad.recopilar_informacion()
        return datos

    def __str__(self):
        return  f"Hospital: {self.nombre} costo total: {self.costos_total} costo muerto: {self.costos_muertos} \n \n" + \
                f"{self.urgencias}\n" + \
                f"{self.operatorio}\n" + \
                f"{self.cuidados_intensivos}\n" + \
                f"{self.cuidados_intermedios}\n" + \
                f"{self.admision}\n"
    