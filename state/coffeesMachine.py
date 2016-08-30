import abc

__author__ = 'Bruno'


class MachineContext:
    """
    Define's the machine's context
    """

    def __init__(self):
        """
        Constructor
        """
        self.state = TurnOnState()


class State:
    """
    Define's the abstract state
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def handle(self, machine_context):
        """
        Define's the abstract method for handle
        :param machine_context: the context of the operation
        :return:
        """
        raise NotImplementedError


class BringCupState(State):
    """
    Define's the State where a cup is bring
    """

    def handle(self, machine_context):
        """
        Bring a cup to the machine
        :param machine_context: the context of the operation
        """
        print("Bringing a cup")
        machine_context.state = ApplyCoffeeState()


class ApplyCoffeeState(State):
    """
    Define's the State where coffee is applied
    """

    def handle(self, machine_context):
        """
        Apply coffee to the cup
        :param machine_context: the context of the operation
        """
        print("Applying coffee to the cup")
        machine_context.state = FillWaterState()


class FillWaterState(State):
    """
    Define's the State where the cup is filled with water
    """

    def handle(self, machine_context):
        """
        Fill the cup with water
        :param machine_context: the context of the operation
        """
        print("Filling water")
        machine_context.state = TurnOffState()


class TurnOffState(State):
    """
    Define's the State where the machine is turned off
    """

    def handle(self, machine_context):
        """
        Turn off the machine
        :param machine_context: the context of the operation
        """
        print("Turned Off - Take your coffee")
        machine_context.state = None


class TurnOnState(State):
    """
    Define's the State where the machine is turned on
    """

    def handle(self, machine_context):
        """
        Turn on the machine
        :param machine_context: the context of the operation
        """
        print("Turned On- Please, wait")
        machine_context.state = BringCupState()
