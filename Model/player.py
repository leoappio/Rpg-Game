from Model.Exceptions.InvalidParameterException import InvalidParameterException
from Model.fighter import Fighter
from DAO.player_dao import PlayerDAO

class Player():
    def __init__(self,initial_fighters):
        self.__fighters = initial_fighters
        self.__coin_balance = 50
        self.__current_battle = 1
        self.__player_DAO = PlayerDAO()
 

    @property
    def coin_balance(self):
        return self.__coin_balance
    

    def add_coins(self,quantity):
        if quantity > 0:
            self.__coin_balance =  self.__coin_balance + quantity
            self.__player_DAO.update(self)
        else:
            raise InvalidParameterException('quantity','add coins','Player')



    def remove_coins(self,quantity):
        if quantity > 0:
            self.__coin_balance =  self.__coin_balance - quantity
            self.__player_DAO.update(self)
        else:
            raise InvalidParameterException('quantity','remove coins','Player')
    

    @property
    def current_battle(self):
        return self.__current_battle
    

    def add_one_to_current_battle(self):
        self.__current_battle = self.__current_battle + 1
        self.__player_DAO.update(self)

    
    @property
    def fighters(self):
        return self.__fighters
    
    
    def add_fighter(self, fighter):
        if isinstance(fighter, Fighter):
            self.__fighters.append(fighter)
            self.__player_DAO.update(self)
        else:
            raise InvalidParameterException('fighter','add fighter','Player')
    

    def remove_fighter(self, fighter):
        if isinstance(fighter, Fighter):
            self.__fighters.remove(fighter)
            self.__player_DAO.update(self)
        else:
            raise InvalidParameterException('fighter','remove fighter','Player')

    
