import abc

__author__= 'Bruno'


class Iterator:
    """
    Iterator class
    """
    __metaclass__ = abc.ABCMeta

    def first(self):
        raise NotImplementedError

    def hasNext(self):
        raise NotImplementedError

    def next(self):
        raise NotImplementedError

class FabricIterator:
    """
    Iterator class
    """
    def __init__(self, cars):
        self.cars = cars
        self.index = 0;

    def first(self):
        return self.cars[0]

    def hasNext(self):
        return self.index < len(self.cars)

    def next(self):
        car = self.cars[self.index]
        self.index += 1
        return car

class Fabric:

    def __init__(self):
        self.cars = []

    def getIterator(self):
        return FabricIterator(self.cars)

class Car:

    def __init__(self,name="", color=""):
        self.name = name
        self.color = color

    def __str__(self):
        return self.name + str(self.color)

fabric = Fabric()
fabric.cars.append(Car('teste', 1))
fabric.cars.append(Car('teste', 2))
fabric.cars.append(Car('teste', 3))
iterator = fabric.getIterator()

while(iterator.hasNext()):
    print(iterator.next())
