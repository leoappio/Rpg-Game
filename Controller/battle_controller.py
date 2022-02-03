from Model import battle
from View.battle_view import BattleView
from Model.battle import Battle
from Controller.combat_controller import CombatController
import random

class BattleController():
    def __init__(self, game_controller):
        self.__battle_view = BattleView()
        self.__game_controller = game_controller
        self.__combat_controller = CombatController()
        self.__battle = False

    def start_new_battle(self, boss, battle_number, fighters):
        self.__battle = Battle(boss, self.__game_controller.player, fighters)
        while True:
            self.show_boss_data(boss, battle_number)
            fighter = self.select_fighter_to_attack(fighters)
            result = self.add_combat(fighters[fighter-1], self.__battle.boss)
            if result == "player":
                return True, self.__battle
            fighter = random.randrange(0, 3)
            result = self.add_combat(self.__battle.boss, fighters[fighter])
            if result == "boss":
                return False
            self.__battle_view.next_round()

    def show_boss_data(self, boss, battle_number):
        boss_data = {
            'name': boss.name,
            'life': boss.life,
            'maximum_life': battle_number*50,
            'attack_name': boss.attack.name,
            'attack_power': boss.attack.power,
            'defense_name': boss.defense.name,
            'defense_power': boss.defense.power
        }
        self.__battle_view.show_boss_data(boss_data)

    def select_fighter_to_attack(self, fighters):
        self.__battle_view.select_fighter_to_attack()
        self.show_all_fighters_from_player(fighters)
        fighter = self.__battle_view.select_fighter()
        return fighter

    def add_combat(self, attacker, defender):
        combat = self.__combat_controller.new_combat(attacker, defender)
        defender.decrease_life(combat.result)
        self.__battle_view.show_round_result(attacker.name, defender.name, combat.result)
        self.__battle.add_combat(combat)
        if self.check_if_player_won():
            return "player"
        elif self.check_if_boss_won():
            return "boss"
        else:
            return ""

    def show_all_fighters_from_player(self, fighters):
        for counter,fighter in enumerate(fighters):
            fighter_data = {'fighter_number': counter+1,
                            'fighter_name':fighter.name,
                            'attack_name':fighter.attack.name,
                            'attack_power':fighter.attack.power,
                            'defense_name':fighter.defense.name,
                            'defense_power':fighter.defense.power,
                            'life':fighter.life}
            self.__battle_view.show_fighter_data(fighter_data)

    def check_if_player_won(self):
        if self.__battle.boss.life <= 0:
            return True
        else:
            return False

    def check_if_boss_won(self):
        if self.__battle.boss.life <= 0:
            return True
        else:
            return False