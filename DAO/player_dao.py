from DAO.dao import DAO

class PlayerDAO(DAO):
    def __init__(self):
        super().__init__('player.pkl')

    def add(self, player):
        from Model.player import Player
        if((player is not None) and isinstance(player, Player)):
            super().add(1,player)


    def update(self, player):
        from Model.player import Player
        if((player is not None) and isinstance(player, Player)):
            super().update(1,player)

    def get(self):
        return super().get(1)


    def remove(self):
        return super().remove(1)

