from View.base_view import BaseView
from Model.Exceptions.InvalidChoiceException import InvalidChoiceException
from Model.Exceptions.InvalidNameException import InvalidNameException
import PySimpleGUI as sg

class FighterView(BaseView):
    def __init__(self):
        self.__window = None
    

    def show_see_all_fighters_header(self):
        self.clear_screen()
        print('-----See all fighters------')
    
    
    def show_sell_fighter_header(self):
        self.clear_screen()
        print('-----Select fighter to sell------')
    
        
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
    
    
    def show_sold_confirmation(self):
        self.show_success_message('fighter successfully sold!')
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
    

    def log_cant_sell_fighter_error(self):
        self.show_error('you must have at least 3 fighters on your account!')
    

    def log_insuficient_balance_error(self):
        self.show_error('you dont have enough coins!')


    def show_fighter_data(self,fighter_data):
        print(fighter_data['fighter_number'],'-',fighter_data['fighter_name'])
        print(fighter_data['attack_name'],'-',fighter_data['attack_power'], 'power')
        print(fighter_data['defense_name'],'-',fighter_data['defense_power'], 'power')
        print('Life',fighter_data['life'],'/100')
    

    def read_data_new_fighter(self):
        while True:
            fighter_name = input('->enter the name for your fighter:')
            try:
                if len(fighter_name) < 3:
                    raise InvalidNameException()
                else:
                    break
            except InvalidNameException as e:
                print(e)
        

        while True:
            attack_name = input('->enter the name for your fighter\'s attack:')
            try:
                if len(attack_name) < 3:
                    raise InvalidNameException()
                else:
                    break
            except InvalidNameException as e:
                print(e)

        while True:
            defense_name = input('->enter the name for your fighter\'s defense:')
            try:
                if len(defense_name) < 3:
                    raise InvalidNameException()
                else:
                    break
            except InvalidNameException as e:
                print(e)


        return {'fighter_name':fighter_name,
                'attack_name':attack_name,
                'defense_name':defense_name}


    def select_fighter(self, max_value):
        while True:
            option = input("Enter the number of the fighter:")
            try:
                if int(option) > 0 and int(option) <= max_value:
                    return int(option)
                else:
                    raise InvalidChoiceException()
            except Exception as e:
                print('Invalid Choice!')
                


    def edit_name_fighter(self,old_name):
        print('----- Edit Fighter name -----')
        print('Current name:',old_name)

        while True:
            new_name = input('New Name: ')
            try:
                if len(new_name) < 3:
                    raise InvalidNameException()
                else:
                    self.show_success_message('name changed successfully')
                    return new_name
            except InvalidNameException as e:
                print(e)
    
    

    def return_to_menu(self):
        print('press enter to return')
        input()
    

    def show_improve_skill_menu(self):
        print('[1] - Improve attack in 3 points = 5 coins')
        print('[2] - Improve defense in 3 points = 5 coins')
        while True:
            option = input("Select 1 or 2:")
            try:
                if option in ['1','2']:
                    return int(option)
                else:
                    raise InvalidChoiceException()
            except InvalidChoiceException as e:
                print(e)

    
    def show_fighter_menu(self):
        self.show_options()
        button, values = self.__window.Read()

        if values['1']:
            option = 1
        elif values['2']:
            option = 2
        elif values['3']:
            option = 3
        elif values['4']:
            option = 4
        elif values['5']:
            option = 5
        elif values['6']:
            option = 6
        elif values['7'] or button in (None, 'Cancel'):
            option = 7

        self.__window.Close()

        return option


    def show_options(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------------- Fighters Menu ---------------',font = ("Helvetica", 25))],
        [sg.Text('Choose your option',font = ("Helvetica", 15))],
        [sg.Radio('1 - See all my fighters','RD1',key = '1')],
        [sg.Radio('2 - Edit fighter','RD1',key = '2')],
        [sg.Radio('3 - Sell fighter (+15 coins)','RD1',key = '3')],
        [sg.Radio('4 - Buy New Fighter (-20 coins)','RD1',key = '4')],
        [sg.Radio('5 - Improve some fighter\'s skill (-5 coins)','RD1',key = '5')],
        [sg.Radio('6 - Complete some fighter\'s life (-10 coins)','RD1',key = '6')],
        [sg.Radio('7 - Return to Home Screen','RD1',key = '7')],
        [sg.Button('Confirm'), sg.Cancel('Cancel')]
        ]

        self.__window = sg.Window('RPG Game - POO 2').Layout(layout)

