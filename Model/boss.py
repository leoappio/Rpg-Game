from Model.character import Character

class Boss(Character):
    def __init__(self,name,attack,defense,life):
        super().__init__(name, attack.name,attack.power, defense.name, defense.power, life)
