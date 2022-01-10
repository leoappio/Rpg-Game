from View.base_view import BaseView

class FighterView(BaseView):
    def __init__(self):
        ...
    
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
