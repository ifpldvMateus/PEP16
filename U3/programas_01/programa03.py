'''
Escribe un programa en Python que muestre un menú que permita al usuario seleccionar qué operación desea realizar. Las operaciones que puede realizar serán calcular el área de un círculo, un triángulo o un rectángulo. El menú que se le muestra al usuario será similar al siguiente:
    1. Calcular el área de un círculo
    2. Calcular el área de un triángulo
    3. Calcular el área de un rectángulo
    4. Salir
    Introduce una opción (1-4):

El programa se estará ejecutando de forma indefinida hasta que el usuario seleccione la
opción 4

Hay que diseñar y definir la siguientes funciones:
    - calcular_area_circulo: recibe como parámetro de entrada el radio del círculo y retorna su área
    - calcular_area_triangulo: recibe como parámetros de entrada la base y la altura del triangulo y retorna su área
    - calcular_area_rectangulo: recibe como parámetros de entrada la base y la altura del rectángulo y retorna su área
    - mostrar_menu: muestra el menú por pantalla con todas las opciones disponibles
    - main(): lee por teclado la opción seleccionada por el usuario, valida que la opción está entre 1 y 4, y una vez que ha leído una opción válida llamará a la función correspondiente en función de la opción seleccionada
    - opcion1: lee por teclado el valor del radio del círculo, valida que el radio siempre sea mayor que 0 y una vez que ha validado el radio llamará a la función calcular_area_circulo
    - opcion2: lee por teclado el valor de la base y la altura del triángulo, valida que los dos datos son mayores que 0 y una vez que los ha validado llamará a la función calcular_area_triangulo
    - opcion3: lee por teclado el valor de la base y la altura del rectángulo, valida que los dos datos son mayores que 0 y una vez que los ha validado llamará a la función calcular_area_rectangulo
'''

import math # Para usar la constante PI y que el cálculo sea lo más exacto posible

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rectangulo(base, altura):
    return base * altura

def mostrar_menu():
    print("1. Calcular el área de un círculo")
    print("2. Calcular el área de un triángulo")
    print("3. Calcular el área de un rectángulo")
    print("4. Salir\n")

def opcion1():
    radio = 0.0
    while (radio <= 0.0):
        radio = float(input("\nDame el radio del círculo. Debe ser mayor a 0: "))

    print(f"\nEl área del círculo con radio {radio} es: {calcular_area_circulo(radio)}\n\n")

def opcion2():
    base = altura = 0.0
    while (base <= 0.0 or altura <= 0.0):
        base = float(input("\nDame la base del triángulo. Debe ser mayor a 0: "))
        altura = float(input("Dame la altura del triángulo. Debe ser mayor a 0: "))

    print(f"\nEl área del triángulo con base {base} y altura {altura} es: {calcular_area_triangulo(base, altura)}\n\n")

def opcion3():
    base = altura = 0.0
    while (base <= 0.0 or altura <= 0.0):
        base = float(input("\nDame la base del rectángulo. Debe ser mayor a 0: "))
        altura = float(input("Dame la altura del rectángulo. Debe ser mayor a 0: "))

    print(f"\nEl área del rectángulo con base {base} y altura {altura} es: {calcular_area_rectangulo(base, altura)}\n\n")

def main():
    salir = False
    while (not salir):
        mostrar_menu()

        respuesta = 0
        while (respuesta < 1 or respuesta > 4):
            respuesta = int(input("Introduce una opción (1-4): "))
        
        match respuesta:
            case 1: opcion1()
            case 2: opcion2()
            case 3: opcion3()
            case 4: salir = True

    print("Saliendo del programa")


main()