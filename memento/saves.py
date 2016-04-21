import datetime

__author__ = 'Bruno'


class SaveFile(object):

    def __init__(self):
        self.__memento = None;
        self.name = 'save_file'
        self.date = datetime.datetime.now()

    def __str__(self, *args, **kwargs):
        return 'Name {} - Date {}'.format(self.name, self.date)

    def save_file(self):
        return SaveFileMemento(self.name,self.date)

    def return_save(self, state):
        self.name = state.name
        self.date = state.date


class SaveFileMemento(object):

    def __init__(self,name,date):
        self.name = name
        self.date = date


class MemoryCard(object):

    def __init__(self):
        self.list_saves = []

    def add_save(self, save):
        self.list_saves.append(save)

    def get_save(self, index):
        return self.list_saves[index]