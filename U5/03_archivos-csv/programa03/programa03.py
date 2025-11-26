from os import strerror
import csv

encabezado = ["Ciudad", "País", "Continente"]
datos = [
    ["París", "Francia", "Europa"],
    ["Canberra", "Australia", "Oceanía"],
    ["Nairobi", "Kenia", "África"],
    ["Ottawa", "Canadá", "América"],
]

try:
    with open("capitales.csv", "w") as capitales_csv:
        writer = csv.writer(capitales_csv)

        writer.writerow(encabezado)
        writer.writerows(datos)

    print("Archivo 'capitales.csv' creado correctamente")

except IOError as e:
    print("Error al escribir en el archivo:", strerror(e.errno))
    exit(e.errno)