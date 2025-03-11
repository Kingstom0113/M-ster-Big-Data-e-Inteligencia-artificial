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