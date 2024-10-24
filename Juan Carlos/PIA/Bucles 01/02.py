num = int (input("Introduce un número: "))

factorial = 1

while num > 0:
    factorial = factorial * num
    num -= 1

print("El factorial es: ", factorial)