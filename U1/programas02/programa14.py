'''
Escribe un programa que reciba un número de bytes y muestre por pantalla cuantos GBytes, MBytes, KBytes y Bytes son. Tanto para el sistema decimal como el binario
'''

bytes_entrada = int(input("Dame el número de bytes: "))

gb = bytes_entrada // (1000 ** 3)
mb = (bytes_entrada % (1000 ** 3)) // (1000 ** 2)
kb = (bytes_entrada % (1000 ** 2)) // 1000
b1 = bytes_entrada % 1000

print(f"\n{bytes_entrada} bytes en sistema decimal (SI): {gb} GB, {mb} MB, {kb} KB, {b1} bytes")

gib = bytes_entrada // (1024 ** 3)
mib = (bytes_entrada % (1024 ** 3)) // (1024 ** 2)
kib = (bytes_entrada % (1024 ** 2)) // 1024
b2 = bytes_entrada % 1024

print(f"{bytes_entrada} bytes en sistema binario (IEC): {gib} GiB, {mib} MiB, {kib} KiB, {b2} bytes")