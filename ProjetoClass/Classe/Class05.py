from rich import print
import time

class Livro:
    def __init__(self, titulo, paginas):
        self.Titulo = titulo
        self.Paginas= paginas
        #Tem como criar variaveis dentro do construtor sem passar parametros para o contrutor
        self.Pagina_atual = 1
        # Pode ter prints dentro do metodo contrutor
        print(f":open_book:[green] Você acabou de abrir o livro [blue]{self.Titulo}[/blue] que tem [blue]{self.Paginas}[/blue] páginas no total. você esta na página [blue]{self.Pagina_atual}[/blue][/green]")


    def avançar_paginas(self, qtd_avançar = 1):
        cont = 0
        for pg in range(0, qtd_avançar, 1):
            if not self.fim_do_livro():
                self.Pagina_atual += 1
                print(f"Pág{self.Pagina_atual} > ", end="")
                time.sleep(0.5)
                cont += 1
        print(f"você esta na página {self.Pagina_atual}")
        if self.fim_do_livro():
            print(f":closed_book:[red]Você chegou no fim do livro {self.Pagina_atual}[/red]")


    def fim_do_livro(self) -> bool:
        return True if self.Pagina_atual == self.Paginas else False


l1 = Livro("João e Maria Caçadores de Bruxa", 30)
l1.avançar_paginas(30)
