from Transporte import *


def main():
    dist = 5

    entrega = Drone(dist)
    print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.Calc_frete()}")


if __name__ == "__main__":
    main()

