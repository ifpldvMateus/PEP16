from os import strerror
import csv

encabezado = ["Ciudad", "País", "Lugar emblemático"]
patrimonios = [
    {"Ciudad": "Roma", "País": "Italia", "Lugar emblemático": "Coliseo"},
    {"Ciudad": "El Cairo", "País": "Egipto", "Lugar emblemático": "Pirámides de Guiza"},
    {"Ciudad": "Kioto", "País": "Japón", "Lugar emblemático": "Templos históricos"}
]

try:
    with open("patrimonios.csv", "w") as patrimonios_csv:
        writer = csv.DictWriter(patrimonios_csv, fieldnames=encabezado, delimiter=";")

        writer.writeheader()
        writer.writerows(patrimonios)

    print("Archivo 'patrimonios.csv' generado correctamente")

except IOError as e:
    print("Error al escribir en el archivo:", strerror(e.errno))
    exit(e.errno)