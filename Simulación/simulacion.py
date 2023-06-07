import parametros_simulacion as ps
import parametros_hospitales as ph
from hospital import Hospital
from sala_de_llegada import ListaDeEspera
from funciones import Archivos as ar
from estrategia import Estrategia
import random
random.seed(ps.SEED)

class Simulacion:
    def __init__(self, estrategia, clase_resultados):
        self.numero_ejecucion = 1
        random.seed(ps.SEED)
        self.estrategia = estrategia
        self.hospitales = []
        self.dias_transcurridos = 0
        self.jornadas_transcurridas = 0
        self.dias_de_simulacion = ps.DIAS_DE_SIMULACION
        self.lista_de_espera = ListaDeEspera()
        self.costo_total_derivacion = 0
        self.costos_muertos_WL = 0
        self.resultados = []
        self.costos_espera_WL = {i : 0 for i in range(self.dias_de_simulacion)}   
        self.costos_derivacion = {i : 0 for i in range(self.dias_de_simulacion)}     
        self.costos_muertos_hospitales = {i : 0 for i in range(self.dias_de_simulacion)}
        self.costos_muertos_hospitales_diarios_simulacion = {}       
        self.costos_espera_WL_simulacion = {}     
        self.costos_derivacion_simulacion = {}     
        self.costos_muertos_hospitales_simulacion = {}     
        self.costos_diarios = {i : 0 for i in range(self.dias_de_simulacion)}
        self.derivaciones = {j : {i : 0 for i in range(self.dias_de_simulacion)} for j in range(1, ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA + 1)}
        self.espera_WL = {j : {i : 0 for i in range(self.dias_de_simulacion)} for j in range(1, ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA + 1)}
        self.pacientes_esperando = {j : {i : {"ICU" : 0, "SDU_WARD" : 0, "OR" : 0, "GA" : 0} for i in range(self.dias_de_simulacion)} for j in range(1, ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA + 1)}
        self.agregar_hospitales()
        self.funciones_objetivos = {}
        self.capacidades_camas = {}
        self.capacidad_cama_por_simulacion = {}
        self.promedio_capacidades = {}
        self.clase_resultados = clase_resultados
        
    def agregar_hospitales(self):
        for i in range(ps.NUMERO_HOSPITALES):
            hospital = Hospital(f"H_{i+1}", simulacion=self)
            self.hospitales.append(hospital)

    def simular_miltiples_veces(self):
        for i in range(ps.SIMULACIONES_POR_ESTRATEGIA):
            self.simular()
            if i == ps.SIMULACIONES_POR_ESTRATEGIA - 1:
                self.clase_resultados.append(self)
            self.resetear_simulacion()

    def simular_mejores_estrategias_multiples_veces(self):
        for i in range(ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA):
            self.simular_cambio_estrategia()
            self.resetear_simulacion()

    def simular(self):
        random.seed(ps.SEED * self.numero_ejecucion)
        for dia in range(self.dias_de_simulacion):
            for jornada in range(ps.JORNADAS_POR_DIAS):
                for hospital in self.hospitales:
                    hospital.simular_jornada()
                jornada_actual = dia * 2 + jornada
                self.lista_de_espera.simular_jornada()
                self.trasladar_pacientes_lista_de_espera()
                self.agregar_costos_jornada_hospitales_y_WL()
                for hospital in self.hospitales:
                    tasas_camas = hospital.revisar_capacidades_camas(self.dias_transcurridos)
                    if tasas_camas != None:
                        self.capacidad_cama_por_simulacion[self.jornadas_transcurridas] = tasas_camas
                self.espera_WL[self.numero_ejecucion][self.dias_transcurridos] += len(self.lista_de_espera.pacientes_atendidos)
                for hospital in self.hospitales:
                    for unidad in hospital.lista_de_unidades:
                        if unidad.codigo != 'ED':
                            self.pacientes_esperando[self.numero_ejecucion][self.dias_transcurridos][unidad.codigo] += unidad.total_de_pacientes_atendidos

                # print(f"Jornada {jornada+1} del dia {dia+1}")
                # print("------------------------------------------------")
                # self.imprimir_estado()
                self.jornadas_transcurridas += 1
            self.dias_transcurridos += 1
        
        self.resultados.append(self.calcular_funcion_objetivo())
        self.calcular_tasas_ocupacion()
        
        self.capacidades_camas[self.numero_ejecucion] = self.capacidad_cama_por_simulacion
        self.promedio_capacidades[self.numero_ejecucion] = self.calcular_tasas_ocupacion()



    def simular_cambio_estrategia(self):
        random.seed(ps.SEED * self.numero_ejecucion)
        self.costos_espera_WL = {i : 0 for i in range(ps.DIAS_SIMULACION_CAMBIO)}   
        self.costos_derivacion = {i : 0 for i in range(ps.DIAS_SIMULACION_CAMBIO)}     
        self.costos_muertos_hospitales = {i : 0 for i in range(ps.DIAS_SIMULACION_CAMBIO)}       
        self.costos_diarios = {i : 0 for i in range(ps.DIAS_SIMULACION_CAMBIO)}
        self.derivaciones = {j : {i : 0 for i in range(ps.DIAS_SIMULACION_CAMBIO)} for j in range(1, ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA + 1)}
        self.espera_WL = {j : {i : 0 for i in range(ps.DIAS_SIMULACION_CAMBIO)} for j in range(1, ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA + 1)}
        self.pacientes_esperando = {j : {i : {"ICU" : 0, "SDU_WARD" : 0, "OR" : 0, "GA" : 0} for i in range(ps.DIAS_SIMULACION_CAMBIO)} for j in range(1, ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA + 1)}
        
        for dia in range(ps.DIAS_SIMULACION_CAMBIO):
            if dia >= self.dias_de_simulacion - 1:
                self.estrategia = Estrategia(ar('None').leer_estrategias()['Estrategia 1'])
            for jornada in range(ps.JORNADAS_POR_DIAS):
                for hospital in self.hospitales:
                    hospital.simular_jornada()
                jornada_actual = dia * 2 + jornada
                self.lista_de_espera.simular_jornada()
                self.trasladar_pacientes_lista_de_espera()
                self.agregar_costos_jornada_hospitales_y_WL()
                for hospital in self.hospitales:
                    tasas_camas = hospital.revisar_capacidades_camas(self.dias_transcurridos)
                    if tasas_camas != None:
                        self.capacidad_cama_por_simulacion[self.jornadas_transcurridas] = tasas_camas
                self.espera_WL[self.numero_ejecucion][self.dias_transcurridos] += len(self.lista_de_espera.pacientes_atendidos)
                for hospital in self.hospitales:
                    for unidad in hospital.lista_de_unidades:
                        if unidad.codigo != 'ED':
                            self.pacientes_esperando[self.numero_ejecucion][self.dias_transcurridos][unidad.codigo] += unidad.total_de_pacientes_atendidos

                # print(f"Jornada {jornada+1} del dia {dia+1}")
                # print("------------------------------------------------")
                # self.imprimir_estado()
                self.jornadas_transcurridas += 1
            self.dias_transcurridos += 1
        self.resultados.append(self.calcular_funcion_objetivo())
        self.calcular_tasas_ocupacion()
        
        self.capacidades_camas[self.numero_ejecucion] = self.capacidad_cama_por_simulacion
        self.promedio_capacidades[self.numero_ejecucion] = self.calcular_tasas_ocupacion()
        diccionario = {}
        diccionario['Costos WL'] = self.costos_espera_WL
        diccionario['Costos muertos hospitales'] = self.costos_muertos_hospitales
        diccionario['Costos derivaciones'] = self.costos_derivacion
        diccionario['Costos diarios'] = self.costos_diarios
        #ar('None').guardar_resultados_cambio_política(diccionario)

                    
    def calcular_tasas_ocupacion(self):
        dicc_tasas = {"ED": 0, "ICU": 0, "SDU_WARD": 0, "GA": 0, "OR": 0}
        for jornada in self.capacidad_cama_por_simulacion.keys():
            for unidad in self.capacidad_cama_por_simulacion[jornada].keys():
                dicc_tasas[unidad] += self.capacidad_cama_por_simulacion[jornada][unidad]
        for unidad in dicc_tasas.keys():
            dicc_tasas[unidad] = dicc_tasas[unidad] / (ps.MUESTRAS_POR_SIMULACION * 2)
        return dicc_tasas


    def agregar_costos_jornada_hospitales_y_WL(self):
        for hospital in self.hospitales:
            costos_totales, costos_muertos = hospital.calcular_costos_jornada()
            self.costos_diarios[self.dias_transcurridos] += costos_muertos
            self.costos_muertos_hospitales[self.dias_transcurridos] += costos_muertos

        
        costos_totales, costos_muertos = self.lista_de_espera.calcular_costos_jornada()
        self.costos_diarios[self.dias_transcurridos] += costos_muertos
        self.costos_espera_WL[self.dias_transcurridos] += costos_muertos
        self.costos_muertos_WL += costos_muertos


    def trasladar_pacientes_lista_de_espera(self):
        pacientes_listos = self.lista_de_espera.pacientes_listos_para_trasladar("GA")
        for paciente in pacientes_listos:
            
            puntaje, hospital = self.generar_puntaje_paciente(paciente)
            ruta = paciente.ruta_paciente[1]
            for unidad in hospital.lista_de_unidades:
                if unidad.codigo == ruta:
                    unidad_paciente = unidad
            if hospital.admision.camas_disponibles > 0 and puntaje >= 0:
                self.lista_de_espera.retirar_paciente(paciente)
                hospital.admision.agregar_paciente(paciente)
                hospital.desplazamiento_entre_unidades()
            elif hospital.admision.camas_disponibles > 0 and unidad_paciente.camas_disponibles > 6:
                self.lista_de_espera.retirar_paciente(paciente)
                hospital.admision.agregar_paciente(paciente)
                hospital.desplazamiento_entre_unidades()
            elif puntaje < 0:
                self.derivaciones[self.numero_ejecucion][self.dias_transcurridos] += 1
                self.derivar_paciente(paciente)
            else:
                if paciente.tiempo_esperado_muerto >= ps.TIEMPO_ESPERADO_MAXIMO[paciente.grupo_diagnostico]:
                    self.derivaciones[self.numero_ejecucion][self.dias_transcurridos] += 1
                    self.derivar_paciente(paciente)

    def derivar_paciente(self, paciente, ED = False):
        if not ED:
            self.lista_de_espera.retirar_paciente(paciente)
            destino = paciente.ruta_paciente[1]
            self.costo_total_derivacion += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.costos_diarios[self.dias_transcurridos] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.costos_derivacion[self.dias_transcurridos] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
        else:
            destino = paciente.ruta_paciente[0]
            self.costo_total_derivacion += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.costos_diarios[self.dias_transcurridos] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.costos_derivacion[self.dias_transcurridos] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]

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
        print(f"Largo de la lista de espera {len(self.lista_de_espera.pacientes_atendidos)}")
        for hospital in self.hospitales:
            print(hospital)

    def recopilar_informacion(self):
        informacion = {}
        for hospital in self.hospitales:
            informacion[hospital.nombre] = hospital.recopilar_informacion()
        informacion["WL"] = self.lista_de_espera.recopilar_informacion()
        return informacion
    
    def calcular_funcion_objetivo(self):
        muestra = []
        muestra_deri = []
        muestra_WL = []
        muestra_muer = []
        self.costos_muertos_hospitales_diarios_simulacion[self.numero_ejecucion] = self.costos_muertos_hospitales
        for i in ps.ID_DIAS_MUESTRAS:
            muestra.append(self.costos_diarios[i])
            muestra_deri.append(self.costos_derivacion[i])
            muestra_WL.append(self.costos_espera_WL[i])
            muestra_muer.append(self.costos_muertos_hospitales[i])
        costo_total = 0
        for hospital in self.hospitales:
            costo_total += hospital.costos_muertos
        print(f"Costo hospital: {costo_total}, costo derivacion: {self.costo_total_derivacion}, costos muertos WL: {self.costos_muertos_WL}" +
              f" estrategia: {self.estrategia.id}")
        
        promedio = sum(muestra)/len(muestra)
        promedio_WL = sum(muestra_WL) / len(muestra_WL)
        promedio_deri = sum(muestra_deri) / len(muestra_deri)
        promedio_muer = sum(muestra_muer) / len(muestra_muer)
        self.costos_espera_WL_simulacion[f"Simulación {self.numero_ejecucion}"] = promedio_WL
        self.costos_derivacion_simulacion[f"Simulación {self.numero_ejecucion}"] = promedio_deri
        self.costos_muertos_hospitales_simulacion[f"Simulación {self.numero_ejecucion}"] = promedio_muer
        self.funciones_objetivos[self.numero_ejecucion] = promedio
        print(f"Promedio diario: {promedio}")
        return promedio

    def resetear_simulacion(self):
        self.costos_diarios = {i : 0 for i in range(self.dias_de_simulacion)}
        self.numero_ejecucion += 1
        self.hospitales = []
        self.dias_transcurridos = 0
        self.jornadas_transcurridas = 0
        self.dias_de_simulacion = ps.DIAS_DE_SIMULACION
        self.lista_de_espera = ListaDeEspera()
        self.costo_total_derivacion = 0
        self.costos_muertos_WL = 0
        self.capacidad_cama_por_simulacion = {}
        self.costos_espera_WL = {i : 0 for i in range(self.dias_de_simulacion)}     # borrar este
        self.costos_derivacion = {i : 0 for i in range(self.dias_de_simulacion)}     # borrar este
        self.costos_muertos_hospitales = {i : 0 for i in range(self.dias_de_simulacion)}     # borrar este
        self.agregar_hospitales()

    def promedio_resultados(self):
        return sum(self.resultados)/len(self.resultados)