import time

class Animale():
    """Classe madre"""

    def __init__(self, nome, eta):
        self.nome=nome
        self.eta=eta
    
    def info(self):
        return None
    
    def parla(self):
        return None
    
    def muove(self):
        return None
    
    def mangia(self):
        return None
    
    def beve(self):
        return None
    
    def dorme(self, attesa):
        time.sleep(attesa)

    def setNome(self, nome):
        self.nome=nome

    def setEta(self,eta):
        self.eta=eta
    
    def getNome(self):
        return self.nome

    def getEta(self):
        return self.eta