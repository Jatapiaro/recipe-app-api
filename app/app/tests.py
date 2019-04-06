from django.test import TestCase
from app.calc import add, subtract


class CalcTest(TestCase):

    def test_add_numbers(self):
        """ Test that tow numbers are added together """
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Values of subtracted are returned """
        self.assertEqual(subtract(11, 5), 6)
