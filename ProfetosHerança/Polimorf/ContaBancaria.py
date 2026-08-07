class ContaBancaria:
    def __init__(self, id, Titular, Saldo = 0):
        self.id = id #publico(+)
        self._Titular = Titular #protegido (#)
        self.__Saldo = Saldo #privado(-)

    def __str__(self):
        #return(f"Conta {self.id}, Esta em nome de {self.Titular}, Saldo R$ {self.Saldo:.2f}")
        return f"Estado atual da conta {self.__dict__}"
    #metodos

    def Depositos(self):
        resp = str(input("Qual depositar [Y/N]"))
        if resp in "Yy":
            dep = float(input("Quanto vai depositar R$ "))
            self.__Saldo += dep 

    def Saque(self):
        saq = float(input("Quanto quer sacar R$ "))
        if saq > self.__Saldo:
            print("Valor insuficiente para operação :(")
        else:
            self.__Saldo -= saq
        



