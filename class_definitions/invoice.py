"""
Program: invoice.py
Author: Daniel Meeker
Date: 7/7/2020

This program defines an Invoice class and associated functions. It
has been updated to include the object Customer for customer name,
phone number, address, and customer ID.
"""
from class_definitions.customer import Customer


class Invoice:
    """
    Invoice Class
    """
    def __init__(self, invoice_id, customer, items_with_price={}):
        """
        Constructor for Invoice class
        :param invoice_id: required
        :param items_with_price: optional - defaults to empty dictionary
        """
        self.invoice_id = invoice_id
        self.items_with_price = items_with_price
        self.customer = customer

    def __str__(self):
        """
        Overrides built-in function
        :return: a simple string with identifying info about object
        """
        return ("Invoice ID {self.invoice_id}\n".format(self=self)
                + str(self.customer))

    def __repr__(self):
        """
        Overrides built-in function
        :return: a string that mimics the constructor
        """
        return ("{self.__class__.__name__}({self.invoice_id}, ".format(self=self)
                + repr(self.customer)
                + ", {self.items_with_price})".format(self=self))

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
        print(self)
        for key, value in self.items_with_price.items():
            print("{}.....${:.2f}".format(key, value))
            subtotal += value
        tax = subtotal * sales_tax
        total = subtotal + tax
        print("Tax.....${:.2f}\nTotal.....${:.2f}".format(tax, total))


# Driver code
if __name__ == '__main__':
    captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones', 'Firefly, somewhere in the verse')
    invoice = Invoice(1, captain_mal)
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
    print(repr(invoice))
    del invoice
