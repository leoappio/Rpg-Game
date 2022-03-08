from DAO.dao import DAO
from Model.player import Player

class PlayerDAO(DAO):
    def __init__(self):
        super().__init__('player.pkl')

    def add(self, player):
        if((player is not None) and isinstance(player, Player)):
            super().add('player',player)


    def update(self, player):
        if((player is not None) and isinstance(player, Player)):
            super().update('player',player)


    def get(self):
        return super().get('player')


    def remove(self):
        return super.remove('player')

