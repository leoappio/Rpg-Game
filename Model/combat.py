from Model.fighter import Fighter
from Model.boss import Boss
from Model.Exceptions.InvalidParameterException import InvalidParameterException
class Combat():
    def __init__(self, attack, defense, attacker, defender):
        self.__attacker = attacker
        self.__defender = defender
        self.__attack = attack
        self.__defense = defense
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
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        if isinstance(attack, int):
            self.__attack = attack
        else:
            raise InvalidParameterException('attack','attack setter','Combat') 

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, defense):
        if isinstance(defense, int):
            self.__defense = defense
        else:
            raise InvalidParameterException('defense','defense setter','Combat') 
