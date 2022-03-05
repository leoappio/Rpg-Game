from View.base_view import BaseView
from Model.Exceptions.InvalidChoiceException import InvalidChoiceException
from Model.Exceptions.InvalidNameException import InvalidNameException
import PySimpleGUI as sg

class FighterView(BaseView):
    def __init__(self):
        self.__window = None
    

    def see_all_fighters(self, fighters_data):
        string_all_fighters_data = ''

        for fighter in fighters_data:
            string_all_fighters_data = string_all_fighters_data + str(fighter['fighter_number']) +' - ' + fighter['fighter_name'] + "\n"
            string_all_fighters_data = string_all_fighters_data + fighter['attack_name']+'-'+str(fighter['attack_power']) + ' power \n'
            string_all_fighters_data = string_all_fighters_data + fighter['defense_name'] + '-' + str(fighter['defense_power']) + ' power \n'
            string_all_fighters_data = string_all_fighters_data + 'Life '+str(fighter['life'])+'/100 \n------------------------------ \n'


        sg.Popup('------- All Fighters --------',string_all_fighters_data)
    

    def show_sell_fighter_header(self):
        self.clear_screen()
        print('-----Select fighter to sell------')
    
        
    def show_select_fighters_for_battle_header(self,selected_fighters):
        self.clear_screen()
        print('-----Select fighters to battle------')
        print('|Fighters selected: '+str(selected_fighters)+'/3 |')
        print()
    

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


    def show_fighter_data(self,fighter):
        
        string_all_fighters_data = ''
        string_all_fighters_data = string_all_fighters_data + str(fighter['fighter_number']) +' - ' + fighter['fighter_name'] + "\n"
        string_all_fighters_data = string_all_fighters_data + fighter['attack_name']+'-'+str(fighter['attack_power']) + ' power \n'
        string_all_fighters_data = string_all_fighters_data + fighter['defense_name'] + '-' + str(fighter['defense_power']) + ' power \n'
        string_all_fighters_data = string_all_fighters_data + 'Life '+str(fighter['life'])+'/100 \n------------------------------ \n'


        sg.Popup('------- Fighter Data --------',string_all_fighters_data)
    

    def buy_new_fighter(self):

        layout = [
                [sg.Text('------------ Buy New Fighter ------------', font = ('Helvetica',15))],
                [sg.Text('Fighters skills are generated randomly', font = ('Helvetica',15))],
                [sg.Text('(10-40) - 60% chance', font = ('Helvetica',10))],
                [sg.Text('(41-50) - 25% chance', font = ('Helvetica',10))],
                [sg.Text('(51-80) - 10% chance', font = ('Helvetica',10))],
                [sg.Text('(81-100) - 5% chance', font = ('Helvetica',10))],
                [sg.Text('--------------------', font = ('Helvetica',10))],
                [sg.Text('Fighter Name:',size = (10,1)),sg.InputText('',key='fighter_name')],
                [sg.Text('Attack Name:',size = (10,1)),sg.InputText('',key='attack_name')],
                [sg.Text('Defense Name:',size = (10,1)),sg.InputText('',key='defense_name')],
                [sg.Button('Confirm'), sg.Cancel('Cancel')]
            ]
        self.__window = sg.Window('RPG Game - POO 2').Layout(layout)

        while True:
            button, values = self.__window.Read()

            fighter_name = values['fighter_name']
            attack_name = values['attack_name']
            defense_name = values['defense_name']
            
            if len(fighter_name) >= 3 and len(attack_name) > 3 and len(defense_name):
                self.__window.Close()
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
    

    def screen_select_fighter(self,fighters_list):
        layout = [[sg.Text('------ Select Fighter -------',font = ("Helvetica",15))]]
        for index, fighter in enumerate(fighters_list):
            layout_item = [sg.Radio(fighter,"RD1", key = str(index))]
            layout.append(layout_item)

        layout.append([sg.Button('Confirm'), sg.Cancel('Cancelar')])

        self.__window = sg.Window('RPG Game - POO 2').Layout(layout)

        button, values = self.__window.Read()

        for index in range(0,len(fighters_list)):
            if values[str(index)]:
                self.__window.Close()
                return index

    def edit_name_fighter(self,old_name):

        layout = [
                [sg.Text('------- Edit Fighter -------', font = ('Helvetica',15))],
                [sg.Text('Fighter Old Name:'+old_name, font = ('Helvetica', 10))],
                [sg.Text('New Name:',size=(10,1)),sg.InputText('',key='name')],
                [sg.Button('Confirm'), sg.Cancel('Cancel')]
        ]

        self.__window = sg.Window('RPG GAME - POO 2').Layout(layout)
        
        while True:
            button, values = self.__window.Read()
            new_name = values['name']
        
            if len(new_name) >= 3:
                self.__window.Close()
                return new_name
    

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

