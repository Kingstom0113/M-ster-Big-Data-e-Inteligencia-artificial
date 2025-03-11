import hashlib
import os
from rich.console import Console
from rich.table import Table

console = Console()

def calcular_hash(archivo, algoritmo):
    hash_func = hashlib.new(algoritmo)
    try:
        with open(archivo, 'rb') as f:
            while chunk := f.read(8192):
                hash_func.update(chunk)
        return hash_func.hexdigest()
    except FileNotFoundError:
        console.print(f"[bold red]❌ Error:[/] El archivo {archivo} no existe.")
        return None

def guardar_hashes(hashes, archivo_salida="hashes.txt"):
    with open(archivo_salida, "w") as f:
        for nombre, hash_valor in hashes.items():
            f.write(f"{nombre}: {hash_valor}\n")
    console.print(f"[bold green]✅ Hashes guardados en {archivo_salida}[/]")

def verificar_integridad(archivo, algoritmo, archivo_hashes="hashes.txt"):
    hash_actual = calcular_hash(archivo, algoritmo)
    if not hash_actual:
        return

    try:
        with open(archivo_hashes, "r") as f:
            hashes_guardados = {}
            for line in f:
                partes = line.strip().split(": ")
                if len(partes) == 2:
                    hashes_guardados[partes[0]] = partes[1]

        if archivo in hashes_guardados:
            table = Table(title=f"Verificación de {archivo}")
            table.add_column("Archivo", justify="left", style="cyan")
            table.add_column("Estado", justify="center", style="magenta")

            if hashes_guardados[archivo] == hash_actual:
                table.add_row(archivo, "✅ NO Modificado")
            else:
                # Si el hash ha cambiado, actualizar el archivo de hashes
                hashes_guardados[archivo] = hash_actual
                with open(archivo_hashes, "w") as f:
                    for nombre, hash_valor in hashes_guardados.items():
                        f.write(f"{nombre}: {hash_valor}\n")
                table.add_row(archivo, "⚠️ MODIFICADO - Hash actualizado")
                
            console.print(table)
        else:
            console.print(f"[bold yellow]⚠️ No se encontró un hash almacenado para {archivo}.[/]")
    except FileNotFoundError:
        console.print(f"[bold red]❌ Error:[/] El archivo de hashes {archivo_hashes} no existe.")

if __name__ == "__main__":
    opcion = console.input("[bold blue]¿Qué deseas hacer?\n1. Calcular y guardar hashes\n2. Verificar integridad\nElige una opción (1/2): [/] ")

    archivos = {
        "archivo.txt": "sha256",
        "imagen.jpg": "md5",
        "documento.pdf": "sha1",
        "comprimido.zip": "sha512",
        "ejecutable.exe": "sha1"
    }

    if opcion == "1":
        hashes_calculados = {archivo: calcular_hash(archivo, algoritmo) for archivo, algoritmo in archivos.items()}
        guardar_hashes(hashes_calculados)
    elif opcion == "2":
        console.print("\n[bold blue]🔍 Verificando integridad de archivos...[/]\n")
        for archivo, algoritmo in archivos.items():
            verificar_integridad(archivo, algoritmo)
    else:
        console.print("[bold red]Opción no válida.[/]")
