from random import seed, randint

NUMERO_CORAZONES = 5


DIAS_DE_SIMULACION = 500
#DIAS_SIMULACION_CAMBIO = 1000
JORNADAS_DE_SIMULACION = 1000
DIAS_TRANCIENTE = 200
MUESTRAS_POR_SIMULACION = 100

COSTO_VIDA = 6266

SIMULACIONES_POR_ESTRATEGIA = 10
SIMULACIONES_POR_MEJOR_ESTRATEGIA = 5
NUMERO_SIMULACIONES_PARALELAS = 10

JORNADAS_POR_DIAS = 2

NUMERO_HOSPITALES = 3


JORNADAS_TRANSIENTE = DIAS_TRANCIENTE * JORNADAS_POR_DIAS

NUMERO_ITERACIONES = 10

SEED = 697669

seed(SEED)
ID_DIAS_MUESTRAS = [randint(DIAS_TRANCIENTE, DIAS_DE_SIMULACION - 1) for i in range(MUESTRAS_POR_SIMULACION)]
ID_JORNADAS_MUESTRAS = [randint(JORNADAS_TRANSIENTE, JORNADAS_DE_SIMULACION - 1) for i in range(MUESTRAS_POR_SIMULACION)]

ANCHO_VENTANA_TEMPORAL_EN_HORAS = 12
TIEMPO_ESPERADO_MAXIMO = {1: 0,
                          2: 0,
                          3: 0,
                          4: 0,
                          5: 54,
                          6: 52,
                          7: 52,
                          8: 53,}



PARAMETROS_ESTRATEGIA_PRINCIPALES = {
    1: {
   "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_2" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_3" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}
    },
    2: {
   "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_2" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_3" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}
    },
    3: {
   "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_2" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_3" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}
    },
    4: {
   "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_2" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_3" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}
    },
    5: {
   "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_2" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_3" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}
    },
    6: {
   "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_2" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_3" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}
    },  
    7: {
   "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_2" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_3" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}
    },
    8: {
   "H_1" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_2" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
   "H_3" :{
        "ED": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 41],
        "OR": [{1: 15, 2: 15, 3: 3, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 5],
        "ICU": [{1: 15, 2: 19, 3: 4, 4: 6, 5: 15, 6: 3, 7: 14, 8: 3}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 3],
        "SDU_WARD": [{1: 15, 2: 31, 3: 29, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 15, 6: 15, 7: 15, 8: 9}, 15],
        "GA": [{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]
   },
    "WL":{"WL":[{1: 15, 2: 15, 3: 15, 4: 15, 5: 1, 6: 1, 7: 15, 8: 9}, {1: 15, 2: 15, 3: 15, 4: 15, 5: 2, 6: 2, 7: 1, 8: 9}, 5]}
    },
}

PARAMETROS_ESTRATEGIA_SECUNDARIOS = {
    "BUFFER": {
        "H_1": 0,
        "H_2": 0,
        "H_3": 0,
    },

    "NUMERO INICIO POLITICA": {
        "H_1": 6,
        "H_2": 6,
        "H_3": 6,
    },

     "NUMERO INICIO POLITICA ED": {
         "H_1": 1,
         "H_2": 1,
         "H_3": 1,
     },
}
    
    