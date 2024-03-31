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
    
def valida_cptype():
        cp_type = str(input("Ex: caractere, inteiro ou decimal: "))
        cp_type = getattr(TiposChavesP, cp_type, None)

        if cp_type is None:
            print('\nEsse tipo não existe.')
            print("Selecione um tipo válido! \nEx: caractere, inteiro ou decimal")
            return valida_cptype()
        return cp_type.value

def criar_chavep(file:io.TextIOWrapper, nome):
    cp_type = valida_cptype()
    chave_p = str(input("Agora digite o nome chave primária: "))
    file.write(chave_p + ',')
    colunas = int(input("Digite quantes colunas a tabela irá ter: "))

    try:
        lista = []
        for i in range(colunas):
            chave = cp_type(input(f'Digite a chave {i+1}: '))
            while chave in lista:
                print(f'A chave {chave} já existe na tabela e não pode ser repetida!')
                chave = cp_type(input(f'Digite outra chave {i+1}: '))
            lista.append(chave)
        for i in lista:
            file.write(f'{i},')
        print(f'\nSucesso na criação da tabela {nome}.')
    except ValueError:
        print(f'\nIsso não é um {cp_type}, digite novamente o tipo da chave primária.')
        return criar_chavep(file, nome)
