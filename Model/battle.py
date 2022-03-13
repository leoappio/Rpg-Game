from Model.Exceptions.InvalidParameterException import InvalidParameterException
from Model.boss import Boss
from Model.combat import Combat
from Model.fighter import Fighter
from Model.player import Player
class Battle():
    def __init__(self, boss, fighters):
        self.__fighters = fighters
        self.__boss = boss

    @property
    def fighters(self):
        return self.__fighters

    @fighters.setter
    def fighters(self, fighters):
        validation = True
        for fighter in fighters:
            if not isinstance(fighter, Fighter):
                validation = False
        if validation:
            self.__fighters = fighters
        else:
            raise InvalidParameterException('fighters', 'fighters setter', 'Battle') 

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss):
        if isinstance(boss, Boss):
            self.__boss = boss
        else:
            raise InvalidParameterException('boss', 'boss setter', 'Battle')

    def add_fighter(self, fighter):
        if isinstance(fighter, Fighter):
            self.__fighters.append(fighter)
        else:
            raise InvalidParameterException('fighter', 'add_fighter', 'Battle')
