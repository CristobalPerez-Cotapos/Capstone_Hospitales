from random import uniform, randint, seed
from parametros_hospitales import PROBABILIDADES_DE_TRANSICION
import parametros_simulacion as ps
import parametros_hospitales as ph
import scipy.stats as sp

seed(ps.SEED)

class Paciente():

    id = 0

    def __init__(self, grupo_diagnostico: int):
        super().__init__()
        self.id = Paciente.id
        Paciente.id += 1
        self.grupo_diagnostico = grupo_diagnostico
        self.tiempo_esperado = 0
        self.ruta_paciente = []
        self.definir_ruta_paciente()
        self.tiempo_atencion_unidad_actual = 0
        self.tiempo_a_esperar = None
        self.hospital_llegada = None

    def definir_ruta_paciente(self):
        if self.grupo_diagnostico >= 5:
            self.ruta_paciente = ["WL", "GA"]
        else:
            self.ruta_paciente = ["ED"]
        while self.ruta_paciente[-1] != "FIN":
            self.agregar_elemento_ruta()
        
    def agregar_elemento_ruta(self):
        azar = uniform(0, 100)
        probabilidades = PROBABILIDADES_DE_TRANSICION[self.grupo_diagnostico][self.ruta_paciente[-1]]
        probabilidad_acumulada = 0
        for i in probabilidades:
            probabilidad_acumulada += probabilidades[i]
            if azar <= probabilidad_acumulada:
                self.ruta_paciente.append(i)
                break

    def tiempo_espera(self, gravedad, unidad):

        if unidad != "GA" and unidad != "FIN":

            distribucion = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["DISTRIBUCION"]

            if distribucion == "lognorm":
                parametro_1 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][0]
                parametro_2 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][1]
                parametro_3 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][2]
                valor = sp.lognorm.rvs(s=parametro_1, loc=parametro_2, scale=parametro_3, size=1)[0]

            elif distribucion == "expon":
                parametro_1 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][0]
                parametro_2 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][1] 
                valor = sp.expon.rvs(loc=parametro_1, scale=parametro_2, size=1)[0]
            
            elif distribucion == "gamma":
                parametro_1 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][0]
                parametro_2 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][1]
                parametro_3 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][2]
                valor = sp.gamma.rvs(a=parametro_1, loc=parametro_2, scale=parametro_3, size=1)[0]
            
            elif distribucion == "norm":
                parametro_1 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][0]
                parametro_2 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][1]
                valor = sp.norm.rvs(loc=parametro_1, scale=parametro_2, size=1)[0]

            elif distribucion == "uniform":
                parametro_1 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][0]
                parametro_2 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][1]
                valor = sp.uniform.rvs(loc=parametro_1, scale=parametro_2, size=1)[0]

            elif distribucion == "beta":
                parametro_1 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][0]
                parametro_2 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][1]
                parametro_3 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][2]
                parametro_4 = ph.PARAMETROS_DISTRIBUCION_TIEMPO[gravedad][unidad]["PARAMETROS"][3]
                valor = sp.beta.rvs(a=parametro_1, b=parametro_2, loc=parametro_3, scale=parametro_4, size=1)[0]
                pass                

                ### pendienteee
            self.tiempo_a_esperar = valor / 2
            
        elif unidad == "GA" and unidad != "FIN":
            self.tiempo_a_esperar = 0

    @property
    def tiempo_esperado_muerto(self):
        return max(0, self.tiempo_atencion_unidad_actual - self.tiempo_a_esperar)

    def __str__(self):
        return f"Paciente {self.id} (grupo {self.grupo_diagnostico})"
    
if __name__ == "__main__":
    for i in range(101):
        grupo = randint(1, 8)
        paciente = Paciente(grupo)
        print(paciente, paciente.ruta_paciente)
