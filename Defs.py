from os import system as sy
import DataBase as db
from datetime import datetime as dt

# Menu
def MainMenu():
    sy('cls')
    opcValidation =' ' 
    while True:

# Mostra a seleção de opições no menu principal
        try: MenuSelect = int(input(f'''
    WILD BUNNY ELETRONICS

>>  MENU.                                               (m) retorna ao menu.

    REGISTRAR:                   CONSULTAR:
    [1] NOVO PRODUTO.            [5] TABELA GERAL DE PRODUTOS.
    [2] ENTRADA DE PRODUTO.      [6] INFORMAÇÕES DE PRODUTO ESPECIFICO.
    [3] SAIDA DE PRODUTO.        [7] HISTORICO DE MOVIMENTAÇÃO DE PRODUTO.
    [4] MUDANÇA DE SETOR.        [8] SETOR DE PROCUTO ESPECIFICO NO ESTOQUE.

    {opcValidation}
    '''))
        except:
            sy('cls')
            opcValidation = '   Opição invalida, por favor digite um numero entre [1] e [6].'
            continue 

# Chama a função equivalente a escolha do ususario
        match MenuSelect:
            case 1:
                addProduct()
                break
            case 2:
                ProductEntry()
                break
            case 3:
                ProductExit()
                break
            case 4:
                pass
                break
            case 5:
                consultProducts()
            case 6:
                consultSpec()
                break
            case 7:
                ProductHistory()
            case 8:
                pass
            case _:
                sy('cls')
                opcValidation = '   Opição invalida, por favor digite um numero entre [1] e [6].'
                continue 

# Retornar ao menu
def ReturnMainmenu(x):
    if x == 'M':
        MainMenu()
    
# Cadastrar novo produto
def addProduct():
    sy('cls')
    while True:

#Pedir nome produto
        while True:
            sy('cls')
            print('\n    WILD BUNNY ELETRONICS\n')
            print('\n>>  Adicionar novo produto.\n   ')
            product = input('\n    Nome do produto:\n    ').upper()
            ReturnMainmenu(product)

# Pedir categoria
            while True:
                try:    ctg = int(input(''' 
    Categoria do produto:
                                        
    [1] Televisores
    [2] Câmeras
    [3] Computadores
    [4] Celulares\n    
    '''))
                except:
                    sy('cls')
                    print('\n    WILD BUNNY ELETRONICS\n')
                    print('\n>>  Adicionar novo produto.\n')
                    print('\n   Categoria invalida!')
                    continue
                ReturnMainmenu(ctg)   
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
                        category = 'Celulares'
                        break
                    case _:
                        sy('cls')
                        print('\n    WILD BUNNY ELETRONICS\n')
                        print('\n>>  Adicionar novo produto.\n')
                        print('\n    Categoria invalida!')
                        continue
                

# Pedir quatidade
            while True:
                try: amount = int(input('\n    Quantidade:\n    '))
                except:
                    sy('cls')
                    print('\n    WILD BUNNY ELETRONICS\n')
                    print('\n>>  Adicionar novo produto.\n') 
                    print('\n    Digite um numero inteiro!', end = ' ')
                    continue
                break

# Converte numeros negativos em positivos
            if amount < 0:
                amount = -amount

# Pergu8ntar local do produto dentro do estoque
            while True:
                try: QLocation = int(input('''
    Setor de armazenamento no estoque:

    [1] Norte
    [2] Sul
    [3] Leste
    [4] Oeste
                                      
    '''))
                except:
                    sy('cls')
                    print('\n    WILD BUNNY ELETRONICS\n')
                    print('\n>>  Adicionar novo produto.\n') 
                    print('\n    Setor invalido!', end = ' ')
                    continue
                match QLocation:
                    case 1:
                        location = 'Norte'
                        break
                    case 2:
                        location = 'Sul'
                        break
                    case 3:
                        location = 'Leste'
                        break
                    case 4:
                        location = 'Oeste'
                        break
                    case _:
                        sy('cls')
                        print('\n    WILD BUNNY ELETRONICS\n')
                        print('\n>>  Adicionar novo produto.\n') 
                        print('\n    Setor invalido!', end = ' ')
                        continue

# Confirmar cadastro do produto
            sy('cls')
            print('\n    WILD BUNNY ELETRONICS\n')
            print('\n>>  Adicionar novo produto.\n')
            print(f'''\n
    Produto: {product}
    Categoria: {category}
    Quantidade: {amount} 
    Setor no estoque: {location}
    
            \n''')
            Q = input('    Confirmar cadastro?   [S/N]\n    ').upper()
            ReturnMainmenu(Q)
            if Q  == 'S':
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
        history = (product, ' ' + str(amount))
        timer = (product, dt.now().strftime('%d/%m/%y   -   %H:%M'))

# Salva as informações no banco de dados "stock"
        db.cur.execute('''
        INSERT INTO stock (id, product, category, amount, location) VALUES (?,?,?,?,?)''', Current_product)
        db.con.commit()

# Adiciona o novo produto na tabela de historico       
        db.cur.execute(f'''
        INSERT INTO history (product, H_productAmount) VALUES (?,?)''', history)
        db.con.commit() 

# Salva a data e o horario em que o produto foi adicionado
        db.cur.execute('''
        INSERT INTO datetimer (product , D_time) VALUES (?,?)''' , timer)
        db.con.commit() 

# Encerrar cadastro de novos produtos
        sy('cls')
        print('\n    WILD BUNNY ELETRONICS\n')
        print('\n>>  Adicionar novo produto.\n')
        print(f'''\n
    Produto cadastrado com sucesso.
              
    Produto: {product}
    Categoria: {category}
    Quantidade: {amount}
    Setor: {location}

    ID: {id:0>4}

        ''')
        
        new = input('\n    Cadastrar novo produto?  [S/N]\n    ').upper()
        sy('cls')
        if new  == 'S':
            continue
        else:
            MainMenu() 
            break


# Consultar tabela de produtos
def consultProducts():
    sy('cls')
    while True:
        while True:
            sy('cls')
            print('\n    WILD BUNNY ELETRONICS\n')
            print('\n>>  Consultar todos os produto.\n')
# Perguntar a ordem dos produtos
            try: select = int(input('''\n
    Verificar estoque por:
                                    
    [1] ID
    [2] Ordem alfabética
    [3] Categoria
    [4] Quantidade no estoque
    [5] Setor no estoque
                                    
    '''))   
            except:
                print('\n    Opção invalida!')
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
                    print('\n    Opção invalida!')
                    continue
        
# Mostrar tabela dos produtos ordenada pela escolha do usuario       
        sy('cls')
        print('\n    WILD BUNNY ELETRONICS\n')
        print('\n>> Consultar todos os produtos.\n')
        format =('ID','PRODUTO','CATEGORIA','QUANTIDADE', 'SETOR')
        for l in format:
            print(f'{l:^20}', end =' ')
        for lines in db.cur.execute(f''' 
        SELECT  * FROM stock ORDER BY {opc}''' ):
            
            print('\n')
            for i in lines:    
                print(f'{i:^20}', end =' ')
        print('\n')

# Perguntar se quer retornar ao menu ou vizualizar a tabela de outra forma 
        exit = input('\n    Voltar ao menu?      [S/N]\n    ').upper()
        if 'S' in exit:
            MainMenu() 
        else: 
            continue

# Comsulta expecifica
def consultSpec():
    sy('cls')
    opc = ' '
    while True:
        
# Perguntar Qual categoria será buscada
        while True:
            sy('cls')
            print('\n    WILD BUNNY ELETRONICS\n')
            print('\n>>  Consultar produto.\n')
            try: select = int(input('''\n
    Procurar produto por:
                                    
    [1] ID
    [2] Nome
    [3] Categoria
                                    
    '''))
            except:
                sy('cls')
                print('\n    WILD BUNNY ELETRONICS\n')
                print('\n>>  Consultar produto.\n')
                print('\n    Opção invalida!')
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
                    sy('cls')
                    print('\n    WILD BUNNY ELETRONICS\n')
                    print('\n>>  Consultar produto.\n')
                    while True:
                        try: catg = int(input('''\n
    Categoria do produto:
    
    [1] Televisores
    [2] Câmeras
    [3] Computadores
    [4] Celulares
                                        
    '''))
                        except:
                            sy('cls')
                            print('\n    Opção invalida!')
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
                                search = 'Celulares'
                                break
                            case _:
                                sy('cls')
                                print('\n    WILD BUNNY ELETRONICS\n')
                                print('\n>>  Consultar produto.\n')
                                print('\n    Opção invalida!')
                                continue
                case _:
                    sy('cls')
                    print('\n    Opção invalida!')
                    continue
            if opc == 'category':
                break

# Caso o produto não estiver sendo procurado pela 'categoria', pergunta ao ususario pelo o que deve procurar
        if opc != 'category':
            sy('cls')
            print('\n    WILD BUNNY ELETRONICS\n')
            print('\n>>  Consultar produto.\n')
            search = input(f'    {by} do produto:\n    ').upper()
            ReturnMainmenu(search)

# Mostrar produtos referentes a pesquisa
        k = db.cur.execute(f'''
        SELECT * FROM stock WHERE {opc} LIKE '%{search}%'
        ''')
        J = k.fetchall()
        if J != []:
            sy('cls')
            print('\n    WILD BUNNY ELETRONICS\n')
            print('\n>>  Consultar produto.\n')
            print('\n')
            format = ('ID','PRODUTO','CATEGORIA','QUANTIDADE', 'SETOR')
            for l in format:
                print(f'{l:^15}', end =' ')
            for lines in J:
                print('\n')
                for i in lines:    
                    print(f'{i:^15}', end =' ')
            print('\n')
        else:
            newTry = input('\n    Produto não encontrado, tentar novamente?   [S/N]\n    ').upper()
            if "S" in newTry:
                continue
            else:
                MainMenu()
                break
        
# Perguntar se quer voltar ao Menu
        exit = input('\n    Voltar ao menu?      [S/N]\n    ').upper()
        if 'S' in exit:
            sy('cls')
            MainMenu()
            break 
        else: 
            continue    
        

# Entrada de produtos no estoque
def ProductEntry():
    sy('cls')
    print('\n    WILD BUNNY ELETRONICS\n') 
    print('\n>>  Entrada de produto no estoque.\n')
    while True:

# Pedir o nome do produto e verificando se ele existe na tabela
        while True:
            entryproduct = input('\n    Nome do produto:\n    ').upper()
            ReturnMainmenu(entryproduct)
            E = db.cur.execute(f'''
            SELECT * FROM stock WHERE product = '{entryproduct}'
            ''')
            if E.fetchall() == []:
                sy('cls')
                print('\n    WILD BUNNY ELETRONICS\n')
                print('\n>>  Entrada de produto no estoque.\n')
                print('\n    Produto não encontrado!')
                continue
            break

# Pedir a quantidade de entrada do produto
        while True:
            try: entry = int(input('\n    Quantidade de entrada:\n    '))
            except:
                sy('cls')
                print('\n    WILD BUNNY ELETRONICS\n')
                print('\n>>  Entrada de produto no estoque.\n')
                print('\n    Valor invalido!')
                continue
            if entry >= 9999 or entry <= 0:
                sy('cls')
                print('\n    WILD BUNNY ELETRONICS\n')
                print('\n>>  Entrada de produto no estoque.\n')
                print('\n    Valor invalido!')
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
        HA = BB + ' +' + str(entry)
        db.cur.execute(f''' 
        UPDATE history SET H_productAmount = '{HA}' WHERE product = '{entryproduct}'
        ''')

# Gravar alterações no DB datetimer
        db.cur.execute(f'''
        INSERT INTO datetimer VALUES ('{entryproduct}', '{dt.now().strftime('%d/%m/%y   -   %H:%M')}')
        ''')
       
# Gravar alterações na tabela "stock"
        db.cur.execute(f'''
        UPDATE stock SET amount = '{total}' WHERE product = '{entryproduct}'
        ''')
        db.con.commit()

# Mensagem de confirmação
        sy('cls')
        print('\n    WILD BUNNY ELETRONICS\n')
        print('\n>>  Entrada de produto no estoque.\n')
        print(f'\n    A quantidade de "{entryproduct}" foi atualizada com sucesso.\n    {VB} >>> {total}\n')

# Perguntar se quer atualizar outro item
        exit = input('\n    Atualizar novo item?      [S/N]\n    ').upper()
        if 'S' not in exit:
            MainMenu()
            break 
            
        else:
            sy('cls')
            print('\n    WILD BUNNY ELETRONICS\n')
            print('\n>>  Entrada de produto no estoque.\n')
            continue    


# Saida de produtos do estoque (mesma logica da entrada de produtos porem subitraindo a quantidade fornecida)
def ProductExit():
    sy('cls')
    print('\n    WILD BUNNY ELETRONICS\n') 
    print('\n>>  Saida de produto do estoque.\n')
    while True:

# Pedir o nome do produto e verificando se ele existe na tabela
        while True:
            entryproduct = input('\n    Nome do produto:\n    ').upper()
            ReturnMainmenu(entryproduct)
            E = db.cur.execute(f'''
            SELECT * FROM stock WHERE product = '{entryproduct}'
            ''')
            if E.fetchall() == []:
                sy('cls')
                print('\n    WILD BUNNY ELETRONICS\n')
                print('\n>>  Saida de produto do estoque.\n')
                print('\n    Produto não encontrado!')
                continue
            break

# Pedir a quantidade de saida do produto
        while True:
            try: entry = int(input('\n    Quantidade de Saida:\n    - '))
            except:
                sy('cls')
                print('\n    WILD BUNNY ELETRONICS\n')
                print('\n>> Saida de produto no estoque.\n')
                print('\n    Valor invalido!')
                continue
            if entry >= 9999 or entry <= 0:
                sy('cls')
                print('\n    WILD BUNNY ELETRONICS\n')
                print('\n>> Saida de produto no estoque.\n')
                print('\n    Valor invalido!')
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
                print('\n    WILD BUNNY ELETRONICS\n')
                print('\n>> Saida de produto no estoque.\n')
                print('\n    Valor invalido!')
                print('    A quantidade no estoque ficaria abaixo de zero.\n')
                continue
            break

# Salvar alteração no historico do produto
        A = db.cur.execute(f'''
        SELECT H_productAmount FROM history WHERE product = '{entryproduct}'
        ''')
        AB = A.fetchone()[0]
        BB = str(AB)
        HA = BB + ' -' + str(entry)
        db.cur.execute(f''' 
        UPDATE history SET H_productAmount = '{HA}' WHERE product = '{entryproduct}'
        ''')

# Gravar alterações no DB datetimer
        db.cur.execute(f'''
        INSERT INTO datetimer VALUES ('{entryproduct}', '{dt.now().strftime('%d/%m/%y   -   %H:%M')}')
        ''')

# Gravar alterações no DB "stock"
        db.cur.execute(f'''
        UPDATE stock SET amount = '{total}' WHERE product = '{entryproduct}'
        ''')
        db.con.commit()

# Mensagem de confirmação
        sy('cls')
        print('\n    WILD BUNNY ELETRONICS\n')
        print('\n>> Saida de produto no estoque.\n')
        print(f'\n    A quantidade de "{entryproduct}" foi atualizada com sucesso.\n    {VB} >>> {total}\n')

# Perguntar se quer atualizar outro item
        exit = input('\n    Atualizar novo item?      [S/N]\n    ').upper()
        if 'S' not in exit:
            MainMenu()
            break     
        else:
            sy('cls')
            print('\n    WILD BUNNY ELETRONICS\n')
            print('\n>> Saida de produto no estoque.\n')
            continue
       

# Historico de entrada e saida de produtos
def ProductHistory():
        sy('cls')
        while True: 
            sy('cls')
            print('\n    WILD BUNNY ELETRONICS\n')
            print('\n>> Historico de movimentação de produto.\n')

# Pedir ao usuario o nome do produto
            Hproduct = input('\n    Produto:\n    ').upper()
            ReturnMainmenu(Hproduct)

# Buscar produto, quantidade e horario de registro no banco de dados 
            H = db.cur.execute(f'''
            SELECT * FROM history WHERE product = '{Hproduct}' 
            ''')
            Y = H.fetchall()

            D = db.cur.execute(f'''
            SELECT * FROM datetimer WHERE product = '{Hproduct}' 
            ''')
            A = D.fetchall()

# Conferir se o produto existe na tabela, caso exista mostra o historico na tela
            sy('cls')
            print('\n    WILD BUNNY ELETRONICS\n')
            print('\n>>  Consultar historico de movimentação do produto.\n')
            if  Y != []:
                T = str(Y[0][1])
                print(f'\n    HISTORICO DE {Hproduct}:')
                print('\n')
            else: 
                print('\n    Produto não encontrado!\n')
                continue
            n = 0
            m = 0
            print('    Movimento        Data          Horario')
            try: 
                for i in A:
                    print ('       ' + T[m]+T[m+1], end =' ')
                    print(f'           {A[n][1]}')
                    n += 1
                    m += 3    
                break
            except:
                print ('       ' + T[-2]+T[-1], end =' ')
                print(f'           {A[n][1]}')
            finally:

# Perguntar se quer ver o historico de movimentação de outro produto
                exit = input('\n    Ver o historico de outro produto?      [S/N]\n    ').upper()
                if 'S' not in exit:
                    MainMenu()
                    break 
                else:
                    continue   

 
        