def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicitar el rango de números
inicio = int(input("Introduce el inicio del rango: "))
fin = int(input("Introduce el fin del rango: "))

# Contar los números primos en el rango
contador_primos = 0
for num in range(inicio, fin + 1):
    if es_primo(num):
        contador_primos += 1

print(f"Hay {contador_primos} números primos en el rango de {inicio} a {fin}.")
