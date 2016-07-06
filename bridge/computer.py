import abc
'''
Created on 10/05/2016

@author: bruno.martins
'''


class Processor(object):
    """
    Generic CPU
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, alu=None):
        """
        Constructor
        """
        self.alu = alu

    def sum_two_numbers(self, number1, number2):
        """
        Sum two numbers
        """
        raise NotImplementedError


class AMDProcessor(Processor):
    """
    AMD CPU
    """

    def __init__(self, alu):
        """
        Constructor
        """
        super().__init__(alu)

    def sum_two_numbers(self, number1, number2):
        print(self.alu.sum(number1, number2))


class Alu(object):
    """
    Generic ALU
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        """
        Constructor
        """

    @abc.abstractmethod
    def sum(self, number1, number2):
        """
        Sum two number
        """
        raise NotImplementedError


class AmdAlu(Alu):
    """
    AMD ALU
    """

    def __init__(self):
        """
        Constructor
        """
        super().__init__()

    def sum(self, number1, number2):
        print('AMD: {} + {} = {}'.format(number1, number2, number1 + number2))
        return number1 + number2


class IntelAlu(Alu):
    """
    Intel ALU
    """

    def sum(self, number1, number2):
        print('Intel: {} + {} = {}'.format(number1, number2, number1 + number2))
        return number1 + number2