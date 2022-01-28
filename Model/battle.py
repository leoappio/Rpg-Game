class Battle():
    def __init__(self, boss, player, fighters):
        self.__fighters = fighters
        self.__boss = boss
        self.__player = player
        self.__combats = []

    @property
    def fighters(self):
        return self.__fighters

    @fighters.setter
    def fighters(self, fighters):
        self.__fighters = fighters

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss):
        self.__boss = boss

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, player):
        self.__player = player

    @property
    def combats(self):
        return self.__combats

    def add_combat(self, combat):
        self.__combats.append(combat)

    def remove_combat(self, combat):
        self.__combats.remove(combat)

    def add_fighter(self, fighter):
        self.__fighters.append(fighter)
