from funciones import Parametros

PARAMETROS = Parametros()

VALOR_RIESGO = PARAMETROS.editar_diccionario("VALOR_RIESGO")

PROBABILIDADES_DE_TRANSICION = PARAMETROS.editar_diccionario("PROBABILIDADES_DE_TRANSICION")

TASA_LLEGADA_HOSPITAL = PARAMETROS.editar_diccionario("TASA_LLEGADA_HOSPITAL")

CAMAS_POR_UNIDAD = PARAMETROS.editar_diccionario("CAMAS_POR_UNIDAD")

COSTOS_POR_UNIDAD = PARAMETROS.editar_diccionario("COSTOS_POR_UNIDAD")

COSTOS_TRASLADO = PARAMETROS.editar_diccionario("COSTOS_TRASLADO")

COSTOS_DERIVACION = PARAMETROS.editar_diccionario("COSTOS_DERIVACION")

# ESTE NO SE DEBERIA USAR
TIEMPOS_ESPERA_POR_UNIDAD ={
    'H_1': {'ED': {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0}, 'ICU': {1: 10.0, 2: 13.0, 3: 1.0, 4: 3.0, 5: 1.0, 6: 1.0, 7: 8.0, 8: 2.0}, 'OR': {1: 0.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 0.0, 6: 0.0, 7: 1.0, 8: 1.0}, 'SDU_WARD': {1: 13.0, 2: 14.0, 3: 5.0, 4: 8.0, 5: 5.0, 6: 9.0, 7: 7.0, 8: 5.0}, 'GA': {5: 2, 6: 1.0, 7: 0.0, 8: 2}},
    'H_2': {'ED': {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0}, 'SDU_WARD': {1: 10.0, 2: 12.0, 3: 8.0, 4: 6.0, 5: 4.0, 6: 5.0, 7: 8.0, 8: 6.0}, 'ICU': {1: 3.0, 2: 2.0, 3: 2.0, 4: 13.0, 5: 1.0, 6: 1.0, 7: 11.0, 8: 3.0}, 'OR': {1: 1.0, 2: 1.0, 3: 1.0, 4: 0.0, 5: 0.0, 6: 0.0, 7: 0.0, 8: 0.0}, 'GA': {5: 2.0, 6: 0.0, 7: 0.0, 8: 2.0}},
    'H_3': {'ED': {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0}, 'SDU_WARD': {1: 16.0, 2: 8.0, 3: 4.0, 4: 11.0, 5: 6.0, 6: 4.0, 7: 6.0, 8: 5.0}, 'OR': {1: 0.0, 2: 0.0, 3: 0.0, 4: 0.0, 5: 1.0, 6: 0.0, 7: 0.0, 8: 1.0}, 'ICU': {1: 4.0, 2: 8.0, 3: 3.0, 4: 1.0, 5: 2.0, 6: 0.0, 7: 6.0, 8: 2.0}, 'GA': {5: 2.0, 6: 2.0, 7: 1.0, 8: 0.0}},
    'WL': {5: 0, 6: 0, 7: 0, 8: 0}} 

PARAMETROS_DISTRIBUCION_LOGNORMAL_TIEMPO = {
        5: {
            "SDU_WARD": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.5,
                "Loc": 0,
                "Scale": 11
            },
            "OR": {
                "Minimo":1,
                "Maximo":2,
                "Sigma": 1,
                "Loc": 0,
                "Scale": 0.1
            },
            "ICU": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.8,
                "Loc": 0,
                "Scale": 2.9
            }
        },
        6: {
            "SDU_WARD": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.5,
                "Loc": 0,
                "Scale": 11
            },
            "OR": {
                "Minimo":1,
                "Maximo":2,
                "Sigma": 1,
                "Loc": 0,
                "Scale": 0.1
            },
            "ICU": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.8,
                "Loc": 0,
                "Scale": 2.9
            }
        },
        7: {
            "SDU_WARD": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.5,
                "Loc": 0,
                "Scale": 11
            },
            "OR": {
                "Minimo":1,
                "Maximo":2,
                "Sigma": 1,
                "Loc": 0,
                "Scale": 0.1
            },
            "ICU": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.8,
                "Loc": 0,
                "Scale": 2.9
            }
        },
        8: {
            "SDU_WARD": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.5,
                "Loc": 0,
                "Scale": 17.5
            },
            "OR": {
                "Minimo":1,
                "Maximo":2,
                "Sigma": 1,
                "Loc": 0,
                "Scale": 0.3
            },
            "ICU": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.8,
                "Loc": 0,
                "Scale": 4.5
            }
        },
        1: {
            "SDU_WARD": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.4,
                "Loc": 0,
                "Scale": 20
            },
            "OR": {
                "Minimo":1,
                "Maximo":2,
                "Sigma": 1,
                "Loc": 0,
                "Scale": 0.5
            },
            "ICU": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 1,
                "Loc": 0,
                "Scale": 4.711
            }
        },
        2: {
            "SDU_WARD": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.5,
                "Loc": 0,
                "Scale": 11
            },
            "OR": {
                "Minimo":1,
                "Maximo":2,
                "Sigma": 1,
                "Loc": 0,
                "Scale": 0.1
            },
            "ICU": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.8,
                "Loc": 0,
                "Scale": 2.9
            }
        },
        4: {
            "SDU_WARD": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.5,
                "Loc": 0,
                "Scale": 17
            },
            "OR": {
                "Minimo":1,
                "Maximo":2,
                "Sigma": 1,
                "Loc": 0,
                "Scale": 0.45
            },
            "ICU": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.9,
                "Loc": 0,
                "Scale": 3.75
            }
        },
        3: {
            "SDU_WARD": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.5,
                "Loc": 0,
                "Scale": 11
            },
            "OR": {
                "Minimo":1,
                "Maximo":2,
                "Sigma": 1,
                "Loc": 0,
                "Scale": 0.1
            },
            "ICU": {
                "Minimo":1,
                "Maximo":55,
                "Sigma": 0.8,
                "Loc": 0,
                "Scale": 2.9
            }
        },
    }
