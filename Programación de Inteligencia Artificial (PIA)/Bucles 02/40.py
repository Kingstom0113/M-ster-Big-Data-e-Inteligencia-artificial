def decimal_a_binario(n):
    if n == 0:
        return "0"
    
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2
    
    return binario

# Solicitar al usuario ingresar un número decimal
numero_decimal = int(input("Introduce un número decimal: "))
numero_binario = decimal_a_binario(numero_decimal)
print(f"El número {numero_decimal} en binario es: {numero_binario}")
