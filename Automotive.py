class Car:
    
    def __init__(self,nome, resaDelCarburante,tipocarburante):
        self.nome = nome
        self.resa = resaDelCarburante
        self.serbatoio = 0
        self.carburante = tipocarburante

    def drive(self, distanza):
        self.serbatoio -= distanza*self.resa

    def getGas(self):
        return self.serbatoio
    
    def addGas(self, quantita):
        self.serbatoio += quantita
    
    def usaBenzina(self):
        if self.carburante == 'benzina':
            return True
        else:
            return False

    def usaGasolio(self):
        if self.carburante == 'gasolio':
            return True
        else:
            return False

    def getCarburante(self):
        return self.carburante

class Autorimessa:

    def __init__(self):
        self.box = list()

    def getMacchine(self):
        return self.box

    def addMacchina(self, auto):
        self.box.append(auto)

    def __str__(self):
        stampa = str()
        for i in self.box:
            stampa += i.nome
            stampa += ', '
        return stampa

class Distributore:

    def __init__(self, prezzoDiesel,prezzoBenzina):
        self.prezzoDiesel = prezzoDiesel
        self.prezzoBenzina = prezzoBenzina
        self.depositoDiesel = 0
        self.depositoBenzina = 0

    def rifornisci(self, quantita, carburante):
        if carburante == 'benzina':
            self.depositoBenzina += quantita
        else:
            self.depositoDiesel += quantita
    def vendi(self, euro, auto): #nuovo
        if auto.usaBenzina():
            litri = euro*self.prezzoBenzina
            self.depositoBenzina -= litri
        else:
            litri = euro*self.prezzoDiesel
            self.depositoDiesel -= litri
        auto.addGas(litri)

    def aggiorna(self, prezzoDiesel,prezzoBenzina):
        self.prezzoDiesel = prezzoDiesel
        self.prezzoBenzina = prezzoBenzina

class MacchinaDaCorsa(Car):

    def __init__(self, nome, resa, carburante, tipoPneumatici, numero):
        super().__init__(nome,resa,carburante)
        self.tipoPneumatici = tipoPneumatici
        self.numero = numero
        self.cambio = 'manuale'
        self.trazione = (50,50)

    def cambio(self):
        if self.cambio == 'manuale':
            self.cambio = 'automatico'
        else:
            self.cambio = 'manuale'

    def setTrazione(self, anteriore, posteriore):
        if anteriore+posteriore != 100:
            print('errore')
        else:
            self.trazione = (anteriore,posteriore)