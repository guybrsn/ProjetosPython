from abc import ABC, abstractmethod

class Bebida_Quente:

    def preparar(self):
        print(f"--- Iniciando o Preparo ---")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print(f"--- Bebida Pronta ---")


    def ferver_agua(self):
        print(f"1. Fervendo a água a 100 C° graus Celsius.")


    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass



class Cafe(Bebida_Quente):
    def __init__(self):
        super().__init__()


    def misturar(self):
        print(f"2. Passando a água pressurizada pelo pó do café moido.")


    def servir(self):
        print(f"3. Servindo em uma xicara pequena.")



class Cha(Bebida_Quente):
    def __init__(self):
        super().__init__()


    def misturar(self):
        print("2. Mergulhando o sachê de ervas na água")

    def servir(self):
        print("3. Servindo na caneca de porcelana com limão")



class Leite(Bebida_Quente):
    def __init__(self):
        super().__init__()


    def misturar(self):
        print("2. Passando vapor pressurizado pelo bico do leite.")

    def servir(self):
        print("3. Servindo na caneca grande, com café.")


