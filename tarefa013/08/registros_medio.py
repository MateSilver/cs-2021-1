import registros_basico

class registro_medio(registros_basico.registro_basico):
    """registro basico herdado de registro"""

    def __init__(self, nome, id, escola, escola_medio):
        super().__init__(self,nome,id,escola)
        self._escola_medio = escola_medio
        self._saldo *= 1.5

    def show(self):
        print(self._nome)
        print(self._saldo)