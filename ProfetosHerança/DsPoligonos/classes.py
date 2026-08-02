from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados


    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass




class Quadrado(Poligono):
    def __init__(self, qtd_lados):
        super().__init__(qtd_lados)


    def area(self):
        area_quadrado = self.qtd_lados * self.qtd_lados

        return f"A area do quadrado e {area_quadrado}"
        