from Controller.history_controller import HistoryController
from View.home_view import HomeView
from Controller.fighter_controller import FighterController
from Controller.boss_controller import BossController
from Controller.battle_controller import BattleController
from Model.player import Player
from Model.battle import Battle
from DAO.player_dao import PlayerDAO

class GameController():
    def __init__(self):
        self.__home_screen = HomeView()
        self.__fighter_controller = FighterController(self)
        self.__boss_controller = BossController()
        self.__battle_controller = BattleController()
        self.__history_controller = HistoryController()
        self.__player_DAO = PlayerDAO()
        _player = self.__player_DAO.get()

        if _player == None:
            self.__player = Player(self.__fighter_controller.generate_starting_fighters(),50,1)
            self.__player_DAO.add(self.__player)
        else:
            self.__player = _player
    
    @property
    def player(self):
        return self.__player

    def start_game(self):
        while True:
            self.open_screen()
    
    def prepare_battle(self):
        if len(self.__fighter_controller.fighters) > 3:
            _fighters = self.__fighter_controller.select_fighters_to_battle()
        else:
            _fighters = self.__fighter_controller.fighters
        fighters = []
        for fighter in _fighters:
            fighters.append(fighter)
        boss = self.__boss_controller.generate_new_boss(self.__player.current_battle)
        outcome, messages = self.__battle_controller.start_new_battle(boss, self.__player.current_battle, fighters)
        self.__fighter_controller.save_multiples(fighters)
        if outcome:
            self.append_to_history(str('---%s %s and %s vs %s---' % (fighters[0].name, fighters[1].name, fighters[2].name, boss.name)))
            for data in messages:
                self.append_to_history(data)
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
        self.__history_controller.filter_events()

    def close_game(self):
        exit(0)
    
    def open_screen(self):
        options_list = {0: self.close_game, 1: self.prepare_battle, 2: self.fighters_menu, 3: self.history}
        chosen_option = self.__home_screen.show_home_screen_options(self.__player.coin_balance, self.__player.current_battle)
        chosen_function = options_list[chosen_option]
        chosen_function()

    def defeat(self):
        self.__history = []
        self.__player.current_battle = 1
        self.__player = Player(self.__fighter_controller.generate_starting_fighters(),50,1)
        self.__home_screen.defeat()

    def append_to_history(self, text):
        self.__history_controller.new_event(text)
