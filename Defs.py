from os import system as sy
import DataBase as db

# Cadastrar novo produto
def addProduct():
    while True:

#Pedir nome produto
        while True:
            product = input('\nNome do produto:\n').upper()

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
            sy('cls')
            print(f'''\n
Produto: {product}
Categoria: {category}
Quantidade: {amount}
Setor: {location}      
            \n''')

            if input('Confirmar cadastro?   [S/N]\n').upper() == 'S':
                break
            else:
                continue

# Criação de ID
        i = db.cur.execute('''SELECT id FROM IDs''')
        id = int(i.fetchall()[0][0] +1)

        db.cur.execute(f'''
        DELETE FROM IDs ''')

        db.cur.execute(f'''
        INSERT INTO IDs VALUES ({id})''')
        db.con.commit()

# Cria lista com as infomações obtidas       
        Current_product = (id, product, category, amount, location)

# Salva as informações no banco de dados "stock"
        db.cur.execute('''
        INSERT INTO stock (id, product, category, amount, location) VALUES (?,?,?,?,?)''', Current_product)
        db.con.commit()

# Adiciona o novo produto na tabela de historico
        history = (product, '+' + str(amount), str(location))
        db.cur.execute(f'''
        INSERT INTO history (product, H_productAmount, H_productLocation) VALUES (?,?,?)''', history)
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
        
        new = input('\nCadastrar novo produto?  [S/N]\n').upper()
        sy('cls')
        if new  == 'S':
            continue
        else: 
            break
        #MENU( )


# Consultar tabela de produtos
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
        sy('cls')
        format =('ID','PRODUTO','CATEGORIA','QUANTIDADE','SETOR')
        for l in format:
            print(f'{l:^20}', end =' ')
        for lines in db.cur.execute(f''' 
        SELECT  * FROM stock ORDER BY {opc}''' ):
            
            print('\n')
            for i in lines:    
                print(f'{i:^20}', end =' ')
        print('\n')

# Perguntar se quer retornar ao menu ou vizualizar a tabela de outra forma 
        exit = input('\nVoltar ao menu?      [S/N]\n').upper()
        if 'S' in exit:
            break
        else: 
            continue

    # Voltar ao Menu
        #menu()


# Comsulta expecifica
def consultSpec():
    opc = ' '
    while True:
        sy('cls')

# Perguntar Qual categoria será buscada
        while True:
            

            try: select = int(input('''\n
Procurar produto por:
[1] ID
[2] Nome
[3] Categoria
[4] Setor no estoque
                                    
        '''))
            except:
                sy('cls')
                print('\nOpção invalida!')
                continue

# Opções possiveis
            match select:
                case 1:
                    opc = 'id'
                    by = 'ID'
                    break
                case 2:
                    opc = 'product'
                    by = 'Nome'
                    break

# Em caso de escolher 'categoria' é necessário outra seleção de opção para facilitar o manuseio do usuario
                case 3:
                    opc = 'category'
                    while True:
                        try: catg = int(input('''\n
Categoria do produto:
[1] Televisores
[2] Câmeras
[3] Computadores
[4] Celulares e acessórios
                                        
                        '''))
                        except:
                            sy('cls')
                            print('\nOpção invalida!')
                            continue
                        match catg:
                            case 1:
                                search = 'Televisores'
                                break
                            case 2:
                                search = 'Câmeras'
                                break
                            case 3:
                                search = 'Computadores'
                                break
                            case 4:
                                search = 'Celulares e acessórios'
                                break
                            case _:
                                sy('cls')
                                print('\nOpção invalida!')
                                continue
                case 4:
                    opc = 'location'
                    by = 'Setor'
                    break
                case _:
                    sy('cls')
                    print('\nOpção invalida!')
                    continue
            if opc == 'category':
                break

# Caso o produto não estiver sendo procurado pela 'categoria', pergunta ao ususario pelo o que deve procurar
        if opc != 'category':
            search = input(f'{by} do produto:\n').upper()

# Mostrar produtos referentes a pesquisa
        k = db.cur.execute(f'''
        SELECT * FROM stock WHERE {opc} LIKE '%{search}%'
        ''')
        print('\n')
        format = ('ID','PRODUTO','CATEGORIA','QUANTIDADE','SETOR')
        for l in format:
            print(f'{l:^20}', end =' ')
        for lines in k:
            print('\n')
            for i in lines:    
                print(f'{i:^20}', end =' ')
        print('\n')
        
# Perguntar se quer voltar ao Menu
        exit = input('\nVoltar ao menu?      [S/N]\n').upper()
        if 'S' in exit:
            break 
            #Menu()
        else: 
            continue    
        

# Entrada de produtos no estoque
def ProductEntry():
    sy('cls') 
    print('\n>> Entrada de produto no estoque.\n')
    while True:

# Pedir o nome do produto e verificando se ele existe na tabela
        while True:
            entryproduct = input('\nNome do produto:\n').upper()
            E = db.cur.execute(f'''
            SELECT * FROM stock WHERE product = '{entryproduct}'
            ''')
            if E.fetchall() == []:
                sy('cls')
                print('\n>> Entrada de produto no estoque.\n')
                print('\nProduto não encontrado!')
                continue
            break

# Pedir a quantidade de entrada do produto
        while True:
            try: entry = int(input('\nQuantidade de entrada:\n'))
            except:
                sy('cls')
                print('\n>> Entrada de produto no estoque.\n')
                print('\nValor invalido!')
                continue
            if entry >= 9999 or entry <= 0:
                sy('cls')
                print('\n>> Entrada de produto no estoque.\n')
                print('\nValor invalido!')
                continue
            break

# Somar Quantidade anterior com a entrada atual
        B = db.cur.execute(f'''
        SELECT amount FROM stock WHERE product = '{entryproduct}'
        ''')
        VB = int(B.fetchall()[0][0])
        total = VB + entry

# Salvar alteração no historico do produto
        A = db.cur.execute(f'''
        SELECT H_productAmount FROM history WHERE product = '{entryproduct}'
        ''')
        AB = A.fetchone()[0]
        BB = str(AB)
        HA = BB + '+' + str(entry)
        db.cur.execute(f''' 
        UPDATE history SET H_productAmount = '{HA}' WHERE product = '{entryproduct}'
        ''')
       
# Gravar alterações na tabela "stock"
        db.cur.execute(f'''
        UPDATE stock SET amount = '{total}' WHERE product = '{entryproduct}'
        ''')
        db.con.commit()

# Mensagem de confirmação
        #sy('cls')
        print('\n>> Entrada de produto no estoque.\n')
        print(f'\nA quantidade de "{entryproduct}" foi atualizada com sucesso.\n{VB} >>> {total}\n')

# Perguntar se quer atualizar outro item
        exit = input('\nAtualizar novo item?      [S/N]\n').upper()
        if 'S' not in exit:
            break 
            #Menu()
        else:
            sy('cls')
            print('\n>> Entrada de produto no estoque.\n')
            continue    


# Saida de produtos do estoque (mesma logica da entrada de produtos porem subitraindo a quantidade fornecida)
def ProductExit():
    sy('cls') 
    print('\n>> Saida de produto do estoque.\n')
    while True:

# Pedir o nome do produto e verificando se ele existe na tabela
        while True:
            entryproduct = input('\nNome do produto:\n').upper()
            E = db.cur.execute(f'''
            SELECT * FROM stock WHERE product = '{entryproduct}'
            ''')
            if E.fetchall() == []:
                sy('cls')
                print('\n>> Saida de produto do estoque.\n')
                print('\nProduto não encontrado!')
                continue
            break

# Pedir a quantidade de saida do produto
        while True:
            try: entry = int(input('\nQuantidade de Saida:\n - '))
            except:
                sy('cls')
                print('\n>> Saida de produto no estoque.\n')
                print('\nValor invalido!')
                continue
            if entry >= 9999 or entry <= 0:
                sy('cls')
                print('\n>> Saida de produto no estoque.\n')
                print('\nValor invalido!')
                continue

# Subitrai Quantidade anterior com a saida atual 
            B = db.cur.execute(f'''
            SELECT amount FROM stock WHERE product = '{entryproduct}'
            ''')
            VB = int(B.fetchall()[0][0])
            total = VB - entry

# Confirmar se o Total não será negativo
            if total < 0:
                sy('cls')
                print('\n>> Saida de produto no estoque.\n')
                print('\nValor invalido!')
                print('A quantidade no estoque ficaria abaixo de zero.\n')
                continue
            break

# Salvar alteração no historico do produto
        A = db.cur.execute(f'''
        SELECT H_productAmount FROM history WHERE product = '{entryproduct}'
        ''')
        AB = A.fetchone()[0]
        BB = str(AB)
        HA = BB + '-' + str(entry)
        db.cur.execute(f''' 
        UPDATE history SET H_productAmount = '{HA}' WHERE product = '{entryproduct}'
        ''')

# Gravar alterações no DB "stock"
        db.cur.execute(f'''
        UPDATE stock SET amount = '{total}' WHERE product = '{entryproduct}'
        ''')
        db.con.commit()

# Mensagem de confirmação
        sy('cls')
        print('\n>> Saida de produto no estoque.\n')
        print(f'\nA quantidade de "{entryproduct}" foi atualizada com sucesso.\n{VB} >>> {total}\n')

# Perguntar se quer atualizar outro item
        exit = input('\nAtualizar novo item?      [S/N]\n').upper()
        if 'S' not in exit:
            break 
            #Menu()
        else:
            sy('cls')
            print('\n>> Saida de produto no estoque.\n')
            continue
       
            
            
