__author__ = 'Bruno'


class Coffee:
    """
    This class represents a coffee
    in the real world
    """

    def __init__(self, name):
        """
        Constructor
        :param name: Coffee's name
        """
        self.name = name


class CoffeeFactory:
    """
    The coffee's factory
    """

    coffees = {}

    @classmethod
    def create_coffee(cls, name):
        """
        Creates a coffee's instance, or
        get from the flyweight's dictionary
        """
        if name in cls.coffees:
            return cls.coffees.get(name)
        else:
            coffee = Coffee(name)
            cls.coffees[name] = coffee
            return coffee


class Orders:
    """
    Orders's class
    """

    orders = {}

    @classmethod
    def order_coffee(cls, name, table):
        """
        Register a order
        :param name: Coffee's name
        :param table: Table's id
        """
        cls.orders[table] = CoffeeFactory.create_coffee(name)

    @classmethod
    def print_orders(cls):
        """
        Print the orders
        """
        for table, coffee in cls.orders.items():
            print('Table = {}  Coffee = {}  Memory Address= {}'.format(table, coffee.name, coffee))
