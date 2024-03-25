import os
from utils import tratar_nome

def criar_tabela():
    nome = str(input("Digite o nome da tabela: "))
    nome = tratar_nome(nome)
    try:
        os.mknod(f'tabelas/{nome}.txt')
    except FileExistsError:
        print("arquivo ja existe")
        criar_tabela()

    with open(f'tabelas/{nome}.txt', 'w') as file:
        chave_p = str(input("Digite a chave primária: "))    
        file.write(chave_p + '; ')

# with open(file = f'tabelas/{nome}.txt',mode = 'w') as file:
#         file.write("nigga")
        

def listar_tabelas():
    with open(f'tabelas/lstabelas.txt', 'r') as file:
        file.read()