import operaciones


a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))

print()

print(f"Suma: {operaciones.suma(a, b)}")
print(f"Resta: {operaciones.resta(a, b)}")
print(f"Multiplicación: {operaciones.multiplicacion(a, b)}")
print(f"División: {operaciones.division(a, b)}")