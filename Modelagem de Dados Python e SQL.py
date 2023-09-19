import pandas as pd
import re

# Os dados brutos devem ser inseridos aqui
raw_data = """
... (seus dados aqui) ...
"""

# Converta os dados brutos em uma estrutura de dados pandas
df = pd.DataFrame({'Texto': re.split(r'\n\n+', raw_data.strip())})
import sqlite3

# Conecte-se ao banco de dados (ou crie um novo)
conn = sqlite3.connect('hyundai_data.db')

# Crie uma tabela para armazenar os dados
conn.execute('''
    CREATE TABLE IF NOT EXISTS hyundai (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        texto TEXT
    )
''')

# Insira os dados na tabela
for row in df['Texto']:
    conn.execute('INSERT INTO hyundai (texto) VALUES (?)', (row,))

# Commit (salvar) as alterações e fechar a conexão
conn.commit()
conn.close()
conn = sqlite3.connect('hyundai_data.db')
cursor = conn.cursor()

cursor.execute('SELECT texto FROM hyundai WHERE texto LIKE "%Vision%"')

result = cursor.fetchone()
if result:
    vision = result[0]
    print(vision)
else:
    print("Visão não encontrada.")

conn.close()
