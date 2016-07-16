import unittest
from facade.customer import Customer, CustomerFacade

__author__ = 'Bruno'


class FacadeTest(unittest.TestCase):
    """
    Facade's Test
    """

    def test_save_customer(self):
        """
        Must save a customer without error
        """
        customer = Customer("Bruno", 21)
        CustomerFacade().save(customer)

    # noinspection PyBroadException
    def test_save_customer_error(self):
        """
        Must save a customer with error
        """
        customer = Customer("", 21)
        try:
            CustomerFacade().save(customer)
        except Exception:
            pass


if __name__ == '__main__':
    unittest.main()
