from os import system as sy
import DataBase as db

# Cadastrar novo produto
def addProduct():
    while True:

#Pedir nome produto
        while True:
            product = input('\nNome do produto:\n')

# Pedir categoria
            while True:
                try:    ctg = int(input(''' 
Categoria do produto:
[1] Televisores
[2] Câmeras
[3] Computadores
[4] Celulares e acessórios\n'''))
                except:
                    print('\nCategoria invalida!')
                    continue   
                match ctg:
                    case 1:
                        category = 'Televisores'
                        break
                    case 2:
                        category = 'Câmeras'
                        break
                    case 3:
                        category = 'Computadores'
                        break
                    case 4:
                        category = 'Celulares e acessórios'
                        break
                    case _:
                        print('\nCategoria invalida!')
                        continue
                

# Pedir quatidade
            while True:
                try: amount = int(input('\nQuantidade:\n'))
                except: 
                    print('\nDigite um numero inteiro!', end = ' ')
                    continue
                break

# Pedir Setor no estoque
            while True:
                try: location = int(input('\nSetor no estoque:\n'))
                except: 
                    print('\nDigite um numero inteiro!', end = ' ')
                    continue
                break

# Confirmar cadastro do produto
            print(f'''\n
            Produto: {product}
            Categoria: {category}
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
        Current_product = (id, product, category, amount, location)

# Salva as informações no banco de dados "stock"
        db.cur.execute('''
        INSERT INTO stock (id, product, category, amount, location) VALUES (?,?,?,?,?)''', Current_product)
        db.con.commit()    


# Encerrar cadastro de novos produtos
        sy('cls')
        print(f'''\n
            Produto cadastrado com sucesso.
              
            Produto: {product}
            Categoria: {category}
            Quantidade: {amount}
            Setor: {location} 

            ID: {id:0>4}

            ''')
        
        new = input('\nCadastrar novo produto?  [S/N]').upper()
        if new  == 'S':
            continue
        else:
            break

# Consultar produtos
def consultProducts():
    while True:
        while True:

# Perguntar a ordem dos produtos
            try: select = int(input('''\n
    Verificar estoque por:
    [1] ID
    [2] Ordem alfabética
    [3] Categoria
    [4] Quantidade no estoque
    [5] Setor do estoque
                                    
    '''))
            except:
                print('\nOpção invalida!')
                continue
            match select:
                case 1:
                    opc = 'id'
                    break
                case 2:
                    opc = 'product'
                    break
                case 3:
                    opc = 'category'
                    break
                case 4:
                    opc = 'amount'
                    break
                case 5:
                    opc = 'location'
                    break
                case _:
                    print('\nOpção invalida!')
                    continue
        
# Mostrar tabela dos produtos ordenada pela escolha do usuario       
        for lines in db.cur.execute(f''' 
        SELECT  id, product, category, amount, location FROM stock ORDER BY {opc}''' ):      
            print(lines)
        exit = input('\nVoltar ao menu?      [S/N]\n').upper()
        if 'S' in exit:
            break
        else: 
            continue

# Voltar ao Menu
    #menu()