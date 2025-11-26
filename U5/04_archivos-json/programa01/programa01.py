from os import strerror
import json

try:
    with open("paises.json", "r", encoding="utf-8") as paises_json:
        paises = json.load(paises_json)

        for pais in paises:
            print(f"{pais['nombre']} está en {pais['continente']} y tiene {pais['poblacion']} millones de habitantes")

except IOError as e:
    print("Error al leer el archivo:", strerror(e.errno))
    exit(e.errno)