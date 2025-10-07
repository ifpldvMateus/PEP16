'''
Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
'''

dia = int(input("Dime el día: "))
mes = int(input("Dime el mes: "))
año = int(input("Dime el año: "))

valida = True

if mes < 1 or mes > 12:
    valida = False
elif dia < 1:
    valida = False
elif (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12) and dia > 31:
    valida = False
elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and dia > 30:
    valida = False
elif mes == 2:
    bisiesto = (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0))
    if (bisiesto and dia > 29) or (not bisiesto and dia > 28):
        valida = False

if valida:
    print("La fecha es correcta")
else:
    print("La fecha es incorrecta")
