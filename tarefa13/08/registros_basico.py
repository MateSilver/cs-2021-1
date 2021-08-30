import registros

class registro_basico(registros.registro):
    """registro medio herdado de registro"""

    def __init__(self, nome, id, escola):
        super().__init__(self,nome,id)
        self._escola = escola
        self._saldo *= 1.1

    def show(self):
        print(self._nome)
        print(self._saldo)