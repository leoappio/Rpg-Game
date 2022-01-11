from View.fighter_view import FighterView

class FighterController():
    def __init__(self, game_controller):
        self.__fighter_view = FighterView()
        self.__game_controller = game_controller


    def show_all_fighters_from_player(self):
        for counter,fighter in enumerate(self.__game_controller.player.fighters):
            fighter_data = {'fighter_number': counter+1,
                            'fighter_name':fighter.name,
                            'attack_name':fighter.attack.name,
                            'attack_power':fighter.attack.power,
                            'defense_name':fighter.defense.name,
                            'defense_power':fighter.defense.power,
                            'life':fighter.life}
            self.__fighter_view.show_fighter_data(fighter_data)


    def see_all_fighters(self):
        self.__fighter_view.show_see_all_fighters_header()
        self.show_all_fighters_from_player()
        self.__fighter_view.return_to_menu()


    def select_fighter(self):
        self.show_all_fighters_from_player()
        number_selected = self.__fighter_view.select_fighter(len(self.__game_controller.player.fighters))
        fighter_selected = self.__player.fighters[number_selected]

        return fighter_selected
    

    def edit_fighter(self):
        fighter = self.select_fighter()
        new_name = self.__fighter_view.edit_name_fighter(fighter.name)

        fighter.name = new_name
        self.__fighter_view.return_to_menu()
    

    def delete_fighter(self):
        self.__fighter_view.show_delete_fighter_header()
        fighter = self.select_fighter()
        self.__game_controller.player.fighters.remove(fighter)
        
        self.__fighter_view.show_delete_confirmation()
        self.__fighter_view.return_to_menu()



    def buy_new_fighter(self):
        ...


    def improve_fighter_skill(self):
        ...


    def complete_fighter_life(self):
        ...
    

    def return_to_main_menu(self):
        self.__game_controller.open_screen()


    def fighter_menu(self):
        options_list = {1: self.see_all_fighters, 2: self.edit_fighter, 3: self.delete_fighter,
                        4: self.buy_new_fighter, 5: self.improve_fighter_skill, 6: self.complete_fighter_life,
                        7: self.return_to_main_menu}
        chosen_option = self.__fighter_view.show_fighter_menu()
        chosen_function = options_list[chosen_option]
        chosen_function()
        

    
