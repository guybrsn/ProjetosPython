from rich import print
from rich.panel import Panel
import os

class ControleRemoto:

    canal_min:int = 1
    canal_max:int = 11
    vol_min:int = 1
    vol_max:int = 11

    def __init__(self, canal = 5, volume = 5):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False


    def liga_desliga(self):
        self.ligado = not self.ligado


    def aumentar_canal(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1


    def diminuir_canal(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1


    def aumentar_volume(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.vol_max:
                self.volume_atual += 1


    def diminuir_volume(self):
        if self.ligado:
            if self.volume_atual != ControleRemoto.vol_min:
                self.volume_atual -= 1


    def mostrar_tv(self):
        conteudo = ""
        if not self.ligado:
            conteudo += ":prohibited: A TV esta desligada !"

        else:
            conteudo += "Canal  = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max):
                if canal == self.canal_atual:
                    conteudo += f"[black on yellow] {canal} [/]"
                else:
                    conteudo += f" {canal} "

            conteudo += "\nVolume = "
            for volume in range(ControleRemoto.vol_min, ControleRemoto.vol_max+1):
                if volume <= self.volume_atual:
                    conteudo += f"[blue on green]  [/]"
                else:
                    conteudo += f"[black on white]  [/]"


        tv = Panel(conteudo, title="[red]TV[/red]", width=50)
        print(tv)


c = ControleRemoto(1, 1)
while True:
    c.mostrar_tv()
    comando = str(input("\n < CH >   - VOL + "))
    os.system('cls')
    if comando == '<':
        c.diminuir_canal()

    if comando == '>':
        c.aumentar_canal()

    if comando == '-':
        c.diminuir_volume()

    if comando == '+':
        c.aumentar_volume()

    if comando == "@":
        c.liga_desliga()

    if comando == "0":
        break

    