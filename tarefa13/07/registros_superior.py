import registros

class registro_superior(registros.registro):
    """ensino superior de registro"""

    def __init__(self,nome,id,escola,faculdade):
        super().__init__(nome,id)
        self._escola = escola
        self._faculdade = faculdade
        self._saldo *= 2