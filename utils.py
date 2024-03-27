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
        
#def