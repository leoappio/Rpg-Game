from View.home_view import HomeView

class GameController():
    def __init__(self):
        self.__home_screen = HomeView()
    
    def start_game(self):
        self.open_screen()
    
    def new_battle(self):
        ...
    
    def fighters_menu(self):
        ...
    
    def historic(self):
        ...
    
    def open_screen(self):
        options_list = {1: self.new_battle, 2: self.fighters_menu, 3: self.historic}
        chosen_option = self.__home_screen.show_home_screen_options('10','1')
        chosen_function = options_list[chosen_option]
        chosen_function()





