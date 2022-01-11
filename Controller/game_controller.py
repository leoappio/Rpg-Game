from View.home_view import HomeView
from Controller.fighter_controller import FighterController
from Model.player import Player
class GameController():
    def __init__(self):
        self.__home_screen = HomeView()
        self.__fighter_controller = FighterController(self)
        #TODO
        self.__player = Player(self.__fighter_controller.generate_starting_fighters())
    
    @property
    def player(self):
        return self.__player

    def start_game(self):
        self.open_screen()
    
    def new_battle(self):
        ...
    
    def fighters_menu(self):
        self.__fighter_controller.fighter_menu()
    
    def historic(self):
        ...
    
    def open_screen(self):
        options_list = {1: self.new_battle, 2: self.fighters_menu, 3: self.historic}
        chosen_option = self.__home_screen.show_home_screen_options(self.__player.coin_balance, self.__player.current_battle)
        chosen_function = options_list[chosen_option]
        chosen_function()





