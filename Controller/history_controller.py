from View.history_view import HistoryView
from Model.history import History
from DAO.history_dao import HistoryDAO

class HistoryController():
    def __init__(self):
        self.__history = History()
        self.__history_view = HistoryView()
        self.__history_DAO = HistoryDAO()
        historySaved = self.__history_DAO.get()

        if historySaved == None:
            self.__history_DAO.add(self.__history)
        else:
            self.__history = historySaved

    def new_event(self, text):
        self.__history.add_event(text)
        self.__history_DAO.update(self.__history)

    def filter_events(self):
        text = self.ask_filter()
        if text:
            filtered = self.__history.search_events(text['filter'])
            self.__history_view.show_history(filtered)
        else:
            return False

    def ask_filter(self):
        values = self.__history_view.fill_filter()
        return values
