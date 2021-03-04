import time

class Animale():
    """Parent class"""

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

class Cane(Animale): 
    """Child class"""

    def __init__(self,nome,eta,razza):
        self.razza=razza
        Animale.__init__(self,nome,eta)
        #super().__init__(nome,eta)

    def info(self):
        return self.razza

    def parla(self):
        return 'abbaia'

    def muove(self):
        return 'corre'

    def mangia(self):
        return 'mangia'

    def beve(self):
        return 'beve'

    def getRazza(self):
        return self.razza

    def setRazza(self,razza):
        self.razza = razza