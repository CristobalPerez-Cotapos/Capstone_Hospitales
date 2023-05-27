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
            sigma = ph.PARAMETROS_DISTRIBUCION_LOGNORMAL_TIEMPO[gravedad][unidad]["Sigma"]
            loc = ph.PARAMETROS_DISTRIBUCION_LOGNORMAL_TIEMPO[gravedad][unidad]["Loc"]
            scale = ph.PARAMETROS_DISTRIBUCION_LOGNORMAL_TIEMPO[gravedad][unidad]["Scale"]
            maximo = ph.PARAMETROS_DISTRIBUCION_LOGNORMAL_TIEMPO[gravedad][unidad]["Maximo"]
            minimo = ph.PARAMETROS_DISTRIBUCION_LOGNORMAL_TIEMPO[gravedad][unidad]["Minimo"]
            valor = sp.lognorm.rvs(loc=loc, s=sigma, scale=scale, size=1)[0]
            valor = min(maximo, valor)
            valor = max(minimo, valor)
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
