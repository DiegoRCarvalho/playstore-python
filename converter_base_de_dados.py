import pandas as pd

# Carregar a base de dados original
arquivo_csv = 'assets/Google-Playstore.csv'

df = pd.read_csv(arquivo_csv)

# Verificar se a coluna 'Maximum Installs' é numérica
df['Maximum Installs'] = pd.to_numeric(df['Maximum Installs'], errors='coerce')

# Remover linhas com valores ausentes em 'Maximum Installs'
df = df.dropna(subset=['Maximum Installs'])

# Selecionar os 50000 aplicativos mais instalados
top_apps = df.sort_values(by='Maximum Installs', ascending=False).head(50000)

# Salvar o resultado em um novo arquivo CSV
top_apps.to_csv('assets/playstore.csv', index=False)

