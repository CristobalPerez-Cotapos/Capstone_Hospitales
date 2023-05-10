from abc import ABC, abstractmethod
import parametros_simulacion as ps
import parametros_hospitales as ph
import random 
random.seed(ps.SEED)

class SalaDeAtencion(ABC):

    def __init__(self, hospital:str, costo:dict, tiempo_espera:dict, capacidad:int):
        super().__init__()
        self.pacientes_en_atencion = {i: [] for i in range(1, 9)}
        self.pacientes_atendidos = [] # lista de pacientes ya atendidos en el orden en que fueron atendidos
        self.costo = costo
        self.tiempos_espera = tiempo_espera  # {grupo_diagnostico: tiempo_espera}
        self.capacidad = capacidad
        self.cantidad_de_pacientes_por_grupo_en_atencion = {i: 0 for i in range(1, 9)}
        self.cantidad_de_pacientes_por_grupo_atendidos = {i: 0 for i in range(1, 9)}
        self.total_de_pacientes_en_atencion = 0
        self.total_de_pacientes_atendidos = 0

    @property
    def total_de_pacientes(self):
        return self.total_de_pacientes_en_atencion + self.total_de_pacientes_atendidos
    
    @property
    def camas_disponibles(self):
        return self.capacidad - self.total_de_pacientes

    def agregar_paciente(self, paciente):
        paciente.tiempo_espera(paciente.grupo_diagnostico, paciente.ruta_paciente[0])
        paciente.ruta_paciente.pop(0)
        paciente.tiempo_atencion_unidad_actual = 0
        self.pacientes_en_atencion[paciente.grupo_diagnostico].append(paciente)
        self.cantidad_de_pacientes_por_grupo_en_atencion[paciente.grupo_diagnostico] += 1
        self.total_de_pacientes_en_atencion += 1

    def simular_jornada(self):
        for paciente in self.pacientes_atendidos:
            paciente.tiempo_atencion_unidad_actual += 0.5

        for grupo in self.pacientes_en_atencion:
            for paciente in self.pacientes_en_atencion[grupo]:
                paciente.tiempo_atencion_unidad_actual += 0.5  # Se mide en días
                if paciente.tiempo_atencion_unidad_actual >= paciente.tiempo_a_esperar:
                    self.pacientes_atendidos.append(paciente)
                    self.pacientes_en_atencion[grupo].remove(paciente)
                    self.cantidad_de_pacientes_por_grupo_en_atencion[grupo] -= 1
                    self.cantidad_de_pacientes_por_grupo_atendidos[grupo] += 1
                    self.total_de_pacientes_en_atencion -= 1
                    self.total_de_pacientes_atendidos += 1

    def pacientes_listos_para_trasladar(self, unidad):
        pacientes_listos = []
        for i in self.pacientes_atendidos:
            if i.ruta_paciente[0] == unidad:
                pacientes_listos.append(i)
        return pacientes_listos
    
    def calcular_costos_jornada(self):
        costos_totales = 0
        costos_muertos = 0
        for i in self.pacientes_atendidos:
            costos_muertos += self.costo[i.grupo_diagnostico]
            if i.ruta_paciente[1] != "FIN":
                costos_muertos += ph.VALOR_RIESGO[i.ruta_paciente[0]][i.grupo_diagnostico][i.ruta_paciente[1]][int(i.tiempo_esperado_muerto * 2) + 1] * ps.COSTO_VIDA
                pass
            #print(f"El paciente {i.id} ha incurrido en un gasto en la unidad {self.codigo} de {self.costo[i.grupo_diagnostico]}")
        costos_totales += costos_muertos
        for grupo in self.pacientes_en_atencion:
            for paciente in self.pacientes_en_atencion[grupo]:
                costos_totales += self.costo[paciente.grupo_diagnostico]
        return costos_totales, costos_muertos    

    def retirar_paciente(self, paciente):
        self.pacientes_atendidos.remove(paciente)
        self.total_de_pacientes_atendidos -= 1
        self.cantidad_de_pacientes_por_grupo_atendidos[paciente.grupo_diagnostico] -= 1

    def recopilar_informacion(self):
        return (self.cantidad_de_pacientes_por_grupo_en_atencion,
                self.cantidad_de_pacientes_por_grupo_atendidos,
                self.camas_disponibles)



class Operatorio(SalaDeAtencion):
    def __init__(self, codigo="OR", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.codigo = codigo

    def __str__(self):
        return f"Operatoria: {self.total_de_pacientes_en_atencion} pacientes en atención, {self.total_de_pacientes_atendidos} pacientes atendidos, {self.camas_disponibles} camas disponibles"
    
class CuidadosIntensivos(SalaDeAtencion):
    def __init__(self, codigo="ICU",*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.codigo = codigo

    def __str__(self):
        return f"Cuidados Intensivos: {self.total_de_pacientes_en_atencion} pacientes en atención, {self.total_de_pacientes_atendidos} pacientes atendidos, {self.camas_disponibles} camas disponibles"
    
class CuidadosIntermedios(SalaDeAtencion):
    def __init__(self, codigo="SDU_WARD", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.codigo = codigo

    def __str__(self):
        return f"Cuidados Intermedios: {self.total_de_pacientes_en_atencion} pacientes en atención, {self.total_de_pacientes_atendidos} pacientes atendidos, {self.camas_disponibles} camas disponibles"
    
class Admision(SalaDeAtencion):
    def __init__(self, codigo="GA",*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.codigo = codigo

    def __str__(self):
        return f"Admision: {self.total_de_pacientes_en_atencion} pacientes en atención, {self.total_de_pacientes_atendidos} pacientes atendidos, {self.camas_disponibles} camas disponibles"