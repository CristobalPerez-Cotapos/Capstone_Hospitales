import scipy.stats as sp
import parametros_hospitales as ph

para = ph.PARAMETROS_DISTRIBUCION_TIEMPO

lista = ["OR", 'ICU', 'SDU_WARD']

for i in range(1,9):
    for unidad in lista:
        diccionario = para[i][unidad]
        distribucion = diccionario["DISTRIBUCION"]
        parametros = diccionario["PARAMETROS"]

        if distribucion == "lognorm":

            valor = sp.lognorm.rvs(s=parametros[0], 
                                loc=parametros[1],
                                scale=parametros[2],
                                    size=1000)
        elif distribucion == "beta":

            valor = sp.beta.rvs(a=parametros[0],
                                b=parametros[1],
                                loc=parametros[2],
                                scale=parametros[3],
                                size=1000)
            
        print(f"Unidad: {unidad} - i: {i}")
        print(valor.mean())
