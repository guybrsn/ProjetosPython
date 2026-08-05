from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):

    Sal_min = 1621.00
    inss = 7.5

    def __init__(self, nome, Sal_bruto = 0, salario = 0):
        self.Nome = nome
        self.Sal_Bruto = Sal_bruto
        self.Salario = salario


    @abstractmethod
    def Calc_Sal(self):
        pass


    def Analisar_Sal(self):
        base = self.Salario / Funcionario.Sal_min
        conteudo = f"Analisando Salario ...\n"
        conteudo += f"O salario de [blue]{self.Nome}[/blue] ({self.__class__.__name__}) é de [green]{self.Calc_Sal()}[/green]"
        conteudo += f" e corresponde a {base:.1f}  [yellow]salário mínimos.[/yellow]"
        painel = Panel(conteudo, title="Funcionario", width=50)
        print(painel)




class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, hora_trab = 220):
        super().__init__(nome)
        self.Valor_Hora = valor_hora
        self.Hora_Trab = hora_trab
        self.Sal_Bruto = self.Valor_Hora * self.Hora_Trab


    def Calc_Sal(self):
        self.Salario = self.Sal_Bruto - (self.Sal_Bruto * Funcionario.inss / 100)
        return f"R$ {self.Salario:.2f}"




class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, Sal_bruto = Funcionario.Sal_min):
        super().__init__(nome, Sal_bruto,)


    def Calc_Sal(self):
        self.Salario = self.Sal_Bruto - (self.Sal_Bruto * Funcionario.inss / 100)
        return f"R$ {self.Salario:.2f}"