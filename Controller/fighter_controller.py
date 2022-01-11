from View.fighter_view import FighterView
from Model.fighter import Fighter
import random

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
        self.fighter_menu()


    def select_fighter(self):
        self.show_all_fighters_from_player()
        number_selected = self.__fighter_view.select_fighter(len(self.__game_controller.player.fighters))
        fighter_selected = self.__game_controller.player.fighters[number_selected-1]

        return fighter_selected
    

    def edit_fighter(self):
        self.__fighter_view.show_edit_fighter_header()
        fighter = self.select_fighter()
        new_name = self.__fighter_view.edit_name_fighter(fighter.name)

        fighter.name = new_name
        self.__fighter_view.return_to_menu()
        self.fighter_menu()
    

    def delete_fighter(self):
        if len(self.__game_controller.player.fighters) >3:
            self.__fighter_view.show_delete_fighter_header()
            fighter = self.select_fighter()
            self.__game_controller.player.fighters.remove(fighter)
            
            self.__fighter_view.show_delete_confirmation()
            self.__fighter_view.return_to_menu()
            self.fighter_menu()
        else:
            self.__fighter_view.log_cant_delete_fighter_error()
            self.__fighter_view.return_to_menu()
            self.fighter_menu()


    def buy_new_fighter(self):
        ...


    def improve_fighter_skill(self):
        if self.__game_controller.player.coin_balance >= 5:
            self.__fighter_view.show_improve_skill_header()
            fighter = self.select_fighter()
            option = self.__fighter_view.show_improve_skill_menu()

            if option == 1:
                fighter.attack.increase_power()
                self.__fighter_view.show_skill_improved_confirmation('attack')
            else:
                fighter.defense.increase_power()
                self.__fighter_view.show_skill_improved_confirmation('defense')
            
            self.__game_controller.player.remove_coins(5)
            
            fighter_data = {'fighter_number': 'Stats',
                            'fighter_name':fighter.name,
                            'attack_name':fighter.attack.name,
                            'attack_power':fighter.attack.power,
                            'defense_name':fighter.defense.name,
                            'defense_power':fighter.defense.power,
                            'life':fighter.life}

            self.__fighter_view.show_fighter_data(fighter_data)
            self.__fighter_view.return_to_menu()
            self.fighter_menu()
        else:
            self.__fighter_view.log_insuficient_balance_error()
            self.__fighter_view.return_to_menu()
            self.fighter_menu()



    def complete_fighter_life(self):
        if self.__game_controller.player.coin_balance >= 10:
            self.__fighter_view.show_edit_fighter_header()
            fighter = self.select_fighter()
            fighter.complete_life()
            self.__game_controller.player.remove_coins(10)
            self.__fighter_view.show_complete_life_confirmation()
            self.__fighter_view.return_to_menu()
            self.fighter_menu()
        else:
            self.__fighter_view.log_insuficient_balance_error()
            self.__fighter_view.return_to_menu()
            self.fighter_menu()
            

    def return_to_main_menu(self):
        self.__game_controller.open_screen()
    

    def generate_starting_fighters(self):
        generated_fighters = []

        for num in range(1,4):
            random_skills = self.random_fighter_skills()
            attack_power = random_skills['attack']
            defense_power = random_skills['defense']
            fighter = Fighter('Fighter '+str(num), 'Attack', attack_power, 'Defense', defense_power, 100)
            generated_fighters.append(fighter)
        
        return generated_fighters
            
    
    def random_fighter_skills(self):
        skill_range = random.randint(1, 100)
        random_attack = 0
        random_defense = 0
        if skill_range <= 60:
            random_attack = random.randint(10, 40)
            random_defense = random.randint(10, 40)
        elif skill_range <= 85:
            random_attack = random.randint(41, 50)
            random_defense = random.randint(41, 50)
        elif skill_range <= 95:
            random_attack = random.randint(51, 80)
            random_defense = random.randint(51, 80)
        else :
            random_attack = random.randint(81, 100)
            random_defense = random.randint(81, 100)
        
        return {'attack':random_attack,'defense': random_defense}
        


    def fighter_menu(self):
        options_list = {1: self.see_all_fighters, 2: self.edit_fighter, 3: self.delete_fighter,
                        4: self.buy_new_fighter, 5: self.improve_fighter_skill, 6: self.complete_fighter_life,
                        7: self.return_to_main_menu}
        chosen_option = self.__fighter_view.show_fighter_menu()
        chosen_function = options_list[chosen_option]
        chosen_function()
        

    
