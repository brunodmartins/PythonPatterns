'''
Created on 15/03/2016

@author: bruno.martins
'''

import abc

class Subject(object):
    '''
    classdocs
    '''
    observers = [];

    def notifyAllObservers(self):
        for observer in self.observers:
            observer.update();


class Observer(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def update(self):
        raise NotImplementedError


class ObserverA(Observer):
    def update(self):
        print('Novo estado')
        

a = ObserverA();
s = Subject();
s.observers.append(a);
s.notifyAllObservers();