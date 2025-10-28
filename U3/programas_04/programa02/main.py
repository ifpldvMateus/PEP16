import matematicas

'''
from matematicas import *
- Antes hacía esto, con la intención de usar TODAS las funciones directamente, sin namespace
- Pero daba advertencias y no está recomendado
'''

def menu_operaciones():
    a = float(input("Introduce el primer número: "))
    b = float(input("Introduce el segundo número: "))

    print(f"Suma: {matematicas.suma(a, b)}")
    print(f"Resta: {matematicas.resta(a, b)}")
    print(f"Multiplicación: {matematicas.multiplicacion(a, b)}")
    print(f"División: {matematicas.division(a, b)}")


def menu_figuras():

    opcion = 0
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Círculo")

    while opcion < 1 or opcion > 3:
        opcion = int(input("Elige una figura: "))

    match opcion:
        case 1:
            base = float(input("Base: "))
            altura = float(input("Altura: "))

            print(f"Área del rectángulo: {matematicas.area_rectangulo(base, altura)}")
        case 2:
            base = float(input("Base: "))
            altura = float(input("Altura: "))

            print(f"Área del triángulo: {matematicas.area_triangulo(base, altura)}")
        case 3:
            radio = float(input("Radio: "))
            print(f"Área del círculo: {matematicas.area_circulo(radio)}")


def menu_conversiones():

    opcion = 0
    print("1. A binario")
    print("2. A hexadecimal")
    print("3. A entero")

    while opcion < 1 or opcion > 3:
        opcion = int(input("Elige una figura: "))

    match opcion:
        case 1:
            numero = int(input("Introduce un número entero: "))
            print(f"Binario: {matematicas.a_binario(numero)}")
        case 2:
            numero = int(input("Introduce un número entero: "))
            print(f"Hexadecimal: {matematicas.a_hexadecimal(numero)}")
        case 3:
            texto = input("Introduce una cadena numérica: ")
            print(f"Entero: {matematicas.a_entero(texto)}")

def main():

    opcion = 0
    while opcion != 4:

        opcion = 0
        print("1. Operaciones matemáticas")
        print("2. Cálculo de áreas geométricas")
        print("3. Conversiones numéricas")
        print("4. Salir")

        while (opcion < 1 or opcion > 4):
            opcion = int(input("Elige una opción: "))

        match opcion:
            case 1:
                menu_operaciones()
            case 2:
                menu_figuras()
            case 3:
                menu_conversiones()
            case 4:
                print("Saliendo del programa")


if __name__ == "__main__":
    main()