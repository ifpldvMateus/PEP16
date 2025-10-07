'''
- Escribe un programa para jugar a adivinar un número. En primer lugar la aplicación solicita genera un número aleatorio entre 1 y 20. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. El programa termina cuando se acierta el número. Puedes generar el número usando la función random.randrange(1, 21) para obtener un número aleatorio entre 1 y 20 (para ello debes poner import random al inicio del programa)
'''

import random


print("Adivinar el número con intentos ilimitados\n\n")

secreto = random.randrange(1, 21)

while True:
    numero = int(input("Introduce un número entre 1 y 20: "))
    
    if numero < secreto:
        print("El número es mayor")
    elif numero > secreto:
        print("El número es menor")
    else:
        print("Has acertado el número", secreto)
        break


print("\n")


print("Adivinar el número con 3 intentos\n\n")

secreto = random.randrange(1, 21)
intento = 0

while intento < 3:
    intento += 1
    numero = int(input(f"Intento {intento}/3: Introduce un número entre 1 y 20: "))
    
    if numero < secreto:
        print("El número es mayor")
    elif numero > secreto:
        print("El número es menor")
    else:
        print(f"Has acertado el número {secreto} en {intento} intentos")
        break
else: # Descubrí que un while en Python puede tener else, y se entra si no se ejecutó un break en él
    print(f"No has adivinado el número. Era {secreto}")