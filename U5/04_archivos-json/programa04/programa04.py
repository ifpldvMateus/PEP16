import json

pais = {
    "nombre": "Islandia",
    "capital": "Reikiavik",
    "idiomas": ["Islandés", "Inglés"],
    "superficie_km2": 103000
}

cadena_json = json.dumps(pais, ensure_ascii=False, indent=2, sort_keys=True)

print(cadena_json)