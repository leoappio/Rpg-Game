class Character():
    def __init__(self,name,attack,defense,life):
        self.__name = name
        self.__attack = attack
        self.__defense = defense
        self.__life = life
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def attack(self):
        return self.__attack
    
    @attack.setter
    def attack(self,attack):
        self.__attack = attack
    
    @property
    def defense(self):
        return self.__defense
    
    @defense.setter
    def defense(self,defense):
        self.__defense = defense

    @property
    def life(self):
        return self.__life
    
    @life.setter
    def life(self,life):
        self.__life = life
    
