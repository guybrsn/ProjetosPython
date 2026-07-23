from operacoes import funcionalidades

funcionalidades.criarTabela()


while True:
    print("-" * 50)
    print("                PROGRAMA PRINCIPAL")
    print("-" * 50)
    print("1 - Cadastrar pessoas ")
    print("2 - Lista pessoas ")
    print("3 - Sair ")

    print()
    resp = int(input("Escolha uma opção acima --> "))

    if resp == 1:
        funcionalidades.cadastrarPessoas()

    if resp == 3:
        break

