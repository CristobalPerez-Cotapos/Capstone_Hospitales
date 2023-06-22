import parametros_simulacion as ps
import parametros_hospitales as ph
from hospital import Hospital
from sala_de_llegada import ListaDeEspera
from abrir_json import Archivos as ar
from estrategia import Estrategia
import random
random.seed(ps.SEED)

class Simulacion:
    def __init__(self, estrategia, resultados_simulaciones):
        self.numero_ejecucion = 1
        random.seed(ps.SEED)
        self.estrategia = estrategia
        self.hospitales = []
        self.dias_transcurridos = 0
        self.jornadas_transcurridas = 0
        self.dias_de_simulacion = ps.DIAS_DE_SIMULACION
        self.jornadas_de_simulacion = ps.JORNADAS_DE_SIMULACION
        self.lista_de_espera = ListaDeEspera()
        self.costo_total_derivacion = 0
        self.costos_muertos_WL = 0
        self.resultados = []   
        self.costos_jornada = {i : 0 for i in range(1, self.jornadas_de_simulacion + 1)}
        self.lista_kpis = ["Costos jornada", "Costos muertos", "Costos derivaciones", "Costos espera WL", "Costos traslados" ,"Derivaciones", "Espera WL", "Pacientes esperando", "Tasas ocupación"]
        self.diccionario_resultados_jornada = {j : 0 for j in self.lista_kpis}
        self.agregar_hospitales()
        self.funciones_objetivos = {}
        self.listorra = ["H_1", "H_2", "H_3", "WL"]
        self.resultados_simulaciones = resultados_simulaciones
        self.reacomodar_diccionarios_jornada()
        self.diccionario_resultados = {f"Simulación {i}" : {j : 0 for j in self.lista_kpis} for i in range(1, ps.SIMULACIONES_POR_ESTRATEGIA + 1)}
        self.reacomodar_diccionarios_simulacion(ps.SIMULACIONES_POR_ESTRATEGIA)
        self.diccionario_resultados_cambio = {f"Simulación {i}" : {j : 0 for j in self.lista_kpis} for i in range(1, ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA + 1)}
        

    def reacomodar_diccionarios_jornada(self):
        lista1 = ["H_1","H_2","H_3","WL"]
        lista2 = ["GA","OR","ICU","SDU_WARD"]
        listakpi1 = ["Costos muertos", "Costos traslados","Tasas ocupación"]
        for kpi in listakpi1:
            self.diccionario_resultados_jornada[kpi] = {i.nombre : {j : 0 for j in range(1, self.jornadas_de_simulacion + 1)} for i in self.hospitales}
        self.diccionario_resultados_jornada["Costos espera WL"] = {i : 0 for i in range(1, self.jornadas_de_simulacion + 1)}
        self.diccionario_resultados_jornada["Costos jornada"] = {i : 0 for i in range(1, self.jornadas_de_simulacion + 1)}
        self.diccionario_resultados_jornada["Costos derivaciones"] = {i : {j : 0 for j in range(1, self.jornadas_de_simulacion + 1)} for i in lista1}
        self.diccionario_resultados_jornada["Derivaciones"] = {i : {j : {k : 0 for k in range(1,9)} for j in range(1, self.jornadas_de_simulacion + 1)} for i in lista1}
        self.diccionario_resultados_jornada["Espera WL"] = {i : 0 for i in range(1, self.jornadas_de_simulacion + 1)}
        self.diccionario_resultados_jornada["Pacientes esperando"] = {i.nombre : {j : {k : 0 for k in lista2} for j in range(1, self.jornadas_de_simulacion + 1)} for i in self.hospitales}

    def reacomodar_diccionarios_simulacion(self, n_simulaciones):
        lista1 = ["H_1","H_2","H_3","WL"]
        listakpi1 = ["Costos muertos", "Costos traslados","Costos jornada","Tasas ocupación"]    
        for n_simulacion in range(1, n_simulaciones + 1):
            for kpi in listakpi1:
                self.diccionario_resultados[f"Simulación {n_simulacion}"][kpi] = {i.nombre : 0 for i in self.hospitales}
            self.diccionario_resultados[f"Simulación {n_simulacion}"]["Costos derivaciones"] = {i : 0 for i in lista1}
            self.diccionario_resultados[f"Simulación {n_simulacion}"]["Derivaciones"] = {i : 0 for i in lista1}
            self.diccionario_resultados[f"Simulación {n_simulacion}"]["Pacientes esperando"] = {i.nombre : 0 for i in self.hospitales}

    def calcular_promedios_kpis(self, kpi):
        listakpi1 = ["Costos muertos", "Costos traslados"]
        if kpi in listakpi1:
            for hospital in self.diccionario_resultados_jornada[kpi].keys():
                suma = 0
                for jornada in self.diccionario_resultados_jornada[kpi][hospital].keys():
                    if jornada in ps.ID_JORNADAS_MUESTRAS:
                        suma += self.diccionario_resultados_jornada[kpi][hospital][jornada] 
                self.diccionario_resultados[f"Simulación {self.numero_ejecucion}"][kpi][hospital] = suma / ps.MUESTRAS_POR_SIMULACION
        elif kpi == "Costos espera WL" or kpi == "Costos jornada":
            suma = 0
            for jornada in self.diccionario_resultados_jornada[kpi].keys():
                if jornada in ps.ID_JORNADAS_MUESTRAS:
                    suma += self.diccionario_resultados_jornada[kpi][jornada]
            self.diccionario_resultados[f"Simulación {self.numero_ejecucion}"][kpi] = suma / ps.MUESTRAS_POR_SIMULACION
        elif kpi == "Costos derivaciones":
            for hospital in self.diccionario_resultados_jornada[kpi].keys():
                suma = 0
                for jornada in self.diccionario_resultados_jornada[kpi][hospital].keys():
                    if jornada in ps.ID_JORNADAS_MUESTRAS:
                        suma += self.diccionario_resultados_jornada[kpi][hospital][jornada]
                self.diccionario_resultados[f"Simulación {self.numero_ejecucion}"][kpi][hospital] = suma / ps.MUESTRAS_POR_SIMULACION
                
        elif kpi == "Derivaciones":
            for hospital in self.diccionario_resultados_jornada[kpi].keys():
                suma = {i : 0 for i in range(1, 9)}
                for jornada in self.diccionario_resultados_jornada[kpi][hospital].keys():
                    if jornada in ps.ID_JORNADAS_MUESTRAS:
                        for grupo_diagnostico in self.diccionario_resultados_jornada[kpi][hospital][jornada].keys():
                            suma[grupo_diagnostico] += self.diccionario_resultados_jornada[kpi][hospital][jornada][grupo_diagnostico]
                self.diccionario_resultados[f"Simulación {self.numero_ejecucion}"][kpi][hospital] = {i : suma[i] / ps.MUESTRAS_POR_SIMULACION for i in range(1, 9)}
        elif kpi == "Espera WL":
            for jornada in self.diccionario_resultados_jornada[kpi].keys():
                suma = 0
                if jornada in ps.ID_JORNADAS_MUESTRAS:
                    suma += self.diccionario_resultados_jornada[kpi][jornada]
                self.diccionario_resultados[f"Simulación {self.numero_ejecucion}"][kpi] = suma / ps.MUESTRAS_POR_SIMULACION
        elif kpi == "Pacientes esperando":
            for hospital in self.diccionario_resultados_jornada[kpi].keys():
                suma = {i : 0 for i in ["ICU", "SDU_WARD", "OR", "GA"]}
                for jornada in self.diccionario_resultados_jornada[kpi][hospital].keys():
                    if jornada in ps.ID_JORNADAS_MUESTRAS:
                        for unidad in self.diccionario_resultados_jornada[kpi][hospital][jornada].keys():
                            suma[unidad] += self.diccionario_resultados_jornada[kpi][hospital][jornada][unidad]
                self.diccionario_resultados[f"Simulación {self.numero_ejecucion}"][kpi][hospital] = {i : suma[i] / ps.MUESTRAS_POR_SIMULACION for i in ["ICU", "SDU_WARD", "OR", "GA"]}
        elif kpi == "Tasas ocupación":
            for hospital in self.diccionario_resultados_jornada[kpi].keys():
                suma = {i : {j : 0 for j in ["ICU", "SDU_WARD", "OR"]} for i in range(1, 9)}
                for jornada in self.diccionario_resultados_jornada[kpi][hospital].keys():
                    if jornada in ps.ID_JORNADAS_MUESTRAS:
                        for grupo_diagnostico in self.diccionario_resultados_jornada[kpi][hospital][jornada].keys():
                            for unidad in self.diccionario_resultados_jornada[kpi][hospital][jornada][grupo_diagnostico].keys():
                                suma[grupo_diagnostico][unidad] += self.diccionario_resultados_jornada[kpi][hospital][jornada][grupo_diagnostico][unidad] / ps.MUESTRAS_POR_SIMULACION
                self.diccionario_resultados[f"Simulación {self.numero_ejecucion}"][kpi][hospital] = suma

        
    def agregar_hospitales(self):
        for i in range(ps.NUMERO_HOSPITALES):
            hospital = Hospital(f"H_{i+1}", simulacion=self)
            self.hospitales.append(hospital)

    def simular_miltiples_veces(self):
        for i in range(ps.SIMULACIONES_POR_ESTRATEGIA):
            self.simular()
            if i == ps.SIMULACIONES_POR_ESTRATEGIA - 1:
                self.resultados_simulaciones.append(self)
            self.resetear_simulacion()

    def simular_mejores_estrategias_multiples_veces(self):
        for i in range(ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA):
            self.simular()
            if i == ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA - 1:
                self.resultados_simulaciones.append(self)
            self.resetear_simulacion()
    
    def simular_cambio_estrategia_multiples_veces(self):
        for i in range(ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA):
            self.simular_cambio_estrategia()
            if i == ps.SIMULACIONES_POR_MEJOR_ESTRATEGIA - 1:
                self.resultados_simulaciones.append(self)
                self.promediar_resultados()
            self.resetear_simulacion()

    def simular(self):
        random.seed(ps.SEED * self.numero_ejecucion)
        for dia in range(self.dias_de_simulacion):
            for jornada in range(ps.JORNADAS_POR_DIAS):
                for hospital in self.hospitales:
                    hospital.simular_jornada()
                self.lista_de_espera.simular_jornada()
                self.trasladar_pacientes_lista_de_espera()
                self.jornadas_transcurridas += 1
                self.agregar_costos_jornada_hospitales_y_WL()
                for hospital in self.hospitales:
                    tasas_camas = hospital.revisar_capacidades_camas()
                    if tasas_camas != None:
                        self.diccionario_resultados_jornada["Tasas ocupación"][hospital.nombre][self.jornadas_transcurridas] = tasas_camas

                self.diccionario_resultados_jornada["Espera WL"][self.jornadas_transcurridas] = len(self.lista_de_espera.pacientes_atendidos)
                for hospital in self.hospitales:
                    for unidad in hospital.lista_de_unidades:
                        if unidad.codigo != 'ED':
                            self.diccionario_resultados_jornada["Pacientes esperando"][hospital.nombre][self.jornadas_transcurridas][unidad.codigo] = unidad.total_de_pacientes_atendidos
                        
                        if unidad.codigo == 'SDU_WARD' and 200 <=dia <= 230:
                            print(f" Hospital : {unidad.hospital} , Unidad: {unidad.codigo}, Jornada: {self.jornadas_transcurridas}, Camas disponibles : {unidad.camas_disponibles}")

            self.dias_transcurridos += 1
        
        for kpi in self.lista_kpis:
            self.calcular_promedios_kpis(kpi)
        self.resultados.append(self.calcular_funcion_objetivo())
        diccionario_tiempos = {}
        for hospital in self.hospitales:
            for unidad in hospital.lista_de_unidades:
                if unidad.codigo != 'ED':
                    diccionario_tiempos[f"{hospital.nombre} - {unidad.codigo}"] = unidad.diccionario_tiempos_espera
        ar('None').guardar_resultados(diccionario_tiempos, "tiempos.json")
        ar('None').guardar_resultados(self.diccionario_resultados, "resultados_paracachar.json")
                    
        

    def simular_cambio_estrategia(self):
        random.seed(ps.SEED * self.numero_ejecucion)
        self.jornadas_de_simulacion = ps.JORNADAS_CAMBIO_ESTRATEGIA
        self.dias_de_simulacion = ps.DIAS_CAMBIO_ESTRATEGIA
        self.costos_jornada = {i : 0 for i in range(1, self.jornadas_de_simulacion + 1)}
        self.diccionario_resultados_jornada = {j : 0 for j in self.lista_kpis}
        self.reacomodar_diccionarios_jornada()
        mejor_estrategia = Estrategia(ar('None').leer_estrategias()['Estrategia 1'])
        
        for dia in range(ps.DIAS_CAMBIO_ESTRATEGIA):
            if dia == self.dias_de_simulacion / 2 - 1:
                self.estrategia = mejor_estrategia
            for jornada in range(ps.JORNADAS_POR_DIAS):
                for hospital in self.hospitales:
                    hospital.simular_jornada()
                self.lista_de_espera.simular_jornada()
                self.trasladar_pacientes_lista_de_espera()
                self.jornadas_transcurridas += 1
                self.agregar_costos_jornada_hospitales_y_WL()
                for hospital in self.hospitales:
                    tasas_camas = hospital.revisar_capacidades_camas()
                    if tasas_camas != None:
                        self.diccionario_resultados_jornada["Tasas ocupación"][hospital.nombre][self.jornadas_transcurridas] = tasas_camas

                self.diccionario_resultados_jornada["Espera WL"][self.jornadas_transcurridas] = len(self.lista_de_espera.pacientes_atendidos)
                for hospital in self.hospitales:
                    for unidad in hospital.lista_de_unidades:
                        if unidad.codigo != 'ED':
                            self.diccionario_resultados_jornada["Pacientes esperando"][hospital.nombre][self.jornadas_transcurridas][unidad.codigo] = unidad.total_de_pacientes_atendidos
                        
                        # if unidad.codigo == 'SDU_WARD' and 200 <=dia <= 230:
                        #     print(f" Hospital : {unidad.hospital} , Unidad: {unidad.codigo}, Jornada: {self.jornadas_transcurridas}, Camas disponibles : {unidad.camas_disponibles}")
            self.dias_transcurridos += 1
        
                    
        for kpi in self.lista_kpis:
            self.diccionario_resultados_cambio[f"Simulación {self.numero_ejecucion}"][kpi] = self.diccionario_resultados_jornada[kpi]
        ar('None').guardar_resultados(self.diccionario_resultados, "resultados_paracachar.json")
        
    def promedio_resultados(self):
        for key in self.diccionario_resultados.keys():
            for kpi in self.diccionario_resultados[key].keys():
                pass

                    
    def agregar_costos_jornada_hospitales_y_WL(self):
        for hospital in self.hospitales:
            costos_totales, costos_muertos = hospital.calcular_costos_jornada()
            self.costos_jornada[self.jornadas_transcurridas] += costos_muertos
            self.diccionario_resultados_jornada["Costos muertos"][hospital.nombre][self.jornadas_transcurridas] = costos_muertos
            self.diccionario_resultados_jornada["Costos jornada"][self.jornadas_transcurridas] += costos_muertos

        
        costos_totales, costos_muertos = self.lista_de_espera.calcular_costos_jornada()
        self.costos_jornada[self.jornadas_transcurridas] += costos_muertos
        self.diccionario_resultados_jornada["Costos espera WL"][self.jornadas_transcurridas] = costos_muertos
        self.diccionario_resultados_jornada["Costos jornada"][self.jornadas_transcurridas] += costos_muertos

        self.costos_muertos_WL += costos_muertos
    def ordenar_pacientes_listos(self, pacientes_listos):
        pacientes = {5: [], 6: [], 7: [], 8: []}
        for paciente in pacientes_listos:
            if paciente.grupo_diagnostico == 5:
                pacientes[5].append(paciente)
            elif paciente.grupo_diagnostico == 6:
                pacientes[6].append(paciente)
            elif paciente.grupo_diagnostico == 7:
                pacientes[7].append(paciente)
            elif paciente.grupo_diagnostico == 8:
                pacientes[8].append(paciente)
        lista_pacientes = pacientes[8] + pacientes[7] + pacientes[6] + pacientes[5]
        return lista_pacientes
    
    def trasladar_pacientes_lista_de_espera(self):
        pacientes_listos = self.lista_de_espera.pacientes_listos_para_trasladar("GA")
        #pacientes_listos = self.ordenar_pacientes_listos(pacientes_listos)
        if self.estrategia.id == 0:
            for paciente in pacientes_listos:
                ruta = paciente.ruta_paciente[1]
                if paciente.tiempo_esperado_muerto >= 51:
                    hospitales_camas = []
                    for hospital in self.hospitales:
                        for unidad in hospital.lista_de_unidades:
                            if unidad.codigo == ruta:
                                unidad_paciente = unidad
                        hospitales_camas.append([hospital, unidad_paciente.camas_disponibles])
                    hospitales_camas.sort(key=lambda x: x[1], reverse=True)
                    if hospitales_camas[0][1] > 0:
                        self.lista_de_espera.retirar_paciente(paciente)
                        hospitales_camas[0][0].admision.agregar_paciente(paciente)
                        hospitales_camas[0][0].desplazamiento_entre_unidades()
                    else:
                        if paciente.tiempo_esperado_muerto >= ps.TIEMPO_ESPERADO_MAXIMO[paciente.grupo_diagnostico]:
                            self.diccionario_resultados_jornada["Derivaciones"]["WL"][self.jornadas_transcurridas][paciente.grupo_diagnostico] += 1
                            self.derivar_paciente(paciente)

                        


        else:
            for paciente in pacientes_listos:
                
                puntajes, hospitales = self.generar_puntaje_paciente(paciente)
                ruta = paciente.ruta_paciente[1]
                condicion = False
                indice = 0
                while not condicion:
                    hospital = hospitales[indice]
                    for unidad in hospital.lista_de_unidades:
                        if unidad.codigo == ruta:
                            unidad_paciente = unidad
                    puntaje = puntajes[indice]
                    if hospital.admision.camas_disponibles > 0 and puntaje >= 0:
                        self.lista_de_espera.retirar_paciente(paciente)
                        hospital.admision.agregar_paciente(paciente)
                        hospital.desplazamiento_entre_unidades()
                        condicion = True
                    elif (hospital.admision.camas_disponibles > 0 
                        and unidad_paciente.camas_disponibles > self.estrategia.parametros_secundarios["NUMERO INICIO POLITICA"][hospital.nombre][unidad_paciente.codigo]):
                        self.lista_de_espera.retirar_paciente(paciente)
                        hospital.admision.agregar_paciente(paciente)
                        hospital.desplazamiento_entre_unidades()
                        condicion = True
                    elif puntaje < 0:
                        self.diccionario_resultados_jornada["Derivaciones"]["WL"][self.jornadas_transcurridas][paciente.grupo_diagnostico] += 1

                        self.derivar_paciente(paciente)
                        condicion = True
                    else:
                        if indice == 2:
                            if paciente.tiempo_esperado_muerto >= ps.TIEMPO_ESPERADO_MAXIMO[paciente.grupo_diagnostico]:
                                self.diccionario_resultados_jornada["Derivaciones"]["WL"][self.jornadas_transcurridas][paciente.grupo_diagnostico] += 1
                                self.derivar_paciente(paciente)
                            condicion = True
                    indice += 1

    def derivar_paciente(self, paciente, ED = False):
        if not ED:
            self.lista_de_espera.retirar_paciente(paciente)
            destino = paciente.ruta_paciente[1]
            self.costo_total_derivacion += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.costos_jornada[self.jornadas_transcurridas] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.diccionario_resultados_jornada["Costos derivaciones"]["WL"][self.jornadas_transcurridas] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.diccionario_resultados_jornada["Costos jornada"][self.jornadas_transcurridas] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
        else:
            destino = paciente.ruta_paciente[0]
            self.costo_total_derivacion += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.costos_jornada[self.jornadas_transcurridas] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.diccionario_resultados_jornada["Costos derivaciones"][paciente.hospital_llegada][self.jornadas_transcurridas] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
            self.diccionario_resultados_jornada["Costos jornada"][self.jornadas_transcurridas] += ph.COSTOS_DERIVACION[destino][paciente.grupo_diagnostico]
    def generar_puntaje_paciente(self, paciente, hospital_actual_ED=""):
        
        informacion = self.recopilar_informacion()
        lista_puntajes = []
        for hospital in self.hospitales:
            datos = informacion[hospital.nombre]
            datos_WL = informacion["WL"]
            puntaje = self.estrategia.generar_punteje_paciente(paciente, datos, datos_WL, hospital.nombre)
            if hospital.nombre == hospital_actual_ED:
                puntaje += self.estrategia.parametros_secundarios["BUFFER"][hospital.nombre]
            lista_puntajes.append([hospital, puntaje])
        
        lista_puntajes.sort(key=lambda x: x[1], reverse=True)
        orden_hospitales = [i[0] for i in lista_puntajes]
        orden_puntajes = [i[1] for i in lista_puntajes]
        return orden_puntajes, orden_hospitales

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
        
        costo_total = 0
        for hospital in self.hospitales:
            costo_total += hospital.costos_muertos
        print(f"Costo hospital: {costo_total}, costo derivacion: {self.costo_total_derivacion}, costos muertos WL: {self.costos_muertos_WL}" +
              f" estrategia: {self.estrategia.id}")
        
        promedio = self.diccionario_resultados[f"Simulación {self.numero_ejecucion}"]["Costos jornada"]
        
        
        self.funciones_objetivos[self.numero_ejecucion] = promedio
        print(f"Promedio diario: {promedio}")
        return promedio

    def resetear_simulacion(self):
        
        self.numero_ejecucion += 1
        self.hospitales = []
        self.dias_transcurridos = 0
        self.jornadas_transcurridas = 0
        self.agregar_hospitales()
        self.dias_de_simulacion = ps.DIAS_DE_SIMULACION
        self.jornadas_de_simulacion = ps.JORNADAS_DE_SIMULACION
        self.lista_de_espera = ListaDeEspera()
        self.costo_total_derivacion = 0
        self.costos_muertos_WL = 0
        self.costos_jornada = {i : 0 for i in range(1, self.jornadas_de_simulacion + 1)}
        self.lista_kpis = ["Costos jornada", "Costos muertos", "Costos derivaciones", "Costos espera WL", "Costos traslados" ,"Derivaciones", "Espera WL", "Pacientes esperando", "Tasas ocupación"]
        self.diccionario_resultados_jornada = {j : 0 for j in self.lista_kpis}
        self.reacomodar_diccionarios_jornada()
        

    def promedio_resultados(self):
        return sum(self.resultados)/len(self.resultados)
    
    def trasladar_paciente(self, paciente, hospital):
        #print(f"El paciente {paciente.id} se traslada al hospital {hospital.nombre}")
        if hospital.urgencias.camas_disponibles > 0:
            hospital.urgencias.agregar_paciente(paciente)
            self.diccionario_resultados_jornada["Costos traslados"][paciente.hospital_llegada][self.jornadas_transcurridas] += ph.COSTOS_TRASLADO[paciente.ruta_paciente[0]][paciente.grupo_diagnostico]
            self.diccionario_resultados_jornada["Costos jornada"][self.jornadas_transcurridas] += ph.COSTOS_TRASLADO[paciente.ruta_paciente[0]][paciente.grupo_diagnostico]
            self.costos_jornada[self.jornadas_transcurridas] += ph.COSTOS_TRASLADO[paciente.ruta_paciente[0]][paciente.grupo_diagnostico]
        else:
            self.derivar_paciente(paciente, ED=True)