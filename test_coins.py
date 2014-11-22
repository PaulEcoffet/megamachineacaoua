import unittest
from coins import Coins
from collections import Counter
import copy

class CoinsTestCase(unittest.TestCase):

    def test_coins_init(self):
        coins_amount = [2, 10, 5, 1, 0]
        coins_type = [200, 100, 50, 20, 10]
        ref = Counter({200:2, 100:10, 50:5, 20:1, 10:0})
        coins = Coins(coins_amount, coins_type)
        self.assertEqual(coins, ref)

    def test_coins_value(self):
        coins_amount = [2, 10, 5, 1, 0]
        coins_type = [200, 100, 50, 20, 10]
        coins = Coins(coins_amount, coins_type)
        expected = 2*200 + 10*100 + 5*50 + 1*20
        self.assertEqual(coins.value, expected)


    # Just testing the alias. Since it's Counter implementation,
    # we can assume it works as expected
    def test_coins_add_in_place(self):
        coins_type = [200, 100, 50]
        coins_amount1 = [10, 2, 5]
        coins_amount2 = [2, 4, 3]
        coins = Coins(coins_amount1, coins_type)
        coins2 = Coins(coins_amount2, coins_type)
        coins.add(coins2)
        self.assertEqual(coins, Coins([12, 6, 8], coins_type))

    # It would be a nice idea to ensure that coins are never in a negative
    # amount.
