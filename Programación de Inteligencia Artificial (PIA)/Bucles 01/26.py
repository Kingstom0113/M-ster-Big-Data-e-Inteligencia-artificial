filas = int(input("Introduce el número de filas para la pirámide: "))

for i in range(1, filas + 1):
    # Imprimir espacios
    for j in range(filas - i):
        print(" ", end="")
    
    # Imprimir números
    for k in range(1, i + 1):
        print(k, end="")
    
    print()
