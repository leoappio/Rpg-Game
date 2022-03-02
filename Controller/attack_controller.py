from Model.attack import Attack
import random

class AttackController():
    def __init__(self):
        self.__attacks = []
    
    def generate_new_random_attack(self,battle_number):
        inferior_limit = (battle_number * 10) + 5
        upper_limit = (battle_number * 12) + 10
        random_attack = random.randint(inferior_limit, upper_limit)

        attack = Attack('Boss Attack', random_attack)
        self.__attacks.append(attack)
        return attack
    
    @property
    def attacks(self):
        return self.__attacks
