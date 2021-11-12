import Cavalo, Cachorro, Preguica

class AnimalTeste():
    """cria tres animais"""
    def __init__(self):
        self._cavalo = Cavalo.cavalo('Ariel',6,'corre','manso')
        self._cachorro = Cachorro.cachorro('BatmanRuivo',4,'corre',7828544,'Labrador')
        self._preguica = Preguica.preguica('mano',20,'pendura em arvores')
    def emitesom(self):
        print(self._cachorro.getSom())
        print(self._cavalo.getSom())
        print(self._preguica.getSom())

animais = AnimalTeste()
animais.emitesom()