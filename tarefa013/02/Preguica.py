import Animal

class preguica(Animal.animal):
    """
    preguiça filho de animal
    """
    def __init__(self,nome,idade,acao):
        super().__init__(nome,idade,acao)
        self._som = 'Aaaaah'
    def getSom(self):
        return self._som
