from View.combat_view import CombatView
from Model.combat import Combat

class CombatController():
    def __init__(self):
        self.__combat_view = CombatView()
        self.__combats = []

    def new_combat(self, attacker, defender):
        combat = Combat(attacker, defender)
        self.__combats.append(combat)
        self.calculate_result(combat)
        defender.decrease_life(combat.result)
        message = attacker.name + ' dealt ' + str(combat.result) + ' damage to ' + defender.name
        self.__combat_view.show_message(message)
        return message

    def calculate_result(self, combat):
        combat.result = combat.attacker.attack.power - combat.defender.defense.power
        if combat.result < 0:
            combat.result = 0
