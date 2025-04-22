import json
import hashlib
import time
from datetime import datetime

# --- Configuración ---
NUM_DISPOSITIVOS = 3
INTERVALO_GENERACION = 5  # segundos
ARCHIVO_NUBE = "datos_nube.json"
ARCHIVO_BLOCKCHAIN = "blockchain.json"

# --- Funciones de simulación ---
def generar_dato(dispositivo_id):
    temperatura = 20 + (dispositivo_id * 2) + (time.time() % 5)
    humedad = 60 - (dispositivo_id * 3) + (time.time() % 10)
    return {
        "dispositivo_id": f"IoT_{dispositivo_id}",
        "timestamp": datetime.now().isoformat(),
        "temperatura": round(temperatura, 2),
        "humedad": round(humedad, 2)
    }

# --- Simulación de la Nube (almacenamiento en archivo JSON) ---
def guardar_en_nube(datos):
    try:
        with open(ARCHIVO_NUBE, 'r') as f:
            datos_existentes = json.load(f)
    except FileNotFoundError:
        datos_existentes = []
    datos_existentes.extend(datos)
    with open(ARCHIVO_NUBE, 'w') as f:
        json.dump(datos_existentes, f, indent=4)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Datos guardados en la nube.")

def leer_datos_nube():
    try:
        with open(ARCHIVO_NUBE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# --- Simulación de la Blockchain ---
def calcular_hash(bloque):
    bloque_str = json.dumps(bloque, sort_keys=True).encode('utf-8')
    return hashlib.sha256(bloque_str).hexdigest()

def crear_genesis_bloque():
    genesis_block = {
        "index": 0,
        "timestamp": datetime.now().isoformat(),
        "datos": "Bloque Genesis",
        "hash_previo": "0" * 64,
        "hash_actual": ""  # Hash se calculará después
    }
    genesis_block["hash_actual"] = calcular_hash(genesis_block)
    return genesis_block

def agregar_bloque(blockchain, datos):
    ultimo_bloque = blockchain[-1]
    nuevo_indice = ultimo_bloque["index"] + 1
    nuevo_timestamp = datetime.now().isoformat()
    nuevo_bloque = {
        "index": nuevo_indice,
        "timestamp": nuevo_timestamp,
        "datos": datos,
        "hash_previo": ultimo_bloque["hash_actual"],
        "hash_actual": "" # Hash se calculará después
    }
    nuevo_bloque["hash_actual"] = calcular_hash(nuevo_bloque)
    blockchain.append(nuevo_bloque)
    guardar_blockchain(blockchain)
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Bloque #{nuevo_indice} añadido a la blockchain.")
    return blockchain

def guardar_blockchain(blockchain):
    with open(ARCHIVO_BLOCKCHAIN, 'w') as f:
        json.dump(blockchain, f, indent=4)

def cargar_blockchain():
    try:
        with open(ARCHIVO_BLOCKCHAIN, 'r') as f:
            blockchain = json.load(f)
            if not blockchain:  # Si el archivo está vacío
                return [crear_genesis_bloque()]
            return blockchain
    except FileNotFoundError:
        return [crear_genesis_bloque()]
    except json.JSONDecodeError: # Si el archivo JSON está corrupto
        return [crear_genesis_bloque()]

def verificar_cadena(blockchain):
    if len(blockchain) <= 1:
        return True, "Cadena de bloques íntegra."
    for i in range(1, len(blockchain)):
        bloque_actual = blockchain[i]
        bloque_previo = blockchain[i-1]

        # Verificar el hash previo
        if bloque_actual["hash_previo"] != bloque_previo["hash_actual"]:
            return False, f"Error en el bloque #{bloque_actual['index']}: El hash previo no coincide."

        # Recalcular el hash del bloque actual BASÁNDOSE EN SU CONTENIDO (excepto el hash_actual en sí)
        bloque_para_hash = bloque_actual.copy()
        del bloque_para_hash["hash_actual"] # Excluimos el hash actual al recalcular
        hash_actual_calculado = calcular_hash(bloque_para_hash)

        # Imprimir hashes para comparación
        print(f"Verificando Bloque #{bloque_actual['index']}:")
        print(f"  Hash Almacenado: {bloque_actual['hash_actual']}")
        print(f"  Hash Calculado: {hash_actual_calculado}")

        # Verificar si el hash actual almacenado es correcto
        if bloque_actual["hash_actual"] != hash_actual_calculado:
            return False, f"Error en el bloque #{bloque_actual['index']}: El hash actual es incorrecto."

    return True, "Cadena de bloques íntegra."

# --- Simulación Principal ---
if __name__ == "__main__":
    blockchain = cargar_blockchain()

    print("--- Simulación de Generación de Datos IoT ---")
    for i in range(5):  # Simular 5 lotes de datos
        lote_de_datos = [generar_dato(j) for j in range(NUM_DISPOSITIVOS)]
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Datos generados: {lote_de_datos}")
        guardar_en_nube(lote_de_datos)
        hash_lote = hashlib.sha256(json.dumps(lote_de_datos, sort_keys=True).encode('utf-8')).hexdigest()
        blockchain = agregar_bloque(blockchain, {"hash_datos": hash_lote, "cantidad": len(lote_de_datos), "timestamp_registro": datetime.now().isoformat()})
        time.sleep(INTERVALO_GENERACION)

    print("\n--- Historial de Datos Generados (Nube) ---")
    datos_en_nube = leer_datos_nube()
    for dato in datos_en_nube:
        print(dato)

    print("\n--- Hashes Almacenados en la Blockchain ---")
    for bloque in blockchain:
        if bloque["index"] > 0:
            print(f"Bloque #{bloque['index']}: Hash de datos = {bloque['datos']['hash_datos']}, Hash actual = {bloque['hash_actual']}, Hash previo = {bloque['hash_previo']}")

    # --- Verificación de Integridad ---
    print("\n--- Verificación de Integridad ---")
    integridad, mensaje = verificar_cadena(blockchain)
    print(mensaje)

    # --- Simulación de Alteración de Datos en la Nube ---
    if datos_en_nube:
        print("\n--- Simulación de Alteración de Datos en la Nube ---")
        indice_a_alterar = 0
        dato_original = datos_en_nube[indice_a_alterar].copy()
        datos_en_nube[indice_a_alterar]["temperatura"] += 5  # Alterar la temperatura
        with open(ARCHIVO_NUBE, 'w') as f:
            json.dump(datos_en_nube, f, indent=4)
        print(f"Dato alterado en la nube: {dato_original} -> {datos_en_nube[indice_a_alterar]}")

        # Volver a verificar la cadena (la integridad de la blockchain no se ve afectada por la alteración de los datos en la nube directamente,
        # pero si se generaran nuevos lotes basados en los datos alterados, sus hashes serían diferentes).
        integridad_post_alteracion, mensaje_post_alteracion = verificar_cadena(blockchain)
        print("\n--- Verificación de Integridad Después de la Alteración en la Nube ---")
        print(mensaje_post_alteracion)

        # Para demostrar cómo se rompería la cadena si los hashes registrados se basaran directamente en los datos alterados,
        # tendríamos que simular una nueva ronda de generación y registro.

    # --- Simulación de Alteración de un Bloque en la Blockchain ---
    if len(blockchain) > 1:
        print("\n--- Simulación de Alteración de un Bloque en la Blockchain ---")
        indice_bloque_alterar = 1
        hash_original = blockchain[indice_bloque_alterar]["hash_actual"]
        blockchain[indice_bloque_alterar]["datos"]["hash_datos"] = "dato_falsificado"
        blockchain[indice_bloque_alterar]["hash_actual"] = calcular_hash(blockchain[indice_bloque_alterar])
        guardar_blockchain(blockchain)
        print(f"Hash del bloque #{indice_bloque_alterar} alterado: {hash_original} -> {blockchain[indice_bloque_alterar]['hash_actual']}")

        integridad_post_alteracion_blockchain, mensaje_post_alteracion_blockchain = verificar_cadena(blockchain)
        print("\n--- Verificación de Integridad Después de la Alteración en la Blockchain ---")
        print(mensaje_post_alteracion_blockchain)