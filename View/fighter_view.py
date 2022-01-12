from View.base_view import BaseView

class FighterView(BaseView):
    def __init__(self):
        ...
    

    def show_see_all_fighters_header(self):
        self.clear_screen()
        print('-----See all fighters------')
    
    
    def show_delete_fighter_header(self):
        self.clear_screen()
        print('-----Select fighter to delete------')
    
        
    def show_select_fighters_for_battle_header(self,selected_fighters):
        self.clear_screen()
        print('-----Select fighters to battle------')
        print('|Fighters selected: '+str(selected_fighters)+'/3 |')
        print()
    

    def show_edit_fighter_header(self):
        self.clear_screen()
        print('-----Select fighter to edit------')
    

    def show_complete_life_header(self):
        self.clear_screen()
        print('-----Select fighter to complete life------')
    

    def show_improve_skill_header(self):
        self.clear_screen()
        print('-----Select fighter to improve skill------')
    

    def show_buy_fighter_header(self):
        self.clear_screen()
        print('--------Buy New Fighter---------')
        print('->fighters skills are generated randomly')
        print('(10-40) - 60% chance')
        print('(41-50) - 25% chance')
        print('(51-80) - 10% chance')
        print('(81-100) - 5% chance')
    
    
    def show_delete_confirmation(self):
        self.show_success_message('fighter successfully deleted!')
        print()
    

    def show_buy_fighter_confirmation(self):
        print()
        self.show_success_message('fighter successfully generated!')
        print()
    

    def show_complete_life_confirmation(self):
        self.show_success_message('life successfully completed!')
        print()
    

    def show_skill_improved_confirmation(self, skill):
        message = 'improved '+skill+'!'
        self.show_success_message(message)
        print()
    

    def log_cant_delete_fighter_error(self):
        self.show_error('you must have at least 3 fighters on your account!')
    

    def log_insuficient_balance_error(self):
        self.show_error('you dont have enough coins!')


    def show_fighter_data(self,fighter_data):
        print(fighter_data['fighter_number'],'-',fighter_data['fighter_name'])
        print(fighter_data['attack_name'],'-',fighter_data['attack_power'], 'power')
        print(fighter_data['defense_name'],'-',fighter_data['defense_power'], 'power')
        print('Life',fighter_data['life'],'/100')
    

    def read_data_new_fighter(self):
        fighter_name = input('->enter the name for your fighter:')
        attack_name = input('->enter the name for your fighter\'s attack:')
        defense_name = input('->enter the name for your fighter\'s defense:')

        return {'fighter_name':fighter_name,
                'attack_name':attack_name,
                'defense_name':defense_name}


    def select_fighter(self, max_value):
        while True:
            option = int(input("Enter the number of the fighter:"))
            if option > 0 and option <=max_value:
                return option


    def edit_name_fighter(self,old_name):
        print('----- Edit Fighter name -----')
        print('Current name:',old_name)
        new_name = input('New Name: ')
        
        self.show_success_message('name changed successfully')
        return new_name
    

    def return_to_menu(self):
        print('press enter to return')
        input()
    

    def show_improve_skill_menu(self):
        print('[1] - Improve attack in 3 points = 5 coins')
        print('[2] - Improve defense in 3 points = 5 coins')
        while True:
            option = int(input("Select 1 or 2:"))
            if option in [1,2]:
                return option

    
    def show_fighter_menu(self):
        self.clear_screen()
        print('-------------- Fighters Menu ---------------')
        print('1 - See all my fighters')
        print('2 - Edit fighter')
        print('3 - Delete fighter')
        print('4 - Buy New Fighter')
        print('5 - Improve some fighter\'s skill (5 coins)')
        print('6 - Complete some fighter\'s life (10 coins)')
        print('7 - Return to Home Screen')

        while True:
            option = int(input("Enter your choice:"))
            if option in [1,2,3,4,5,6,7]:
                return option
