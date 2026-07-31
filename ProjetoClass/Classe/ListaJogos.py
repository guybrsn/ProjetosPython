from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.Nome = nome
        self.Nick = nick
        self.Favoriro = list()
        self.conteudo = ''

    #metodos da classe
    def add_favirito(self, nome_jogo):
        self.Favoriro.append(nome_jogo)
        self.Favoriro = sorted(self.Favoriro, key=str.lower)
        return

    def Lista_jogos(self):
        conteudo = f"Nome real: {self.Nome}\n"
        conteudo += f"Nick Jogador: {self.Nick}\n"
        conteudo += f"\n"
        for jogo in self.Favoriro:
            conteudo += f":video_game: [green]{jogo}[/green]\n"

        painel = Panel(conteudo, title="[red]Status Do Jogador[/red]", width=50)
        print(painel)
        return


j1 = Gamer("Mario", "Mario Broz")
j1.add_favirito("Forza Horizon")
j1.add_favirito("GTA 6")
j1.add_favirito("Super Mario")
j1.add_favirito("Detroit Becuse Human")

j1.Lista_jogos()

j2 = Gamer("Maria Edarda", "Maria 3x4")
j2.add_favirito("Homen Aranha")
j2.add_favirito("Batman")
j2.add_favirito("Swordigo")
j2.add_favirito("Minecraft")
j2.add_favirito("Free Fire")
j2.add_favirito("Arck")
j2.add_favirito("Batlefield 2042")

j2.Lista_jogos()