from View.base_view import BaseView

class HomeView(BaseView):
    
    def show_home_screen_options(self, coins_quantity, current_battle):
        self.clear_screen()
        print('-------------Home Screen----------')
        print('| ',coins_quantity,' Coins | Current Battle ',current_battle)
        print('1- New Battle')
        print('2- Fighters Menu')
        print('3- Historic')

        while True:
            option = int(input("Enter your choice:"))
            if option in [1,2,3]:
                return option