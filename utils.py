import re
import io
from enum import Enum
class TiposChavesP(Enum):
    caractere = str
    inteiro = int
    decimal = float

def tratar_nome(nome:str) -> str:
    nome_t = re.sub(r'\W', '', nome)
    return nome_t
    
def valida_ctype():
        c_type = str(input("Ex: caractere, inteiro ou decimal: "))
        c_type = getattr(TiposChavesP, c_type, None)

        if c_type is None:
            print('\nEsse tipo não existe.')
            print("Selecione um tipo válido! \nEx: caractere, inteiro ou decimal")
            return valida_ctype()
        return c_type.value

def criar_chavep(file:io.TextIOWrapper, nome, colunas):
    c_type = valida_ctype()
    chave_p = str(input("Agora digite o nome chave primária: "))
    file.write(chave_p + ',')

    try:
        lista = []
        for i in range(colunas):
            chave = c_type(input(f'Digite a chave {i+1}: '))
            while chave in lista:
                print(f'A chave {chave} já existe na tabela e não pode ser repetida!')
                chave = c_type(input(f'Digite outra chave {i+1}: '))
            lista.append(chave)
        for i in lista:
            file.write(f'{i},')
        print(f'\nSucesso na criação da tabela {nome}.')
    except ValueError:
        print(f'\nIsso não é um {c_type}, digite novamente o tipo da chave primária.')
        return criar_chavep(file, nome)
    
def criar_chave(file:io.TextIOWrapper, virgula_count):
    c_type = valida_ctype()
    chave = str(input("Digite o nome da chave: "))
    file.write(chave + ',')
    try:
        for i in range(virgula_count):
            chave = c_type(input(f'Digite a chave {i+1}: '))
            file.write(f'{chave},')
        print("\nSucesso na criação da linha.")

    except ValueError:
        print(f'\nIsso não é um {c_type}, digite novamente o tipo da chave.')
        return criar_chave(file, virgula_count)
    