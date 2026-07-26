class ContaBancaria:
    def __init__(self, id, Titular, Saldo = 0):
        self.id = id
        self.Titular = Titular
        self.Saldo = Saldo

    #metodos

    def Depositos(self):
        resp = str(input("Qual depositar [Y/N]"))
        if resp in "Yy":
            dep = float(input("Quanto vai depositar R$ "))
            self.Saldo += dep 

    def Saque(self):
        saq = float(input("Quanto quer sacar R$ "))
        if saq > self.Saldo:
            print("Valor insuficiente para operação :(")
        else:
            self.Saldo -= saq
        

    def __str__(self):
        return(f"Conta {self.id}, Esta em nome de {self.Titular}, Saldo R$ {self.Saldo:.2f}")



ContaCorrente = ContaBancaria(121, "Matheus", 50)
ContaCorrente.Saque()
print(ContaCorrente)