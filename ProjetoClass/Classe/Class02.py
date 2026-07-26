class Funcionario:
     # atributo de classe
    empresa = "Governo federal"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    #metodos

    def __str__(self):
        return (f"Olá, sou {self.nome} e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}")


#programa principal

while True: 
    print()
    print("1 - Cadastrar funcionario")
    print("2 - Listar Funcionarios")
    print("3 - Sair")
    print()
    resp = int(input("Escolha uma opção acima --> "))
    print()


    if resp == 1:
        nome = str(input("Nome do novo funcionario: "))
        setor = str(input("Setor do novo funcionario: "))
        cargo = str(input("Cargo do novo funcionario: "))

        Funcionario01 = Funcionario(nome, setor, cargo)

    if resp == 2:
        print()
        print(Funcionario01)
        print()

    if resp == 3:
        break