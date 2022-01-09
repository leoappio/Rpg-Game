import os

class BaseView():
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_error(self,error):
        red = '\033[31m'
        white = '\033[0;0m'
        print(red + error + white)


