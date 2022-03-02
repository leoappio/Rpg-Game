from Model.attack import Attack
from Model.defense import Defense
from Model.character import Character
class Fighter(Character):
    def __init__(self,name,attack_name,attack_power,defense_name,defense_power,life):
        super().__init__(name,attack_name,attack_power,defense_name,defense_power,life)


    def complete_life(self):
        self.life = 100

