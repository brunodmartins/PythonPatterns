import unittest
from observer import *

__author__ = 'Bruno'


class Test(unittest.TestCase):
    def test_observer(self):
        temperature = TemperatureSubject()
        CelsiusThermometer(temperature)
        KelvinThermometer(temperature)
        FahrenheitThermometer(temperature)
        temperature.temperature = 36


if __name__ == '__main__':
    unittest.main()
