from os.path import join
import json

def editar_parametros(self):
        ruta = join("parametros.json")
        with open(ruta, "r") as archivo:
            diccionario_data = json.load(archivo)
            for llave in self.llaves:
                diccionario_data[llave] = self.diccionario_gen[llave]
        with open(ruta, "w") as archivo:
            json.dump(diccionario_data, archivo, indent = 4)

def leer_parametros(llave): ## con esta podes extraer datos del json
    ruta = join("parametros.json")
    with open(ruta, "r") as archivo:
        diccionario_data = json.load(archivo)
    valor = diccionario_data[llave]
    return valor