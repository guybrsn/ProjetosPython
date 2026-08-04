from Cafeteria import Cafe, Cha, Leite

def main():
    Bebida01 = Cafe()
    Bebida02 = Cha()
    Bebida03 = Leite()
    print(Bebida01.preparar())
    print()
    print(Bebida02.preparar())
    print()
    print(Bebida03.preparar())



if __name__ == "__main__":  
    main()