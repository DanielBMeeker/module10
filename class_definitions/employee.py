"""
Program: employee.py
Author: Daniel Meeker
Date: 7/5/2020

This program defines an employee class with a
display function as well as a str and repr function.
I've included getters and setters for all the fields.
"""
import datetime


class Employee:
    """Employee Class """
    # Constructor
    def __init__(self, last_name, first_name, address,
                 phone_number, salaried, start_date, salary):
        """
        Constructor for the Employee class
        :param last_name: string
        :param first_name: string
        :param address: string
        :param phone_number: string
        :param salaried: boolean
        :param start_date: datetime
        :param salary: float
        """
        self._last_name = last_name
        self._first_name = first_name
        self._address = address
        self._phone_number = phone_number
        self._salaried = salaried
        self._start_date = start_date
        self._salary = salary

    # Getters and Setters
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        self._phone_number = value

    @property
    def salaried(self):
        return self._salaried

    @salaried.setter
    def salaried(self, value):
        self._salaried = value

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        self._start_date = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        self._salary = value

    # Class functions
    def display(self):
        """
        This function organizes all the information from the object
        into a nicely formatted output string
        :return: a string
        """
        address_array = str(self.address).split(',')
        street = address_array[0]
        city = address_array[1]
        state = address_array[2]
        if self.salaried:
            salary_formatted = 'Salaried employee: $' + str(self.salary) + '/year'
        else:
            salary_formatted = 'Hourly employee: $' + str(self.salary) + '/hour'
        date = self.start_date.strftime("%m-%d-%Y")
        return (str(self.first_name) + " " + str(self.last_name) + "\n"
                + str(street).strip() + '\n' + str(city).strip() + ', ' + str(state).strip() + '\n'
                + str(salary_formatted) + '\n' + 'Start Date: ' + str(date))

    def __str__(self):
        """
        Overrides the built-in string function to provide a basic string describing the class object
        :return: a string giving a little information about the object
        """
        return "Employee with last name " + str(self.last_name) + ', first name ' + str(self.first_name)

    def __repr__(self):
        """
        Overrides the built-in repr function.
        :return: a string that contains all the information needed to recreate the object
        """
        return ("{self.__class__.__name__}({self.last_name}, "
                "{self.first_name}, '{self.address}', {self.phone_number}, "
                "{self.salaried}, {self.start_date}, {self.salary})".format(self=self))


# Driver
emp = Employee('Ruiz', 'Matthew', '123 Fake Street, Des Moines, Iowa',
               '515-555-5555', False, datetime.datetime.now(), '7.25')  # hourly emp
emp2 = Employee('Meeker', 'Daniel', '123 Fake Street, Des Moines, Iowa',
               '515-555-5555', True, datetime.datetime.now(), '30,000')  # salaried emp
print(emp.display())  # display returns a str, so print the information
print(emp)
print(repr(emp))
print(emp2.display())
print(emp2)
print(repr(emp2))
del emp, emp2  # clean up!
