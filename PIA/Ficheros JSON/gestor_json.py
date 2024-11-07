import json
import shutil  # Importar el módulo shutil

# Ruta del archivo JSON
json_file_path = r'c:\Users\alumno\Documents\Manuel Soto Romero\M-ster-Big-Data-e-Inteligencia-artificial\Juan Carlos\PIA\Ficheros JSON\superheroe_spain.json'

# Función para cargar el archivo JSON
def cargar_datos_json(ruta):
    try:
        with open(ruta, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"El archivo {ruta} no se encontró.")
        return None
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON. Verifica que el formato sea correcto.")
        return None

# Función para guardar datos en el archivo JSON
def guardar_datos_json(ruta, data):
    try:
        with open(ruta, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print("Datos guardados exitosamente.")
        
        # Copiar el archivo JSON a una copia
        copia_ruta = ruta.replace('.json', '_ManuelSoto.json')  # Cambiar el nombre para la copia
        shutil.copy(ruta, copia_ruta)  # Hacer la copia
        print(f"Copia del archivo guardada como {copia_ruta}.")
        
    except Exception as e:
        print(f"Error al guardar el archivo JSON: {e}")

# Función para agregar un nuevo héroe
def agregar_heroe(data, nombre_real, alias, habilidades, ciudad, equipo):
    nuevo_heroe = {
        "nombre_real": nombre_real,
        "alias": alias,
        "habilidades": habilidades,
        "ciudad": ciudad,
        "equipo": equipo
    }
    data["superheroes_espanoles"].append(nuevo_heroe)

# Función para mostrar los datos de todos los héroes
def mostrar_datos(data):
    if data:
        print("Lista de Superhéroes Españoles:")
        for heroe in data.get("superheroes_espanoles", []):
            print(f"Alias: {heroe['alias']}, Nombre Real: {heroe['nombre_real']}, Ciudad: {heroe['ciudad']}, Equipo: {heroe['equipo']}")
            print(f"Habilidades: {', '.join(heroe['habilidades'])}\n")

# Cargar datos del archivo JSON
datos = cargar_datos_json(json_file_path)

# Agregar héroes nuevos
if datos:
    # Primer héroe nuevo
    agregar_heroe(datos, "Manuel", "Soto", ["desarrollador", "jugón", "noseq"], "Sevilla", "Sevilla FC")
    
    # Segundo héroe nuevo
    agregar_heroe(datos, "Lucía López", "La Tormenta", ["control del clima", "electroquinesis", "vuelo"], "Madrid", "Guardianes del Centro")
    
    # Tercer héroe nuevo
    agregar_heroe(datos, "Carlos Ruiz", "El Sabio", ["telepatía", "visión remota", "psicometría"], "Salamanca", "Los Iluminados")

    # Guardar los cambios en el archivo JSON
    guardar_datos_json(json_file_path, datos)

    # Mostrar todos los héroes después de agregar los nuevos
    mostrar_datos(datos)
else:
    print("No se pudieron cargar los datos.")
