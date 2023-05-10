import parametros_simulacion as ps
import parametros_hospitales as ph
from hospital import Hospital
from sala_de_llegada import ListaDeEspera
import random
random.seed(ps.SEED)

class Simulacion:
    def __init__(self, estrategia):
        self.numero_ejecucion = 1
        random.seed(ps.SEED)
        self.estrategia = estrategia
        self.hospitales = []
        self.dias_transcurridos = 0
        self.dias_de_simulacion = ps.DIAS_DE_SIMULACION
        self.lista_de_espera = ListaDeEspera()
        self.costo_total_derivacion = 0
        self.resultados = []
        self.costos_diarios = {i : 0 for i in range(self.dias_de_simulacion)}
        self.agregar_hospitales()

    def agregar_hospitales(self):
        for i in range(ps.NUMERO_HOSPITALES):
            hospital = Hospital(f"H_{i+1}", simulacion=self)
            self.hospitales.append(hospital)

    def simular_miltiples_veces(self):
        for i in range(ps.SIMULACIONES_POR_ESTRATEGIA):
            self.simular()
            self.resetear_simulacion()

    def simular(self):
        random.seed(ps.SEED * self.numero_ejecucion)
        for dia in range(self.dias_de_simulacion):
            for jornada in range(ps.JORNADAS_POR_DIAS):
                for hospital in self.hospitales:
                    hospital.simular_jornada()
                self.lista_de_espera.simular_jornada()
                self.trasladar_pacientes_lista_de_espera()
                self.agregar_costos_jornada_hospitales()
                print(f"Jornada {jornada+1} del dia {dia+1}")
                print("------------------------------------------------")
                self.imprimir_estado()
            self.dias_transcurridos += 1
        self.resultados.append(self.calcular_funcion_objetivo())

    def agregar_costos_jornada_hospitales(self):
        for hospital in self.hospitales:
            costos_totales, costos_muertos = hospital.calcular_costos_jornada()
            self.costos_diarios[self.dias_transcurridos] += costos_muertos

    def trasladar_pacientes_lista_de_espera(self):
        pacientes_listos = self.lista_de_espera.pacientes_listos_para_trasladar("GA")
        for paciente in pacientes_listos:
            puntaje, hospital = self.generar_puntaje_paciente(paciente)
            if hospital.admision.camas_disponibles > 0 and puntaje > 0:
                self.lista_de_espera.retirar_paciente(paciente)
                hospital.admision.agregar_paciente(paciente)
                hospital.desplazamiento_entre_unidades()
            else:
                self.derivar_paciente(paciente)

    def derivar_paciente(self, paciente, ED = False):
        if not ED:
            self.lista_de_espera.retirar_paciente(paciente)
            destino = paciente.ruta_paciente[1]
            self.costo_total_derivacion += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.costos_diarios[self.dias_transcurridos] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
        else:
            destino = paciente.ruta_paciente[0]
            self.costo_total_derivacion += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.costos_diarios[self.dias_transcurridos] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]

    def generar_puntaje_paciente(self, paciente):
        max_puntaje = -1000000000000000000
        for hospital in self.hospitales:
            datos = self.recopilar_informacion()[hospital.nombre]
            datos_WL = self.recopilar_informacion()["WL"]
            puntaje = self.estrategia.generar_punteje_paciente(paciente, datos, datos_WL, hospital.nombre)
            if puntaje > max_puntaje:
                max_puntaje = puntaje
                hospital_asignado = hospital
        return max_puntaje, hospital_asignado

    def imprimir_estado(self):
        for hospital in self.hospitales:
            print(hospital)

    def recopilar_informacion(self):
        informacion = {}
        for hospital in self.hospitales:
            informacion[hospital.nombre] = hospital.recopilar_informacion()
        informacion["WL"] = self.lista_de_espera.recopilar_informacion()
        return informacion
    
    def calcular_funcion_objetivo(self):
        valores = list(self.costos_diarios.values())
        muestra = []
        for i in ps.ID_DIAS_MUESTRAS:
            muestra.append(valores[i])
        costo_total = 0
        for hospital in self.hospitales:
            costo_total += hospital.costos_muertos
        print(f"Costo total: {self.costo_total_derivacion}, Costo hospital: {costo_total}, costo derivacion: {self.costo_total_derivacion}," +
               f" estrategia: {self.estrategia.id}")
        
        promedio = sum(muestra)/len(muestra)
        #print(f"Promedio diario: {promedio}")
        return promedio

    def resetear_simulacion(self):
        self.costos_diarios = {i : 0 for i in range(self.dias_de_simulacion)}
        self.numero_ejecucion += 1
        self.hospitales = []
        self.dias_transcurridos = 0
        self.dias_de_simulacion = ps.DIAS_DE_SIMULACION
        self.lista_de_espera = ListaDeEspera()
        self.costo_total_derivacion = 0
        self.agregar_hospitales()

    def promedio_resultados(self):
        return sum(self.resultados)/len(self.resultados)