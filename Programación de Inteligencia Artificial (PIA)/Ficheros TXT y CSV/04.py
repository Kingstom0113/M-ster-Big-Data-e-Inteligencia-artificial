import csv

def leer_calificaciones(fichero):

    try:
        with open(fichero, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")  # Usar el delimitador correcto
            lista_calificaciones = []
            for row in reader:
                # Convertir notas y asistencia a los tipos correctos
                row["Asistencia"] = int(row["Asistencia"].replace("%", ""))  # Convertir asistencia a entero
                row["Parcial1"] = float(row["Parcial1"].replace(",", ".")) if row["Parcial1"] else 0.0
                row["Parcial2"] = float(row["Parcial2"].replace(",", ".")) if row["Parcial2"] else 0.0
                row["Ordinario1"] = float(row["Ordinario1"].replace(",", ".")) if row["Ordinario1"] else 0.0
                row["Ordinario2"] = float(row["Ordinario2"].replace(",", ".")) if row["Ordinario2"] else 0.0
                row["Practicas"] = float(row["Practicas"].replace(",", ".")) if row["Practicas"] else 0.0
                row["OrdinarioPracticas"] = float(row["OrdinarioPracticas"].replace(",", ".")) if row["OrdinarioPracticas"] else 0.0
                lista_calificaciones.append(row)

            # Ordenar la lista por el campo 'Apellidos'
            lista_calificaciones.sort(key=lambda x: x["Apellidos"])
            return lista_calificaciones
    except FileNotFoundError:
        print(f"El fichero '{fichero}' no existe.")
        return None
    except Exception as e:
        print(f"Error al procesar el fichero: {e}")
        return None


def calcular_nota_final(lista_calificaciones):

    for alumno in lista_calificaciones:
        parcial1 = alumno["Parcial1"] if alumno["Parcial1"] >= 4 else alumno["Ordinario1"]
        parcial2 = alumno["Parcial2"] if alumno["Parcial2"] >= 4 else alumno["Ordinario2"]
        practicas = alumno["Practicas"] if alumno["Practicas"] >= 4 else alumno["OrdinarioPracticas"]

        nota_final = (parcial1 * 0.3) + (parcial2 * 0.3) + (practicas * 0.4)
        alumno["NotaFinal"] = nota_final
    return lista_calificaciones


def separar_aprobados_suspensos(lista_calificaciones):

    aprobados = []
    suspensos = []

    for alumno in lista_calificaciones:
        asistencia = alumno["Asistencia"]
        parcial1 = alumno["Parcial1"] if alumno["Parcial1"] >= 4 else alumno["Ordinario1"]
        parcial2 = alumno["Parcial2"] if alumno["Parcial2"] >= 4 else alumno["Ordinario2"]
        practicas = alumno["Practicas"] if alumno["Practicas"] >= 4 else alumno["OrdinarioPracticas"]
        nota_final = alumno["NotaFinal"]

        if (
            asistencia >= 75 and
            parcial1 >= 4 and
            parcial2 >= 4 and
            practicas >= 4 and
            nota_final >= 5
        ):
            aprobados.append(alumno)
        else:
            suspensos.append(alumno)

    return aprobados, suspensos

def main():
    fichero = "calificaciones.csv"

    # Paso 1: Leer las calificaciones
    lista_calificaciones = leer_calificaciones(fichero)
    if not lista_calificaciones:
        return

    # Paso 2: Calcular la nota final
    lista_calificaciones = calcular_nota_final(lista_calificaciones)

    # Paso 3: Separar aprobados y suspensos
    aprobados, suspensos = separar_aprobados_suspensos(lista_calificaciones)

    # Imprimir resultados
    print("\n--- ALUMNOS APROBADOS ---")
    for alumno in aprobados:
        print(f"{alumno['Nombre']} {alumno['Apellidos']}: Nota Final = {alumno['NotaFinal']:.2f}")

    print("\n--- ALUMNOS SUSPENSOS ---")
    for alumno in suspensos:
        print(f"{alumno['Nombre']} {alumno['Apellidos']}: Nota Final = {alumno['NotaFinal']:.2f}")

if __name__ == "__main__":
    main()
