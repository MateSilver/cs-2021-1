import registros

class registro_superior(registros.registro):
    """ensino superior de registro"""

    def __init__(self,nome,id,escola,faculdade):
        super().__init__(nome,id)
        self.escola = escola
        self.faculdade = faculdade