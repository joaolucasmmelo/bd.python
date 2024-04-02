import os
from utils import tratar_nome, criar_chavep, criar_chave

#Função Criar Tabela:
def criar_tabela():

    nome = str(input("Digite o nome da tabela: "))
    nome = tratar_nome(nome)

    try:
        colunas = int(input("Digite quantas colunas a tabela irá ter: "))

    except ValueError:
        print("ERRO! Digite o número de colunas corretamente!")
        return

    try:
        os.mknod(f'tabelas/{nome}.csv')

    except FileExistsError:
        print("Essa tabela já existe!\n")
        criar_tabela()

    with open(f'tabelas/{nome}.csv', 'w+') as file:
            print("\nDigite o tipo da chave primária")
            criar_chavep(file, nome, colunas)

    with open('tabelas/lstabelas.csv', 'a') as lista_tabelas:
        lista_tabelas.write(f'{nome}\n')

#Função Listar Tabelas:
def listar_tabelas():
    print("----------LISTA DE TABELAS----------\n")
    try:
        with open("tabelas/lstabelas.csv", 'r') as lista_tabelas:
            check_file = os.path.getsize("tabelas/lstabelas.csv")
            if check_file == 0:
                print("Não existem tabelas a serem exibidas no momento.")
                print("\n------------------------------------")
            else:
                print(lista_tabelas.read(None))
                print("------------------------------------")

    except FileNotFoundError:
        print("Não existem tabelas a serem exibidas no momento.")
        print("\n------------------------------------")

#Função Criar Linha na Tabela:
def criar_linha_tabela():
    listar_tabelas()
    nome = str(input("Digite o nome da tabela na qual deseja criar uma nova linha: \n"))
    nome = tratar_nome(nome)

    try:
        with open(f'tabelas/{nome}.csv', 'r') as file:
            r = file.readline()
            virgula_count = -1
            for i in r:
                if i == ",":
                    virgula_count+=1
        with open(f'tabelas/{nome}.csv', 'a') as file:
            file.write("\n")
            print("\nDigite o tipo da chave")
            criar_chave(file, virgula_count)
            print(f'Tabela {nome}:\n')

        with open(f'tabelas/{nome}.csv', 'r') as file:
            print(file.read(None))

    except FileNotFoundError:
        print("Essa tabela não existe!\n")

#Função Listar Dados Tabela
def listar_dados_tabela():
    listar_tabelas()
    nome = str(input("Digite o nome da tabela que deseja ver: \n"))
    nome = tratar_nome(nome)

    try:
        with open(f'tabelas/{nome}.csv', 'r') as tabela:
            print(f'\n-----------Tabela {nome}-----------\n')
            print(tabela.read(None))
            print("\n------------------------------------")

    except FileNotFoundError:
        print("Essa tabela não exite!\n")

#Função Pesquisar Valor
def pesquisar_valor():
    listar_tabelas()
    nome = str(input("Digite o nome da tabela em que deseja pesquisar um valor: \n"))
    nome = tratar_nome(nome)
    try:
        with open(f'tabelas/{nome}.csv', 'r') as file:
            busca = str(input('''Digite agora o "valor" que deseja buscar: '''))
            busca_tratado =',' + busca + ','
            r = file.readline()
            i = 1
            while r:
                if busca_tratado in r:
                    print("\nO valor foi encontrado.\n")
                    print(r)
                    return
                i = i+1
                r = file.readline()
            print(f'\nO valor {busca} não foi encontrado na tabela {nome}.')     

    except FileNotFoundError:
        print("Essa tabela não existe.\n")
    
#Função Apagar Tabela:
def apagar_tabela():
    listar_tabelas()
    nome = str(input("Digite o nome da tabela que deseja apagar: \n"))
    nome = tratar_nome(nome)

    try:
        with open(f'tabelas/{nome}.csv', 'r') as tabela:
            if tabela:
                os.remove(f'tabelas/{nome}.csv')

        with open("tabelas/file_test.csv", 'w') as file_test:
            with open("tabelas/lstabelas.csv", 'r') as lista_tabelas:
                r = lista_tabelas.readline()
                nome_tratado = nome + '\n'
                while r:
                    if nome_tratado != r:
                        file_test.write(f'{r}')
                    
                    r = lista_tabelas.readline()
                    
        with open("tabelas/lstabelas.csv", 'w') as lista_tabelas:
            with open("tabelas/file_test.csv", 'r') as file_test:
                r = file_test.readline()
                while r:
                    lista_tabelas.write(f'{r}')
                    r = file_test.readline()
            os.remove("tabelas/file_test.csv")  
            print(f'Sucesso! tabela {nome} excluída\n')

        print("--------NOVA LISTA DE TABELAS--------")
        listar_tabelas()

    except FileNotFoundError:
        print("\nEssa tabela não existe!!!")
        listar_tabelas()

#Função Apagar Linha Tabela:
def apagar_linha():
    listar_tabelas()
    nome = str(input("Digite o nome da tabela em que deseja apagar uma linha: "))
    nome = tratar_nome(nome)

    #verifica se o arquivo exite e pode ser aberto
    try:
        with open(f'tabelas/{nome}.csv', 'r') as tabela:
            print('\n' + tabela.read(None))
    except FileNotFoundError:
        print("Essa tabela não exite.")
        return
    
    #verifica se a tabela tem linhas a serem excluidas (que não sejam a chave primária)
    with open(f'tabelas/{nome}.csv', 'r') as tabela:
        vef_linhas = 0
        r= tabela.readline()
        while r:
            vef_linhas+=1
            r= tabela.readline()
        if vef_linhas <= 1:
            print("Essa tabela não tem chaves a serem excluidas.")
            return
    
    with open(f'tabelas/{nome}.csv', 'r') as tabela:
        #adiciona o nome da chave primária as listas
        r = tabela.readline()
        lista_chavep = []
        while r:
            lista_chavep.append(',')
            for i in r:
                if i == ',':
                    r = tabela.readline()
                    break
                else:    
                    lista_chavep.append(i)
        chaves = ''.join(lista_chavep) 
        chaves = str(chaves + ',') 

    chave = str(input("\nDigite a chave da linha que deseja excluir: "))
    chave = chave + ','
    chave_vef = ',' + chave
    if chave_vef not in chaves:
        print("Essa chave não existe.")
        return

    with open(f'tabelas/{nome}.csv', 'r') as tabela:
        r = tabela.readline()
        while (chave in r) or (chave_vef not in chaves):
            chave = str(input("A chave não pode ser excluída ou não exite. Digite outra chave: "))
            chave = chave + ','
            chave_vef = ',' + chave
        
    with open(f'tabelas/{nome}.csv', 'r') as tabela:
        with open('tabelas/test.csv', 'w') as file_test:
            r = tabela.readline()
            x = 0
            n = 1
            while r:
                if r != '':
                    if (chave not in r) and r != '\n':
                        file_test.write(f'{r}')
                        r = tabela.readline()
                        n+=1
                    else:
                        r = tabela.readline()
                        if n == vef_linhas:
                            x = 1
            
    with open(f'tabelas/{nome}.csv', 'r') as tabela:
        with open('tabelas/test.csv', 'r') as file_test:
            vef_tabela = tabela.read(None)
            vef_test = file_test.read(None)
            if vef_tabela == vef_test:
                print("Essa chave não existe.")
                os.remove('tabelas/test.csv')
                return
    
    with open(f'tabelas/{nome}.csv', 'w') as tabela:
        with open('tabelas/test.csv', 'r') as file_test:
            if x == 1:
                x = 1
                r = file_test.readline()
                while r:
                    if x == (vef_linhas - 1):
                        r = r.replace('\n', '')
                        tabela.write(f'{r}')
                        r = file_test.readline()
                    else:
                        tabela.write(f'{r}')
                        r = file_test.readline()
                    x+=1
                os.remove('tabelas/test.csv')
            else:
                r = file_test.readline()
                while r:
                    if r != '\n':
                        tabela.write(f'{r}')
                    r = file_test.readline()
                os.remove('tabelas/test.csv')

    with open(f'tabelas/{nome}.csv', 'r') as tabela:
        print(f'Sucesso na remoção da linha. Tabela {nome} agora:\n')
        print(tabela.read(None))
