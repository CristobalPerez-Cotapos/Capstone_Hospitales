from simulacion import Simulacion
from estrategia import Estrategia
import parametros_simulacion as ps
import random
from threading import Thread
random.seed(ps.SEED)
from copy import deepcopy
import scipy.stats as st
import numpy as np


class Analisis:
    def __init__(self, estrategia_inicial, estrategia_optima):
        self.estrategia_inicial = estrategia_inicial
        self.estrategia_optima = estrategia_optima
        self.intervalo_confianza_derivaciones = []
        self.intervalo_confianza_espera_WL = []
        self.intervalo_confianza_costos_muertos = []
        self.condicion_WL = True
        self.condicion_costos_muertos = True
        self.condicion_derivaciones = True
        self.intervalo_de_confianza()
    
    def intervalo_de_confianza(self):
        valores_WL = list(self.estrategia_optima.costos_espera_WL_simulacion.values())
        print(valores_WL)
        valores_costos_muertos = list(self.estrategia_optima.costos_muertos_hospitales_simulacion.values())
        print(valores_costos_muertos)
        valores_derivaciones = list(self.estrategia_optima.costos_derivacion_simulacion.values())
        print(valores_derivaciones)

        if len(valores_WL) < 30:
            self.intervalo_confianza_espera_WL = st.t.interval(confidence = 0.95, df = len(valores_WL),loc = np.mean(valores_WL), scale = st.sem(valores_WL))
            self.intervalo_confianza_costos_muertos = st.t.interval(confidence = 0.95, df = len(valores_costos_muertos), loc = np.mean(valores_costos_muertos), scale = st.sem(valores_costos_muertos))
            self.intervalo_confianza_derivaciones = st.t.interval(confidence = 0.95, df = len(valores_derivaciones), loc = np.mean(valores_derivaciones), scale = st.sem(valores_derivaciones))
        else:
            self.intervalo_confianza_espera_WL = st.norm.interval(confidence = 0.95, loc = np.mean(valores_WL), scale = st.sem(valores_WL))
            self.intervalo_confianza_costos_muertos = st.norm.interval(confidence = 0.95, loc = np.mean(valores_costos_muertos), scale = st.sem(valores_costos_muertos))
            self.intervalo_confianza_derivaciones = st.norm.interval(confidence = 0.95, loc = np.mean(valores_derivaciones), scale = st.sem(valores_derivaciones))
    
    def chequear_intervalo(self):
        valores_WL_inicial = list(self.estrategia_inicial.costos_espera_WL_simulacion.values())
        valores_costos_muertos_inicial = list(self.estrategia_inicial.costos_muertos_hospitales_simulacion.values())
        valores_derivaciones_inicial = list(self.estrategia_inicial.costos_derivacion_simulacion.values())

        
        for valor in valores_WL_inicial:
            if self.intervalo_confianza_espera_WL[0] > valor or self.intervalo_confianza_espera_WL[1] < valor:
                self.condicion_WL = False

        for valor in valores_costos_muertos_inicial:
            if self.intervalo_confianza_costos_muertos[0] > valor or self.intervalo_confianza_costos_muertos[1] < valor:
                self.condicion_costos_muertos = False

        for valor in valores_derivaciones_inicial:
            if self.intervalo_confianza_derivaciones[0] > valor or self.intervalo_confianza_derivaciones[1] < valor:
                self.condicion_derivaciones = False
        
        
        print(self.intervalo_confianza_espera_WL)
        print("")
        print(valores_WL_inicial)
        print("")
        print("")
        print(self.intervalo_confianza_costos_muertos)
        print("")
        print(valores_costos_muertos_inicial)
        print("")
        print("")
        print(self.intervalo_confianza_derivaciones)
        print("")
        print(valores_derivaciones_inicial)


