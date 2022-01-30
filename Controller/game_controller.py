from View.home_view import HomeView
from Controller.fighter_controller import FighterController
from Controller.boss_controller import BossController
from Controller.battle_controller import BattleController
from Model.player import Player
from Model.battle import Battle

class GameController():
    def __init__(self):
        self.__home_screen = HomeView()
        self.__fighter_controller = FighterController(self)
        self.__boss_controller = BossController()
        self.__battle_controller = BattleController(self)
        self.__history = []
        #TODO
        self.__player = Player(self.__fighter_controller.generate_starting_fighters())
    
    @property
    def player(self):
        return self.__player

    def start_game(self):
        while True:
            self.open_screen()
    
    def new_battle(self):
        boss = self.__boss_controller.generate_new_boss(self.__player.current_battle)
        outcome, battle = self.__battle_controller.start_new_battle(boss, self.__player.current_battle)
        if outcome:
            self.append_to_history('---Against %s---' % battle.boss.name)
            for data in battle.combats:
                text = '%s dealt %d damage to %s' % (data.attacker, data.result, data.defender)
                self.append_to_history(text)
            self.player.add_coins(self.__player.current_battle*5)
            if self.__player.current_battle != 10:
                self.__player.add_one_to_current_battle()
                self.__home_screen.victory()
            else:
                self.__home_screen.ending()
                exit()
        else:
            self.defeat()

    def fighters_menu(self):
        self.__fighter_controller.fighter_menu()
    
    def history(self):
        self.__home_screen.show_history(self.__history)
    
    def open_screen(self):
        options_list = {1: self.new_battle, 2: self.fighters_menu, 3: self.history}
        chosen_option = self.__home_screen.show_home_screen_options(self.__player.coin_balance, self.__player.current_battle)
        chosen_function = options_list[chosen_option]
        chosen_function()

    def defeat(self):
        self.__history = []
        self.__player.current_battle = 1
        self.__player = Player(self.__fighter_controller.generate_starting_fighters())
        self.__home_screen.defeat()

    def append_to_history(self, text):
        self.__history.append(text)
