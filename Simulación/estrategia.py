class Estrategia:
    def __init__(self, parametros_estrategia:dict):
        self.parametros_estrategia = parametros_estrategia

    def generar_punteje_paciente(self, paciente, datos_hospital, hospital):
        parametros = self.parametros_estrategia[paciente.grupo_diagnostico][hospital]
        puntaje = 0
        for unidad in datos_hospital:
            for grupo_diagnostico in datos_hospital[unidad][0]: #pacientes en atencion
                puntaje += datos_hospital[unidad][0][grupo_diagnostico] * parametros[unidad][0][grupo_diagnostico]
            
            for grupo_diagnostico in datos_hospital[unidad][1]: #pacientes atendidos en espera
                puntaje += datos_hospital[unidad][1][grupo_diagnostico] * parametros[unidad][1][grupo_diagnostico]

            # Camas disponibles
            puntaje += datos_hospital[unidad][2] * parametros[unidad][2]
        return puntaje

        

    

    