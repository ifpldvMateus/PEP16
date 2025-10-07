'''
Escribe un programa que pida dos numero y muestre su división. Se deben tener en cuenta que no se puede dividir por 0 mostrando en ese caso un aviso
'''

numero1 = float(input("Dame un número: "))
numero2 = float(input("Dame otro número: "))

if numero2 == 0:
    print("No se puede dividir por 0")
else:
    print("El resultado de la división es:", numero1 / numero2)