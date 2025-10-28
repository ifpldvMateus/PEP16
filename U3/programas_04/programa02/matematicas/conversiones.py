def a_binario(n):
    return bin(n)[2:] # Slicing

def a_hexadecimal(n):
    return hex(n)[2:] # Slicing

def a_entero(texto):
    numero = 0.0
    try:
        numero = float(texto)
    except ValueError:
        return "Inválido"
    else:
        return numero