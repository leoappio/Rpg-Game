from Model import battle
from View.battle_view import BattleView
from Model.battle import Battle
from Controller.combat_controller import CombatController
import random

class BattleController():
    def __init__(self):
        self.__battle_view = BattleView()
        self.__combat_controller = CombatController()
        self.__battles = []
        self.__battle_messages = []

    def start_new_battle(self, boss, battle_number, fighters):
        self.__battles.append(Battle(boss, fighters))
        while True:
            fighter = self.show_battle(boss, battle_number, fighters)
            if isinstance(fighter, int):
                self.add_combat(fighters[fighter], self.__battles[-1].boss)
            else:
                continue
            if boss.life <= 0:
                return True, self.__battle_messages
            result = self.boss_attack(boss, fighters)
            if result:
                return False, self.__battle_messages

    def show_battle(self, boss, battle_number, fighters):
        bossData = self.get_boss_data(boss, battle_number)
        fightersData = self.show_all_fighters_from_player(fighters)
        fighter = self.__battle_view.show_battle(bossData, fightersData)
        return fighter

    def get_boss_data(self, boss, battle_number):
        boss_data = {
            'name': boss.name,
            'life': boss.life,
            'maximum_life': battle_number*50,
            'attack_name': boss.attack.name,
            'attack_power': boss.attack.power,
            'defense_name': boss.defense.name,
            'defense_power': boss.defense.power
        }
        return boss_data

    def add_combat(self, attacker, defender):
        message = self.__combat_controller.new_combat(attacker, defender)
        self.__battle_messages.append(message)

    def show_all_fighters_from_player(self, fighters):
        fighter_data = {}
        for counter, fighter in enumerate(fighters):
            fighter_data[counter] = {'fighter_name':fighter.name,
                            'attack_name':fighter.attack.name,
                            'attack_power':fighter.attack.power,
                            'defense_name':fighter.defense.name,
                            'defense_power':fighter.defense.power,
                            'life':fighter.life}
        return fighter_data

    def check_if_player_won(self):
        if self.__battles[-1].boss.life <= 0:
            return True
        else:
            return False

    def check_if_boss_won(self):
        pass

    def boss_attack(self, boss, fighters):
        while True:
            fighter = random.randrange(0, 3)
            if fighters[fighter].life > 0:
                break
        self.add_combat(boss, fighters[fighter])
        if fighters[0].life <= 0 and fighters[1].life <= 0 and fighters[2].life <= 0:
            return True
        else:
            return False