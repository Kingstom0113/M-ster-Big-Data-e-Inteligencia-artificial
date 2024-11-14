def es_primo(n):
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    for i in range(2, int(n ** 0.5) + 1):  # Iteramos hasta la raíz cuadrada de n
        if n % i == 0:
            return False  # Si n es divisible por i, no es primo
    return True  # Si no se encontró ningún divisor, n es primo


print(es_primo(7))
print(es_primo(10))