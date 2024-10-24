inicio = int(input("Ingrese la temperatura inicial en Celsius: "))
fin = int(input("Ingrese la temperatura final en Celsius: "))

for celsius in range(inicio, fin + 1):
    fahrenheit = celsius * 9/5 + 32
    print(f"{celsius}°C es equivalente a {fahrenheit}°F")