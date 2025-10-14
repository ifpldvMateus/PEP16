'''
Escribe un programa donde crees varias funciones y pruebes el ámbito de las variables en Python (globales, no locales y locales)
'''

x = 20 # Variable global

def funcion_local():
    x = 10 # Variable local
    print("En funcion_local, x (local) =", x)

def funcion_global():
    # Modificar la variable global
    global x 
    x = 200

    print("En funcion_global(), x (modificada global) =", x)

def funcion_no_local():
    z = 2 # Variable local
    def interna():
        # Modificar variable no local
        nonlocal z
        z = 8

        print("Dentro de interna() en funcion_no_local(), z (modificada no local) =", z)
    
    print("Antes de interna() en funcion_no_local(), z (local) =", z)
    interna()
    print("Después de interna() en funcion_no_local(), z (local) =", z)


print("=== ÁMBITO LOCAL ===")
print("Antes de funcion_local(), x (global) =", x)
funcion_local()
print("Después de funcion_local(), x (global) =", x)

print()

print("=== ÁMBITO GLOBAL ===")
print("Antes de funcion_global(), x (global) =", x)
funcion_global()
print("Después de funcion_global(), x (global) =", x)

print()

print("=== ÁMBITO NO LOCAL ===")
funcion_no_local()