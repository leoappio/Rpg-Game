from DAO.dao import DAO
from Model.boss import Boss

class BossesDAO(DAO):
    def __init__(self):
        super().__init__('bosses.pkl')

    def add(self, boss_id, boss):
        if((boss is not None) and isinstance(boss, Boss) and isinstance(boss_id,int)):
            super().add(boss_id, boss)


    def update(self, boss_id, boss):
        if((boss is not None) and isinstance(boss, Boss) and isinstance(boss_id,int)):
            super().update(boss_id, boss)


    def get(self, boss_id:int):
        if isinstance(boss_id, int):
            return super().get(boss_id)


    def remove(self, boss_id: int):
        if isinstance(boss_id,int):
            return super().remove(boss_id)

