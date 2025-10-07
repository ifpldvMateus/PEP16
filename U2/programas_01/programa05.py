'''
Escribe un programa que pida dos números y que indique cuál es el menor, cuál el mayor o que indique que son iguales
'''

numero1 = int(input("Dame un número: "))
numero2 = int(input("Dame otro número: "))

if numero1 < numero2:
    print("El menor es", numero1, "y el mayor es", numero2)
elif numero1 > numero2:
    print("El menor es", numero2, "y el mayor es", numero1)
else:
    print("Los dos números son iguales")