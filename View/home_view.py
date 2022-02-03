from View.base_view import BaseView
from Model.Exceptions.InvalidChoiceException import InvalidChoiceException

class HomeView(BaseView):
    
    def show_home_screen_options(self, coins_quantity, current_battle):
        self.clear_screen()
        print('-----------Home Screen----------')
        print('|',coins_quantity,'Coins | Current Battle:',current_battle,'|')
        print('1- New Battle')
        print('2- Fighters Menu')
        print('3- History')

        while True:
            try:
                option = input("Enter your choice:")
                if option in ['1','2','3']:
                    return int(option)
                else:
                    raise InvalidChoiceException()
            except InvalidChoiceException as e:
                print(e)

    def defeat(self):
        print('You Lost!')

    def victory(self):
        input('You Won! Press enter to continue')

    def show_history(self, data):
        self.clear_screen()
        print('-----------Battles fought----------')
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