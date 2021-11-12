import Cachorro
import Cavalo
import Preguica

class zoo():
    """
    zoologico com 10 animais aleatorios
    """
    def __init__(self,nome):
        self.nome = nome
        self.jaulas = []
        self.jaulas.append(Cachorro.cachorro('john',3,'corre',12345,'chiwawa'))
        self.jaulas.append(Cavalo.cavalo('Logan',20,'corre','manso'))
        self.jaulas.append(Preguica.preguica('otto',2,'dorme'))
        self.jaulas.append(Cachorro.cachorro('Batman',12,'corre',21221,'dalmata'))
        self.jaulas.append(Cachorro.cachorro('luciano',5,'corre',452345,'buldog'))
        self.jaulas.append(Cavalo.cavalo('Juan',23,'corre','manso'))
        self.jaulas.append(Preguica.preguica('bob',3,'dorme'))
        self.jaulas.append(Cachorro.cachorro('Robin',11,'corre',21421,'dalmata'))
        self.jaulas.append(Preguica.preguica('Natanael',11,'dorme'))
        self.jaulas.append(Cavalo.cavalo('justus',1,'corre','arredio'))
    def passeio(self):
        for i in range(0,10):
            obj = self.jaulas[i]
            print(obj.getSong())
            if self.jaulas[i]._acao == 'correr':
                print('corre')


zoologico = zoo('Cidade Jardim')
zoologico.passeio()
