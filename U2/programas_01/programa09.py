'''
- Escribe un programa en Python que simule el juego de piedra, papel o tijera. En primer lugar el programa tendrá que mostrar un mensaje por pantalla al usuario para preguntarle qué opción desea elegir. Por ejemplo:
    1. Piedra
    2. Papel
    3. Tijera
    Seleccione una opción (1, 2 o 3):
- Después de leer la opción seleccionada por el usuario el programa generará un número
aleatorio para simular una jugada y mostrará un mensaje indicando si el usuario ha ganado o ha perdido dependiendo del resultado
- Ten en cuenta que:
    - La piedra gana a la tijera pero pierde contra el papel
    - El papel gana a la piedra pero pierde contra la tijera
    - La tijera gana al papel pero pierde contra la piedra
'''

import random

print("1. Piedra")
print("2. Papel")
print("3. Tijera")
usuario = int(input("Selecciona una opción: "))
programa = random.randint(1, 3)

print("Elegiste:", usuario)
print("El programa eligió:", programa)

if usuario == programa:
    print("Empate")
elif (usuario == 1 and programa == 3) or (usuario == 2 and programa == 1) or (usuario == 3 and programa == 2):
    print("¡Has ganado!")
else:
    print("Has perdido")