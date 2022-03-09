from View.boss_view import BossView
from Model.boss import Boss
from Controller.attack_controller import AttackController
from Controller.defense_controller import DefenseController
from DAO.bosses_dao import BossesDAO

class BossController():
    def __init__(self):
        self.__boss_view = BossView()
        self.__attack_controller = AttackController()
        self.__defense_controller = DefenseController()
        self.__bosses_DAO = BossesDAO()
    
    def generate_new_boss(self, battle_number):
        
        boss_attack = self.__attack_controller.generate_new_random_attack(battle_number)
        boss_defense = self.__defense_controller.generate_new_random_defense(battle_number)

        life = battle_number * 50

        generated_boss = Boss('Boss '+str(battle_number), boss_attack, boss_defense, life)

        boss_id = len(self.__bosses_DAO.get_all()) + 1
        self.__bosses_DAO.add(boss_id,generated_boss)

        return generated_boss
    

    @property
    def bosses(self):
        return self.__bosses_DAO.get_all()
