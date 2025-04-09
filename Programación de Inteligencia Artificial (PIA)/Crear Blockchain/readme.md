# Proyecto: Cadena de Bloques (Blockchain) en Python

## Introducción
Este proyecto implementa un modelo básico de cadena de bloques en Python, permitiendo comprender los fundamentos del encadenamiento de bloques, el uso de hashes para garantizar la integridad y cómo validar una blockchain.

## Actividades y Respuestas

### 1. ¿Qué es el hash de un bloque? ¿Por qué es importante que sea único?
El hash de un bloque es un valor único generado a partir del contenido del bloque (incluyendo el id, emisor, receptor, mensaje y el hash del bloque anterior) mediante una función hash (en este caso, SHA-256). Es importante que sea único porque garantiza la integridad del bloque; cualquier cambio en el contenido del bloque alterará su hash, lo que invalidará la cadena de bloques.

### 2. ¿Qué ocurre si se modifica un bloque anterior en la cadena?
Si se modifica un bloque anterior, el hash de ese bloque cambiará. Como cada bloque contiene el hash del bloque anterior, todos los bloques posteriores también se volverán inválidos, ya que sus hashes no coincidirán con los hashes recalculados. Esto asegura la seguridad de la cadena de bloques.

### 3. ¿Qué representa el bloque génesis y qué lo diferencia de los demás?
El bloque génesis es el primer bloque de la cadena de bloques. Se diferencia de los demás porque no tiene un bloque anterior (su hash anterior es "0"). Es el punto de partida de la cadena y establece la base para todos los bloques subsiguientes.

### 4. Modifica el código base para incluir más información en cada bloque (por ejemplo, emisor y receptor del mensaje).
El código ya incluye el emisor y el receptor en cada bloque. Cada bloque tiene atributos `emisor` y `receptor` que se utilizan al crear un nuevo bloque.

### 5. Simula una alteración modificando manualmente el contenido de un bloque intermedio y verifica si la cadena es válida.
Se ha añadido un bloque de código que simula la alteración del mensaje de un bloque intermedio. Al verificar la validez de la cadena después de la alteración, se confirma que la cadena ya no es válida.

### 6. Agrega una función que imprima solo las transacciones de todos los bloques (sin hashes).
La función [mostrar_transacciones](cci:1://file:///c:/Users/alumno/Documents/M-ster-Big-Data-e-Inteligencia-artificial/Programaci%C3%B3n%20de%20Inteligencia%20Artificial%20%28PIA%29/Crear%20Blockchain/main.py:49:4-51:77) ya está implementada y muestra las transacciones de todos los bloques, omitiendo el bloque génesis y los hashes.

### 7. Crea una función que exporte la cadena completa a un archivo .json.
La función [guardar_en_json](cci:1://file:///c:/Users/alumno/Documents/M-ster-Big-Data-e-Inteligencia-artificial/Programaci%C3%B3n%20de%20Inteligencia%20Artificial%20%28PIA%29/Crear%20Blockchain/main.py:53:4-56:41) ya está implementada y permite exportar la cadena completa a un archivo JSON.

## Ejecución del Código
Para ejecutar el código, asegúrate de tener Python instalado y ejecuta el archivo [main.py](cci:7://file:///c:/Users/alumno/Documents/M-ster-Big-Data-e-Inteligencia-artificial/Programaci%C3%B3n%20de%20Inteligencia%20Artificial%20%28PIA%29/Crear%20Blockchain/main.py:0:0-0:0). La cadena de bloques se generará y se guardará en un archivo `cadena_blockchain.json`.

## Conclusión
Este proyecto proporciona una comprensión básica de cómo funciona una cadena de bloques, su estructura y la importancia de la integridad de los datos mediante hashes.