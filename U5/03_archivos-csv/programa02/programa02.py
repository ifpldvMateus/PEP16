from os import strerror
import csv

try:
    with open("ciudades.csv") as capitales_csv:
        reader = csv.DictReader(capitales_csv)
        encabezado = reader.fieldnames
    
        print(" - ".join(encabezado), "\n")
    
        for fila in reader:
            print(f"La ciudad de {fila[encabezado[0]]} está en {fila[encabezado[1]]} y tiene {fila[encabezado[2]]} millones de habitantes")

except IOError as e:
    print("Error al leer el archivo:", strerror(e.errno))
    exit(e.errno)