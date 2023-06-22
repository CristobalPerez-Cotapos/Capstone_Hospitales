from random import seed, randint
import math
import psutil

# Obtener información sobre la CPU
cpu_info = psutil.cpu_count()

######### IMPORTANTES

NUMERO_CORAZONES = math.trunc(cpu_info * 0.5)
DIAS_DE_SIMULACION = 500
SIMULACIONES_POR_ESTRATEGIA = 5
NUMERO_SIMULACIONES_PARALELAS = 8
# NUMERO_UNIDADES_FUTURAS = 1 #####
NUMERO_ITERACIONES = 200

SIMULACIONES_POR_MEJOR_ESTRATEGIA = 100

######### CAMBIAR ESTOOOOOOO
#########
COSTO_VIDA = 6266 # TRINI=0, DANI=500, JAVI=3133, PANCHO=62660
SEED = 610579 # TRINI=11117, DANI=22227, JAVI=333337, PANCHO=44447
#########
#########

seed(SEED)

######### NO IMPORTANTES

JORNADAS_POR_DIAS = 2
NUMERO_HOSPITALES = 3
ANCHO_VENTANA_TEMPORAL_EN_HORAS = 12

######### PARAMETROS DE SIMULACION DEPENDIENTES - no tocar si no se sabe lo que se hace

#DIAS_SIMULACION_CAMBIO = math.trunc(DIAS_DE_SIMULACION * 0.5)

NUMERO_SIMULACIONES_MEZCLA = math.trunc(NUMERO_SIMULACIONES_PARALELAS * 0.2)
DIAS_TRANCIENTE = math.trunc(DIAS_DE_SIMULACION * 0.2)
MUESTRAS_POR_SIMULACION = math.trunc(DIAS_DE_SIMULACION * 0.2)

JORNADAS_TRANSIENTE = DIAS_TRANCIENTE * JORNADAS_POR_DIAS
JORNADAS_DE_SIMULACION = DIAS_DE_SIMULACION * JORNADAS_POR_DIAS

ID_DIAS_MUESTRAS = [randint(DIAS_TRANCIENTE, DIAS_DE_SIMULACION - 1) for i in range(MUESTRAS_POR_SIMULACION)]
ID_JORNADAS_MUESTRAS = [randint(JORNADAS_TRANSIENTE, JORNADAS_DE_SIMULACION - 1) for i in range(MUESTRAS_POR_SIMULACION)]



### CAMBIO DE ESTRATEGIA ###

DIAS_CAMBIO_ESTRATEGIA = 1000
JORNADAS_CAMBIO_ESTRATEGIA = DIAS_CAMBIO_ESTRATEGIA * JORNADAS_POR_DIAS


TIEMPO_ESPERADO_MAXIMO = {1: 0,
                          2: 0,
                          3: 0,
                          4: 0,
                          5: 53,
                          6: 53,
                          7: 54,
                          8: 54,}

PARAMETROS_ESTRATEGIA_SECUNDARIOS = {
    "BUFFER": {
        "H_1": 0,
        "H_2": 0,
        "H_3": 0,
    },

    "NUMERO INICIO POLITICA": {
        "H_1": {
            "SDU_WARD": 6,
            "ICU": 4,
            "OR": 3,
        },
        "H_2": {
            "SDU_WARD": 6,
            "ICU": 3,
            "OR": 2,
        },
        "H_3": {
            "SDU_WARD": 6,
            "ICU": 3,
            "OR": 2,
        }
    },

     "NUMERO INICIO POLITICA ED": {
         "H_1": 1,
         "H_2": 1,
         "H_3": 1,
     },
}
    
    