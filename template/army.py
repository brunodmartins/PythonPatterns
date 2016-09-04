import abc

__author__ = 'Bruno'


class Soldier:
    """
    The soldier class
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def combat_move(self):
        """
        Do the combat's move
        """
        raise NotImplementedError

    @abc.abstractmethod
    def load_weapon(self):
        """
        Loads the weapon
        """
        raise NotImplementedError

    def attack(self):
        """
        Do the attack
        """
        self.load_weapon()
        self.combat_move()


class Warrior(Soldier):
    """
    The warrior class
    """

    def load_weapon(self):
        """
        Loads his sword
        """
        print('The brave warrior unsheathe his sword')

    def combat_move(self):
        """
        The combat move
        """
        print('Then, he falls it into his enemy')


class Archer(Soldier):
    """
    The archer class
    """

    def load_weapon(self):
        """
        Loads his arrow
        """
        print('The precise archer take the arrow from his bag')

    def combat_move(self):
        """
        The combat move
        """
        print("He aims the enemy, take a deep breath and hold...he shoots the arrow in the bull's eye ")


class SpellCaster(Soldier):
    """
    The SpellCaster class
    """

    def load_weapon(self):
        """
        Loads his book
        """
        print('The SpellCaster start reading his book')

    def combat_move(self):
        """
        The combat move
        """
        print("Then he start to spell some words and rises his tome, creating a fireball that toast the enemy!")
