from Model.defense import Defense
import random

class DefenseController():
    def __init__(self):
        self.__defenses = []
    
    def generate_new_random_defense(self,battle_number):
        inferior_limit = (battle_number * 10) + 5
        upper_limit = (battle_number * 12) + 10
        random_defense = random.randint(inferior_limit, upper_limit)

        defense = Defense('Boss Defense', random_defense)
        self.__defenses.append(defense)

        return defense
    

    @property
    def defenses(self):
        return self.__defenses

