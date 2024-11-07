for i in range(1, 11):
    print(f"Tabla de multiplicar del {i}:")
    print("\n".join([f"{i} x {j} = {i * j}" for j in range(1, 11)]))
    print()

