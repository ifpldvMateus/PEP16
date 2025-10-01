'''
Escribe un programa que
    - Cree una variable que almacene el número entero 6
    - Muestre por pantalla el tipo del objeto que contiene el número 6, y el tipo del objeto al que apunta la variable (deben ser iguales)
    - Cree otra variable a la que se asigne la primera variable
    - Muestre por pantalla el tipo del objeto que contiene el número 6 y el tipo del objeto al que apunta la variable (deben ser iguales)
    - Utilice los operadores de identidad (is e is not) para comprobar y mostrar por pantalla que los dos variables apuntan al mismo objeto y por lo tanto a la misma posición de memoria
    - Asigne la cadena "Hola" a la primera variable
    - Muestre por pantalla el tipo del objeto que contiene la cadena "Hola" y el tipo del objeto al que apunta la variable (deben ser iguales) (y diferentes al objeto 6)
    - Utilice la función isinstance() para comprobar y mostrar por pantalla que el objeto al que apunta la primera variable es de tipo int y el de la segunda es de tipo str
'''

variable1 = 6
print(f"Tipo del número literal: {type(6)}\nTipo de variable1: {type(variable1)}")

variable2 = variable1
print(f"Tipo del número literal: {type(6)}\nTipo de variable2: {type(variable2)}\n")

print(f"{variable1} is {variable2}: {variable1 is variable2}")
print(f"{variable1} is not {variable2}: {variable1 is not variable2}\n")

variable1 = "Hola"
print(f"Tipo de la cadena literal: {type('Hola')}\nTipo de variable1: {type(variable1)}\n")

print(f"variable1 es entero: {isinstance(variable1, int)}\nvariable2 es cadena: {isinstance(variable2, str)}")