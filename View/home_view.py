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
