class Articolo():
    
    def __init__(self,collocazione,titolo,autore,genere):
        self.collocazione = collocazione
        self.titolo = titolo
        self.autore = autore
        self.genere = genere

    def durataPrestito(self, prestito=30):
        self.prestito = prestito
        return self.prestito

class Libro(Articolo):

    def __init__(self, tipo):
        Articolo.__init__(self,collocazione,titolo,autore,genere)
        if self.tipo == 'libro':
            self.tipo = tipo
        else:
            print('Tipo non supportato')

class CD(Articolo):

    def __init__(self, tipo):
        Articolo.__init__(self,collocazione,titolo,autore,genere)
        if self.tipo == 'CD':
            self.tipo = tipo
        else:
            print('Tipo non supportato')

    def durataPrestito(self,prestito=7):
        self.prestito = prestito
        return self.dprestito

class Cliente():

    def __init__(self,nome,cognome):
        self.nome= nome
        self.cognome = cognome
        self.bonus = 0
        
    def isStudente(self):
        return False

    def bonusGiorniPrestito(self):
        if isStudente:
            bonus = 10
        else:
            bonus = 0

class Studente(Cliente):
    
    def __init__(self, nome, cognome, facolta):
        Cliente.__init__(self, nome, cognome)
        self.facolta = facolta

    def isStudente(self):
        return True

class Prestito():

    def __init__(self,Cliente,Articolo,dataInizioPrestito):
        self.Cliente= Cliente
        self.Articolo= Articolo
        self.dataInizioPrestito= dataInizioPrestito

    def durataPrestito(self):
        self.ddprestito = self.Articolo.durataPrestito() + self.Cliente.bonusGiorniPrestito()
        return self.ddprestito

class Biblioteca():

    def __init__(self,denominazione,luogo):
        self.denominazione = denominazione
        self.luogo = luogo
        self.lista_prestiti = list()
        self.lista_articoli = list()
        self.lista_clienti = list()

    def getListaPrestiti(self):
        return lista_prestiti

    def getListaAriticoli(self):
        return lista_articoli

    def getListaClienti(self):
        return lista_clienti

    def aggiungiCliente(self, nome, cognome):
        cliente_agg = Cliente(nome,cognome)
        self.lista_clienti.append(cliente_agg)

    def aggiungiStudente(self, nome, cognome,facolta):
        studente_agg = Studente(nome,cognome,facolta)
        self.lista_clienti.append(studente_agg)
    
    def aggiungiArticolo(self, collocazione, titolo, autore,genere,tipo):
        articoli_agg = Articoli(collocazione, titolo, autore,genere,tipo)
        self.lista_articoli.append(articoli_agg)

    def cercaCliente(self, nome, cognome):
        for i in range(len(lista_clienti)):
            if nome == lista_clienti[i].nome and cognome == lista_clienti[i].cognome:
                return lista_clienti[i]