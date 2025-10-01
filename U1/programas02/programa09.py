'''
Escribe un programa que calcule la calificación de estudiante en un módulo. La calificación se obtiene de la calificación parcial en cada RA (RA1 20%, RA2, 60% y RA3 20%)
'''

calific_ra1 = float(input("Dime la calificación del RA1: "))
calific_ra2 = float(input("Dime la calificación del RA2: "))
calific_ra3 = float(input("Dime la calificación del RA3: "))

resultado = round((calific_ra1 * 0.20) + (calific_ra2 * 0.60) + (calific_ra3 * 0.20), 2)
print("La calificación del estudiante en el módulo es: ", resultado)