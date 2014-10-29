import unittest
from machine import Machine, Order, Drink

class DrinkTestCase(unittest.TestCase):
    """
    Test for the Drink choosen
    """
    def test_drink_base(self):
        array_drink = ["café","thé","chocolat"]

        for drink in array_drink:
            dr = Drink(drink)
            self.assertEqual(dr.base,drink)

        dr = Drink("capuccino")
        self.assertFalse(dr.base == "capuccino")
        #capuccino not a base, café would be the base
        #should be treated before calling Drink()

    def test_drink_sugar(self):

        for p in range(0,4):
            dr = Drink("café", supp_sugar=p)
            self.assertEqual(dr.supp_sugar,p)
    
