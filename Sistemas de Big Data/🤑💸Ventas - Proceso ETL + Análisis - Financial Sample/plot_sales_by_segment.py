import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'c:\Users\alumno\Documents\M-ster-Big-Data-e-Inteligencia-artificial\Sistemas de Big Data\🤑💸Ventas - Proceso ETL + Análisis - Financial Sample\Financial Sample.xlsx')
df.columns = df.columns.str.strip()
sales_by_segment = df.groupby('Segment')['Sales'].sum().sort_values()

ax = sales_by_segment.plot(kind='bar', title='Total de Ventas por Segmento')
plt.ylabel('Total de Ventas')
plt.xlabel('Segmento')

for p in ax.patches:
    ax.annotate(f'{p.get_height():,.0f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='bottom')

plt.tight_layout()
plt.show()
