import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random

# Aseguramos que los recursos de NLTK estén disponibles y descargados, si no lo están
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt_tab')  # Descargamos 'punkt_tab' para evitar errores con el tokenizador

# 1. Definimos un conjunto de preguntas y respuestas que va a utilizar el chatbot
qa_pairs = [
    ("¿Cómo estás?", "¡Estoy bien, gracias por preguntar!"),
    ("¿Cuál es tu nombre?", "Soy un chatbot creado para ayudarte."),
    ("¿Qué es Python?", "Python es un lenguaje de programación popular y fácil de aprender."),
    ("¿Cuál es la capital de Francia?", "La capital de Francia es París."),
    ("¿Cuántos continentes hay?", "Hay siete continentes en el mundo."),
    ("¿Cómo está el clima hoy?", "Lo siento, no tengo acceso a información en tiempo real."),
    ("¿Qué es la inteligencia artificial?", "La inteligencia artificial es un campo de la informática que estudia la creación de máquinas capaces de realizar tareas que normalmente requieren inteligencia humana."),
    ("¿Qué es un chatbot?", "Un chatbot es un software diseñado para simular conversaciones con usuarios humanos."),
    ("¿Qué es la computación cuántica?", "La computación cuántica es un tipo de computación que utiliza principios de la mecánica cuántica para procesar información."),
    ("¿Cuándo fue fundada la NASA?", "La NASA fue fundada el 29 de julio de 1958.")
]

# 2. Preprocesamos el texto: eliminamos puntuación, lo convertimos a minúsculas, quitamos palabras vacías y lematizamos
def preprocesar_texto(texto):
    # Convertimos el texto a minúsculas para unificar todo
    texto = texto.lower()
    
    # Eliminamos los signos de puntuación que no aportan nada al análisis
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    
    # Tokenizamos el texto, dividiéndolo en palabras. Es importante especificar el idioma.
    palabras = nltk.word_tokenize(texto, language='spanish')
    
    # Filtramos las stopwords, es decir, las palabras que no aportan mucho (como "y", "el", etc.)
    stop_words = set(stopwords.words('spanish'))
    palabras = [palabra for palabra in palabras if palabra not in stop_words]
    
    # Lematizamos las palabras, lo que significa reducirlas a su raíz o forma base
    lemmatizer = WordNetLemmatizer()
    palabras = [lemmatizer.lemmatize(palabra) for palabra in palabras]
    
    return " ".join(palabras)

# 3. Función para obtener la respuesta del chatbot según la pregunta del usuario
def obtener_respuesta_usuario(pregunta_usuario):
    # Preprocesamos la pregunta del usuario (eliminamos ruido y normalizamos el texto)
    pregunta_usuario = preprocesar_texto(pregunta_usuario)
    
    # Preprocesamos las preguntas del conjunto de preguntas predefinidas
    preguntas = [preprocesar_texto(par[0]) for par in qa_pairs]
    
    # Creamos el vectorizador TF-IDF para convertir el texto en vectores
    vectorizador = TfidfVectorizer().fit_transform(preguntas + [pregunta_usuario])
    
    # Calculamos la similitud entre la pregunta del usuario y las preguntas predefinidas usando el coseno
    similitudes = cosine_similarity(vectorizador[-1], vectorizador[:-1])
    
    # Buscamos la pregunta más similar
    indice_similar = similitudes.argmax()
    
    # Si la similitud es suficientemente alta (más del 75%), devolvemos la respuesta correspondiente
    if similitudes[0][indice_similar] > 0.75:
        return random.choice([qa_pairs[indice_similar][1]])
    else:
        # Si no encontramos una buena coincidencia, sugerimos temas relacionados
        temas_sugeridos = [par[0] for par in qa_pairs]
        return f"No entiendo tu pregunta, intenta reformularla. Tal vez quieras preguntar sobre: {', '.join(temas_sugeridos[:3])}"

# 4. Ciclo principal para interactuar con el usuario en la consola
def chat():
    print("¡Hola! Soy un chatbot. Puedes preguntarme algo. Escribe 'salir' para terminar.")
    
    while True:
        # Solicitamos una pregunta del usuario
        pregunta_usuario = input("Tú: ")
        
        # Si el usuario escribe 'salir', terminamos la conversación
        if pregunta_usuario.lower() == "salir":
            print("¡Hasta luego!")
            break
        
        # Obtenemos la respuesta del chatbot y la mostramos
        respuesta = obtener_respuesta_usuario(pregunta_usuario)
        print("Chatbot:", respuesta)

# Ejecutamos el chatbot
if __name__ == "__main__":
    chat()
