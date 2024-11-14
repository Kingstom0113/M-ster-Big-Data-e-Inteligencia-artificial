# Definir una función lambda para verificar si una cadena es un palíndromo
es_palindromo = lambda texto: texto == texto[::-1]

print(es_palindromo("anita lava la tina"))  # True