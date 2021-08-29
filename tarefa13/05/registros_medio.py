import registros

class registro_medio(registros.registro):
    """registro medio herdado de registro"""

    def __init__(self,nome,id,escola):
        super().__init__(self,nome,id)
        self._escola = escola