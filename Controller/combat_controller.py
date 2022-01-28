from View.combat_view import CombatView
from Model.combat import Combat

class CombatController():
    def __init__(self):
        self.__combat_view = CombatView()
        self.__combat = False

    def new_combat(self, attacker, defender):
        self.__combat = Combat(attacker.attack.power, defender.defense.power, attacker.name, defender.name)
        self.calculate_result()
        return self.__combat

    def calculate_result(self):
        self.__combat.result = self.__combat.attack - self.__combat.defense
        if self.__combat.result < 0:
            self.__combat.result = 0
