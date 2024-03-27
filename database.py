import os
from utils import tratar_nome, criar_chavep

#Função Criar Tabela:
def criar_tabela():

    nome = str(input("Digite o nome da tabela: "))
    nome = tratar_nome(nome)

    try:
        os.mknod(f'tabelas/{nome}.txt')
    except FileExistsError:
        print("Essa tabela já existe!\n")
        criar_tabela()

    with open(f'tabelas/{nome}.txt', 'w') as file:
        print("\nDigite o tipo da chave primária: ")
        print("Ex: caractere, inteiro ou decimal")
        criar_chavep(file)

    with open('tabelas/lstabelas.txt', 'a') as lista_tabelas:
        lista_tabelas.write(f'{nome}\n')

#Função Listar Tabelas:
def listar_tabelas():
    print("----------LISTA DE TABELAS----------\n")
    try:
        with open("tabelas/lstabelas.txt", 'r') as lista_tabelas:
            check_file = os.path.getsize("tabelas/lstabelas.txt")
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
    pass

#Função Listar Dados Tabela
def listar_dados_tabela():
    nome = str(input("Digite o nome da tabela que deseja ver: \n"))
    nome = tratar_nome(nome)

    try:
        with open(f'tabelas/{nome}.txt', 'r') as tabela:
            print(f'\n-----------Tabela {nome}-----------\n')
            print(tabela.read(None))
            print("\n------------------------------------")
    except FileNotFoundError:
        print("Essa tabela não exite!\n")
    
#Função Apagar Tabela:
def apagar_tabela():
    nome = str(input("Digite o nome da tabela que deseja apagar: \n"))
    nome = tratar_nome(nome)

    try:
        with open(f'tabelas/{nome}.txt', 'r') as tabela:
            if tabela:
                os.remove(f'tabelas/{nome}.txt')

        with open("tabelas/file_test.txt", 'w') as file_test:
            with open("tabelas/lstabelas.txt", 'r') as lista_tabelas:
                r = lista_tabelas.readline()
                nome_tratado = nome + '\n'
                while r:
                    if nome_tratado != r:
                        file_test.write(f'{r}')
                    
                    r = lista_tabelas.readline()
                    
        with open("tabelas/lstabelas.txt", 'w') as lista_tabelas:
            with open("tabelas/file_test.txt", 'r') as file_test:
                r = file_test.readline()
                while r:
                    lista_tabelas.write(f'{r}')
                    r = file_test.readline()
            os.remove("tabelas/file_test.txt")  
            print(f'Sucesso! tabela {nome} excluída\n')

        print("--------NOVA LISTA DE TABELAS--------")
        listar_tabelas()

    except FileNotFoundError:
        print("\nEssa tabela não existe!!!")
        listar_tabelas()
