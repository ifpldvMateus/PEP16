from os import strerror
import json

def normalizar(cadena):
    return cadena.lower().translate(str.maketrans("áéíóúñ", "aeioun"))

try:
    filtrados = []
    with open("paises.json", "r", encoding="utf-8") as paises_json:
        paises = json.load(paises_json)
        
        continente = normalizar(input("Dame el nombre de un continente: "))
        filtrados = [pais for pais in paises if normalizar(pais['continente']) == continente]

    if filtrados:
        with open("paises_filtrados.json", "w", encoding="utf-8") as filtrados_json:
            json.dump(filtrados, filtrados_json, ensure_ascii=False, indent=4)
            
        print("Archivo 'paises_filtrados.json' creado correctamente")
    
    else:
        print("No se ha encontrado ningún país")

except IOError as e:
    print("Error al procesar archivos:", strerror(e.errno))
    exit(e.errno)
