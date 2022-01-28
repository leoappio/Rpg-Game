class Combat():
    def __init__(self, attack, defense, attacker_name, defender_name):
        self.__attacker = attacker_name
        self.__defender = defender_name
        self.__attack = attack
        self.__defense = defense
        self.__result = 0

    @property
    def attacker(self):
        return self.__attacker

    @attacker.setter
    def attacker(self, attacker):
        self.__attacker = attacker

    @property
    def defender(self):
        return self.__defender

    @defender.setter
    def defender(self, defender):
        self.__defender = defender

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, attack):
        self.__attack = attack

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def defense(self, defense):
        self.__defense = defense
