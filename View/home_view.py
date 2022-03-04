from View.base_view import BaseView
from Model.Exceptions.InvalidChoiceException import InvalidChoiceException
import PySimpleGUI as sg


class HomeView(BaseView):

    def __init__(self):
        self.__window = None
        self.init_components(50,1)
    

    def show_home_screen_options(self, coins_quantity, current_battle):
        self.init_components(coins_quantity,current_battle)
        button, values = self.__window.Read()
        
        option = 0

        if values['1']:
            option = 1
        elif values['2']:
            option = 2
        elif values['3']:
            option = 3

        if values ['0'] or button in (None,'Cancel'):
            option = 0

        self.close()
        return option


    def close(self):
        self.__window.Close()


    def init_components(self, coins_quantity, current_battle):
        text_player_data = str(coins_quantity) +' Coins || Current Battle: '+str(current_battle)
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Welcome to RPG Game!', font =("Helvetica",25))],
            [sg.Text(text_player_data, font =("Helvetica",15))],
            [sg.Text('Choose your option', font =("Helvetica",15))],
            [sg.Radio('New Battle',"RD1" ,key = '1')],
            [sg.Radio('Fighters Menu',"RD1" ,key = '2')],
            [sg.Radio('History',"RD1" ,key = '3')],
            [sg.Radio('Exit',"RD1" ,key = '0')],
            [sg.Button('Confirm',sg.Cancel('Cancel'))]
        ]

        self.__window = sg.Window('RPG Game - POO 2').Layout(layout)


    def defeat(self):
        print('You Lost!')


    def victory(self):
        input('You Won! Press enter to continue')


    def show_history(self, data):
        self.clear_screen()
        for text in data:
            print(text)
        input('Press enter to continue')


    def ending(self):
        self.clear_screen()
        input('Congratulations, you finished the game!')
        input('Press enter to continue')


    def select_fighters_for_battle(self):
        self.clear_screen()
        print('---- Please, select 3 fighters for this battle. ----')

    def history_filter(self, fighters, max_value):
        self.clear_screen()
        print('---- Choose which fighter to show their history ----')
        print('1- Everybody')
        for fighter in fighters:
            print(fighter[0] + '- ' + fighter[1])
        while True:
            try:
                value = input('Choose one option:')
                if int(value) > 1 or int(value) <= max_value:
                    return int(value)
                else:
                    raise InvalidChoiceException()
            except Exception as e:
                print('Invalid Choice!')
