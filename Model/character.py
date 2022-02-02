from abc import ABC, abstractmethod
from Model.Exceptions.InvalidNameException import InvalidNameException
class Character(ABC):    
    @property
    @abstractmethod
    def name(self):
        return self.__name
    
    @name.setter
    @abstractmethod
    def name(self,name):
        if len(name) >= 3:
            self.__name = name
        else:
            raise InvalidNameException()
    
    @property
    @abstractmethod
    def attack(self):
        return self.__attack
    
    @attack.setter
    @abstractmethod
    def attack(self,attack):
        self.__attack = attack
    
    @property
    @abstractmethod
    def defense(self):
        return self.__defense
    
    @defense.setter
    @abstractmethod
    def defense(self,defense):
        self.__defense = defense

    @property
    @abstractmethod
    def life(self):
        return self.__life
    
    
