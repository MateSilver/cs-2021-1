class animal():
    """
    initial animal class
    """
    def __init__(self,nome,idade,acao):
        self._nome = nome
        self._idade = idade
        self._som = "som"
        self._acao = acao
    def getSong(self):
        print(self._som)