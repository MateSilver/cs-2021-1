class registro():
    """faz registro de graduação de funcionarios"""

    def __init__(self,nome,id):
        self._nome = nome
        self._id = id
        self._saldo = 1000.0
    def show(self):
        print(self._nome)
        print(self._saldo)