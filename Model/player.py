class Player():
    def __init__(self,initial_fighters):
        self.__fighters = initial_fighters
        self.__coin_balance = 0
        self.__current_battle = 1

    

    @property
    def coin_balance(self):
        return self.__coin_balance
    

    def add_coins(self,quantity):
        self.__coin_balance =  self.__coin_balance + quantity


    def remove_coins(self,quantity):
        self.__coin_balance =  self.__coin_balance - quantity
    

    @property
    def current_battle(self):
        return self.__current_battle
    

    def add_one_to_current_battle(self):
        self.__current_battle = self.__current_battle + 1

    
    @property
    def fighters(self):
        return self.__fighters
    
    
    def add_fighter(self, fighter):
        self.__fighters.append(fighter)
    
    
    def remove_fighter(self, fighter):
        self.__fighters.remove(fighter)

    