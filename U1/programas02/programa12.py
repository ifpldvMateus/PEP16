'''
Sabiendo que 1 milla equivale a 1,61 Km escribe un programa que pida un número de millas y un número de Km, muestre respectivamente el número de millas y kilómetros. Los resultados deben estar redondeados a 2 decimales
'''

millas = float(input("Dame la cantidad de millas: "))
km = float(input("Dame la cantidad de kilómetros: "))

print(f"{millas} millas son {round(millas * 1.61, 2)} km")
print(f"{km} km son {round(km / 1.61, 2)} millas")