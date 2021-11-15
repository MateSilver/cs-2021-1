import registros_medio

class registro_superior(registros_medio.registro_medio):
    """ensino superior de registro"""

    def __init__(self,nome,id,escola,escola_medio,faculdade):
        super().__init__(nome,id,escola,escola_medio)
        self._faculdade = faculdade
        self._saldo *= 2

    def show(self):
        print(self._nome)
        print(self._saldo)