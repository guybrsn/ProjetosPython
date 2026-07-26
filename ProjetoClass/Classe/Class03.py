from rich import print
from rich.panel import Panel
import sqlite3

class Produto:
    def __init__(self, nome, preço):
        self.nome = nome
        self.preço = preço

    #metodos

    def etiqueta(self):
        print(Panel(f"{self.nome}\nR$ {self.preço}", title="Produto", width=35))


while True:
    print("1 - Cadastrar produto")
    print("2 - Listar produto")
    print("3 - Sair")

    resp = int(input("Escolha uma opção acima --> "))

    if resp == 1:
        nome = str(input("Qual e o nome do produto: "))
        preco = float(input("Qual e o valor do produto R$ "))

        Produto01 = Produto(nome, preco)

    if resp == 2: 
        Produto01.etiqueta()

    if resp == 3:
        break