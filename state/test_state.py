import unittest
from state.coffeesMachine import MachineContext

__author__ = 'Bruno'


class TestState(unittest.TestCase):
    def test(self):
        machine = MachineContext()
        while machine.state is not None:
            machine.state.handle(machine)


if __name__ == '__main__':
    unittest.main()
