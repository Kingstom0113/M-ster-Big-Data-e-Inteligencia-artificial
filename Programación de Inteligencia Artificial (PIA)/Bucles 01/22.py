numero = int(input("Introduce el número: "))
inicio = int(input("Introduce el valor inicial del rango: "))
fin = int(input("Introduce el valor final del rango: "))

print(f"Múltiplos de {numero} en el rango de {inicio} a {fin}:")

for i in range(inicio, fin + 1):
    if i % numero == 0:
        print(i)
