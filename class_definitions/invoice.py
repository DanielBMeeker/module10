"""
Program: invoice.py
Author: Daniel Meeker
Date: 7/5/2020

This program defines an Invoice class and associated functions.
"""


class Invoice:
    """
    Invoice Class
    """
    def __init__(self, invoice_id, customer_id, last_name, first_name,
                 phone_number, address, items_with_price={}):
        """
        Constructor for Invoice class
        :param invoice_id: required
        :param customer_id: required
        :param last_name: required
        :param first_name: required
        :param phone_number: required
        :param address: required
        :param items_with_price: optional - defaults to empty dictionary
        """
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number
        self.items_with_price = items_with_price

    def __str__(self):
        """
        Overrides built-in function
        :return: a simple string with identifying info about object
        """
        return ("Invoice with with first name {self.first_name}, last name {self.last_name}, "
                "and Invoice ID {self.invoice_id}".format(self=self))

    def __repr__(self):
        """
        Overrides built-in function
        :return: a string that mimics the constructor
        """
        return ("{self.__class__.__name__}({self.invoice_id}, {self.customer_id}, "
                "'{self.last_name}', '{self.first_name}', '{self.address}', "
                "'{self.phone_number}', {self.items_with_price})".format(self=self))

    def add_item(self, item_to_add):
        """
        Adds an item to the dictionary
        :param item_to_add: key value pair to add to dictionary
        :return: no return
        """
        self.items_with_price.update(item_to_add)

    def create_invoice(self):
        """
        that prints each item and price, then a total with tax calculated
        :return: prints in method instead of returning a value as per instructions
        """
        subtotal = 0
        sales_tax = .06
        for key, value in self.items_with_price.items():
            print("{}.....${:.2f}".format(key, value))
            subtotal += value
        tax = subtotal * sales_tax
        total = subtotal + tax
        print("Tax.....${:.2f}\nTotal.....${:.2f}".format(tax, total))


# Driver code
invoice = Invoice(1, 123, 'Mouse', 'Minnie', '555-867-5309', '1313 Disneyland Dr, Anaheim, CA 92802')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
print(invoice)
print(repr(invoice))
del invoice
