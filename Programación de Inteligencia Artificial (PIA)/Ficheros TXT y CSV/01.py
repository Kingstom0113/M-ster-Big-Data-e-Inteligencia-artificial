def crear_tabla(numero):
  """Crea un archivo de texto con la tabla de multiplicar del número dado."""
  if 1 <= numero <= 10:
    nombre_archivo = f"tabla-{numero}.txt"
    with open(nombre_archivo, 'w') as archivo:
      for i in range(1, 11):
        archivo.write(f"{numero} x {i} = {numero * i}\n") 
    print(f"Tabla de multiplicar de {numero} creada exitosamente.")
  else:
    print("El número debe estar entre 1 y 10.")

def mostrar_tabla(numero):
  """Muestra la tabla de multiplicar del número dado desde un archivo."""
  nombre_archivo = f"tabla-{numero}.txt"
  try:
    with open(nombre_archivo, 'r') as archivo:
      print(archivo.read())
  except FileNotFoundError:
    print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea(numero, linea):
  """Muestra una línea específica de la tabla de multiplicar."""
  nombre_archivo = f"tabla-{numero}.txt"
  try:
    with open(nombre_archivo, 'r') as archivo:
      lineas = archivo.readlines()
      if 1 <= linea <= 10:
        print(lineas[linea - 1].strip())
      else:
        print("La línea debe estar entre 1 y 10.")
  except FileNotFoundError:
    print(f"El archivo tabla-{numero}.txt no existe.")

# Ejemplo de uso:
numero = int(input("Ingrese un número entre 1 y 10: "))
crear_tabla(numero)

mostrar_tabla(numero)

linea = int(input("Ingrese una línea a mostrar (1-10): "))
mostrar_linea(numero, linea)