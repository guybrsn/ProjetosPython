class ControleRemoto:

    canal_min:int = 1
    canal_max:int = 5
    vol_min:int = 1
    vol_max:int = 10

    def __init__(self, canal = 1, volume = 5):
        self.canal_atual:int = 2