'''
Modifica el programa anterior par que pida en primer lugar el número de jugadores que van a jugar. Cada jugador irá jugando y el programa mostrará si ha ganado o no a la banca
'''

import random

banca = random.randrange(17, 22)


num_jugadores = int(input("¿Cuántos jugadores van a jugar?: "))

for jugador in range(1, num_jugadores + 1):
    print(f"\n--- Turno del Jugador {jugador} ---")
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

    print(f"\nPuntuación final del Jugador {jugador}: {puntos_jugador}")

    if puntos_jugador > 21 or puntos_jugador <= banca:
        print("Has perdido contra la banca")
    else:
        print("Has ganado contra la banca")