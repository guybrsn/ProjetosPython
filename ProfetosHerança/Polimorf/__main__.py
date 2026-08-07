from ContaBancaria import *


def main():
    c1 = ContaBancaria(321, "Marcos", 500)
    #c1.Depositos()
    #c1.Saque()
    c1.__Saldo = 500
    print(c1)



if __name__ == "__main__":
    main()