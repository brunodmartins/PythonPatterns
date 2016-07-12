"""
Created on 15/03/2016

@author: bruno.martins
"""

import abc


class TemperatureSubject(object):
    """
    classdocs
    """
    thermometers = []

    def __init__(self):
        self.__temperature = None
    
    @property
    def temperature(self):
        """Returns the current Celsius temperature"""
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):
        """Sets the current temperature in Celsius"""
        self.__temperature = value
        self.notify_thermometers()

    def notify_thermometers(self):
        """Notify all observer"""
        for thermometer in self.thermometers:
            thermometer.update()
            
    def attach(self, thermometer):
        """attach observer"""
        self.thermometers.append(thermometer)
    
    def deatach(self, thermometer):
        """detach obsrever"""
        self.thermometers.remove(thermometer)
    

class Thermometer(object):
    """
    Abstract class to thermometer
    """
    __metaclass__ = abc.ABCMeta
    
    temperature = 0
    
    @abc.abstractmethod
    def update(self):
        """updates the temperature in thermometer"""
        raise NotImplementedError


class CelsiusThermometer(Thermometer):
    """
    Celsius thermometer
    """
    temperature_subject = None
    
    def __init__(self, temperature_subject):
        self.temperature_subject = temperature_subject
        temperature_subject.attach(self)
      
    def update(self):
        self.temperature = self.temperature_subject.temperature
        print('Celsius:' + str(self.temperature))


class FahrenheitThermometer(Thermometer):
    """
    Fahrenheit thermometer
    """
      
    temperature_subject = None
    
    def __init__(self, temperature_subject):
        self.temperature_subject = temperature_subject
        temperature_subject.attach(self)
      
    def update(self):
        self.temperature = self.temperature_subject.temperature * 1.8000 + 32.00
        print('Fahrenheit:' + str(self.temperature))


class KelvinThermometer(Thermometer):
    """
    Kelvin thermometer
    """
    temperature_subject = None
    
    def __init__(self, temperature_subject):
        self.temperature_subject = temperature_subject
        temperature_subject.attach(self)
      
    def update(self):
        self.temperature = self.temperature_subject.temperature + 273.15
        print('Kelvin:' + str(self.temperature))