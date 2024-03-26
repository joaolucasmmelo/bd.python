import os
from enum import Enum
import io
from utils import tratar_nome

class TiposChavesP(Enum):
    caractere = str
    inteiro = int
    decimal = float

#Função Criar Tabela:
def criar_tabela():

    def valida_cptype():
        cp_type = str(input())
        cp_type = getattr(TiposChavesP, cp_type, None)

        if cp_type is None:
            print('\nEsse tipo não existe.')
            print("Selecione um tipo válido! \nEx: caractere, inteiro ou decimal")
            return valida_cptype()
        return cp_type.value

    def criar_chavep(file:io.TextIOWrapper):
        cp_type = valida_cptype()
        chave_p = str(input("Agora digite o nome chave primária: "))
        try:
            chave = cp_type(input("Digite uma chave: "))
        except ValueError:
            print(f'\nIsso não é um {cp_type}')
            print("Digite o tipo da chave primária: \nEx: caractere, inteiro ou decimal")
            return criar_chavep(file)
        file.write(chave_p + ': ')
        file.write(f'{chave}, ')

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
        lista_tabelas.write(f'{nome}; ')

#Função Listar Tabelas:
def listar_tabelas():
    pass

# with open(file = f'tabelas/{nome}.txt',mode = 'w') as file:
#         file.write("nigga")
        

# def listar_tabelas():
#     with open(f'tabelas/lstabelas.txt', 'r') as file:
#         file.read()