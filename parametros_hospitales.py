PROBABILIDADES_DE_TRANSICION = {
    1: {
        'ED': {'ICU': 23.531933133304758, 'SDU_WARD': 66.05229318474068, 'OR': 10.415773681954565},
        'ICU': {'OR': 7.663197729422895, 'SDU_WARD': 92.3368022705771},
        'OR': {'ICU': 95.39295392953929, 'SDU_WARD': 4.607046070460704},
        'SDU_WARD': {'FIN': 92.06787687450671, 'ICU': 6.156274664561957, 'OR': 1.7758484609313336}
    },
    2: {
        'ED': {'ICU': 23.168214654282764, 'SDU_WARD': 65.53147574819401, 'OR': 11.30030959752322},
        'ICU': {'SDU_WARD': 91.26891734575088, 'OR': 8.731082654249127},
        'SDU_WARD': {'FIN': 93.17307692307692, 'OR': 1.6826923076923077, 'ICU': 5.144230769230769},
        'OR': {'ICU': 92.09726443768997, 'SDU_WARD': 7.90273556231003}
        },
    3: {
        'ED': {'OR': 25.635808748728383, 'ICU': 43.641912512716175, 'SDU_WARD': 30.722278738555442},
        'OR': {'ICU': 92.73927392739274, 'SDU_WARD': 7.2607260726072615},
        'ICU': {'SDU_WARD': 94.37908496732025, 'OR': 5.620915032679739},
        'SDU_WARD': {'FIN': 93.97705544933078, 'ICU': 5.25812619502868, 'OR': 0.7648183556405354},
        'PS': {'FIN': 100.0}
        },
    4: {
        'ED': {'ICU': 23.30300909727082, 'SDU_WARD': 64.45066480055984, 'OR': 12.24632610216935},
        'ICU': {'SDU_WARD': 89.22852983988355, 'OR': 10.771470160116449},
        'SDU_WARD': {'FIN': 91.24600638977635, 'ICU': 8.498402555910543, 'OR': 0.25559105431309903},
        'OR': {'ICU': 87.35177865612648, 'SDU_WARD': 12.648221343873518},
        'PS': {'FIN': 100.0}
        },
    5: {
        'GA': {'OR': 22.001725625539258, 'ICU': 22.993960310612596, 'SDU_WARD': 55.00431406384815},
        'OR': {'ICU': 89.28571428571429, 'SDU_WARD': 10.714285714285714},
        'ICU': {'SDU_WARD': 96.55913978494624, 'OR': 3.4408602150537635},
        'SDU_WARD': {'FIN': 94.1510966693745, 'ICU': 3.736799350121852, 'OR': 2.1121039805036554},
        'PS': {'FIN': 100.0}
        },
    6: {
        'GA': {'OR': 44.81103779244151, 'ICU': 45.830833833233356, 'SDU_WARD': 9.358128374325135},
        'OR': {'ICU': 91.18279569892474, 'SDU_WARD': 8.817204301075268},
        'ICU': {'SDU_WARD': 90.24822695035462, 'OR': 9.75177304964539},
        'SDU_WARD': {'FIN': 94.44759206798867, 'OR': 1.019830028328612, 'ICU': 4.53257790368272},
        'PS': {'FIN': 100.0}
        },
    7: {
        'GA': {'SDU_WARD': 59.93575034419458, 'OR': 19.022487379531896, 'ICU': 21.04176227627352},
        'SDU_WARD': {'FIN': 92.46764269043072, 'ICU': 5.6227455972841085, 'OR': 1.9096117122851686},
        'OR': {'ICU': 97.79661016949153, 'SDU_WARD': 2.2033898305084745},
        'ICU': {'SDU_WARD': 88.82705479452055, 'OR': 11.172945205479452}
        },
    8: {
        'GA': {'OR': 19.200351493848856, 'SDU_WARD': 60.72056239015817, 'ICU': 20.07908611599297},
        'OR': {'ICU': 90.14373716632443, 'SDU_WARD': 9.856262833675565},
        'ICU': {'SDU_WARD': 97.28601252609603, 'OR': 2.7139874739039667},
        'SDU_WARD': {'FIN': 96.35901778154107, 'ICU': 2.6248941574936495, 'OR': 1.0160880609652836}
    }
}

# Tasa de llegada de pacientes a los hospitales por cada grupo de diagnositico
TASA_LLEGADA_HOSPITAL = {
    "H_1" :{1: 1,
            2: 1,
            3: 1,
            4: 1},

    "H_2" :{1: 1,
            2: 1,
            3: 1,
            4: 1},

    "H_3" :{1: 1,
            2: 1,
            3: 1,
            4: 1},

    "WL"  :{5: 1,
            6: 1,
            7: 1,
            8: 1}
}


