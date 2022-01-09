from abc import ABC, abstractmethod
class Character(ABC):    
    @property
    @abstractmethod
    def name(self):
        return self.__name
    
    @name.setter
    @abstractmethod
    def name(self,name):
        self.__name = name
    
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
    
    @life.setter
    @abstractmethod
    def life(self,life):
        self.__life = life
    
