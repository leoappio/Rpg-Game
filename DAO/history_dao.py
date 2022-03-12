from DAO.dao import DAO
from Model.history import History

class HistoryDAO(DAO):
    def __init__(self):
        super().__init__('histories.pkl')

    def add(self, history):
        if((history is not None) and isinstance(history, History)):
            super().add(1, history)


    def update(self, history):
        if((history is not None) and isinstance(history, History)):
            super().update(1, history)


    def get(self):
        return super().get(1)

    def remove(self):
        return super().remove(1)