import re

def tratar_nome(nome:str) -> str:
    nome_t = re.sub(r'\W', '', nome)
    return nome_t
    
        
#def