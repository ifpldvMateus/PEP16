'''
Escribe un programa que pida números hasta que se introduzca un cero. Debe imprimir la suma y la media de todos los números introducidos. Realiza dos versiones: una que utiliza la instrucción break y otra no
'''

print("Versión con break\n\n")

suma = 0
contador = 0

while True:
    numero = int(input("Introduce un número (0 para salir): "))
    if numero == 0:
        break

    suma += numero
    contador += 1

if contador > 0:
    print(f"Suma: {suma}, Media: {suma / contador}")
else:
    print("No introdujiste ningún número")


print("\n")

print("Versión sin break\n\n")

numero = -1
suma = 0
contador = 0

while numero != 0:
    numero = int(input("Dame un número (0 para salir): "))
    if numero != 0:
        suma += numero
        contador += 1

if contador > 0:
    print(f"Suma: {suma}, Media: {suma / contador}")
else:
    print("No introdujiste ningún número")