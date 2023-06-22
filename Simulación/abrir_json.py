import json
from os.path import join
import parametros_simulacion as ps
import numpy as np

class Parametros:

    def __init__(self):
        pass
        
    def leer_parametros(self, llave): ## con esta podes extraer datos del json
        ruta = join("parametros.json")
        with open(ruta, "r") as archivo:
            diccionario_data = json.load(archivo)
        valor = diccionario_data[llave]
        return valor

    def editar_diccionario(self, llave):
        diccionario_json = self.leer_parametros(llave)
        nuevo_diccionario = {}

        if llave == "PROBABILIDADES_DE_TRANSICION":
            for i in diccionario_json:
                nuevo_diccionario[int(i)] = {}
                for j in diccionario_json[i]:
                    nuevo_diccionario[int(i)][j] = {}
                    for k in diccionario_json[i][j]:
                        nuevo_diccionario[int(i)][j][k] = diccionario_json[i][j][k]

        elif llave == "TASA_LLEGADA_HOSPITAL":
            for i in diccionario_json:
                nuevo_diccionario[i] = {}
                for j in diccionario_json[i]:
                    nuevo_diccionario[i][int(j)] = diccionario_json[i][j]

        elif llave == "CAMAS_POR_UNIDAD":
            for i in diccionario_json:
                nuevo_diccionario[i] = {}
                for j in diccionario_json[i]:
                    nuevo_diccionario[i][j] = diccionario_json[i][j]

        elif llave == "COSTOS_POR_UNIDAD":
            for i in diccionario_json:
                nuevo_diccionario[i] = {}
                for j in diccionario_json[i]:
                    nuevo_diccionario[i][j] = {}
                    for k in diccionario_json[i][j]:
                        nuevo_diccionario[i][j][int(k)] = diccionario_json[i][j][k]
        
        elif llave == "COSTOS_TRASLADO":
            for i in diccionario_json:
                nuevo_diccionario[i] = {}
                for j in diccionario_json[i]:
                    nuevo_diccionario[i][int(j)] = diccionario_json[i][j]

        elif llave == "COSTOS_DERIVACION":
            for i in diccionario_json:
                nuevo_diccionario[i] = {}
                for j in diccionario_json[i]:
                    nuevo_diccionario[i][int(j)] = diccionario_json[i][j]
        
        elif llave == "VALOR_RIESGO":
            for i in diccionario_json:
                nuevo_diccionario[i] = {}
                for j in diccionario_json[i]:
                    nuevo_diccionario[i][int(j)] = {}
                    for k in diccionario_json[i][j]:
                        nuevo_diccionario[i][int(j)][k] = {}
                        for r in diccionario_json[i][j][k]:
                            nuevo_diccionario[i][int(j)][k][int(r)] = diccionario_json[i][j][k][r]

        elif llave == "DISTRIBUCION_TIEMPO":
            for i in diccionario_json:
                nuevo_diccionario[int(i)] = {}
                for j in diccionario_json[i]:
                    nuevo_diccionario[int(i)][j] = diccionario_json[i][j]

        elif llave == "PARAMETROS_ESTRATEGIA_PRINCIPALES":
            for i in diccionario_json:
                nuevo_diccionario[int(i)] = {}
                for j in diccionario_json[i]:
                    nuevo_diccionario[int(i)][j] = {}
                    for k in diccionario_json[i][j]:
                        nuevo_diccionario[int(i)][j][k] = {}
                        for r in diccionario_json[i][j][k]:
                            lista_provisoria = []
                            lista_1 = diccionario_json[i][j][k][0]
                            lista_2 = diccionario_json[i][j][k][1]
                            valor = diccionario_json[i][j][k][2]
                            diccionario_provisorio_1 = {}
                            diccionario_provisorio_2 = {}
                            for gravedad in lista_1:
                                diccionario_provisorio_1[int(gravedad)] = lista_1[gravedad]
                            for gravedad in lista_2:
                                diccionario_provisorio_2[int(gravedad)] = lista_2[gravedad]
                            lista_provisoria.append(diccionario_provisorio_1)
                            lista_provisoria.append(diccionario_provisorio_2)
                            lista_provisoria.append(valor)
                            nuevo_diccionario[int(i)][j][k] = lista_provisoria   

        elif llave == "TIEMPOS_ESPERA":
            for i in diccionario_json:
                nuevo_diccionario[i] = {}
                for j in diccionario_json[i]:
                    nuevo_diccionario[i][int(j)] = diccionario_json[i][j]
        return nuevo_diccionario

class Archivos:
    
    def __init__(self, opcion):
        self.opcion = opcion
        self.accion()        

    def accion(self):
        if self.opcion == "crear":
            self.recetear_hojas()

        elif self.opcion == "editar":
            self.abrir_hojas()
            
    def recetear_hojas(self):
        self.hoja_fo_std = open(ps.RUTA_FUNCION_OBJETIVO_DESVIACION_ESTANDAR, "w")   
        self.hoja_fo = open(ps.RUTA_FUNCION_OBJETIVO, "w")
        self.hoja_cc = open(ps.RUTA_COSTOS_CAPACIDADES, "w")
        self.hoja_dh = open(ps.RUTA_DATOS_HOSPITALES, "w")
        self.hoja_cd = open(ps.RUTA_COSTOS_DERIVACIONES, "w")
        self.hoja_me = open(ps.RUTA_MEJOR_ESTRATEGIA, "w")
        self.poner_titulo_csv() # comentar si no trabajaras con los csv
        self.abrir_hojas()

    def poner_titulo_csv(self):
        self.hoja_cc.write(f"ITERACION-SIMULACION-DIA-JORNADA-ESTRATEGIA ID-HOSPITAL-COSTOS TOTALES JORNADA-COSTOS MUERTOS JORNADA\n")
        self.hoja_dh.write(f"ITERACION-SIMULACION-DIA-JORNADA-ESTRATEGIA ID-HOSPITAL\n")
        self.hoja_dh.write(f"ITERACION-SIMULACION-DIA-JORNADA-ESTRATEGIA DICCIONARIO DATOS HOSPITAL\n")
        self.hoja_cd.write(f"ITERACION-SIMULACION-DIA-JORNADA-ESTRATEGIA ID-COSTOS DERIVACION-CANTIDAD PACIENTES DERIVADOS-DICCIONARIO CANTIDAD PACIENTES GRAVEDAD\n")
        self.hoja_fo_std.write(f"PROMEDIO-DESVIACION ESTANDAR-ESTRATEGIA ID\n")
        self.hoja_fo.write(f"ITERACION-FUNCION OBJETIVO-ESTRATEGIA ID\n")

    def abrir_hojas(self):
        self.hoja_fo_std = open(ps.RUTA_FUNCION_OBJETIVO_DESVIACION_ESTANDAR, "a")   
        self.hoja_fo = open(ps.RUTA_FUNCION_OBJETIVO, "a")
        self.hoja_cc = open(ps.RUTA_COSTOS_CAPACIDADES, "a")
        self.hoja_dh = open(ps.RUTA_DATOS_HOSPITALES, "a")
        self.hoja_cd = open(ps.RUTA_COSTOS_DERIVACIONES, "a")
        self.hoja_me = open(ps.RUTA_MEJOR_ESTRATEGIA, "a")

    def escribir_resultados_simulacion(self, 
                            hospital, 
                            numero_iteracion, 
                            numero_simulacion, 
                            costo_total, 
                            costos_muertos, 
                            costos_derivacion, 
                            dia, 
                            jornada, 
                            cantidad_pacientes_derivados, 
                            diccionario_pacientes, 
                            estrategia_id, 
                            resultados, 
                            elegir):
        
        if elegir == "costos_capacidad":
            #self.hoja_cc.write(f"Iteracion - {numero_iteracion} - Simulacion - {numero_simulacion} - Dia - {dia} - Jornada - {jornada} - Estrategia id - {estrategia_id} - Hospital - {hospital.nombre} - Costos totales jornada - {costo_total} - Costos muertos jornada- {costos_muertos}\n")
            self.hoja_cc.write(f"{numero_iteracion}-{numero_simulacion}-{dia}-{jornada}-{estrategia_id}-{hospital.nombre}-{costo_total}-{costos_muertos}\n")

            self.hoja_dh.write(f"Iteracion - {numero_iteracion} - Simulacion - {numero_simulacion} - Dia - {dia} - Jornada - {jornada} - Estrategia id - {estrategia_id} - Hospital - {hospital.nombre}\n")
            self.hoja_dh.write(f"{hospital}\n")
            #self.hoja_dh.write(f"{numero_iteracion}-{numero_simulacion}-{dia}-{jornada}-{estrategia_id}-{hospital.nombre}\n")
            #dicionario_datos_hospital = self.sacar_datos_hospital(hospital)#***##***#
            #self.hoja_dh.write(f"{numero_iteracion}-{numero_simulacion}-{dia}-{jornada}-{estrategia_id}-{dicionario_datos_hospital}\n")   ## creo que esta no funcionara tan bien en csv, hay que verla
        
        elif elegir == "costos_derivaciones":
            #self.hoja_cd.write(f"Iteracion - {numero_iteracion} - Simulacion - {numero_simulacion} - Dia - {dia} - Jornada - {jornada} - Estrategi id - {estrategia_id} - Costo derivacion - {costos_derivacion} - Cantidad pacientes derivados - {cantidad_pacientes_derivados} - Cantidad pacientes gravedad {diccionario_pacientes}\n")
            self.hoja_cd.write(f"{numero_iteracion}-{numero_simulacion}-{dia}-{jornada}-{estrategia_id}-{costos_derivacion}-{cantidad_pacientes_derivados}-{diccionario_pacientes}\n")

        elif elegir == "funcion_objetivo_desviacion_estandar":
            #self.hoja_fo_std.write(f"Promedio resultados - {sum(resultados)/len(resultados)} - Desviacion estandar - {np.std(resultados)} - Estrategia id - {estrategia_id}\n")
            self.hoja_fo_std.write(f"{sum(resultados)/len(resultados)}-{np.std(resultados)}-{estrategia_id}\n")

    def escribir_resultados_simulador(self, numero_iteracion, valor, estrategia_id, mejor_estrategia, elegir):

        if elegir == "funcion_objetivo":
            #self.hoja_fo.write(f"Iteracion - {numero_iteracion} - Funcion objetivo - {valor} - Id estrategia - {estrategia_id}\n")
            self.hoja_fo.write(f"{numero_iteracion}-{valor}-{estrategia_id}\n")

        elif elegir == "mejor_estrategia":
            #self.hoja_me.write(f"Mejor estrategia - {mejor_estrategia}\n")
            self.hoja_me.write(f"{mejor_estrategia}\n")

    def sacar_datos_hospital(self, hospital): # VER ESTO, NO ESTA TERMINADO, SI NO SIRVE CHAO Y SE AREGGLA #***#

        diccionario_datos = {}
        diccionario_urgencias = {}
        diccionario_operatorio = {}
        diccionario_cuidados_intensivos = {}
        diccionario_cuidados_intermedios = {}
        diccionario_admision = {}

        diccionario_datos[hospital.nombre] = {}

        diccionario_urgencias["CAPACIDAD"] = hospital.urgencias.capacidad
        diccionario_operatorio["CAPACIDAD"] = hospital.operatorio.capacidad
        diccionario_cuidados_intensivos["CAPACIDAD"] = hospital.cuidados_intensivos.capacidad
        diccionario_cuidados_intermedios["CAPACIDAD"] = hospital.cuidados_intermedios.capacidad
        diccionario_admision["CAPACIDAD"] = hospital.admision.capacidad

        diccionario_datos[hospital.nombre]["ED"] = diccionario_urgencias
        diccionario_datos[hospital.nombre]["OR"] = diccionario_operatorio
        diccionario_datos[hospital.nombre]["ICU"] = diccionario_cuidados_intensivos
        diccionario_datos[hospital.nombre]["SDU_WARD"] = diccionario_cuidados_intermedios
        diccionario_datos[hospital.nombre]["GA"] = diccionario_admision

        return diccionario_datos


    def cerrar_hojas(self):
        self.hoja_fo_std.close()
        self.hoja_fo.close()
        self.hoja_cc.close()
        self.hoja_cd.close()

    def leer_estrategias(self):
        ruta = join("estrategias.json")
        with open(ruta, "r") as archivo:
            diccionario = json.load(archivo)
        diccionario_auxiliar = {}
        for key in diccionario.keys():
            diccionario_auxiliar[key] = {"Parametros principales": {}, "Parametros secundarios": {}}
            for key2 in diccionario[key]["Parametros principales"].keys():
                diccionario_auxiliar[key]["Parametros principales"][int(key2)] = {}
                for key3 in diccionario[key]["Parametros principales"][key2].keys():
                    diccionario_auxiliar[key]["Parametros principales"][int(key2)][key3] = {}
                    for key4 in diccionario[key]["Parametros principales"][key2][key3].keys():
                        lista = []
                        for elemento in diccionario[key]["Parametros principales"][key2][key3][key4]:
                            dicc = {}
                            if isinstance(elemento, dict):
                                for llave in elemento.keys():
                                    dicc[int(llave)] = elemento[llave]
                                lista.append(dicc)
                            else:
                                lista.append(elemento)
                        diccionario_auxiliar[key]["Parametros principales"][int(key2)][key3][key4] = lista
            diccionario_auxiliar[key]["Parametros secundarios"] = diccionario[key]["Parametros secundarios"]

        return diccionario_auxiliar


    def leer_resultados(self, nombre_archivo):
        #ruta = join("resultados_estrategias.json")
        #ruta = join("resultados_diarios_estrategias.json")
        ruta = join(nombre_archivo)
        with open(ruta, "r") as archivo:
            diccionario = json.load(archivo)
        return diccionario
    
    def guardar_resultados(self, diccionario, nombre_archivo):
        ruta = join(nombre_archivo)
        with open(ruta, 'w') as archivo:
            json.dump(diccionario, archivo)

