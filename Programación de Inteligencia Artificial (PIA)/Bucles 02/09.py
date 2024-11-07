n = int(input("Introduce el número de términos de la serie de Fibonacci: "))

a, b = 0, 1

for _ in range(n):
    print(a)
    a, b = b, a + b
