from View.base_view import BaseView

class FighterView(BaseView):
    def __init__(self):
        ...
    

    def show_see_all_fighters_header(self):
        self.clear_screen()
        print('-----See all fighters------')


    def show_fighter_data(self,fighter_data):
        print(fighter_data['fighter_number'],'-',fighter_data['fighter_name'])
        print('Attack',fighter_data['attack_name'],'-',fighter_data['attack_power'], 'power')
        print('Defense',fighter_data['defense_name'],'-',fighter_data['defense_power'], 'power')
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
        
        print('name changed successfully')
        return new_name
    

    def return_to_menu(self):
        print('press enter to return')
        input()
        self.show_fighter_menu()

    
    def show_fighter_menu(self):
        self.clear_screen()
        print('-------------- Fighters Menu ---------------')
        print('1 - See all my fighters')
        print('2 - Edit fighter')
        print('3 - Delete fighter')
        print('4 - Buy New Fighter')
        print('5 - Improve some fighter\'s skill (5 coins)')
        print('6 - Complete some fighter\'s life (10 coins)')

        while True:
            option = int(input("Enter your choice:"))
            if option in [1,2,3,4,5,6]:
                return option
