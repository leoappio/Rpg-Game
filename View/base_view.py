import os
from abc import ABC
import PySimpleGUI as sg

class BaseView(ABC):
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_message(self,message):
        sg.Popup('Message', message)



