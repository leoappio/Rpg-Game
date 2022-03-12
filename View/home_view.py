from View.base_view import BaseView
from Model.Exceptions.InvalidChoiceException import InvalidChoiceException
import PySimpleGUI as sg


class HomeView(BaseView):

    def __init__(self):
        self.__window = None
    

    def show_home_screen_options(self, coins_quantity, current_battle):
        self.init_components(coins_quantity,current_battle)
        button, values = self.__window.Read()
        
        option = 0

        if values['1']:
            option = 1
        if values['2']:
            option = 2
        if values['3']:
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
            [sg.Button('Confirm'),sg.Cancel('Cancel')]
        ]

        self.__window = sg.Window('RPG Game - POO 2').Layout(layout)


    def defeat(self):
        self.show_message('You have been defeated!')


    def victory(self):
        self.show_message('You\'ve Won! Press enter to continue')


    def show_history(self, data):
        self.clear_screen()
        for text in data:
            print(text)
        input('Press enter to continue')


    def ending(self):
        self.show_message('Congratulations, you finished the game!')
