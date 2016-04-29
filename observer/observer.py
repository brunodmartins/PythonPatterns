'''
Created on 15/03/2016

@author: bruno.martins
'''

import abc

class TemperatureSubject(object):
    '''
    classdocs
    '''
    themometers = [];
    
    @property
    def temperature(self):
        """Returns the current Celsius temperature"""
        return self.__temperature
    
    @temperature.setter
    def temperature(self,value):
        """Sets the current temperature in Celsius"""
        self.__temperature = value
        self.notifyThermometers()
    
     
    def notifyThermometers(self):
        for thermometer in self.themometers:
            thermometer.update();
            
    def attach(self, thermometer):
        self.themometers.append(thermometer)
    
    def deatach(self, thermometer):
        self.themometers.remove(thermometer)
    

class Thermometer(object):
    __metaclass__ = abc.ABCMeta
    
    temperature = 0
    
    @abc.abstractmethod
    def update(self):
        raise NotImplementedError


class CelsiusThermometer(Thermometer):
      
    temperature_subject = None
    
    def __init__(self, temperature_subject):
        self.temperature_subject = temperature_subject
        temperature_subject.attach(self)
      
    def update(self):
        self.temperature = self.temperature_subject.temperature
        print('Celsius:' + str(self.temperature))
        
class FahrenheitThermometer(Thermometer):
      
    temperature_subject = None
    
    def __init__(self, temperature_subject):
        self.temperature_subject = temperature_subject
        temperature_subject.attach(self)
      
    def update(self):
        self.temperature = self.temperature_subject.temperature * 1.8000 + 32.00
        print('Fahrenheit:' + str(self.temperature))

class KelvinThermometer(Thermometer):
      
    temperature_subject = None
    
    def __init__(self, temperature_subject):
        self.temperature_subject = temperature_subject
        temperature_subject.attach(self)
      
    def update(self):
        self.temperature = self.temperature_subject.temperature + 273.15
        print('Kelvin:' + str(self.temperature))