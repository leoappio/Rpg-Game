from abc import ABC, abstractmethod

class Skill(ABC):
    @abstractmethod
    def __init__(self, name, power):
        self.__name = name
        self.__power = power
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def power(self):
        return self.__power
    
    @power.setter
    def power(self,power):
        self.__power = power
