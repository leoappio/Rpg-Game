from abc import ABC, abstractmethod
from Model.Exceptions.InvalidParameterException import InvalidParameterException

class Skill(ABC):
    @abstractmethod
    def __init__(self, name, power):
        if isinstance(name, str) and isinstance(power, int):
            self.__name = name
            self.__power = power
        else:
            InvalidParameterException('name or power','Skill constructor','Skill')
    
    
    @property
    def name(self):
        return self.__name
    
    
    @name.setter
    def name(self,name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise InvalidParameterException('name','name setter','Skill')

    
    @property
    def power(self):
        return self.__power

    
    @power.setter
    def power(self,power):
        if isinstance(power,int):
            self.__power = power
        else:
            raise InvalidParameterException('power', 'power setter','Skill')


    def increase_power(self):
        self.__power = self.__power + 3
