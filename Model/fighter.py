from Model.attack import Attack
from Model.defense import Defense
from Model.character import Character
class Fighter(Character):
    def __init__(self,name,attack_name,attack_power,defense_name,defense_power,life):
        super().__init__(name,attack_name,attack_power,defense_name,defense_power,life)
    
    def decrease_life(self, value):
        self.__life = self.__life - value
        
        if self.__life < 0:
            self.__life = 0
    
    def complete_life(self):
        self.__life = 100
    
    


