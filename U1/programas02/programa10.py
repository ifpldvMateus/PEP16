'''
Escribe un programa que dado un número de dos cifras, diseñe un algoritmo que permita obtener el número invertido
'''

numero = int(input("Dame un número de dos cifras para invertirlo (por favor): "))
print("Número invertido:", ((numero % 10) * 10) + (numero // 10))