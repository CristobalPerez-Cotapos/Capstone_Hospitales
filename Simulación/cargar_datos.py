import pandas as pd
import fitter as ft
import json
from os.path import join
import pandas as pd
import itertools as it
from scipy import stats
import matplotlib.pyplot as plt

class Datos_Registro:

    def __init__(self, nombre_archivo, nombre_hoja):
        self.nombre_archivo = nombre_archivo
        self.nombre_hoja = nombre_hoja
        datos = self.abrir_hoja()
        datos = self.ajustes_datos(datos)
        self.lista_datos = self.transformar_datos(datos)

    # funcion para abrir los datos
    def abrir_hoja(self):
        ruta = self.nombre_archivo
        datos = pd.read_excel(ruta, sheet_name= self.nombre_hoja)
        return datos

    def ajustes_datos(self, datos):
        if self.nombre_hoja == "Registros":
            datos.columns = ["ID", "START_TIMESTAMP", "COMPLETE_TIMESTAMP", "MS_DRG", "HOSPITAL", "UNIDAD"]
            datos["TIME"] = datos["COMPLETE_TIMESTAMP"] - datos["START_TIMESTAMP"]
            return datos

    def transformar_datos(self, datos):
        lista_datos = datos.values.tolist()
        return lista_datos

    # funciones principales

    def tiempos_espera(self):
        diccionario_tiempos_espera = {}
        unidades = ["WL"]
        grupos = [1, 2, 3, 4, 5, 6, 7, 8]
        valor = 0
        for unidad in unidades:
            for grupo in grupos:
                frase = f"{unidad} - {grupo}"
                diccionario_tiempos_espera[frase] = valor

        diccionario_tiempos_espera = self.mostrar_diccionario_bonito(diccionario_tiempos_espera, 2)

        return diccionario_tiempos_espera

    def distribucion_tiempo(self): 

        datos = self.sacar_tasas()
        datos = datos.values
        base_de_datos = []

        for dato in datos:
            primera_fila_lista = dato.tolist()
            primera_fila_separada = list(it.chain.from_iterable(
                str(elemento).split(',') for elemento in primera_fila_lista))
            base_de_datos.append(primera_fila_separada)

        grupos_diagnostico = [1, 2, 3, 4, 5, 6, 7, 8]
        unidad_medica = ["OR", "ICU", "SDU_WARD"]

        lista_combinaciones = []

        for grupo in grupos_diagnostico:
            for unidad in unidad_medica:
                combi = str(grupo) + str(unidad)
                lista_combinaciones.append(combi)

        diccionario_valores = {}

        for lista in lista_combinaciones:
            diccionario_valores[lista] = []

        for linea in base_de_datos:
            i = 0
            for elemento in linea:
                if elemento != "nan":
                    diccionario_valores[lista_combinaciones[i]].append(float(elemento))
                i += 1

        diccionario_valores_tiempo = {}

        for lista in lista_combinaciones:

            grupo = lista[0]
            unidad = lista[1:]
            datos = diccionario_valores[lista]
            distribuciones = ['lognorm', 'expon', 'norm', 'beta', 'uniform']
            resultados = []

            for dist_name in distribuciones:
                dist = getattr(stats, dist_name)
                params = dist.fit(datos)
                log_likelihood = dist.logpdf(datos, *params).sum()
                k = len(params)
                n = len(datos)
                aic = 2 * k - 2 * log_likelihood
                resultados.append({'DISTRIBUCION': dist_name,
                          'PARAMETROS': params, 'AIC': aic})
                
            resultados = sorted(resultados, key=lambda x: x['AIC'])
            frase = f"{grupo} - {unidad}"

            nuevo_diccionario = {}
            for resultado in resultados:
                nuevo_diccionario["DISTRIBUCION"] = resultado["DISTRIBUCION"]
                nuevo_diccionario["PARAMETROS"] = resultado["PARAMETROS"]
                diccionario_valores_tiempo[frase] = nuevo_diccionario
                break
            if grupo == "3" and unidad == "ICU":
                nuevo_diccionario["DISTRIBUCION"] = "lognorm"
                nuevo_diccionario["PARAMETROS"] = [0.70731469,0,2.0285367]
                diccionario_valores_tiempo[frase] = nuevo_diccionario
            elif unidad == "OR":
                nuevo_diccionario["DISTRIBUCION"] = "lognorm"
                if grupo == "1":
                    nuevo_diccionario["PARAMETROS"] = [0.2732350451844458,0,1.3142091070469946]
                elif grupo == "2":
                    nuevo_diccionario["PARAMETROS"] = [0.26049830399467266,0,1.297576513153843]
                elif grupo == "3":
                    nuevo_diccionario["PARAMETROS"] = [0.20702594867247723,0,1.2300144886097584]
                elif grupo == "4":
                    nuevo_diccionario["PARAMETROS"] = [0.2650591886409824,0,1.3035081263696362]
                elif grupo == "5":
                    nuevo_diccionario["PARAMETROS"] = [0.071635208787302,0,1.0742633907325323]
                elif grupo == "7":
                    nuevo_diccionario["PARAMETROS"] = [0.20234561427064507,0,1.2242710605503309]
                elif grupo == "8":
                    nuevo_diccionario["PARAMETROS"] = [0.18365536463378365,0,1.2016016373085456]
                
                if grupo == "6":
                    nuevo_diccionario["DISTRIBUCION"] = "None"
                    nuevo_diccionario["PARAMETROS"] = "None"
                diccionario_valores_tiempo[frase] = nuevo_diccionario
                
        diccionario_valores_tiempo = self.mostrar_diccionario_bonito(diccionario_valores_tiempo, 2)
        return diccionario_valores_tiempo

    def llegada_poisson(self):
        diccionario_probabilidad_llegada = {}

        for i in range(0, len(self.lista_datos)):
            registro = False
            if self.lista_datos[i][5] == "WL":
                # if self.lista_datos[i+1][5] != "PS":
                llegada = "WL"
                gravedad = self.lista_datos[i][3]
                #unidad_medica = self.lista_datos[i+2][5]
                frase = f"{llegada} - {gravedad}"
                registro = True
            if self.lista_datos[i][5] == "ED":
                if self.lista_datos[i+1][5] != "ED" and self.lista_datos[i-1][5] != "ED":
                    llegada = "ED"
                    gravedad = self.lista_datos[i][3]
                    #unidad_medica = self.lista_datos[i+1][5]
                    hospital = self.lista_datos[i][4]
                    frase = f"{hospital} - {gravedad}"
                    registro = True
                else:
                    if self.lista_datos[i+1][5] == "ED":
                        llegada = "ED"
                        gravedad = self.lista_datos[i+1][3]
                        hospital = self.lista_datos[i][4]
                        frase = f"{hospital} - {gravedad}"
                        registro = True
            
            if registro:
                if frase in diccionario_probabilidad_llegada:
                    diccionario_probabilidad_llegada[frase] += 1
                else:
                    diccionario_probabilidad_llegada[frase] = 1

        cantidad_dias = 395 
        diccionario_probabilidad_llegada = self.calcular_promedio(diccionario_probabilidad_llegada, cantidad_dias)
        diccionario_probabilidad_llegada = self.mostrar_diccionario_bonito(diccionario_probabilidad_llegada, 2)
        
        return diccionario_probabilidad_llegada

    def probabilidades_movimientos(self):
        diccionario_probabilidad_movimientos = {}
        for i in range(0, len(self.lista_datos) - 1):
            #if self.lista_datos[i][5] != "ED":
            gravedad = self.lista_datos[i][3]
            hospital_actual = self.lista_datos[i][4]
            hospital_siguiente = self.lista_datos[i+1][4]
            inicio = self.lista_datos[i][5]
            destino = self.lista_datos[i+1][5]
            id = self.lista_datos[i][0]
            frase = ""
            if (destino == "WL" or destino == "ED") and id != self.lista_datos[i+1][0] :
                frase = f"{gravedad} - {inicio} - FIN"
            elif hospital_actual == hospital_siguiente:
                frase = f"{gravedad} - {inicio} - {destino}"
            
            if frase != "":
                if frase in diccionario_probabilidad_movimientos:
                    diccionario_probabilidad_movimientos[frase] += 1
                else:     
                    diccionario_probabilidad_movimientos[frase] = 1
           
        diccionario_probabilidad_movimientos = self.calcular_probabilidad(diccionario_probabilidad_movimientos)
        diccionario_probabilidad_movimientos = self.mostrar_diccionario_bonito(diccionario_probabilidad_movimientos, 3)
        return diccionario_probabilidad_movimientos

    # sub-funciones
    def calcular_promedio(self, diccionario, cantidad_dias):
        cantidad_jornadas = cantidad_dias * 2
        for i in diccionario:
            diccionario[i] = diccionario[i] / cantidad_jornadas
        return diccionario

    def mostrar_diccionario_bonito(self, diccionario, numero): 
        diccionario = self.ordenar_diccionario(diccionario)
        diccionario_transi = {}
       
        if numero == 3:
            for i in diccionario:
                a = i.split(" - ")
                if a[0] in diccionario_transi.keys():
                    pass
                else:
                    diccionario_transi[a[0]] = {}

                if a[1] in diccionario_transi[a[0]].keys():
                    pass
                else:
                    diccionario_transi[a[0]][a[1]] = {}

                if a[-1] in diccionario_transi[a[0]][a[1]].keys():
                    pass
                else:
                    diccionario_transi[a[0]][a[1]][a[-1]] = diccionario[i]

            return diccionario_transi
      
        elif numero == 2:
            for i in diccionario:
                a = i.split(" - ")
                if a[0] in diccionario_transi.keys():
                    pass
                else:
                    diccionario_transi[a[0]] = {}

                if a[-1] in diccionario_transi[a[0]].keys():
                    pass
                else:
                    diccionario_transi[a[0]][a[-1]] = diccionario[i]
            return diccionario_transi
       
        elif numero == 4:
            for i in diccionario:
                a = i.split(" - ")
                if a[0] in diccionario_transi.keys():
                    pass
                else:
                    diccionario_transi[a[0]] = {}
                if a[1] in diccionario_transi[a[0]].keys():
                    pass
                else:
                    diccionario_transi[a[0]][a[1]] = {}

                if a[2] in diccionario_transi[a[0]][a[1]].keys():
                    pass
                else:
                    diccionario_transi[a[0]][a[1]][a[-1]] = {}

                if a[-1] in diccionario_transi[a[0]][a[1]][a[2]].keys():
                    pass
                else:
                    diccionario_transi[a[0]][a[1]][a[2]][a[-1]] = diccionario[i]
            return diccionario_transi
        
    def ordenar_diccionario(self, diccionario):
        nuevo_diccionario = {}
        llaves = sorted(diccionario.keys(), reverse = False, key = lambda x: x[-1])
        for llave in llaves:
            nuevo_diccionario[llave] = diccionario[llave]
        return nuevo_diccionario

    def calcular_probabilidad(self, diccionario):
        diccionario_sumas = {}
        for i in diccionario:
            parametros = i.split(" - ")
            frase = f"{parametros[0]} - {parametros[1]}"
            if frase in diccionario_sumas:
                diccionario_sumas[frase] += diccionario[i]
            else:
                diccionario_sumas[frase] = diccionario[i]
        for i in diccionario:
            parametros = i.split(" - ")
            frase = f"{parametros[0]} - {parametros[1]}"
            diccionario[i] = diccionario[i] / diccionario_sumas[frase] * 100
        return diccionario

    def estadia_jornada(self, TimeStamp1, TimeStamp2):
        n_jornadas = ((TimeStamp1 - TimeStamp2).days) * 2
        cantidad_horas = ((TimeStamp1 - TimeStamp2).seconds) / 3600

        if cantidad_horas >= 22:
            cantidad_horas = 24

        if 10 <= cantidad_horas <= 14:
            cantidad_horas = 12

        if cantidad_horas <= 3:
            cantidad_horas = 0

        n_jornadas += cantidad_horas // 12

        return n_jornadas

    def sacar_tasas(self):
    
        base_de_datos = []

        for dato in self.lista_datos:
            primera_fila_lista = dato

            primera_fila_separada = list(it.chain.from_iterable(
                str(elemento).split(',') for elemento in primera_fila_lista))
            
            base_de_datos.append(primera_fila_separada)

        hospitales = ["H1", "H2", "H3"]
        grupos_diagnostico = [1, 2, 3, 4, 5, 6, 7, 8]
        unidad_medica = ["OR", "ICU", "SDU_WARD"]
        lista_combinaciones = []

        for grupo in grupos_diagnostico:
            for unidad in unidad_medica:
                combi = str(grupo) + str(unidad)
                lista_combinaciones.append(combi)

        diccionario_hospital = {}
        diccionario_grupo_unidades = {}
    
        for llave in lista_combinaciones:
            diccionario_grupo_unidades[llave] = []

        for linea in base_de_datos:
            if linea[5] in unidad_medica:
                llave = str(linea[3]) + str(linea[5])
                tiempo_1 = pd.to_datetime(str(linea[1]))
                tiempo_2 = pd.to_datetime(str(linea[2]))
                cantidad_jornadas = self.estadia_jornada(tiempo_2, tiempo_1)
                valor = float(cantidad_jornadas)
                actual = diccionario_grupo_unidades[llave]
                actual.append(valor)
                diccionario_grupo_unidades[llave] = actual

        df_nuevo = pd.DataFrame.from_dict(
            diccionario_grupo_unidades, orient='index').transpose()

        return df_nuevo

class Datos_Costos:

    def __init__(self, nombre_archivo, nombre_hoja):
        self.nombre_archivo = nombre_archivo
        self.nombre_hoja = nombre_hoja
        datos = self.abrir_hoja()
        self.lista_datos = self.transformar_datos(datos)

    # funcion para abrir los datos
    def abrir_hoja(self):
        ruta = self.nombre_archivo
        datos = pd.read_excel(ruta, sheet_name= self.nombre_hoja)
        return datos

    def transformar_datos(self, datos):
        lista_datos = datos.values.tolist()
        return lista_datos

    # funciones principales
    def costos_operacionales(self):
        diccionario_costos_unidades = {}
        diccionario_costos_traslados = {}
        diccionario_costos_derivados = {}
        unidades = ['H_1','H_2','H_3']
        traslados = ['TRASLADO']
        derivados = ['PS']
        for centro in self.lista_datos:
            hospital = centro[-1]
            unidad = centro[0]
            if hospital in unidades:
                for severidad in range(1,9):
                    costo = centro[severidad]
                    diccionario_costos_unidades[f"{hospital} - {unidad} - {severidad}"] = costo
            elif hospital in traslados:
                for severidad in range(1,9):
                    costo = centro[severidad]
                    diccionario_costos_traslados[f"{unidad} - {severidad}"] = costo
            elif hospital in derivados:
                for severidad in range(1,9):
                    costo = centro[severidad]
                    diccionario_costos_derivados[f"{unidad} - {severidad}"] = costo
        diccionario_costos_unidades = self.mostrar_diccionario_bonito(diccionario_costos_unidades, 3)
        diccionario_costos_traslados = self.mostrar_diccionario_bonito(diccionario_costos_traslados, 2)
        diccionario_costos_derivados = self.mostrar_diccionario_bonito(diccionario_costos_derivados, 2)

        return diccionario_costos_unidades, diccionario_costos_traslados, diccionario_costos_derivados
    
    # sub-funciones
    def mostrar_diccionario_bonito(self, diccionario, numero): 
        diccionario = self.ordenar_diccionario(diccionario)
        diccionario_transi = {}
        if numero == 3:
            for i in diccionario:
                a = i.split(" - ")
                if a[0] in diccionario_transi.keys(): 
                    pass
                else:
                    diccionario_transi[a[0]] = {}
                if a[1] in diccionario_transi[a[0]].keys(): 
                    pass
                else:
                    diccionario_transi[a[0]][a[1]] = {}
                if int(a[-1]) in diccionario_transi[a[0]][a[1]].keys(): 
                    pass
                else:
                    diccionario_transi[a[0]][a[1]][int(a[-1])] = diccionario[i]
            return diccionario_transi
        
        elif numero == 2:
            for i in diccionario:
                a = i.split(" - ")
                if a[0] in diccionario_transi.keys(): # gravedad
                    pass
                else:
                    diccionario_transi[a[0]] = {}
                if a[-1] in diccionario_transi[a[0]].keys(): # unidad anterior
                    pass
                else:
                    diccionario_transi[a[0]][a[-1]] = diccionario[i]
            return diccionario_transi

    def ordenar_diccionario(self, diccionario):
        nuevo_diccionario = {}
        llaves = sorted(diccionario.keys(), reverse = False, key = lambda x: x[-1])
        for llave in llaves:
            nuevo_diccionario[llave] = diccionario[llave]
        return nuevo_diccionario

class Datos_Capacidad:

    def __init__(self, nombre_archivo, nombre_hoja):
        self.nombre_archivo = nombre_archivo
        self.nombre_hoja = nombre_hoja
        datos = self.abrir_hoja()
        self.lista_datos = self.transformar_datos(datos)

    # funcion para abrir los datos
    def abrir_hoja(self):
        ruta = self.nombre_archivo
        datos = pd.read_excel(ruta, sheet_name= self.nombre_hoja)
        return datos

    def transformar_datos(self, datos):
        lista_datos = datos.values.tolist()
        return lista_datos

    # funciones principales
    def capacidad_camas(self):
        diccionario_camas = {}
        categoria_unidades = {1:"OR", 2:"GA", 3:"ED", 4:"ICU", 5:"SDU_WARD"}
        cantidad_unidades = len(categoria_unidades)
        for fila in self.lista_datos:
            hospital = fila[0]
            for unidad_numerica in range(1, cantidad_unidades + 1):
                cantidad = fila[unidad_numerica]
                unidad = categoria_unidades[unidad_numerica]
                frase = f"{hospital} - {unidad}"
                diccionario_camas[frase] = cantidad
        diccionario_camas = self.mostrar_diccionario_bonito(diccionario_camas, 2)
        return diccionario_camas # le agregue gravedad para que fuera igual a los otros
        
    # sub-funciones
    def mostrar_diccionario_bonito(self, diccionario, numero): 
        diccionario = self.ordenar_diccionario(diccionario)
        diccionario_transi = {}
        if numero == 2:
            for i in diccionario:
                a = i.split(" - ")
                if a[0] in diccionario_transi.keys(): # gravedad
                    pass
                else:
                    diccionario_transi[a[0]] = {}
                if a[-1] in diccionario_transi[a[0]].keys(): # unidad anterior
                    pass
                else:
                    diccionario_transi[a[0]][a[-1]] = diccionario[i]
            return diccionario_transi

    def ordenar_diccionario(self, diccionario):
        nuevo_diccionario = {}
        llaves = sorted(diccionario.keys(), reverse = False, key = lambda x: x[-1])
        for llave in llaves:
            nuevo_diccionario[llave] = diccionario[llave]
        return nuevo_diccionario

class Datos_Riesgo():

    def __init__(self, nombre_archivo, lista_nombres_hojas):        
        self.diccionario_riesgos = {}
        self.nombre_archivo = nombre_archivo
        for nombre_hoja in lista_nombres_hojas:
            self.nombre_hoja = nombre_hoja
            datos = self.abrir_hoja()
            self.lista_datos = self.transformar_datos(datos)
            self.diccionario_riesgos[nombre_hoja] = self.lista_datos

    # funcion para abrir los datos
    def abrir_hoja(self):
        ruta = self.nombre_archivo
        datos = pd.read_excel(ruta, sheet_name= self.nombre_hoja)
        return datos

    def transformar_datos(self, datos):
        lista_datos = datos.values.tolist()
        return lista_datos

    # funciones principales
    def riesgo_operaciones(self):
        diccionario_riesgo = {}
        lista_severidades = ["MS-DRG 1",
                             "MS-DRG 2",
                             "MS-DRG 3",
                             "MS-DRG 4",
                             "MS-DRG 5",
                             "MS-DRG 6",
                             "MS-DRG 7",
                             "MS-DRG 8"]
        lista_unidades = ["OR", "GA", "ED", "ICU", "SDU_WARD", "PS"]
        for fila in self.diccionario_riesgos:
            unidad_origen = self.nombre_unidad_origen(fila)
            lista_datos = self.diccionario_riesgos[fila]
            for fila in lista_datos:
                elemento = fila[0]
                if elemento in lista_severidades:
                    severidad = self.severidad_caso(elemento)
                elif elemento == "Periodo":
                    periodo = len(fila)
                elif elemento in lista_unidades:
                    for i in range(1, periodo):
                        frase = f"{unidad_origen} - {severidad} - {elemento} - {i}"
                        diccionario_riesgo[frase] = fila[i]
        diccionario_riesgo = self.mostrar_diccionario_bonito(diccionario_riesgo, 4)
        return diccionario_riesgo

    # sub-funciones
    def nombre_unidad_origen(self, escriro):
        nombre = escriro.split(" ")[1]
        return nombre
    
    def severidad_caso(self, escriro):
        severidad = escriro.split(" ")[1]
        return severidad

    def mostrar_diccionario_bonito(self, diccionario, numero): 
        diccionario = self.ordenar_diccionario(diccionario)
        diccionario_transi = {}
        if numero == 4:
            for i in diccionario:
                a = i.split(" - ")
                if a[0] in diccionario_transi.keys():
                    pass
                else:
                    diccionario_transi[a[0]] = {}
                if int(a[1]) in diccionario_transi[a[0]].keys(): 
                    pass
                else:
                    diccionario_transi[a[0]][int(a[1])] = {}
                if a[2] in diccionario_transi[a[0]][int(a[1])].keys(): 
                    pass
                else:
                    diccionario_transi[a[0]][int(a[1])][a[2]] = {}
                if int(a[-1]) in diccionario_transi[a[0]][int(a[1])][a[2]].keys(): 
                    pass
                else:
                    diccionario_transi[a[0]][int(a[1])][a[2]][int(a[-1])] = diccionario[i]
            return diccionario_transi

    def ordenar_diccionario(self, diccionario):
        nuevo_diccionario = {}
        llaves = sorted(diccionario.keys(), reverse = False, key = lambda x: x[-1])
        for llave in llaves:
            nuevo_diccionario[llave] = diccionario[llave]
        return nuevo_diccionario

class Datos_vida():

    def __init__(self, nombre_archivo, nombre_hoja):        
        self.nombre_archivo = nombre_archivo
        self.nombre_hoja = nombre_hoja
        datos = self.abrir_hoja()
        self.lista_datos = self.transformar_datos(datos)

    # funcion para abrir los datos
    def abrir_hoja(self):
        ruta = self.nombre_archivo
        datos = pd.read_excel(ruta, sheet_name= self.nombre_hoja)
        return datos

    def transformar_datos(self, datos):
        lista_datos = datos.values.tolist()
        return lista_datos

    # funciones principales
    def valor_vida(self):
        diccionario_vida = {}
        lista_unidades = ["OR", "GA", "ED", "ICU", "SDU_WARD", "PS"]
        
        for fila in self.lista_datos:

            elemento = fila[0]

            if elemento == "Periodo":
                periodo = len(fila)
                
            elif elemento in lista_unidades:
                for i in range(1, periodo):
                    frase = f"{elemento} - {i}"
                    diccionario_vida[frase] = fila[i]
                            
        diccionario_vida = self.mostrar_diccionario_bonito(diccionario_vida, 2)
        return diccionario_vida

    # sub-funciones
    def mostrar_diccionario_bonito(self, diccionario, numero): 
        diccionario = self.ordenar_diccionario(diccionario)
        diccionario_transi = {}
        if numero == 2:
            for i in diccionario:
                a = i.split(" - ")
                if a[0] in diccionario_transi.keys(): 
                    pass
                else:
                    diccionario_transi[a[0]] = {}
                if int(a[-1]) in diccionario_transi[a[0]].keys(): 
                    pass
                else:
                    diccionario_transi[a[0]][int(a[-1])] = diccionario[i]
            return diccionario_transi

    def ordenar_diccionario(self, diccionario):
        nuevo_diccionario = {}
        llaves = sorted(diccionario.keys(), reverse = False, key = lambda x: x[-1])
        for llave in llaves:
            nuevo_diccionario[llave] = diccionario[llave]
        return nuevo_diccionario

class Datos_partida():

    def __init__(self, registros, costos, capacidad, riesgo, vida):        
        self.registros = registros
        self.costos = costos
        self.capacidad = capacidad
        self.riesgo = riesgo
        self.vida = vida
        self.llaves = ["PROBABILIDADES_DE_TRANSICION", 
                       "TASA_LLEGADA_HOSPITAL", 
                       "DISTRIBUCION_TIEMPO",
                       "CAMAS_POR_UNIDAD", 
                       "COSTOS_POR_UNIDAD", 
                       "COSTOS_TRASLADO", 
                       "COSTOS_DERIVACION", 
                       "VALOR_RIESGO", 
                       "PARAMETROS_ESTRATEGIA_PRINCIPALES",
                       "TIEMPOS_ESPERA"]

    def cargar_diccionarios(self):
        self.diccionario_registros_llegada_poisson = self.registros.llegada_poisson()
        self.diccionario_distribucion_tiempo = self.registros.distribucion_tiempo()
        self.diccionario_registros_probabilidades_movimientos = self.registros.probabilidades_movimientos()
        self.diccionario_costos_unidades_operacionales, self.diccionario_costos_traslados_operacionales, self.diccionario_costos_derivados_operacionales = self.costos.costos_operacionales()
        self.diccionario_capacidad_camas = self.capacidad.capacidad_camas()
        self.diccionario_riesgo_operaciones = self.riesgo.riesgo_operaciones()
        self.diccionario_parametros_estrategia_inicial = self.cargar_primera_estrategia()
        self.diccionario_tiempo_espera = self.registros.tiempos_espera()
        self.diccionario_general()
    
    def diccionario_general(self):

        self.diccionario_gen = {"PROBABILIDADES_DE_TRANSICION": self.diccionario_registros_probabilidades_movimientos,
                            "TASA_LLEGADA_HOSPITAL": self.diccionario_registros_llegada_poisson,
                            "DISTRIBUCION_TIEMPO": self.diccionario_distribucion_tiempo,
                            "CAMAS_POR_UNIDAD": self.diccionario_capacidad_camas,
                            "COSTOS_POR_UNIDAD": self.diccionario_costos_unidades_operacionales,
                            "COSTOS_TRASLADO": self.diccionario_costos_traslados_operacionales,
                            "COSTOS_DERIVACION": self.diccionario_costos_derivados_operacionales,
                            "VALOR_RIESGO": self.diccionario_riesgo_operaciones,
                            "PARAMETROS_ESTRATEGIA_PRINCIPALES": self.diccionario_parametros_estrategia_inicial,
                            "TIEMPOS_ESPERA": self.diccionario_tiempo_espera}
        
    def cargar_primera_estrategia(self):
        diccionario_estrategia = {}
        total_gravedades = 8
        total_unidades = ["ED","ICU","OR","SDU_WARD","GA"]
        hospitales = ["H_1","H_2","H_3","WL"]
        valor = 15
        lista = {1: valor, 2: valor, 3: valor, 4: valor, 5: valor, 6: valor, 7: valor, 8: valor}
        
        for gravedad in range(1,total_gravedades + 1):
            diccionario_estrategia[gravedad] = {}
            for hospital in hospitales:
                diccionario_estrategia[gravedad][hospital] = {}
                for unidad in total_unidades:
                    lista_temporal = []
                    lista_temporal.append(lista)
                    lista_temporal.append(lista)
                    if hospital == "WL": 
                        camas = 15  
                        lista_temporal.append(camas) 
                        diccionario_estrategia[gravedad][hospital][hospital] = lista_temporal
                    else:
                        camas = self.diccionario_capacidad_camas[hospital][unidad]
                        lista_temporal.append(camas)
                        diccionario_estrategia[gravedad][hospital][unidad] = lista_temporal

        return diccionario_estrategia

    def editar_parametros(self):
        ruta = join("parametros.json")
        with open(ruta, "r") as archivo:
            diccionario_data = json.load(archivo)
            for llave in self.llaves:
                diccionario_data[llave] = self.diccionario_gen[llave]
        with open(ruta, "w") as archivo:
            json.dump(diccionario_data, archivo, indent = 4)

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
                    nuevo_diccionario[i][j] = {}
                    for k in diccionario_json[i][j]:
                        nuevo_diccionario[i][j][int(k)] = diccionario_json[i][j][k]

        elif llave == "COSTOS_DERIVACION":
            for i in diccionario_json:
                nuevo_diccionario[i] = {}
                for j in diccionario_json[i]:
                    nuevo_diccionario[i][j] = {}
                    for k in diccionario_json[i][j]:
                        nuevo_diccionario[i][j][int(k)] = diccionario_json[i][j][k]
        
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
    
registros = Datos_Registro('Datos_Historicos_Hospital.xlsx','Registros')
costos = Datos_Costos('Datos_Historicos_Hospital.xlsx', 'Costos Operacionales')
capacidad = Datos_Capacidad('Datos_Historicos_Hospital.xlsx','Hospitales')
riesgo = Datos_Riesgo('Datos_Historicos_Hospital.xlsx', 
                       ['Riesgo WL', 
                        'Riesgo ED', 
                        'Riesgo GA', 
                        'Riesgo OR',
                        'Riesgo ICU', 
                        'Riesgo SDU_WARD'])
vida = Datos_vida('Datos_Historicos_Hospital.xlsx', 'Valor Estadístico de la Vida')
datos = Datos_partida(registros, costos, capacidad, riesgo, vida)

datos.cargar_diccionarios()
datos.editar_parametros()

