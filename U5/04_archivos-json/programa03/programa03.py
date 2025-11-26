import json

cadena_json = '''
[
    {"nombre": "Chile", "moneda": "Peso chileno"},
    {"nombre": "Egipto", "moneda": "Libra egipcia"}
]
'''

paises = json.loads(cadena_json)

print("Tipo:", type(paises))

for pais in paises:
    print(f"{pais['nombre']} usa la moneda {pais['moneda']}")