import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'c:\Users\alumno\Documents\M-ster-Big-Data-e-Inteligencia-artificial\Sistemas de Big Data\🤑💸Ventas - Proceso ETL + Análisis - Financial Sample\Financial Sample.xlsx')
df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'])
df['YearMonth'] = df['Date'].dt.to_period('M')
sales_trend = df.groupby('YearMonth')['Sales'].sum()

ax = sales_trend.plot(kind='line', title='Evolución de Ventas a lo Largo del Tiempo')
plt.ylabel('Total de Ventas')
plt.xlabel('Mes y Año')
plt.xticks(rotation=45)

for x, y in zip(sales_trend.index, sales_trend):
    ax.annotate(f'{y:,.0f}', (x, y), textcoords="offset points", xytext=(0,10), ha='center')

plt.tight_layout()
plt.show()
