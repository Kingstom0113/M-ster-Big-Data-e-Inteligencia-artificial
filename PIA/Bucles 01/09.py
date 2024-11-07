N = int(input("Introduce cuántos números de la serie de Fibonacci quieres generar: "))

fibonacci = [0, 1]

for i in range(2, N):
    siguiente = fibonacci[i-1] + fibonacci[i-2]  
    fibonacci.append(siguiente)

print(f"Los primeros {N} números de la serie de Fibonacci son: {fibonacci[:N]}")
