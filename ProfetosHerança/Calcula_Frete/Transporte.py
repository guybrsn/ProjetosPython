from abc import ABC, abstractmethod

class Transporte(ABC):

    def __init__(self, distancia):
        self.Distancia = distancia
        self.Frete = 0


    @abstractmethod
    def Calc_frete(self):
        pass



class Moto(Transporte):

    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)


    def Calc_frete(self) -> float:
        #Sempre que declarar um variavel de classe tem que especificar a classe
        self.Frete = self.Distancia * Moto.fator
        return f"R$ {self.Frete:.2f}"
        


class Caminhao(Transporte):

    fator = 1.20

    def __init__(self, distancia):
        super().__init__(distancia)

    #minimo 50 km
    def Calc_frete(self):
        if self.Distancia >= 50:
            self.Frete = self.Distancia * Caminhao.fator
            return f"R$ {self.Frete:.2f}"
        else:
            return f"Raio minimo de entrega e 50km"


class Drone(Transporte):

    fator = 9.50

    def __init__(self, distancia):
        super().__init__(distancia)

    #maximo 10 km
    def Calc_frete(self):
        if self.Distancia <= 10:
            self.Frete = self.Distancia * Drone.fator
            return f"R$ {self.Frete:.2f}"
        else:
            return f"Raio máximo e de 10km"

