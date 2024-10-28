import sqlite3

# Estabelece a conexão com o DB "stock" ou o cria caso não exista.
con = sqlite3.connect('stock.db')

# Cria o cursor.
cur = con.cursor()

#-----------------------------------------------------#

# Cria a tabela "stock" caso não exista.
cur.execute('''CREATE TABLE IF NOT EXISTS stock(
    id,
    product,
    category,
    amount,
    location    
    )''')

#-----------------------------------------------------#

# Cria a tabela "IDs" caso não exista.
cur.execute('''CREATE TABLE IF NOT EXISTS IDs(
    id 
    )''')

# Adiciona iten a tabela "IDs".
cur.execute('''
INSERT INTO IDs VALUES (
0)
''')

#-----------------------------------------------------#

# Cria a tabela "history" caso não exista.
cur.execute('''CREATE TABLE IF NOT EXISTS history(
    product, H_productAmount, H_productLocation
    )''')

#-----------------------------------------------------#
