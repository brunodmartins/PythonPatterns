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
    
    state = 0
    
    def setState(self, value):
        self.state = value
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


class ConcreteObserver(Observer):
      
    subject = None
    
    def __init__(self, subject):
        self.subject = subject
        subject.attach(self)
      
    def update(self):
        print('Novo estado ' + str(self.subject.state))
        

s = Subject();
observer = ConcreteObserver(s)
s.setState(2)
s.setState(3)
s.setState(4)