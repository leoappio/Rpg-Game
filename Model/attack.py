from Model.skill import Skill
class Attack(Skill):
    def __init__(self, name, power):
        self.__name = name
        self.__power = power
        