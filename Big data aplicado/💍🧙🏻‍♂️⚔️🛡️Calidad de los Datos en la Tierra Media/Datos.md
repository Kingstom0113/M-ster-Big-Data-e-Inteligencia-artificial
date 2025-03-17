# Limpieza de Datos en la Guerra del Anillo
=====================================================

## Contexto
Como archivista de la Biblioteca de Minas Tirith, he recibido un dataset con información sobre las batallas de la Guerra del Anillo. Sin embargo, este dataset contiene varios problemas de calidad que deben ser resueltos antes de realizar un análisis estratégico.

## Dataset: Batallas de la Guerra del Anillo
El dataset contiene las siguientes columnas:

* **`ID_Batalla`**: Identificador único de la batalla.
* **`Nombre_Batalla`**: Nombre de la batalla (ejemplo: "La Batalla del Abismo de Helm").
* **`Fecha`**: Fecha en la que ocurrió la batalla (en formato YYYY-MM-DD).
* **`Lugar`**: Lugar donde se llevó a cabo la batalla (ejemplo: "Abismo de Helm", "Minas Tirith").
* **`Bando`**: Bando principal involucrado (ejemplo: "Comunidad del Anillo", "Saurón", "Saruman").
* **`Líder`**: Líder del bando (ejemplo: "Aragorn", "Saurón", "Saruman").
* **`Bajas_Enemigas`**: Número de bajas enemigas reportadas.
* **`Bajas_Propias`**: Número de bajas propias reportadas.
* **`Victoria`**: Indica si el bando ganó la batalla (valores: "Sí", "No").
* **`Anotaciones`**: Notas adicionales sobre la batalla.

## Problemas de Calidad Identificados
---------------------------

* **Valores Faltantes:**
  + Columna "Líder": Valores NaN presentes.
  + Columna "Bajas_Propias": Un valor NaN presente.
* **Inconsistencias y Errores Tipográficos:**
  + Columna "Bando": Inconsistencia entre "Saurón" y "Sauron".
* **Valores Atípicos:**
  + Columna "Bajas_Enemigas": Valor extremadamente alto (1,000,000) y valor negativo (-1000).
  + Columna "Bajas_Propias": Valores atípicos presentes.
* **Errores de Formato:**
  + Columna "Fecha": Formatos inconsistentes ("YYYY-MM-DD" y "DD/MM/YYYY").
* **Violación de Reglas de Negocio:**
  + Columna "Victoria": Valor incorrecto ("Tal vez").
  + Columnas "Bajas_Enemigas" y "Bajas_Propias": Valores negativos.

## Técnicas de Limpieza de Datos Aplicadas
--------------------------------------

* **Valores Faltantes:**
  + Imputación de "Desconocido" en la columna "Líder".
  + Imputación de la mediana en la columna "Bajas_Propias".
* **Inconsistencias y Errores Tipográficos:**
  + Unificación de la columna "Bando" a "Sauron".
* **Valores Atípicos:**
  + Conversión a valor absoluto de los valores negativos en las columnas de bajas.
  + Acotación de valores atípicos mediante el método IQR.
* **Errores de Formato:**
  + Estandarización del formato de la columna "Fecha" a "YYYY-MM-DD".
* **Violación de Reglas de Negocio:**
  + Corrección del valor incorrecto en la columna "Victoria" a "No".

## Código de Limpieza de Datos en Python
```python
import pandas as pd
import numpy as np

# Crear dataset ficticio
data = {
    'ID_Batalla': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Nombre_Batalla': ['Abismo de Helm', 'Minas Tirith', 'Batalla de los Campos del Pelennor', 'Batalla del Morannon', 'Batalla de Cuernavilla', 'Batalla de Lothlórien', 'Batalla de Erebor', 'Batalla de Dale', 'Batalla de la Puerta Negra', 'Batalla de Bywater'],
    'Fecha': ['3019-03-03', '3019-03-15', '3019-03-15', '3019-03-25', '3019-03-03', '3019-03-22', '3019-03-17', '3019-03-17', '3019-03-25', '03/11/3019'],  # Formato inconsistente
    'Lugar': ['Abismo de Helm', 'Minas Tirith', 'Campos del Pelennor', 'Morannon', 'Cuernavilla', 'Lothlórien', 'Erebor', 'Dale', 'Puerta Negra', 'Bywater'],
    'Bando': ['Comunidad del Anillo', 'Comunidad del Anillo', 'Comunidad del Anillo', 'Comunidad del Anillo', 'Comunidad del Anillo', 'Saurón', 'Sauron', 'Saruman', 'Saurón', 'Comunidad del Anillo'],  # Error tipográfico
    'Líder': ['Aragorn', 'Gandalf', 'Théoden', 'Aragorn', np.nan, np.nan, 'Sauron', 'Saruman', 'Sauron', 'Sam'],  # Valores faltantes
    'Bajas_Enemigas': [10000, 50000, -1000, 70000, 8000, 2000, 1000000, 4000, 5000, 100],  # Valor negativo y atípico
    'Bajas_Propias': [500, 2000, 3000, 4000, np.nan, 5000, 6000, 7000, 8000, 10],  # Valor faltante
    'Victoria': ['Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Tal vez', 'No', 'No', 'Sí'],  # Valor incorrecto
    'Anotaciones': ['Victoria decisiva', 'Derrota de Sauron', 'Derrota de los Nazgûl', 'Destrucción del Anillo', 'Defensa exitosa', 'Ataque repelido', 'Ataque repelido', 'Ataque repelido', 'Ataque repelido', 'Victoria en la Comarca']
}

# Crear DataFrame
df = pd.DataFrame(data)

# Limpieza de datos
# Corregir errores tipográficos en la columna 'Bando'
df['Bando'] = df['Bando'].replace({'Saurón': 'Sauron'})

# Imputar valores faltantes en 'Líder' con 'Desconocido'
df['Líder'] = df['Líder'].fillna('Desconocido')

# Imputar valores faltantes en 'Bajas_Propias' con la mediana de la columna
df['Bajas_Propias'] = df['Bajas_Propias'].fillna(df['Bajas_Propias'].median())

# Corregir formato de fechas a YYYY-MM-DD
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, format='%Y-%m-%d')
    except ValueError:
        return pd.to_datetime(date_str, format='%d/%m/%Y', errors='coerce')

# Aplicar la función de parseo a la columna de fechas
df['Fecha'] = df['Fecha'].apply(parse_date)

# Eliminar valores negativos en 'Bajas_Enemigas' y 'Bajas_Propias'
df['Bajas_Enemigas'] = df['Bajas_Enemigas'].apply(lambda x: abs(x) if x < 0 else x)

df['Bajas_Propias'] = df['Bajas_Propias'].apply(lambda x: abs(x) if x < 0 else x)

# Asegurar que 'Victoria' solo contenga 'Sí' o 'No'
df['Victoria'] = df['Victoria'].apply(lambda x: 'No' if x not in ['Sí', 'No'] else x)

# Identificar y manejar valores atípicos en 'Bajas_Enemigas' y 'Bajas_Propias'
q1_enemigas = df['Bajas_Enemigas'].quantile(0.25)
q3_enemigas = df['Bajas_Enemigas'].quantile(0.75)
iqr_enemigas = q3_enemigas - q1_enemigas
limite_inferior_enemigas = q1_enemigas - 1.5 * iqr_enemigas
limite_superior_enemigas = q3_enemigas + 1.5 * iqr_enemigas
df['Bajas_Enemigas'] = df['Bajas_Enemigas'].apply(lambda x: limite_superior_enemigas if x > limite_superior_enemigas else (limite_inferior_enemigas if x < limite_inferior_enemigas else x))

q1_propias = df['Bajas_Propias'].quantile(0.25)
q3_propias = df['Bajas_Propias'].quantile(0.75)
iqr_propias = q3_propias - q1_propias
limite_inferior_propias = q1_propias - 1.5 * iqr_propias
limite_superior_propias = q3_propias + 1.5 * iqr_propias
df['Bajas_Propias'] = df['Bajas_Propias'].apply(lambda x: limite_superior_propias if x > limite_superior_propias else (limite_inferior_propias if x < limite_inferior_propias else x))

# Mostrar dataset limpio
print("Dataset limpio y corregido:")
print(df)