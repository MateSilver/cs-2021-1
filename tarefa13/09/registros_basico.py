import registros

class registro_basico(registros.registro):
    """registro medio herdado de registro"""

    def __init__(self, nome, id, escola, cargo):
        super().__init__(self,nome,id)
        self._escola = escola
        self._saldo *= 1.1
        if cargo == 'gerente':
            self._saldo += 1500.0
        elif cargo == 'supervisor':
            self._saldo += 600.0
        elif cargo == 'vendedor':
            self._saldo += 250.0
    def show(self):
        print(self._nome)
        print(self._saldo)