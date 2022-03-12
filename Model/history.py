from Model.Exceptions.InvalidParameterException import InvalidParameterException
import random

class History():
    def __init__(self):
        self.__history = []

    def add_event(self, event):
        if isinstance(event, str):
            self.__history.append(event)
        else:
            raise InvalidParameterException('event', 'add event', 'History')

    def search_events(self, filter):
        events = []
        for event in self.__history:
            if filter in event:
                events.append(event)
        return events

    @property
    def id(self):
        return self.__id