from operacoes import produtos

listaProdutos = []

while True:
    print(("-" * 50))
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Atualizar quantidade")
    print("4 - Buscar produto")
    print("5 - Ver valor total do estoque")
    print("6 - Listar todos os produtos")
    print("7 - Sair")
    print()

    resp = int(input("Escolha uma opção acima --> "))
    print("-" * 50)

    if resp == 1:
        print()
        print("Digite as informações do protudo ")
        listaProdutos = produtos.adicionarProduto(listaProdutos)

    if resp == 2:
        removerEstoque = str(input("Nome do produto a ser removido do estoque --> "))
        nome = removerEstoque
        produtos.removerProdutos(listaProdutos, nome)

    if resp == 3:
        procuraProduto = str(input("Nome do produto para atualizar quantidade: "))
        nome = procuraProduto
        addQuantidade = int(input("Quanto vai adicionar --> "))
        quantidade = addQuantidade
        produtos.atualizaQuantidade(listaProdutos, nome, quantidade)

    if resp == 4:
        procuraProduto = str(input("Qual produto quer busca --> "))
        nome = procuraProduto
        produtos.buscaProdutos(listaProdutos, nome)

    if resp == 5:
        print("Total de produto no estoque")
        produtos.totalProdutos(listaProdutos)

    if resp == 6:
        print("-" * 50)
        print("Quantidade total de produtos \n")
        produtos.visualizarProduto(listaProdutos)
        print("-" * 50)

    if resp == 7:
        break