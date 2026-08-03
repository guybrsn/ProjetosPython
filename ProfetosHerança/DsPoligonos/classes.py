from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qtd_lados=0):
        self.qtd_lados = qtd_lados


    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass




class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__()
        self.lado = lado

    
    def area(self):
        area_quadrado = self.lado * self.lado
        return f"Area = {area_quadrado}"

    
    def perimetro(self):
        perimetro_quadrado = self.lado * 4
        return f" Perimetro = {perimetro_quadrado}"



class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(raio)
        self.Raio:float = raio


    def area(self):
        raio_circulo = (self.Raio * self.Raio) * 3.14
        return f"Area = {raio_circulo}"


    def perimetro(self):
        p = 2 * 3.14 * self.Raio
        return f"Perimetro = {p}"