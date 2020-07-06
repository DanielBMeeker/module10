"""
Program: test_student.py
Author: Daniel Meeker
Date: 7/5/2020

This file contains unittests for the student class.
"""
import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Meeker', 'Daniel', 'BIS-OOP', 3.9)

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Meeker')
        self.assertEqual(self.student.first_name, 'Daniel')
        self.assertEqual(self.student.major, 'BIS-OOP')

    def test_object_created_all_attributes(self):
        student = s.Student('Meeker', 'Daniel', 'BIS-OOP', 3.9) # this is not self.person from setUp, but local
        assert student.last_name == 'Meeker'                 # note no self here on person or assert
        assert student.first_name == 'Daniel'
        assert student.major == 'BIS-OOP'
        assert student.gpa == 3.9

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Meeker, Daniel has major BIS-OOP with gpa: 3.9')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            p = s.Student('123', 'Daniel', 'BIS-OOP')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(ValueError):
            p = s.Student('Meeker', '123', 'BIS-OOP')

    def test_object_not_created_error_in_major(self):
        with self.assertRaises(ValueError):
            p = s.Student('Meeker', 'Daniel', 'Yoga')

    def test_object_not_created_error_in_gpa(self):
        with self.assertRaises(ValueError):
            p = s.Student('Meeker', 'Daniel', 'CIS', 5.0)  # out of range
            d = s.Student('Meeker', 'Daniel', 'CIS', 2)  # int not float
            q = s.Student('Meeker', 'Daniel', 'CIS', 'Four Point O')  # not a float


