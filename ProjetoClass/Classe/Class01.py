#declaração da classe
class pessoa:#classe
    def __init__(self, parametroNome = "", parametroIdade = 0): #metodo contrutor
        #Atributos de instancias
        self.nome = parametroNome
        self.idade = parametroIdade

    #Obs:self e ele msm --> quem chamou

    #Metodos de instancia
    def aniversario(self):
        self.idade += 1

    #Metodo exibir mensagem
    #def mensagem(self):
    #   return(f"Olá {self.nome}, vc tem {self.idade} anos de idade")

    # Metodo string
    def __str__(self):
        return (f"Olá {self.nome}, vc tem {self.idade} anos de idade")


#declaração do objeto
# cria um objeto pessoa1 com a class pessoa
pessoa1 = pessoa("João", 30)
pessoa1.aniversario()
#clama o medoto de mensagem de pessoa
print(pessoa1)

pessoa2 = pessoa("Izabella", 23)
print(pessoa2)