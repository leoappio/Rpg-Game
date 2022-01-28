from View.base_view import BaseView

class BattleView(BaseView):
    def __init__(self):
        ...

    def select_fighter_to_attack(self):
        print('-----Select fighter to attack------')

    def show_fighter_data(self,fighter_data):
        print(fighter_data['fighter_number'],'-',fighter_data['fighter_name'])
        print(fighter_data['attack_name'],'-',fighter_data['attack_power'], 'power')
        print(fighter_data['defense_name'],'-',fighter_data['defense_power'], 'power')
        print('Life',fighter_data['life'],'/100')

    def show_boss_data(self, boss_data):
        self.clear_screen()
        print('-----Boss Status------')
        print(boss_data['name'])
        print(boss_data['attack_name'],'-',boss_data['attack_power'], 'power')
        print(boss_data['defense_name'],'-',boss_data['defense_power'], 'power')
        print('Life',boss_data['life'],'/', boss_data['maximum_life'])

    def show_round_result(self, fighter, defender, dmg):
        print('%s dealt %d damage to %s' % (fighter, dmg, defender))

    def show_battle_report(self, report):
        self.clear_screen()
        print(report)

    def select_fighter(self):
        while True:
            try:
                option = int(input('Enter the number of the fighter:'))
            except:
                continue
            if option > 0 and option <= 3:
                return option

    def next_round(self):
        input('Press enter to continue:')
