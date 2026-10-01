import pandas as pd
import sqlite3

# Cargar el archivo Excel
excel_path = 'Nominas.xlsx'
df = pd.read_excel(excel_path)

# Normalizar columnas
df.columns = df.columns.str.strip().str.lower()

# --- AQUÍ CAMBIAS EL NOMBRE ---
conn = sqlite3.connect('nominas.db') 

df.to_sql('jugadores', conn, if_exists='replace', index=False)
conn.close()

print("¡Base de datos 'nominas.db' creada exitosamente!")