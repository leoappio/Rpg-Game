from View.base_view import BaseView
from Model.Exceptions.InvalidChoiceException import InvalidChoiceException
from Model.Exceptions.InvalidNameException import InvalidNameException
import PySimpleGUI as sg

class HistoryView():
    def __init__(self):
        ...

    def show_history(self, text):
        layout = []
        for event in text:
            layout.append([sg.Text('- ' + event)])
        layout.append([sg.Ok()])
        self.__window = sg.Window('History').Layout(layout)
        button, values = self.__window.Read()
        
        self.__window.Close()

    def fill_filter(self):
        layout = [[sg.Text('Please insert the name of a character you want to search for in the history:')],
                [sg.InputText('',key='filter')],
                [sg.Submit(), sg.Cancel()]]
        self.__window = sg.Window('History').Layout(layout)
        button, values = self.__window.Read()
        self.__window.Close()

        if button == 'Cancel':
            return False
        else:
            return values