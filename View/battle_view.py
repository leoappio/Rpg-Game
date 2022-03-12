from View.base_view import BaseView
import PySimpleGUI as sg
class BattleView(BaseView):
    def __init__(self):
        ...

    def show_battle(self, boss, fighters):
        layout = [[sg.Text('------ ' + boss['name'] + ' -------',font = ("Helvetica",15))]]
        layout.append([sg.Text(str(boss['life']) + ' / ' + str(boss['maximum_life']), font = ("Helvetica",15))])
        layout.append([sg.Text(boss['attack_name'] + ' - ' + str(boss['attack_power']) + ' power', font = ("Helvetica",15))])
        layout.append([sg.Text(boss['defense_name'] + ' - ' + str(boss['defense_power']) + ' power', font = ("Helvetica",15))])
        layout.append([sg.Text('------ Select Fighter -------',font = ("Helvetica",15))])
        for index, fighter in enumerate(fighters):
            fighter = fighters[fighter]
            layout.append([sg.Radio(fighter['fighter_name'] + '\n' + str(fighter['life']) + ' / 100' + '\n' + fighter['attack_name'] + ' - ' + str(fighter['attack_power']) + ' power' + '\n' + fighter['defense_name'] + ' - ' + str(fighter['defense_power']) + ' power',"RD1", key = str(index))])

        layout.append([sg.Button('Confirm')])

        self.__window = sg.Window('Battle!').Layout(layout)

        button, values = self.__window.Read()

        for index in range(0,len(fighters)):
            if values[str(index)]:
                self.__window.Close()
                return index

    def show_battle_report(self, report):
        self.clear_screen()
        print(report)
