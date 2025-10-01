'''
Escribe un programa que use varias veces la función printf() para
- Mostrar las operaciones del los operadores aritméticos de Python entre dos números
- Mostrar las operaciones de los operadores lógicos de Python con valores booleanos
- Mostrar las operaciones de los operadores de comparación de Python con valores booleanos y/o números
'''

a = 10
b = 3
print(f"{a} + {b}: ", a + b)
print(f"{a} - {b}: ", a - b)
print(f"{a} * {b}: ", a * b)
print(f"{a} / {b}: ", a / b)
print(f"{a} // {b}: ", a // b)
print(f"{a} % {b}: ", a % b)
print(f"{a} ** {b}: ", a ** b)

print()

x = True
y = False
print(f"{x} AND {y}: ", x and y)
print(f"{x} OR {y}: ", x or y)
print(f"{x} NOT {y}: ", not x)

print()

print(f"{a} == {b}: ", a == b)
print(f"{a} != {b}: ", a != b)
print(f"{a} > {b}: ", a > b)
print(f"{a} < {b}: ", a < b)
print(f"{a} >= {b}: ", a >= b)
print(f"{a} <= {b}: ", a <= b)
