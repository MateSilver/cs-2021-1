import Animal
import Preguica
import Cachorro
import Cavalo

class veterinario():
    """Veterinario examina animais"""
    def __init__(self, anosdeexperiencia,especialidade):
        self.anos = anosdeexperiencia
        self.especialidade = especialidade

    def examinar(self,animal):
        animal.DoSong()

novo = veterinario(12,'odontologia')

# RECEBENDO ANIMAL ALEATORIO
animalNovo = Animal.animal('jonhatan',5,'voa')
novo.examinar(animalNovo)

# RECEBENDO PREGUIÇA
animalNovo = Preguica.preguica('wesley',32,'pula')
novo.examinar(animalNovo)

# RECEBENDO CAVALO
animalNovo = Cavalo.cavalo('Juan',12,'corre','arredio')
novo.examinar(animalNovo)

# RECEBENDO CACHORRO
animalNovo = Cachorro.cachorro('Pedro',7,'fareja',123442,'Galgo')
novo.examinar(animalNovo)