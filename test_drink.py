import unittest
from drink import Drink

pu = {'coffee': 10, 'chocolate': 10, 'tea': 10, 'milk':10, 'tea': 10, 'sugar': [0, 5, 15, 15]}

class DrinkTestCase(unittest.TestCase):

    def test_parse_order(self):
        drink_stock = {'milk': 1, 'sugar': 3, 'coffee': 1, 'tea': 0, 'chocolate':0}
        drink = Drink((1,1,1,0,1,0), None)
        self.assertEqual(drink.stocks, drink_stock)

        drink_stock = {'milk': 0, 'sugar': 0, 'coffee': 0, 'tea': 0, 'chocolate':0}
        drink = Drink((0,0,0,0,0,0), None)
        self.assertEqual(drink.stocks, drink_stock)

        drink_stock = {'milk': 0, 'sugar': 0, 'tea': 1, 'coffee': 0, 'chocolate':0}
        drink = Drink((0,0,0,1,1,1), None)
        self.assertEqual(drink.stocks, drink_stock)

        drink_stock = {'milk': 0, 'sugar': 0, 'tea': 0, 'coffee': 1, 'chocolate':1}
        drink = Drink((0,0,0,0,1,1), None)
        self.assertEqual(drink.stocks, drink_stock)

    def test_drink_price(self):
    	drink = Drink((1,1,1,0,1,0), pu)
    	self.assertEqual(drink.price, 15 + 10 + 10)

    	drink = Drink((0,0,0,0,0,0), pu)
    	self.assertEqual(drink.price, 0)

    def test_drink_has_beverage(self):
        drink = Drink((1,1,1,0,1,0), None)
        self.assertTrue(drink.has_beverage)

        drink = Drink((0,1,1,0,0,0), None)
        self.assertFalse(drink.has_beverage)

        drink = Drink((0,0,0,1,1,1), None)
        self.assertTrue(drink.has_beverage)

        drink = Drink((0,0,0,0,1,1), None)
        self.assertTrue(drink.has_beverage)