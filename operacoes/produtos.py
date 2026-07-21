def adicionarProduto(listaProdutos, nome='', preco=0, quantidade=0):
    nomeProduto = str(input("Nome do produto --> "))
    precoProduto = float(input("Preço do produto R$ "))
    quantidadeProduto = int(input("Quantidade produto --> "))

    nome = nomeProduto
    preco = precoProduto
    quantidade = quantidadeProduto

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    listaProdutos.append(produto)
    print("-" * 50)
    print("Produto adicionado com sucesso :) ")
    return listaProdutos


def removerProdutos(listaProdutos, nome):
    for produto in listaProdutos:
        if produto["nome"] == nome:
            listaProdutos.remove(produto)
            print("-" * 50)
            print("Produto removido com sucesso !")
            print("-" * 50)

        if produto["nome"] != nome:
            print("-" * 50)
            print("Produto não encontrado !")
            print("-" * 50)
            break

    return listaProdutos


def atualizaQuantidade(listaProdutos, nome='', quantidade=0):
    for produto in listaProdutos:
        if produto["nome"] == nome and produto["quantidade"] >= 0:
            produto["quantidade"] += quantidade
            print("Quantidade adicionada com sucesso !")
            break
        
        if produto["nome"] != nome or produto["quantidade"] < 0:
            print("Opção invalida :( ")
            break

    return listaProdutos

def visualizarProduto(listaProdutos):
    i = 0
    for produto in listaProdutos:
        i += 1
        print(f"Produto de N° {i}")
        print(f"Nome produto: {produto["nome"]}")
        print(f"Preço do produto R$ {produto["preco"]}")
        print(f"Quantidade do produto {produto["quantidade"]}")
        print()