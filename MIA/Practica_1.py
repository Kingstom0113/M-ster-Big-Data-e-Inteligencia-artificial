import nltk
import re
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import urllib.request

# Paso 1: Descargar un texto desde el Proyecto Gutenberg
url = "https://www.gutenberg.org/cache/epub/2701/pg2701.txt"  # Usaremos "Moby Dick"
response = urllib.request.urlopen(url)
text = response.read().decode('utf-8')

# Paso 2: Limpiar el texto
# Eliminar encabezado y pie de página del proyecto Gutenberg
start_text = "Moby Dick by Herman Melville"
end_text = "End of Project Gutenberg's Moby Dick"
start_index = text.find(start_text)
end_index = text.find(end_text)

# Verificar si se encontraron las cadenas
if start_index == -1 or end_index == -1:
    print("No se encontraron las cadenas de inicio o fin.")
else:
    text = text[start_index:end_index]

    # Verificar el texto descargado (imprimir más de 1000 caracteres)
    print("Primeros 2000 caracteres del texto descargado:")
    print(text[:2000])

    # Paso 3: Tokenizar el texto usando expresiones regulares (mejor control)
    nltk.download('stopwords')
    stop_words = set(stopwords.words('english'))

    # Usamos una expresión regular para extraer solo las palabras (sin puntuación)
    tokens = re.findall(r'\b\w+\b', text.lower())  # Extrae palabras y las pasa a minúsculas

    # Imprimir las primeras 20 palabras tokenizadas
    print("\nPrimeras 20 palabras tokenizadas:")
    print(tokens[:20])

    # Paso 4: Eliminar palabras vacías (stopwords)
    filtered_tokens = [word for word in tokens if word not in stop_words]

    # Imprimir las primeras 20 palabras después de eliminar stopwords
    print("\nPrimeras 20 palabras después de eliminar stopwords:")
    print(filtered_tokens[:20])

    # Paso 5: Contar la frecuencia de las palabras
    freq_dist = FreqDist(filtered_tokens)

    # Verificar la cantidad de palabras con frecuencia
    print("\nNúmero de palabras en la lista de frecuencia:", len(freq_dist))

    # Paso 6: Generar la nube de palabras
    if len(freq_dist) > 0:
        wordcloud = WordCloud(width=800, height=400, background_color="white").generate_from_frequencies(freq_dist)

        # Paso 7: Guardar la imagen de la nube de palabras
        wordcloud.to_file("wordcloud.png")

        # Mostrar la nube de palabras
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")  # Desactivar los ejes
        plt.show()
    else:
        print("No hay palabras suficientes para generar la nube de palabras.")