'''
Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. El tiempo de viaje hasta llegar a otra ciudad B es de N segundos. Escribie un programa que determine la hora de llegada a la ciudad B
'''

hora = int(input("Dame la hora de salida: "))
minuto = int(input("Dame el minuto de salida: "))
segundo = int(input("Dame los segundos de salida: "))
tiempo = int(input("Dime cuántos segundos se tarda en llegar a la ciudad: "))

resultado = ((hora * 3600) + (minuto * 60) + segundo) + tiempo

hora_llegada = (resultado // 3600) % 24
minuto_llegada = ((resultado % 3600) // 60) % 60
segundo_llegada = resultado % 60

print("Hora de llegada:", hora_llegada, minuto_llegada, segundo_llegada, sep = ":")