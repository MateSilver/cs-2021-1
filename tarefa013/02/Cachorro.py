import Animal

class cachorro(Animal.animal):
    """
    classe cachorro filha de animal
    """
    def __init__(self,nome,idade,acao,pedigree,raca):
        super().__init__(nome,idade,acao)
        self._som = 'Au'
        self._acao = acao
        self._pedigree = pedigree
        self._raca = raca

    def getRaca(self):
        return self._raca

    def getSom(self):
        return self._som