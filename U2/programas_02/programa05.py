'''
Escribe un programa que pida un número y muestre una lista de números desde 1 al número. Se debe controlar que el número no se menor que 1 ni mayor que 10, si es así se pedirá que si introduzca de nuevo, y así hasta que se introduzca el número correcto
'''

numero = 0

while numero < 1 or numero > 10:
    numero = int(input("Dame un número entre 1 y 10: "))

print(f"\nLista de números del 1 al {numero}:")
for i in range(1, numero + 1):
    print(i, end=" ")

print()