import unittest
from coins import Coins, NoChangePossibleException
from collections import Counter
import copy

class CoinsTestCase(unittest.TestCase):

    def test_coins_init(self):
        coins_amount = [2, 10, 5, 1, 0]
        coins_type = [200, 100, 50, 20, 10]
        ref = Counter({200:2, 100:10, 50:5, 20:1, 10:0})
        coins = Coins({type_:amount for type_, amount
                       in zip(coins_type, coins_amount)})
        self.assertEqual(coins, ref)
        self.assertEqual(Coins(), Coins())
        coins_repeat = [200, 200, 50, 10]
        coins = Coins(coins_repeat)
        ref = Counter({200: 2, 50: 1, 10:1})
        self.assertEqual(coins, ref)

    def test_coins_not_working_init(self):
        self.assertRaises(ValueError, Coins, ['gibi', 4, 5, 5])
        self.assertRaises(ValueError, Coins, {100: 'gégène'})
        self.assertRaises(ValueError, Coins, {'#YOLO': 20})
        self.assertRaises(ValueError, Coins, 4)

    def test_coins_value(self):
        coins_amount = [2, 10, 5, 1, 0]
        coins_type = [200, 100, 50, 20, 10]
        coins = Coins({type_:amount for type_, amount
                       in zip(coins_type, coins_amount)})
        expected = 2*200 + 10*100 + 5*50 + 1*20
        self.assertEqual(coins.value, expected)

    def test_coins_copy(self):
        coins = Coins({100: 2, 50: 4})
        copied_coins = copy.copy(coins)
        self.assertEqual(coins, copied_coins)
        self.assertIsNot(coins, copied_coins)

    # Just testing the alias. Since it's Counter implementation,
    # we can assume it works as expected
    def test_coins_add_in_place(self):
        coins_type = [200, 100, 50]
        coins_amount1 = [10, 2, 5]
        coins_amount2 = [2, 4, 3]
        coins = Coins({type_:amount for type_, amount
                       in zip(coins_type, coins_amount1)})
        coins2 = Coins({type_:amount for type_, amount
                       in zip(coins_type, coins_amount2)})
        coins.add(coins2)
        self.assertEqual(coins, Coins({type_:amount for type_, amount
                                       in zip(coins_type, [12, 6, 8])}))


    def test_compute_surplus(self):
        c = Coins({200: 1, 100: 1, 50: 2, 20: 1, 10:1 })
        change = c.compute_surplus(200)
        self.assertEqual(change.value, 230)

        c = Coins({200: 0, 20: 1, 50: 2, 100: 1, 10: 1})
        change = c.compute_surplus(200)
        self.assertEqual(change.value,30)

        c = Coins({200: 0, 20: 6, 50: 1, 100: 1, 10: 1})
        change = c.compute_surplus(200)
        self.assertEqual(change.value,80)

        c = Coins({200: 0, 20: 8, 50: 1, 100: 0, 10: 1})
        change = c.compute_surplus(200)
        self.assertEqual(change.value,20)

        c = Coins({200: 0, 20: 8, 50: 1, 100: 0, 10: 0})
        self.assertRaises(NoChangePossibleException, c.compute_surplus, 200)

        c = Coins({200: 0, 20: 4, 50: 0, 100: 0, 10: 0})
        change = c.compute_surplus(200)
        self.assertEqual(change, Coins())

    def test_compute_change(self):
        c = Coins({200: 0, 100: 1, 50: 100, 20: 100, 10:100})
        change = c.compute_change(200)
        self.assertEqual(change.value, 200)

    def test_compute_change_not_enough_cash(self):
        c = Coins({200: 0, 100: 1, 50: 0, 20: 0, 10: 0})
        self.assertRaises(NoChangePossibleException, c.compute_change, 200)

    def test_compute_change_impossible(self):
        c = Coins({200: 1, 100: 1, 50: 1, 20: 0, 10: 1})
        self.assertRaises(NoChangePossibleException, c.compute_change, 70)
