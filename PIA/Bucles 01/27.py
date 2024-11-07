import random

cara_consecutiva = 0

while cara_consecutiva < 3:
    lanzamiento = random.choice(['cara', 'cruz'])
    print(f"Lanzamiento: {lanzamiento}")
    
    if lanzamiento == 'cara':
        cara_consecutiva += 1
    else:
        cara_consecutiva = 0

print("¡Salieron tres caras consecutivas!")
