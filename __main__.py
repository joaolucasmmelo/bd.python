from database import criar_tabela, listar_tabelas, criar_linha_tabela, listar_dados_tabela,pesquisar_valor ,apagar_tabela, apagar_linha

def cli():
    print("\nSelecione um numero de 1 a 7 para prosseguir:\n")
    print("[1] - criar uma tabela")
    print("[2] - Listar todas as tabelas")
    print("[3] - Criar uma nova linha na tabela")
    print("[4] - Listar todos os dados de uma tabela")
    print("[5] - Pesquisar valor em uma tabela")
    print("[6] - Apagar uma linha de uma tabela")
    print("[7] - Apagar uma tabela")
    print("[0] - Sair\n")

    try:
        op = int(input())
        
        if op == 1:
            criar_tabela()
            cli()
        elif op == 2:
            listar_tabelas()
            cli()
        elif op == 3:
            criar_linha_tabela()
            cli()
        elif op == 4:
            listar_dados_tabela()
            cli()
        elif op == 5:
            pesquisar_valor()
            cli()
        elif op == 6:
            apagar_linha()
            cli()
        elif op == 7:
            apagar_tabela()
            cli()
        elif op == 0:
            exit("Saindo do programa...")
        else:
            print("-----ESSA FUNÇÃO NÃO EXISTE!-----")
            print("Selecione oma opção válida!\n")
            cli()
    except ValueError:
        print("-----ESSA FUNÇÃO NÃO EXISTE!-----")
        print("Selecione oma opção válida!")
        cli()

if __name__ == "__main__":
    cli()
    