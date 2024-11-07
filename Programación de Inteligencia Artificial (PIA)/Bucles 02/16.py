puntaje = float(input("Introduce el puntaje (entre 0 y 100): "))

if puntaje >= 90:
    print("Calificación: A")
elif puntaje >= 80:
    print("Calificación: B")
elif puntaje >= 70:
    print("Calificación: C")
elif puntaje >= 60:
    print("Calificación: D")
elif puntaje >= 0:
    print("Calificación: F")
else:
    print("Puntaje inválido. Debe estar entre 0 y 100.")
