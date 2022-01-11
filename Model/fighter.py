from Model.attack import Attack
from Model.defense import Defense
class Fighter(Character):
    def __init__(self,name,attack_name,attack_power,defense_name,defense_power,life):
        self.__name = name
        self.__attack = Attack(attack_name, attack_power)
        self.__defense = Defense(defense_name, defense_power)
        self.__life = life
    
    


