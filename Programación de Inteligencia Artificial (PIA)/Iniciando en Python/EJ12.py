# 1. Crear el set 'animales' con los valores dados
animales = {"gato", "perro", "loro", "pez"}

# 2. Crear el segundo set 'animales_domesticos' con los valores dados
animales_domesticos = {"gato", "perro", "conejo"}

# 3. Encontrar la intersección entre ambos sets
interseccion = animales.intersection(animales_domesticos)
print("Intersección (animales en ambos sets):", interseccion)

# 4. Encontrar la diferencia entre 'animales' y 'animales_domesticos'
diferencia = animales.difference(animales_domesticos)
print("Diferencia (animales que no son domésticos):", diferencia)

# 5. Hacer la unión de los dos sets
union = animales.union(animales_domesticos)
print("Unión de ambos sets:", union)
