"""
Program: customer.py
Author: Daniel Meeker
Date: 7/5/2020

This program defines a customer class with a constructor and 3 methods:
str, repr, and display.
"""


class Customer:
    """
    Customer Class
    """

    def __init__(self, customer_id, last_name, first_name, phone_number, address):
        """
        Constructor for customer class - throws an error if customer_id not an int
        :param customer_id: required
        :param last_name: required
        :param first_name: required
        :param phone_number: required
        :param address: required
        """
        if isinstance(customer_id, int):
            self.customer_id = customer_id
        else:
            raise AttributeError("Customer ID not an int \nCustomer not created")
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number

    def __str__(self):
        """
        overrides built-in function
        :return: a basic string to identify the object
        """
        return ("Customer with first name {self.first_name}, last name {self.last_name}, "
                "and Customer ID {self.customer_id}".format(self=self))

    def __repr__(self):
        """
        overrides built-in function
        :return: a string that mimics the constructor.
        """
        return ("{self.__class__.__name__}({self.customer_id}, '{self.last_name}', "
                "'{self.first_name}', '{self.address}', '{self.phone_number}')".format(self=self))

    def display(self):
        """
        gathers all the info from the object to create a prettyfied string
        :return: a string
        """
        address_array = str(self.address).split(',')
        street = address_array[0]
        city = address_array[1]
        state = address_array[2]
        return ("Customer ID: " + str(self.customer_id) + "\n" + str(self.first_name) + " "
                + str(self.last_name) + "\n" + str(street).strip() + "\n" + str(city).strip() + ', '
                + str(state).strip() + "\n" + str(self.phone_number))


# Driver
print("Customer 1:")
customer1 = Customer(12345, 'Meeker', 'Daniel', '515-555-5555', '123 Fake St, Des Moines, Iowa')
print(customer1.display())
print(customer1)
print(repr(customer1))
del customer1
print('')
try:
    print("Customer 2:")
    customer2 = Customer('Member', 'Meeker', 'Daniel', '515-555-5555', '123 Real St, Des Moines, Iowa')
    print(customer2.display())
    print(customer2)
    print(repr(customer2))
    del customer2
except AttributeError as e:
    print(e)

