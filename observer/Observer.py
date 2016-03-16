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
    
    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self,value):
        self.__state = value
        self.notifyAllObservers()
    
     
    def notifyAllObservers(self):
        for observer in self.observers:
            observer.update();
            
    def attach(self, observer):
        self.observers.append(observer)
    
    def deatach(self, observer):
        self.observers.remove(observer)
    

class Observer(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def update(self):
        raise NotImplementedError


class ConcreteObserverA(Observer):
      
    subject = None
    
    def __init__(self, subject):
        self.subject = subject
        subject.attach(self)
      
    def update(self):
        print('Novo estado a ' + str(self.subject.state))
        
class ConcreteObserverB(Observer):
      
    subject = None
    
    def __init__(self, subject):
        self.subject = subject
        subject.attach(self)
      
    def update(self):
        print('Novo estado b ' + str(self.subject.state))

s = Subject();
observer = ConcreteObserverA(s)
observer = ConcreteObserverB(s)
s.state = 2
s.state = 3
s.state = 4