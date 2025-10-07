'''
Escribe un programa que use un bucle while y le pida continuamente al usuario que introduzca un número hasta que ingrese 45 como la número de salida secreto, en cuyo caso el mensaje "¡Has dejado el bucle con éxito" debe imprimirse en la pantalla y el bucle
debe terminar. Haz dos dos versiones del programa
    - Versión 1: Utiliza el concepto de ejecución condicional y la instrucción break. En este caso el bucle no evaluará ninguna condición, es decir, será un bucle infinito
    - Versión 2: Realmente no es necesario usar la instrucción break. Diseña una solución donde no se use break y el bucle while controle la condición de salida
'''

print("Versión con break\n\n")

while True:
    numero = int(input("Dame un número (adivina el número secreto para salir): "))
    if numero == 45:
        print("¡Has dejado el bucle con éxito!")
        break
    else:
        print("Número incorrecto, intenta de nuevo\n")

print("\n")

print("Versión sin break\n\n")
numero = 0

while numero != 45:
    numero = int(input("Dame un número (adivina el número secreto para salir): "))
    if numero != 45:
        print("Número incorrecto, intenta de nuevo\n")

print("¡Has dejado el bucle con éxito!")