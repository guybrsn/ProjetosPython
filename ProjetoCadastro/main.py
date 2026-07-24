from operacoes import funcionalidades

funcionalidades.criarTabela()


while True:
    print("-" * 50)
    print("                PROGRAMA PRINCIPAL")
    print("-" * 50)
    print("1 - Cadastrar pessoas ")
    print("2 - Lista pessoas ")
    print("3 - Busca pessoas ")
    print("7 - Sair ")

    print()
    resp = int(input("Escolha uma opção acima --> "))
    print("-" * 50)

    if resp == 1:
        funcionalidades.cadastrarPessoas()

    if resp == 2:
        funcionalidades.listarPessoas()

    if resp == 3:
        nome = str(input("Qual o nome da pessoa --> "))
        funcionalidades.buscarPessoa(nome)

    if resp == 4:
        #editar cargo da pessoa
        ...

    if resp == 5:
        #Remover pessoa cadastrada
        ...

    if resp == 6:
        break

