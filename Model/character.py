from abc import ABC, abstractmethod
from Model.Exceptions.InvalidNameException import InvalidNameException
from Model.Exceptions.InvalidParameterException import InvalidParameterException
from Model.attack import Attack
from Model.defense import Defense

class Character(ABC):
    @abstractmethod
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
        if len(name) >= 3:
            self.__name = name
        else:
            raise InvalidNameException()
    
    @property
    def attack(self):
        return self.__attack
    
    @attack.setter
    def attack(self,attack):
        if isinstance(attack, Attack):
            self.__attack = attack
        else:
            raise InvalidParameterException('attack','attack setter','Character')
    
    @property
    def defense(self):
        return self.__defense
    
    @defense.setter
    def defense(self,defense):
        if isinstance(defense,Defense):
            self.__defense = defense
        else:
            raise InvalidParameterException('defense','defense setter','Character')

    @property
    def life(self):
        return self.__life
    
    def decrease_life(self, value):
        self.__life = self.__life - value
        
        if self.__life < 0:
            self.__life = 0   
