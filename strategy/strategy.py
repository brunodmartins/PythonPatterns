'''
Created on 10/03/2016

@author: bruno.martins
'''
import abc


class Speak(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def speak(self):
        raise NotImplementedError


class Human(Speak):
    def speak(self):
        return 'Hello!'


class Dog(Speak):
    def speak(self):
        return 'Bark!'
