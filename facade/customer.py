__author__ = 'Bruno'


class Customer:
    """
    Customer class
    """

    def __init__(self, name="", age=0):
        """
        Constructor
        :param name: costumer's name
        :param age: costumer's age
        """
        self.name = name
        self.age = age


class CustomerDao:
    """
    Customer's DataAccess class
    """

    @classmethod
    def save(cls, customer):
        """
        Saves the Customer in a database
        :param customer: costumer to save
        """
        print("Saving customer {} with {} years".format(customer.name, customer.age))


class CustomerValidate:
    """
    This class validate if a client is
    valid
    """

    @classmethod
    def validate(cls, customer):
        """
        Validate customer
        :param customer: customer to be validated
        :return: True or False
        """
        if customer.name == "":
            print("Customer {} is not ok".format(customer.name))
            return False
        else:
            print("Customer {} is ok".format(customer.name))
            return True


class CustomerFacade:
    """
    Facade class to call
    all rules to save a customer
    """

    def __init__(self):
        self.dao = CustomerDao()
        self.validate = CustomerValidate()

    def save(self, customer):
        """
        Save the customer
        :param customer:
        """
        if not self.validate.validate(customer):
            raise Exception("Customer {} is invalid".format(customer.name))

        self.dao.save(customer)
