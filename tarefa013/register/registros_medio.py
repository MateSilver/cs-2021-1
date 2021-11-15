import registros_basico

class registro_medio(registros_basico.registro_basico):
    """registro basico herdado de registro"""

    def __init__(self, nome, id, escola, escola_medio, cargo):
        super().__init__(self,nome,id,escola)
        self._escola_medio = escola_medio
        self._saldo *= 1.5
        if cargo == 'gerente':
            self._saldo += 1500.0
        elif cargo == 'supervisor':
            self._saldo += 600.0
        elif cargo == 'vendedor':
            self._saldo += 250.0
    def show(self):
        print(self._nome)
        print(self._saldo)
    def toString(self,cargo):
        if cargo == 'gerente':
            return f'nome: {self._nome} saldo: {self._saldo} cargo: 1500.00'
        elif cargo == 'supervisor':
            return f'nome: {self._nome} saldo: {self._saldo} cargo: 600.00'
        elif cargo == 'vendedor':
            return f'nome: {self._nome} saldo: {self._saldo} cargo: 250.00'