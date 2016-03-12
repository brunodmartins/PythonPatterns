'''
Created on 10/03/2016

@author: bruno.martins
'''
import abc

class Speak(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod
    def falar(self):
        """"implementacao"""

class Humano(Speak):
    
    def falar(self):
        return 'oi'
    
class Cachorro(Speak):
    
    def falar(self):
        return 'Au au'

lista = [Humano(), Cachorro()]
for speak in lista:
    print(speak.falar());
