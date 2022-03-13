from Model.fighter import Fighter
from Model.boss import Boss
from Model.Exceptions.InvalidParameterException import InvalidParameterException
class Combat():
    def __init__(self, attacker, defender):
        self.__attacker = attacker
        self.__defender = defender
        self.__result = 0

    @property
    def attacker(self):
        return self.__attacker

    @attacker.setter
    def attacker(self, attacker):
        if isinstance(attacker, Fighter) or isinstance(attacker, Boss):
            self.__attacker = attacker
        else:
            raise InvalidParameterException('attacker','attacker setter','Combat')

    @property
    def defender(self):
        return self.__defender

    @defender.setter
    def defender(self, defender):
        if isinstance(defender, Fighter) or isinstance(defender, Boss):
            self.__defender = defender
        else:
            raise InvalidParameterException('defender','defender setter','Combat')

    @property
    def result(self):
        return self.__result

    @result.setter
    def result(self, result):
        if isinstance(result, int):
            self.__result = result
        else:
            raise InvalidParameterException('result','result setter','Combat')