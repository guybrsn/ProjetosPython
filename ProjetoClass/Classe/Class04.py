from rich import print
from rich.panel import Panel

class Churrasco:
        
    consumo_padrão:float = 0.400
    Preço_kg:float = 82.40

    def __init__(self, titulo, quant=0):
        self.Titulo = titulo
        self.Quant = quant

    #Metodos da classe

    def __str__(self):
        return f"Esse é {self.Titulo}, com {self.Quant} pessoas participando."


    def calcular_qtd_carne(self) -> float:
        return self.Quant * Churrasco.consumo_padrão


    def calcular_qtd_total(self) -> float:
        return self.calcular_qtd_carne * churrasco.Preço_kg


    def calcular_custo_individual(self) -> float:
        return self.calcular_qtd_total / self.Quant


    def analisar(self):
        conteudo = f"\nAnalisando {self.Titulo} com {self.Quant} convidados"
        conteudo += f"\nCada participante comerá {...}Kg e cada Kg custa R$ {...}"
        conteudo += f"\nRecomendo comprar {...}Kg de carne"
        conteudo += f"\nO custo total será de {...}"
        conteudo += f"\nCada pessoa pagará {...} para participar."
        
        painel = Panel(conteudo, title=self.Titulo, width=70)
        print(painel)


churrasco = Churrasco("Churras dos Amigos", 15)
churrasco.analisar()
