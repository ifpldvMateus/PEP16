'''
Escribe un programa en Python que haga uso de una función llamada saludar que cumpla los siguientes requisitos:
    - Entrada: Tiene 4 parámetros de entrada, que serán 4 cadenas de texto: nombre, primer apellido, segundo apellido y curso. El parámetro curso tendrá en la declaración de la función el valor por defecto "2DAW"
    - Salida: No tiene parámetros de salida
    - Funcionalidad: Imprime por pantalla un mensaje saludando al alumno/a que se haya pasado como parámetro de entrada

El programa debe invocar a la función varias veces. En algunas de ellas se tiene que usar el paso de parámetros de forma nominal (con clave valor)
'''

def saludar(nombre, apellido1, apellido2, curso="2DAW"):
    print("Un saludo,", nombre, apellido1, apellido2, "de", curso)

saludar("Mateus", "Leandro", "Barros")
saludar("Mateus", "Leandro", "Barros", "2SMR")
saludar(curso="1DAW", apellido1="Leandro", apellido2="Barros", nombre="Mateus")
saludar("Mateus", "Leandro", curso="1SMR", apellido2="Barros")
