def fibonacci(n):
    fib = [0, 1]  # Los dos primeros términos de la serie
    while len(fib) < n:
        # El siguiente término es la suma de los dos anteriores
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

print(fibonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]