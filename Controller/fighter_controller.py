from View.fighter_view import FighterView
from Model.player import Player

class FighterController():
    def __init__(self):
        self.__fighter_view = FighterView()
        self.__player = Player([])

    def see_all_fighters(self):
        ...
    

    def edit_fighter(self):
        ...
    

    def delete_fighter(self):
        ...


    def buy_new_fighter(self):
        ...


    def improve_fighter_skill(self):
        ...



    def complete_fighter_life(self):
        ...


    def fighter_menu(self, player):
        self.__player = player
        options_list = {1: self.see_all_fighters, 2: self.edit_fighter, 3: self.delete_fighter,
                        4: self.buy_new_fighter, 5: self.improve_fighter_skill, 6: self.complete_fighter_life}
        chosen_option = self.__fighter_view.show_fighter_menu()
        chosen_function = options_list[chosen_option]
        chosen_function()
        

    
