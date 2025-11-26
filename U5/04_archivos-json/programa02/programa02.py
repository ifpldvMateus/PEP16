from os import strerror
import json

try:
    capitales = [
        {"país": "Francia", "capital": "París"},
        {"país": "Australia", "capital": "Canberra"},
        {"país": "Kenia", "capital": "Nairobi"},
        {"país": "Brasil", "capital": "Brasilia"}
    ]

    with open("capitales.json", "w", encoding="utf-8") as capitales_json:
        json.dump(capitales, capitales_json, ensure_ascii=False, indent=4)
    
    print("Archivo 'capitales.json' creado correctamente")
    
except IOError as e:
    print("Error al escribir en el archivo:", strerror(e.errno))
    exit(e.errno)