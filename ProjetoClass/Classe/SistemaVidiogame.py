from rich import print


class Pesonagem:
    def __init__(self, nome, clase):
        self.Nome = nome
        self.Clase = clase # ex: guerreiro, mago, invocador...
        self.Vida = 100
        self.Vida_maxima = 100
        self.Nivel = 1
        self.Experiencia = 0
        self.Inventario = []

        print(f"⚔️  {self.Nome}, o {self.Clase}, entrou na masmorra! Vida: {self.Vida}/{self.Vida_maxima} | Nível: {self.Nivel}")



    def sofrer_dano(self, quantidade):
        self.Vida -= quantidade
        print(f"⚔️  {self.Nome}, o sofreu {quantidade} de dano! Vida atual: {self.Vida}/{self.Vida_maxima}")

        if self.esta_morto():
            print(f"[red] Fim de jogo :( [/red]")
            return



    def esta_morto(self) -> bool:
        return True if self.Vida <= 0 else False
         


    def Cura(self, quantidade):
        self.Vida += quantidade
        if self.Vida <= self.Vida_maxima:
            print(f"⚔️  {self.Nome}, recebeu {quantidade} de cura! Vida atual: {self.Vida}/{self.Vida_maxima}")
            return
        #else:
            #self.Vida = self.Vida_maxima
            #print(f"A cura não pode ultrapassar a vida maxima. Vida atual {self.Vida}/{self.Vida_maxima}")
            #return
        

    def ganhar_experiencia(self, quantidade):
        self.Experiencia += quantidade
        print(f"Sua experiencia aumentou em {quantidade}, experiencia atual {self.Experiencia}")

        if self.verificar_nivel_up():
            print(f"[green]Barabens!, Você subiu de nivel [blue]{self.Nivel}[/blue][/green]")
        return


    def verificar_nivel_up(self) -> bool:
        if self.Experiencia >= 100:
            self.Nivel += 1
            self.Experiencia = 0
            self.Vida_maxima += 20
            self.Vida = self.Vida_maxima
            return True
        return False


#programa principal

p1 = Pesonagem("Chico2000", "Mago")
p1.sofrer_dano(10)
p1.ganhar_experiencia(20)
p1.ganhar_experiencia(20)
