import random as rd
from copy import deepcopy
import parametros_simulacion as ps
import parametros_hospitales as ph
class Estrategia:

    id = 0

    def __init__(self, parametros_estrategia:dict, parametros_secundarios:dict):
        self.parametros_estrategia = parametros_estrategia
        self.parametros_secundarios = parametros_secundarios
        self.id = Estrategia.id
        Estrategia.id += 1

    def reconstruir_parametros(self):
        nuevo_parametros = {}
        for grupo_diagnostico in self.parametros_estrategia:
            nuevo_parametros[int(grupo_diagnostico)] = {}
            for unidad in self.parametros_estrategia[int(grupo_diagnostico)]:
                nuevo_parametros[int(grupo_diagnostico)][unidad] = {}
                for tipo in self.parametros_estrategia[int(grupo_diagnostico)][unidad]:
                    nuevo_parametros[int(grupo_diagnostico)][unidad][int(tipo)] = {}
                    for subtipo in self.parametros_estrategia[int(grupo_diagnostico)][unidad][int(tipo)]:
                        nuevo_parametros[int(grupo_diagnostico)][unidad][int(tipo)][subtipo] = self.parametros_estrategia[grupo_diagnostico][unidad][tipo][subtipo]
        self.parametros_estrategia = nuevo_parametros

    def generar_punteje_paciente(self, paciente, datos_hospital, datos_WL, hospital):
        parametros = self.parametros_estrategia[paciente.grupo_diagnostico][hospital]
        puntaje = 0

# ####
#         unidades_futura = []
#         maximo_unidades_futuras = min(ps.NUMERO_UNIDADES_FUTURAS, len(paciente.ruta_paciente), 1)
#         grupo_diagnostico_persona = paciente.grupo_diagnostico
        
#         for i in range(1,maximo_unidades_futuras):
#             if len(paciente.ruta_paciente) != 0:
#                 unidades_futura.append(paciente.ruta_paciente[i])
# ####

        datos_WL = datos_WL["WL"]

        for unidad in datos_hospital:
            for i in range(0,2):
                for grupo_diagnostico in datos_hospital[unidad][i]: 
                    puntaje += datos_hospital[unidad][i][grupo_diagnostico] * parametros[unidad][i][grupo_diagnostico]
                for grupo_diagnostico in datos_WL[i]: 
                    puntaje += datos_WL[i][grupo_diagnostico] * self.parametros_estrategia[paciente.grupo_diagnostico]["WL"]["WL"][i][grupo_diagnostico]
        
            # Camas disponibles
            puntaje += datos_hospital[unidad][2] * parametros[unidad][2]

# ###
#         for unidad in unidades_futura:
#             for grupo_diagnostico in datos_hospital[unidad][0]: #pacientes en atencion
#                 puntaje += datos_hospital[unidad][0][grupo_diagnostico_persona] * parametros[unidad][0][grupo_diagnostico]
#             for grupo_diagnostico in datos_hospital[unidad][1]: #pacientes atendidos en espera
#                 puntaje += datos_hospital[unidad][1][grupo_diagnostico_persona] * parametros[unidad][1][grupo_diagnostico]
#             for grupo_diagnostico in datos_WL[0]: #pacientes en lista de espera
#                 puntaje += datos_WL[0][grupo_diagnostico_persona] * self.parametros_estrategia[paciente.grupo_diagnostico]["WL"]["WL"][0][grupo_diagnostico]
#             for grupo_diagnostico in datos_WL[1]:
#                 puntaje += datos_WL[1][grupo_diagnostico_persona] * self.parametros_estrategia[paciente.grupo_diagnostico]["WL"]["WL"][1][grupo_diagnostico]
# ###
        return puntaje
    
    def mutar_estrategia_fuerte(self):
        nueva_estrategia = deepcopy(self.parametros_estrategia)
        for grupo_diagnostico in nueva_estrategia:
            for hospital in nueva_estrategia[grupo_diagnostico]:
                for unidad in nueva_estrategia[grupo_diagnostico][hospital]:
                    for i in range(0,2):
                        for grupo in nueva_estrategia[grupo_diagnostico][hospital][unidad][i]:
                            nueva_estrategia[grupo_diagnostico][hospital][unidad][i][grupo] = nueva_estrategia[grupo_diagnostico][hospital][unidad][i][grupo] + rd.uniform(-20, 20)
                    nueva_estrategia[grupo_diagnostico][hospital][unidad][2] = nueva_estrategia[grupo_diagnostico][hospital][unidad][2] + rd.uniform(-20, 20)
        return nueva_estrategia 
    
    def mutar_estrategia_media(self):
        nueva_estrategia = deepcopy(self.parametros_estrategia)
        grupo_diagnostico = rd.choice(list(nueva_estrategia.keys()))
        hospital = rd.choice(list(nueva_estrategia[grupo_diagnostico].keys()))
        unidad = rd.choice(list(nueva_estrategia[grupo_diagnostico][hospital].keys()))
        indice = rd.choice([0, 1, 2])
        if indice == 0 or indice == 1:
            grupo = rd.choice(list(nueva_estrategia[grupo_diagnostico][hospital][unidad][indice].keys()))
            nueva_estrategia[grupo_diagnostico][hospital][unidad][indice][grupo] = nueva_estrategia[grupo_diagnostico][hospital][unidad][indice][grupo] + rd.uniform(-20, 20)
        else:
            nueva_estrategia[grupo_diagnostico][hospital][unidad][indice] = nueva_estrategia[grupo_diagnostico][hospital][unidad][indice] + rd.uniform(-20, 20)
        return nueva_estrategia
    def mutar_estrategia_media_unidad(self):
        nueva_estrategia = deepcopy(self.parametros_estrategia)
        unidad = rd.choice(["ICU","SDU_WARD","OR"])
        numero = rd.uniform(-10, 10)
        for grupo_diagnostico in nueva_estrategia:
            for hospital in nueva_estrategia[grupo_diagnostico]:
                if hospital != "WL":
                    for i in range(0,2):
                        for grupo in nueva_estrategia[grupo_diagnostico][hospital][unidad][i]:
                            nueva_estrategia[grupo_diagnostico][hospital][unidad][i][grupo] = nueva_estrategia[grupo_diagnostico][hospital][unidad][i][grupo] + numero
        return nueva_estrategia
    
    def mutar_estrategia_media_tipo_paciente(self):
        nueva_estrategia = deepcopy(self.parametros_estrategia)
        grupo_diagnostico = rd.choice(list(nueva_estrategia.keys()))
        numero = rd.uniform(-10, 10)
        for hospital in nueva_estrategia[grupo_diagnostico]:
            for unidad in nueva_estrategia[grupo_diagnostico][hospital]:
                for i in range(0,2):
                    for grupo in nueva_estrategia[grupo_diagnostico][hospital][unidad][i]:
                        nueva_estrategia[grupo_diagnostico][hospital][unidad][i][grupo] = nueva_estrategia[grupo_diagnostico][hospital][unidad][i][grupo] + numero
        return nueva_estrategia
    
    def mutar_estrategia_debil(self):
        nueva_estrategia = deepcopy(self.parametros_estrategia)
        grupo_diagnostico = rd.choice(list(nueva_estrategia.keys()))
        hospital = rd.choice(list(nueva_estrategia[grupo_diagnostico].keys()))
        unidad = rd.choice(list(nueva_estrategia[grupo_diagnostico][hospital].keys()))
        for i in range(0,2):
            for grupo in nueva_estrategia[grupo_diagnostico][hospital][unidad][i]:
                nueva_estrategia[grupo_diagnostico][hospital][unidad][i][grupo] = nueva_estrategia[grupo_diagnostico][hospital][unidad][i][grupo] + rd.uniform(-5, 5)
        nueva_estrategia[grupo_diagnostico][hospital][unidad][2] = nueva_estrategia[grupo_diagnostico][hospital][unidad][2] + rd.uniform(-5, 5)
        return nueva_estrategia
    
    def mutar_estrategia_muy_debil(self):
        nueva_estrategia = deepcopy(self.parametros_estrategia)
        grupo_diagnostico = rd.choice(list(nueva_estrategia.keys()))
        hospital = rd.choice(list(nueva_estrategia[grupo_diagnostico].keys()))
        unidad = rd.choice(list(nueva_estrategia[grupo_diagnostico][hospital].keys()))
        indice = rd.choice([0, 1, 2])
        if indice == 0 or indice == 1:
            grupo = rd.choice(list(nueva_estrategia[grupo_diagnostico][hospital][unidad][indice].keys()))
            nueva_estrategia[grupo_diagnostico][hospital][unidad][indice][grupo] = nueva_estrategia[grupo_diagnostico][hospital][unidad][indice][grupo] + rd.uniform(-2, 2)
        else:
            nueva_estrategia[grupo_diagnostico][hospital][unidad][indice] = nueva_estrategia[grupo_diagnostico][hospital][unidad][indice] + rd.uniform(-2, 2)
        return nueva_estrategia

    def mutar_parametros_secundarios(self):
        nueva_estrategia = deepcopy(self.parametros_secundarios)
        llave = rd.choice(list(nueva_estrategia.keys()))
        hospital = rd.choice(list(nueva_estrategia[llave].keys()))

        if llave == "BUFFER":
            nueva_estrategia[llave][hospital] = nueva_estrategia[llave][hospital] + rd.uniform(-2, 2)

        elif llave == "NUMERO INICIO POLITICA":
            lista = ["OR","ICU","SDU_WARD"]
            for unidad in lista:
                nueva_estrategia[llave][hospital][unidad] = max(nueva_estrategia[llave][hospital][unidad] + rd.randint(-2, 2), 0)

        elif llave == "NUMERO INICIO POLITICA ED":
            nueva_estrategia[llave][hospital] = max(nueva_estrategia[llave][hospital] + rd.randint(-2, 2), 0)


        return nueva_estrategia

        

        

    
