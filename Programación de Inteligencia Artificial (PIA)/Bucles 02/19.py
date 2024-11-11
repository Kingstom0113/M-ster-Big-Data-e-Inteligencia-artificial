numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    resultado = numero1 + numero2
    print(f"El resultado de {numero1} + {numero2} es {resultado}.")
elif operacion == "-":
    resultado = numero1 - numero2
    print(f"El resultado de {numero1} - {numero2} es {resultado}.")
elif operacion == "*":
    resultado = numero1 * numero2
    print(f"El resultado de {numero1} * {numero2} es {resultado}.")
elif operacion == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"El resultado de {numero1} / {numero2} es {resultado}.")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida.")
