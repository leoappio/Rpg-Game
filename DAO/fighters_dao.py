from DAO.dao import DAO
from Model.fighter import Fighter

class FightersDAO(DAO):
    def __init__(self):
        super().__init__('fighters.pkl')

    def add(self, fighter_id, fighter):
        if((fighter is not None) and isinstance(fighter, Fighter) and isinstance(fighter_id,int)):
            super().add(fighter_id,fighter)


    def update(self, fighter_id, fighter):
        if((fighter is not None) and isinstance(fighter, Fighter) and isinstance(fighter_id,int)):
            super().update(fighter_id,fighter)


    def get(self, fighter_id:int):
        if isinstance(fighter_id, int):
            return super().get(fighter_id)


    def remove(self, fighter_id: int):
        if isinstance(fighter_id,int):
            return super.remove(fighter_id)

