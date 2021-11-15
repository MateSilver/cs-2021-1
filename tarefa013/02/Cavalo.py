import Animal

class cavalo(Animal.animal):
    """
    classe filha de animal
    """
    def __init__(self,nome,idade,acao,estado):
        super().__init__(nome,idade, acao)
        self._som = "iririri"
        self._estado = estado
    def getEstado(self):
        return self._estado
    def getSom(self):
        return self._som