import json

# Función para cargar los superhéroes desde un archivo JSON
def cargar_superheroes():
    try:
        with open("red_superheroes.json", "r") as file:
            data = json.load(file)
            return data['superheroes']
    except FileNotFoundError:
        # Si el archivo no existe, devolver una lista vacía
        return []

# Función para guardar los superhéroes en el archivo JSON
def guardar_superheroes(superheroes):
    with open("red_superheroes.json", "w") as file:
        json.dump({"superheroes": superheroes}, file, indent=4)

# Función para agregar un nuevo superhéroe
def agregar_superheroe(superheroes, alias, habilidades, ciudad, equipo):
    nuevo_superheroe = {
        "alias": alias,
        "habilidades": habilidades,
        "ciudad": ciudad,
        "equipo": equipo
    }
    superheroes.append(nuevo_superheroe)
    guardar_superheroes(superheroes)

# Función para filtrar los superhéroes por ciudad
def filtrar_por_ciudad(superheroes, ciudad):
    return [superheroe for superheroe in superheroes if superheroe['ciudad'].lower() == ciudad.lower()]

# Función para filtrar los superhéroes por equipo
def filtrar_por_equipo(superheroes, equipo):
    return [superheroe for superheroe in superheroes if superheroe['equipo'].lower() == equipo.lower()]

# Función para listar las habilidades únicas
def listar_habilidades_unicas(superheroes):
    habilidades = {habilidad for superheroe in superheroes for habilidad in superheroe['habilidades']}
    return habilidades

# Función para mostrar todos los superhéroes
def mostrar_superheroes(superheroes):
    if not superheroes:
        print("No hay superhéroes disponibles.")
    for superheroe in superheroes:
        print(f"Alias: {superheroe['alias']}, Habilidades: {', '.join(superheroe['habilidades'])}, Ciudad: {superheroe['ciudad']}, Equipo: {superheroe['equipo']}")

# Inicialización de datos
superheroes = cargar_superheroes()

# Insertar al menos 10 superhéroes si no existen
if not superheroes:
    superheroes = [
        {"alias": "El Cid", "habilidades": ["esgrima", "estrategia"], "ciudad": "Burgos", "equipo": "Los Defensores"},
        {"alias": "La Dama de Plata", "habilidades": ["manipulación de metales"], "ciudad": "Toledo", "equipo": "Los Defensores"},
        {"alias": "El Halcón", "habilidades": ["agilidad", "visión aguda"], "ciudad": "Madrid", "equipo": "Los Vengadores"},
        {"alias": "La Mujer Invisible", "habilidades": ["invisibilidad", "campo force"], "ciudad": "Barcelona", "equipo": "Los Cuatro Fantásticos"},
        {"alias": "El Hombre Araña", "habilidades": ["trepar paredes", "sentido arácnido"], "ciudad": "Nueva York", "equipo": "Los Vengadores"},
        {"alias": "Thor", "habilidades": ["fuerza sobrehumana", "control del trueno"], "ciudad": "Asgard", "equipo": "Los Vengadores"},
        {"alias": "Iron Man", "habilidades": ["tecnología avanzada", "inteligencia"], "ciudad": "Los Ángeles", "equipo": "Los Vengadores"},
        {"alias": "La Viuda Negra", "habilidades": ["agilidad", "espionaje"], "ciudad": "Moscú", "equipo": "Los Vengadores"},
        {"alias": "Doctor Strange", "habilidades": ["magia", "teletransportación"], "ciudad": "Kamar-Taj", "equipo": "Los Vengadores"},
        {"alias": "Black Panther", "habilidades": ["fuerza mejorada", "agilidad"], "ciudad": "Wakanda", "equipo": "Los Vengadores"}
    ]
    guardar_superheroes(superheroes)

# Ejemplo de uso

# Mostrar todos los superhéroes
print("Superhéroes disponibles en la red:")
mostrar_superheroes(superheroes)

# Filtrar superhéroes por ciudad (ejemplo: Madrid)
print("\nFiltrar superhéroes por ciudad 'Madrid':")
superheroes_ciudad = filtrar_por_ciudad(superheroes, "Madrid")
for superheroe in superheroes_ciudad:
    print(f"Alias: {superheroe['alias']}, Habilidades: {', '.join(superheroe['habilidades'])}, Ciudad: {superheroe['ciudad']}, Equipo: {superheroe['equipo']}")

# Filtrar superhéroes por equipo (ejemplo: Los Vengadores)
print("\nFiltrar superhéroes por equipo 'Los Vengadores':")
superheroes_equipo = filtrar_por_equipo(superheroes, "Los Vengadores")
for superheroe in superheroes_equipo:
    print(f"Alias: {superheroe['alias']}, Habilidades: {', '.join(superheroe['habilidades'])}, Ciudad: {superheroe['ciudad']}, Equipo: {superheroe['equipo']}")

# Listar habilidades únicas
print("\nHabilidades únicas de los superhéroes:")
habilidades_unicas = listar_habilidades_unicas(superheroes)
for habilidad in habilidades_unicas:
    print(habilidad)

# Agregar un nuevo superhéroe
print("\nAgregar un nuevo superhéroe:")
agregar_superheroe(superheroes, "La Sombra", ["sigilo", "telequinesis"], "Valencia", "Los Defensores")
print("Superhéroe agregado con éxito.")
mostrar_superheroes(superheroes)
