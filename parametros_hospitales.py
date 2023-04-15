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

CAMAS_POR_UNIDAD = {
    'H_1' :{'GA': 12, 'ED': 41, 'SDU_WARD': 245, 'OR': 9, 'ICU': 50},
    'H_2' :{'GA': 8, 'ED': 20, 'SDU_WARD': 135, 'OR': 5, 'ICU': 30},
    'H_3' :{'GA': 5, 'ED': 12, 'SDU_WARD': 95, 'OR': 3, 'ICU': 16}}

COSTOS_POR_UNIDAD = {
    'H_1':{
        'ED': {'1': 88.551790593792, '2': 160.496, '3': 91.615184584061, '4': 140.71856827666144, '5': 49.83116634162744, '6': 152.0673982047947, '7': 84.30966466177121, '8': 111.23742112701551},
        'GA': {'1': 66.413842945344, '2': 120.37200000000001, '3': 68.71138843804574, '4': 105.53892620749608, '5': 37.37337475622058, '6': 114.05054865359602, '7': 63.23224849632841, '8': 83.42806584526163}, 
        'OR': {'1': 44.275895296896, '2': 80.248, '3': 45.8075922920305, '4': 70.35928413833072, '5': 24.91558317081372, '6': 76.03369910239735, '7': 42.154832330885604, '8': 55.618710563507754}, 
        'ICU': {'1': 22.137947648448, '2': 40.124, '3': 22.90379614601525, '4': 35.17964206916536, '5': 12.45779158540686, '6': 38.016849551198675, '7': 21.077416165442802, '8': 27.809355281753877}, 
        'SDU_WARD': {'1': 11.068973824224, '2': 20.062, '3': 11.451898073007625, '4': 17.58982103458268, '5': 6.22889579270343, '6': 19.008424775599337, '7': 10.538708082721401, '8': 13.904677640876939}},

    'H_2':{
        'ED': {'1': 97.54837975124512, '2': 82.18526459413911, '3': 172.5738832176332, '4': 113.30612583706561, '5': 76.32740838702574, '6': 49.93067940471605, '7': 125.61706128526181, '8': 79.26232540567777},
        'GA': {'1': 73.16128481343384, '2': 61.638948445604335, '3': 129.4304124132249, '4': 84.9795943777992, '5': 57.245556290269306, '6': 37.44800955353704, '7': 94.21279596394636, '8': 59.44674405425833}, 
        'OR': {'1': 48.77418987562256, '2': 41.09263229706956, '3': 86.2869416088166, '4': 56.653062918532804, '5': 38.16370419351287, '6': 24.965339702358026, '7': 62.808530642630906, '8': 39.631162702838886}, 
        'ICU': {'1': 24.38709493781128, '2': 20.54631614853478, '3': 43.1434708044083, '4': 28.326531459266402, '5': 19.081852096756435, '6': 12.482669851179013, '7': 31.404265321315453, '8': 19.815581351419443}, 
        'SDU_WARD': {'1': 12.19354746890564, '2': 10.27315807426739, '3': 21.57173540220415, '4': 14.163265729633201, '5': 9.540926048378218, '6': 6.2413349255895065, '7': 15.702132660657727, '8': 9.907790675709721}},

    'H_3':{
        'ED': {'1': 162.353747988151, '2': 92.77329034125304, '3': 86.18080849736951, '4': 124.57322697794142, '5': 147.52062016060765, '6': 50.96405806530921, '7': 50.00531420203252, '8': 83.4053694889629},
        'GA': {'1': 121.76531099111327, '2': 69.57996775593978, '3': 64.63560637302713, '4': 93.42992023345606, '5': 110.64046512045573, '6': 38.223043548981906, '7': 37.50398565152439, '8': 62.55402711672218},
        'OR': {'1': 81.1768739940755, '2': 46.38664517062652, '3': 43.090404248684756, '4': 62.28661348897071, '5': 73.76031008030382, '6': 25.482029032654605, '7': 25.00265710101626, '8': 41.70268474448145},
        'ICU': {'1': 40.58843699703775, '2': 23.19332258531326, '3': 21.545202124342378, '4': 31.143306744485354, '5': 36.88015504015191, '6': 12.741014516327303, '7': 12.50132855050813, '8': 20.851342372240726}, 
        'SDU_WARD': {'1': 20.294218498518877, '2': 11.59666129265663, '3': 10.772601062171189, '4': 15.571653372242677, '5': 18.440077520075956, '6': 6.370507258163651, '7': 6.250664275254065, '8': 10.425671186120363}}}

COSTOS_TRASLADO = {'OR': {'1': 11.06, '2': 13.33, '3': 5.56, '4': 10.27, '5': 5.03, '6': 3.42, '7': 8.21, '8': 7.12}, 
                   'ICU': {'1': 4.94, '2': 6.09, '3': 2.23, '4': 4.45, '5': 2.11, '6': 1.36, '7': 3.56, '8': 3.16}, 
                   'SDU_WARD': {'1': 2.87, '2': 3.12, '3': 1.3, '4': 2.75, '5': 1.27, '6': 0.77, '7': 2.06, '8': 1.87}}

COSTOS_DERIVACION = {'OR': {'1': 2005.41327941982, '2': 2415.61034675992, '3': 1008.41486960933, '4': 1861.5825416618, '5': 912.45669865699, '6': 619.861579253242, '7': 1487.56669723246, '8': 1291.08942628276},
                     'ICU': {'1': 1864.05859173256, '2': 2297.97272407409, '3': 839.468705124632, '4': 1713.2005514875, '5': 797.6893283243201, '6': 514.845929678587, '7': 1344.50984975789, '8': 1192.08128639087}, 
                     'SDU_WARD': {'1': 1107.42139781389, '2': 1203.71996592045, '3': 500.19022524300294, '4': 1062.02869089599, '5': 491.001001553362, '6': 295.919849357805, '7': 796.4106515726999, '8': 722.289502801522}}

TIEMPOS_ESPERA_POR_UNIDAD ={
    'H_1':{
        'ED': {'1': 0.0, '2': 0.0, '3': 0.0, '4': 0.0},
        'ICU': {'1': 3.8180535966149507, '2': 5.702258726899384, '3': 1.4452214452214451, '4': 2.9028132992327365, '5': 1.861139896373057, '6': 1.335987261146497, '7': 3.455611390284757, '8': 3.0496760259179267},
        'OR': {'1': 0.20238095238095238, '2': 0.19540229885057472, '3': 0.09815950920245399, '4': 0.1619718309859155, '5': 0.006147540983606557, '6': 0.0, '7': 0.0889967637540453, '8': 0.07142857142857142}, 
        'SDU_WARD': {'1': 10.715076071922544, '2': 12.375232774674116, '3': 4.94488188976378, '4': 9.096368715083798, '5': 6.141160949868074, '6': 3.9970282317979198, '7': 10.414953271028038, '8': 9.511301636788776}, 
        'GA': {'5': 0.44765006979990696, '6': 0.11773940345368916, '7': 0.3980543169841913, '8': 0.28433734939759037}},

    'H_2': {
        'ED': {'1': 0.0, '2': 0.0, '3': 0.0, '4': 0.0}, 
        'SDU_WARD': {'1': 10.823275862068966, '2': 12.898026315789474, '3': 4.942965779467681, '4': 9.328530259365994, '5': 6.326152004787552, '6': 3.981164383561644, '7': 10.54069355980184, '8': 9.680575539568345}, 
        'ICU': {'1': 3.0738916256157633, '2': 5.344947735191638, '3': 1.4078947368421053, '4': 2.7443181818181817, '5': 1.9591346153846154, '6': 1.2636203866432338, '7': 3.5170068027210886, '8': 3.07667731629393}, 
        'OR': {'1': 0.18181818181818182, '2': 0.15833333333333333, '3': 0.10869565217391304, '4': 0.22058823529411764, '5': 0.01160092807424594, '6': 0.0, '7': 0.11602209944751381, '8': 0.03571428571428571}, 
        'GA': {'5': 0.5050825921219823, '6': 0.1882998171846435, '7': 0.4305343511450382, '8': 0.33534743202416917}},

    'H_3': {
        'ED': {'1': 0.0, '2': 0.0, '3': 0.0, '4': 0.0}, 
        'SDU_WARD': {'1': 10.996794871794872, '2': 12.271356783919598, '3': 4.810909090909091, '4': 9.345924453280318, '5': 6.415730337078652, '6': 3.9744094488188977, '7': 10.4304, '8': 9.559895833333334}, 
        'OR': {'1': 0.1568627450980392, '2': 0.08571428571428572, '3': 0.08333333333333333, '4': 0.16279069767441862, '5': 0.017543859649122806, '6': 0.0, '7': 0.07, '8': 0.15789473684210525}, 
        'ICU': {'1': 3.6551724137931036, '2': 6.247058823529412, '3': 1.4074074074074074, '4': 2.8666666666666667, '5': 2.043560606060606, '6': 1.3555555555555556, '7': 3.4324324324324325, '8': 3.181318681318681}, 
        'GA': {'5': 0.5498357064622125, '6': 0.3830227743271222, '7': 0.5817555938037866, '8': 0.48509485094850946}},

    'WL': {'5': 26.599492781896217, '6': 26.116410256410255, '7': 26.488067921064708, '8': 26.214850615114237}}

