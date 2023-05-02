import random as rd
from copy import deepcopy

class Estrategia:
    def __init__(self, parametros_estrategia:dict):
        self.parametros_estrategia = parametros_estrategia

    def generar_punteje_paciente(self, paciente, datos_hospital, datos_WL, hospital):
        parametros = self.parametros_estrategia[paciente.grupo_diagnostico][hospital]
        puntaje = 0
        for unidad in datos_hospital:
            for grupo_diagnostico in datos_hospital[unidad][0]: #pacientes en atencion
                puntaje += datos_hospital[unidad][0][grupo_diagnostico] * parametros[unidad][0][grupo_diagnostico]
            
            for grupo_diagnostico in datos_hospital[unidad][1]: #pacientes atendidos en espera
                puntaje += datos_hospital[unidad][1][grupo_diagnostico] * parametros[unidad][1][grupo_diagnostico]

            # Camas disponibles
            puntaje += datos_hospital[unidad][2] * parametros[unidad][2]

        datos_WL = datos_WL["WL"]

        for grupo_diagnostico in datos_WL[0]: #pacientes en lista de espera
            puntaje += datos_WL[0][grupo_diagnostico] * self.parametros_estrategia[paciente.grupo_diagnostico]["WL"]["WL"][0][grupo_diagnostico]
        for grupo_diagnostico in datos_WL[1]:
            puntaje += datos_WL[1][grupo_diagnostico] * self.parametros_estrategia[paciente.grupo_diagnostico]["WL"]["WL"][1][grupo_diagnostico]
        return puntaje
    
    def mutar_estrategia_fuerte(self):
        nueva_estrategia = deepcopy(self.parametros_estrategia)
        for grupo_diagnostico in nueva_estrategia:
            for hospital in nueva_estrategia[grupo_diagnostico]:
                for unidad in nueva_estrategia[grupo_diagnostico][hospital]:
                    for grupo in nueva_estrategia[grupo_diagnostico][hospital][unidad][0]:
                        nueva_estrategia[grupo_diagnostico][hospital][unidad][0][grupo] = nueva_estrategia[grupo_diagnostico][hospital][unidad][0][grupo] + rd.uniform(-10, 10)
                    for grupo in nueva_estrategia[grupo_diagnostico][hospital][unidad][1]:
                        nueva_estrategia[grupo_diagnostico][hospital][unidad][1][grupo] = nueva_estrategia[grupo_diagnostico][hospital][unidad][1][grupo] + rd.uniform(-10, 10)
                    nueva_estrategia[grupo_diagnostico][hospital][unidad][2] = nueva_estrategia[grupo_diagnostico][hospital][unidad][2] + rd.uniform(-10, 10)
        return nueva_estrategia 
    
    def mutar_estrategia_debil(self):
        nueva_estrategia = deepcopy(self.parametros_estrategia)
        grupo_diagnostico = rd.choice(list(nueva_estrategia.keys()))
        hospital = rd.choice(list(nueva_estrategia[grupo_diagnostico].keys()))
        unidad = rd.choice(list(nueva_estrategia[grupo_diagnostico][hospital].keys()))
        for grupo in nueva_estrategia[grupo_diagnostico][hospital][unidad][0]:
            nueva_estrategia[grupo_diagnostico][hospital][unidad][0][grupo] = nueva_estrategia[grupo_diagnostico][hospital][unidad][0][grupo] + rd.uniform(-5, 5)
        for grupo in nueva_estrategia[grupo_diagnostico][hospital][unidad][1]:
            nueva_estrategia[grupo_diagnostico][hospital][unidad][1][grupo] = nueva_estrategia[grupo_diagnostico][hospital][unidad][1][grupo] + rd.uniform(-5, 5)
        nueva_estrategia[grupo_diagnostico][hospital][unidad][2] = nueva_estrategia[grupo_diagnostico][hospital][unidad][2] + rd.uniform(-5, 5)
        return nueva_estrategia

        

    

    