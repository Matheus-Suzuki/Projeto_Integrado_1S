from os import system as sy
import DataBase as db

# Cadastrar novo produto
def addProduct():
    while True:

#Pedir nome produto
        while True:
            product = input('\nNome do produto:\n')

# Pedir quatidade
            while True:
                try: amount = int(input('\nQuantidade:\n'))
                except: 
                    print('\nDigite um numero inteiro!', end = ' ')
                    continue
                break

# Pedir Setor do produto
            while True:
                try: location = int(input('\nSetor do produto:\n'))
                except: 
                    print('\nDigite um numero inteiro!', end = ' ')
                    continue
                break

# Confirmar cadastro do produto
            print(f'''\n
            Produto: {product}
            Quantidade: {amount}
            Setor: {location}      
            \n''')

            if input('Confirmar cadastro?   [S/N]').upper() == 'S':
                break
            else:
                continue

# Criação de ID
        i = db.curd.execute('''SELECT id FROM IDs''')
        id = int(i.fetchall()[0][0] +1)

        db.curd.execute(f'''
        DELETE FROM IDs ''')

        db.curd.execute(f'''
        INSERT INTO IDs VALUES ({id})''')
        db.cond.commit()

# Cria lista com as infomações obtidas       
        Current_product = (id, product, amount, location)

# Salva as informações no banco de dados "stock"
        db.cur.execute('''
        INSERT INTO stock (id, product, amount, location) VALUES (?,?,?,?)''', Current_product)
        db.con.commit()    


# Encerrar cadastro de novos produtos
        #sy('cls')
        print(f'''\n
            Produto: {product}
            Quantidade: {amount}
            Setor: {location}      
            ID: {id}
            
            Cadastrado com sucesso.
            ''')
        new = input('\nCadastrar novo produto?  [S/N]').upper()
        if new  == 'S':
            continue
        else:
            break



        