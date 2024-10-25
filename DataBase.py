import sqlite3

# Estabelece a conexão com DB "stock"
con = sqlite3.connect('stock.db')

# Cria o cursor
cur = con.cursor()

# Cria a tabela caso não exista
cur.execute('''CREATE TABLE IF NOT EXISTS stock(
    id,
    product,
    amount,
    location 
    )''')

#--------------------------------------------------------------

# Estabelece a conexão com o DB "ID"
cond = sqlite3.connect('ID.db')

# Cria o cursor
curd = cond.cursor()

# Cria a tabela caso não exista
curd.execute('''CREATE TABLE IF NOT EXISTS IDs(
    id 
    )''')

# Adiciona itens ao DB
curd.execute('''
INSERT INTO IDs VALUES (
0)
''')

#--------------------------------------------------------------
