# Limpieza de Datos en la Guerra del Anillo

---

## Contexto

Como archivista de la Biblioteca de Minas Tirith, he recibido un dataset con información sobre las batallas de la Guerra del Anillo. Sin embargo, este dataset contiene varios problemas de calidad que deben ser resueltos antes de realizar un análisis estratégico.

---

## Dataset: Batallas de la Guerra del Anillo

El dataset contiene las siguientes columnas:

- **`ID_Batalla`**: Identificador único de la batalla.
- **`Nombre_Batalla`**: Nombre de la batalla (ejemplo: "La Batalla del Abismo de Helm").
- **`Fecha`**: Fecha en la que ocurrió la batalla (en formato YYYY-MM-DD).
- **`Lugar`**: Lugar donde se llevó a cabo la batalla (ejemplo: "Abismo de Helm", "Minas Tirith").
- **`Bando`**: Bando principal involucrado (ejemplo: "Comunidad del Anillo", "Sauron", "Saruman").
- **`Líder`**: Líder del bando (ejemplo: "Aragorn", "Sauron", "Saruman").
- **`Bajas_Enemigas`**: Número de bajas enemigas reportadas.
- **`Bajas_Propias`**: Número de bajas propias reportadas.
- **`Victoria`**: Indica si el bando ganó la batalla (valores: "Sí", "No").
- **`Anotaciones`**: Notas adicionales sobre la batalla.

---

## Problemas de Calidad Identificados

- **Valores Faltantes:**
  - Columna "Líder": Valores NaN presentes.
  - Columna "Bajas_Propias": Un valor NaN presente.
- **Inconsistencias y Errores Tipográficos:**
  - Columna "Bando": Inconsistencia entre "Saurón" y "Sauron".
- **Valores Atípicos:**
  - Columna "Bajas_Enemigas": Valor extremadamente alto (1,000,000) y valor negativo (-1000).
  - Columna "Bajas_Propias": Valores atípicos presentes.
- **Errores de Formato:**
  - Columna "Fecha": Formatos inconsistentes ("YYYY-MM-DD" y "DD/MM/YYYY").
- **Violación de Reglas de Negocio:**
  - Columna "Victoria": Valor incorrecto ("Tal vez").
  - Columnas "Bajas_Enemigas" y "Bajas_Propias": Valores negativos.
  - Columna "Lugar": Puede contener lugares no reconocidos de la Tierra Media.

---

## Técnicas de Limpieza de Datos Aplicadas

- **Valores Faltantes:**
  - Imputación de "Desconocido" en la columna "Líder".
  - Imputación de la mediana en la columna "Bajas_Propias".
- **Inconsistencias y Errores Tipográficos:**
  - Unificación de la columna "Bando" a "Sauron".
- **Valores Atípicos:**
  - Conversión a valor absoluto de los valores negativos en las columnas de bajas.
  - Acotación de valores atípicos mediante el método IQR (rango intercuartílico).
- **Errores de Formato:**
  - Estandarización del formato de la columna "Fecha" a "YYYY-MM-DD" usando una función personalizada que acepta ambos formatos.
- **Violación de Reglas de Negocio:**
  - Corrección del valor incorrecto en la columna "Victoria" a "No" si no es "Sí" o "No".
  - Validación de la columna "Lugar" para que solo contenga lugares conocidos de la Tierra Media; si no, se reemplaza por "Lugar desconocido".

---

## Justificación de las Decisiones Tomadas

- **Imputación de valores faltantes:**  
  Se optó por imputar "Desconocido" en "Líder" para no perder información relevante y la mediana en "Bajas_Propias" para mantener la tendencia central sin distorsionar el análisis.
- **Corrección de errores tipográficos:**  
  Unificar nombres de bandos evita duplicidades y facilita el análisis.
- **Tratamiento de valores atípicos y negativos:**  
  Los valores negativos no tienen sentido en el contexto de bajas, por lo que se convierten a positivos. Los valores atípicos se acotan usando el IQR para evitar distorsiones en el análisis.
- **Estandarización de fechas:**  
  Unificar el formato de fechas permite análisis temporales correctos.
- **Normalización de la columna "Victoria":**  
  Solo se aceptan los valores "Sí" o "No" para cumplir las reglas de negocio.
- **Validación de lugares:**  
  Solo se aceptan lugares reconocidos de la Tierra Media para asegurar la calidad y coherencia del dato.

---

## Código de Limpieza de Datos en Python

```python
import pandas as pd
import numpy as np

# Crear dataset ficticio
data = {
    'ID_Batalla': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Nombre_Batalla': ['Abismo de Helm', 'Minas Tirith', 'Batalla de los Campos del Pelennor', 'Batalla del Morannon', 'Batalla de Cuernavilla', 'Batalla de Lothlórien', 'Batalla de Erebor', 'Batalla de Dale', 'Batalla de la Puerta Negra', 'Batalla de Bywater'],
    'Fecha': ['3019-03-03', '3019-03-15', '3019-03-15', '3019-03-25', '3019-03-03', '3019-03-22', '3019-03-17', '3019-03-17', '3019-03-25', '03/11/3019'],
    'Lugar': ['Abismo de Helm', 'Minas Tirith', 'Campos del Pelennor', 'Morannon', 'Cuernavilla', 'Lothlórien', 'Erebor', 'Dale', 'Puerta Negra', 'Bywater'],
    'Bando': ['Comunidad del Anillo', 'Comunidad del Anillo', 'Comunidad del Anillo', 'Comunidad del Anillo', 'Comunidad del Anillo', 'Saurón', 'Sauron', 'Saruman', 'Saurón', 'Comunidad del Anillo'],
    'Líder': ['Aragorn', 'Gandalf', 'Théoden', 'Aragorn', np.nan, np.nan, 'Sauron', 'Saruman', 'Sauron', 'Sam'],
    'Bajas_Enemigas': [10000, 50000, -1000, 70000, 8000, 2000, 1000000, 4000, 5000, 100],
    'Bajas_Propias': [500, 2000, 3000, 4000, np.nan, 5000, 6000, 7000, 8000, 10],
    'Victoria': ['Sí', 'Sí', 'Sí', 'Sí', 'Sí', 'No', 'Tal vez', 'No', 'No', 'Sí'],
    'Anotaciones': ['Victoria decisiva', 'Derrota de Sauron', 'Derrota de los Nazgûl', 'Destrucción del Anillo', 'Defensa exitosa', 'Ataque repelido', 'Ataque repelido', 'Ataque repelido', 'Ataque repelido', 'Victoria en la Comarca']
}

df = pd.DataFrame(data)

# 1. Corregir errores tipográficos en la columna 'Bando'
df['Bando'] = df['Bando'].replace({'Saurón': 'Sauron'})

# 2. Imputar valores faltantes en 'Líder' con 'Desconocido'
df['Líder'] = df['Líder'].fillna('Desconocido')

# 3. Imputar valores faltantes en 'Bajas_Propias' con la mediana de la columna
df['Bajas_Propias'] = df['Bajas_Propias'].fillna(df['Bajas_Propias'].median())

# 4. Corregir formato de fechas a YYYY-MM-DD
def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, format='%Y-%m-%d')
    except ValueError:
        return pd.to_datetime(date_str, format='%d/%m/%Y', errors='coerce')

df['Fecha'] = df['Fecha'].apply(parse_date)

# 5. Eliminar valores negativos en 'Bajas_Enemigas' y 'Bajas_Propias'
df['Bajas_Enemigas'] = df['Bajas_Enemigas'].apply(lambda x: abs(x) if x < 0 else x)
df['Bajas_Propias'] = df['Bajas_Propias'].apply(lambda x: abs(x) if x < 0 else x)

# 6. Asegurar que 'Victoria' solo contenga 'Sí' o 'No'
df['Victoria'] = df['Victoria'].apply(lambda x: 'No' if x not in ['Sí', 'No'] else x)

# 7. Identificar y manejar valores atípicos en 'Bajas_Enemigas' y 'Bajas_Propias' usando IQR
q1_enemigas = df['Bajas_Enemigas'].quantile(0.25)
q3_enemigas = df['Bajas_Enemigas'].quantile(0.75)
iqr_enemigas = q3_enemigas - q1_enemigas
limite_inferior_enemigas = q1_enemigas - 1.5 * iqr_enemigas
limite_superior_enemigas = q3_enemigas + 1.5 * iqr_enemigas
df['Bajas_Enemigas'] = df['Bajas_Enemigas'].apply(
    lambda x: limite_superior_enemigas if x > limite_superior_enemigas else (limite_inferior_enemigas if x < limite_inferior_enemigas else x)
)

q1_propias = df['Bajas_Propias'].quantile(0.25)
q3_propias = df['Bajas_Propias'].quantile(0.75)
iqr_propias = q3_propias - q1_propias
limite_inferior_propias = q1_propias - 1.5 * iqr_propias
limite_superior_propias = q3_propias + 1.5 * iqr_propias
df['Bajas_Propias'] = df['Bajas_Propias'].apply(
    lambda x: limite_superior_propias if x > limite_superior_propias else (limite_inferior_propias if x < limite_inferior_propias else x)
)

# 8. Validar que 'Lugar' solo contenga lugares conocidos de la Tierra Media
lugares_conocidos = [
    'Abismo de Helm', 'Minas Tirith', 'Campos del Pelennor', 'Morannon', 'Cuernavilla',
    'Lothlórien', 'Erebor', 'Dale', 'Puerta Negra', 'Bywater'
]
df['Lugar'] = df['Lugar'].apply(lambda x: x if x in lugares_conocidos else 'Lugar desconocido')

# Mostrar dataset limpio
print("Dataset limpio y corregido:")
print(df)
```

---

## Resumen de Cambios Realizados

- Errores tipográficos en "Bando" corregidos.
- Valores faltantes en "Líder" y "Bajas_Propias" imputados.
- Formato de fechas unificado a YYYY-MM-DD.
- Valores negativos en bajas corregidos.
- Columna "Victoria" normalizada a "Sí" o "No".
- Valores atípicos en bajas tratados con IQR.
- Lugares validados contra lista de lugares conocidos.

---