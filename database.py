import os
from utils import tratar_nome, criar_chavep, criar_chave

#Função Criar Tabela:
def criar_tabela():

    nome = str(input("Digite o nome da tabela: "))
    nome = tratar_nome(nome)

    try:
        os.mknod(f'tabelas/{nome}.csv')

    except FileExistsError:
        print("Essa tabela já existe!\n")
        criar_tabela()

    with open(f'tabelas/{nome}.csv', 'w+') as file:
            print("\nDigite o tipo da chave primária")
            criar_chavep(file, nome)

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
