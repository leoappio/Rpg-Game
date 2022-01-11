from Model.attack import Attack
from Model.defense import Defense
from Model.character import Character
class Fighter(Character):
    def __init__(self,name,attack_name,attack_power,defense_name,defense_power,life):
        self.__name = name
        self.__attack = Attack(attack_name, attack_power)
        self.__defense = Defense(defense_name, defense_power)
        self.__life = life
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def attack(self):
        return self.__attack
    
    @attack.setter
    def attack(self,attack):
        self.__attack = attack
    
    @property
    def defense(self):
        return self.__defense
    
    @defense.setter
    def defense(self,defense):
        self.__defense = defense

    @property
    def life(self):
        return self.__life
    
    def decrease_life(self, value):
        self.__life = self.__life - value
        
        if self.__life < 0:
            self.__life = 0
    
    def complete_life(self):
        self.__life = 100
    
    


