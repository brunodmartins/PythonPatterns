import abc

__author__= 'Bruno'


class Iterator:
    """
    Iterator class
    """
    __metaclass__ = abc.ABCMeta

    def first(self):
        """
        Return first element
        """
        raise NotImplementedError

    def hasNext(self):
        """
        Verify if there is a next element
        """
        raise NotImplementedError

    def next(self):
        """
        Return the next element
        """
        raise NotImplementedError

class FabricIterator:
    """
    Fabric's Iterator class
    """

    def __init__(self, cars):
        """
        Constructor
        """
        self.cars = cars
        self.index = 0;

    def first(self):
        """
        Return the first car
        """
        self.index=0;
        return self.cars[0]

    def hasNext(self):
        """
        Verifiy if there is another car
        """
        return self.index < len(self.cars)

    def next(self):
        """
        Return the next car
        """
        car = self.cars[self.index]
        self.index += 1
        return car

class Fabric:
    """
    Fabric class
    """

    def __init__(self):
        """
        Constructor
        """
        self.cars = []

    def getIterator(self):
        """
        Return the fabric iterator
        """
        return FabricIterator(self.cars)

class Car:
    """
    Car class
    """

    def __init__(self,name="", color=""):
        """
        Construcor
        """
        self.name = name
        self.color = color

    def __str__(self):
        """
        Override
        """
        return "Car -> Name: {}, Color: {}".format(self.name,self.color)
