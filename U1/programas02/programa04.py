'''
Escribe un programa que pregunte la base y altura de una rectángulo y calcule su área y perímetro
'''

base = int(input("Dame la base de tu rectángulo: "))
altura = int(input("Dame la altura de tu rectángulo: "))

print("Área:", base * altura)
print("Perímetro:", 2 * (base + altura))