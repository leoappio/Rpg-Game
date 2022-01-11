from abc import ABC, abstractmethod

class Skill(ABC):

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
    def power(self):
        return self.__power
    
    @power.setter
    @abstractmethod
    def power(self,power):
        self.__power = power
