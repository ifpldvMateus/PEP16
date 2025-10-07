'''
Escribe un programa para jugar a una versión muy simplificada del black jack. En primer lugar el ordenador obtendrá un número aleatorio entre 17 y 21 (está será su jugada). A continuación el jugador ira sacando cartas (con valores entre 1 y 5), que se irán sumando para obtener su puntuación, hasta que el quiera. Si se pasa de 21 pierde, si obtiene una puntuación igual o menor que la banca pierde, y si obtiene una puntuación superior a la banca gana
'''

import random


banca = random.randrange(17, 22)
puntos_jugador = 0
seguir = True

while seguir:
    carta = random.randint(1, 5)
    puntos_jugador += carta
    print(f"Has sacado un {carta}. Total de puntos: {puntos_jugador}")

    if puntos_jugador > 21:
        print("Te has pasado de 21")
        break

    seguir = int(input("¿Quieres sacar otra carta? (si = 1, no = 0): "))


print(f"\nPuntuación final del jugador: {puntos_jugador}")
print(f"Puntuación de la banca: {banca}")


if puntos_jugador > 21 or puntos_jugador <= banca:
    print("Has perdido")
else:
    print("Has ganado")