DIAS_DE_SIMULACION = 100

JORNADAS_POR_DIAS = 2

NUMERO_HOSPITALES = 1

NUMERO_SIMULACIONES_PARALELAS = 15

SEED = 12345

# ALGUNOS PARAMETROS QUE ESTÁN INCLUIDOS EN LA HOJA DE MATÍAS. ALGUNO PODRÍA SER ÚTIL PARA UN FUTURO
PERIODOS_RELEVANTES = 40 
PONDERADOR_ESPERAS = 1
CAPACIDAD_MAXIMA_LISTA_ESPERA = 2000
ANCHO_VENTANA_TEMPORAL_EN_HORAS = 12


PARAMETROS_ESTRATEGIA_PROVISORIOS = {
    1: {
   "H_1" :{
        "ED": [{1: 1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 41],
        "OR": [{1: 1, 2: 0, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 5],
        "ICU": [{1: 7, 2: 10, 3: 4, 4: 6, 5: 0, 6: 3, 7: 14, 8: 3}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 20, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 91],
        "GA": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]
   },
    "WL":{"WL":[{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]}
    },
   2: {
       "H_1" :{
        "ED": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 41],
        "OR": [{1: 1, 2: 0, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 5],
        "ICU": [{1: 7, 2: 10, 3: 4, 4: 6, 5: 0, 6: 3, 7: 14, 8: 3}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 20, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 91],
        "GA": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]
    },
    "WL":{"WL":[{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]}},
   3: {
       "H_1" :{
        "ED": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 41],
        "OR": [{1: 1, 2: 0, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 5],
        "ICU": [{1: 7, 2: 10, 3: 4, 4: 6, 5: 0, 6: 3, 7: 14, 8: 3}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 20, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 91],
        "GA": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]
    },
    "WL":{"WL":[{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]}},
   4: {
       "H_1" :{
        "ED": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 41],
        "OR": [{1: 1, 2: 0, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 5],
        "ICU": [{1: 7, 2: 10, 3: 4, 4: 6, 5: 0, 6: 3, 7: 14, 8: 3}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 20, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 91],
        "GA": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]
    },
    "WL":{"WL":[{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]}},
   5: {
       "H_1" :{
        "ED": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 41],
        "OR": [{1: 1, 2: 0, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 5],
        "ICU": [{1: 7, 2: 10, 3: 4, 4: 6, 5: 0, 6: 3, 7: 14, 8: 3}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 20, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 91],
        "GA": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]
    },
    "WL":{"WL":[{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]}},
   6: {
       "H_1" :{
        "ED": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 41],
        "OR": [{1: 1, 2: 0, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 5],
        "ICU": [{1: 7, 2: 10, 3: 4, 4: 6, 5: 0, 6: 3, 7: 14, 8: 3}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 20, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 91],
        "GA": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]
    },
    "WL":{"WL":[{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]}},
   7: {
       "H_1" :{
        "ED": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 41],
        "OR": [{1: 1, 2: 0, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 5],
        "ICU": [{1: 7, 2: 10, 3: 4, 4: 6, 5: 0, 6: 3, 7: 14, 8: 3}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 20, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 91],
        "GA": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]
    },
    "WL":{"WL":[{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]}},
   8: {
       "H_1" :{
        "ED": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 41],
        "OR": [{1: 1, 2: 0, 3: 3, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 5],
        "ICU": [{1: 7, 2: 10, 3: 4, 4: 6, 5: 0, 6: 3, 7: 14, 8: 3}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 3],
        "SDU_WARD": [{1: 37, 2: 31, 3: 20, 4: 18, 5: 7, 6: 7, 7: 22, 8: 12}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}, 91],
        "GA": [{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]
    },
    "WL":{"WL":[{1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 0, 8: 0}, {1: 0, 2: 0, 3: 0, 4: 0, 5: 2, 6: 2, 7: 1, 8: 0}, 5]}}
}
    