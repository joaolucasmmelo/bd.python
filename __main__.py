from database import criar_tabela

def cli():
    print("Selecione um numero de 1 a 7 para prosseguir:")
    print("[1] - criar uma tabela")
    print("[2] - Listar todas as tabelas")
    print("[3] - Criar uma nova linha na tabela")
    print("[4] - Listar todos os dados de uma tabela")
    print("[5] - Pesquisar valor em uma tabela")
    print("[6] - Apagar uma linha de uma tabela")
    print("[7] - Apagar uma tabela")
    print("[0] - Sair\n")

    op = int(input())

    if op == 1:
        print('OP1')
        criar_tabela()
    elif op == 2:
        print('OP2')
    elif op == 3:
        print('OP3')
    elif op == 4:
        print('OP4')
    elif op == 5:
        print('OP5')
    elif op == 6:
        print('OP6')
    elif op == 7:
        print('OP7')
    elif op == 0:
        print('OP0')
    else:
        print("errado")

if __name__ == "__main__":
    cli()