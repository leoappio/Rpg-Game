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
    

    def show_edit_fighter_header(self):
        self.clear_screen()
        print('-----Select fighter to edit------')
    

    def show_complete_life_header(self):
        self.clear_screen()
        print('-----Select fighter to complete life------')
    

    def show_delete_confirmation(self):
        self.show_success_message('fighter successfully deleted!')
        print()
    
    def show_complete_life_confirmation(self):
        self.show_success_message('life successfully completed!')
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
