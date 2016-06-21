import abc

__author__ = 'Bruno'


class Food:
    """
    The food class is responsible
    to provide functions to the client
    knows things like price and description
    of what it gonna eat
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def description(self):
        """
        This function returns the food's description
        """
        raise NotImplementedError

    @abc.abstractmethod
    def price(self):
        """
        This function returns the food's price
        """
        raise NotImplementedError


class Hamburger(Food):
    """
    This class is responsible
    to implement the Food class
    """

    def description(self):
        return 'A Big Mac'

    def price(self):
        return 5


class DecoratorFood(Food):
    """
    This class is responsible
    to provide decorators to be used
    on a food
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, food_wrapper=None):
        self.food = food_wrapper

    def description(self):
        return self.food.description()

    def price(self):
        return self.food.price()


class SaladDecorator(DecoratorFood):
    """
    This class is responsible
    to decorate a food with salad
    """

    def __init__(self, food_wrapper):
        DecoratorFood.__init__(self, food_wrapper)

    def description(self):
        return DecoratorFood.description(self) + ', with salad'

    def price(self):
        return DecoratorFood.price(self) + 2


class CheeseDecorator(DecoratorFood):
    """
    This class is responsible
    to decorate a food with chesse
    """

    def __init__(self, food_wrapper):
        DecoratorFood.__init__(self, food_wrapper)

    def description(self):
        return DecoratorFood.description(self) + ', with cheese'

    def price(self):
        return DecoratorFood.price(self) + 1


class BaconDecorator(DecoratorFood):
    """
    This class is responsible
    to decorate a food with Bacon
    """

    def __init__(self, food_wrapper):
        DecoratorFood.__init__(self, food_wrapper)

    def description(self):
        return DecoratorFood.description(self) + ', with bacon'

    def price(self):
        return DecoratorFood.price(self) + 3
