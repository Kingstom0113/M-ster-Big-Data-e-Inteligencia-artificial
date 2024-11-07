num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    mayor = num1
else:
    mayor = num2

encontrado = False
while not encontrado:
    if mayor % num1 == 0 and mayor % num2 == 0:
        mcm = mayor
        encontrado = True
    else:
        mayor += 1

print(f"El MCM de {num1} y {num2} es: {mcm}")