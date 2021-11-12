import registros

class registro_medio(registros.registro):
    """registro medio herdado de registro"""

    def __init__(self,nome,id,escola,escola_medio):
        super().__init__(self,nome,id)
        self._escola = escola
        self._escola_medio = escola_medio
        self._saldo *= 1.5