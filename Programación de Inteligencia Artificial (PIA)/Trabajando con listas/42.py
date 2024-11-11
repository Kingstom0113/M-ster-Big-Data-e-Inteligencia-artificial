# Crea una lista de temperaturas y convierte todas las temperaturas de Celsius a Fahrenheit.

import random

temperaturas = [random.randint(-20, 40) for _ in range(10)]
print(temperaturas)
fahrenheit = [((9/5) * celsius + 32) for celsius in temperaturas]
print(fahrenheit)



