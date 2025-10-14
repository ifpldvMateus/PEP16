# NOTA IMPORTANTE: El enunciado del ejercicio anterior ya pidió comprobar que los valores fueran mayores a 0. El único cambio que hice fue mostrar un aviso dedicado

'''
Mejora el programa anterior de forma que compruebe si el usuario está introduciendo valores correctos (por ejemplo, el radio no puede ser un número negativo) y si no es así que pida muestre un aviso y vuelva a pedir el valor
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
        radio = float(input("\nDame el radio del círculo"))

        if (radio <= 0.0): print("AVISO: Debes introducir un valor mayor a 0")

    print(f"\nEl área del círculo con radio {radio} es: {calcular_area_circulo(radio)}\n\n")

def opcion2():
    base = altura = 0.0
    while (base <= 0.0 or altura <= 0.0):
        base = float(input("\nDame la base del triángulo. Debe ser mayor a 0: "))
        altura = float(input("Dame la altura del triángulo. Debe ser mayor a 0: "))

        if (base <= 0.0 or altura <= 0.0): print("AVISO: Debes introducir valores mayores a 0")

    print(f"\nEl área del triángulo con base {base} y altura {altura} es: {calcular_area_triangulo(base, altura)}\n\n")

def opcion3():
    base = altura = 0.0
    while (base <= 0.0 or altura <= 0.0):
        base = float(input("\nDame la base del rectángulo. Debe ser mayor a 0: "))
        altura = float(input("Dame la altura del rectángulo. Debe ser mayor a 0: "))

        if (base <= 0.0 or altura <= 0.0): print("AVISO: Debes introducir valores mayores a 0")

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