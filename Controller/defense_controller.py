from Model.defense import Defense
import random

class DefenseController():
    def __init__(self):
        ...
    
    def generate_new_random_defense(self,battle_number):
        inferior_limit = (battle_number * 2) + 5
        upper_limit = (battle_number * 3) + 10
        random_defense = random.randint(inferior_limit, upper_limit)

        return Defense('Boss Defense', random_defense)