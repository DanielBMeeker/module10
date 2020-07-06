import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Meeker', 'Daniel', 'BIS-OOP', 3.9)

    def tearDown(self):
        del self.student

    def test_initial_value_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Meeker')
        self.assertEqual(self.student.first_name, 'Daniel')
        self.assertEqual(self.student.major, 'BIS-OOP')
        self.assertEqual(self.student.gpa, 3.9)
