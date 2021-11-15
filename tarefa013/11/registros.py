class registro():
    """faz registro de graduação de funcionarios"""

    def __init__(self,nome,id,cargo):
        self._nome = nome
        self._id = id
        self._saldo = 1000.0
        self._cargo = cargo
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