from os import strerror
import csv

try:
    with open("ciudades.csv") as ciudades_csv:
        reader = csv.reader(ciudades_csv, delimiter=",")
        
        encabezado = next(reader)
        print(" - ".join(encabezado), "\n")

        for fila in reader:
            print(f"La ciudad de {fila[0]} está en {fila[1]} y tiene {fila[2]} millones de habitantes")

except IOError as e:
    print("Error al leer el archivo:", strerror(e.errno))
    exit(e.errno)