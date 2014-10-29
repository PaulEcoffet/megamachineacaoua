import unittest
from machine import Machine


class MachineTestCase(unittest.TestCase):
    """
    Test for MMC, to test use in cmd : python3 -m unittest test_XXXXX.py
    """

    def test_init_in_maintenance(self):
        mc = Machine()
        self.assertTrue(mc.maintenance)

    def test_init_default_maxstock(self):
        mc = Machine()
        for name, max_stock in mc.max_stock.items():
            self.assertEqual(max_stock, 100)

    def test_init_default_maxcoins(self):
        mc = Machine()
        for value, max_coins in mc.max_coins.items():
            self.assertEqual(max_coins, 100)

    def test_init_empty_stocks(self):
        mc = Machine()
        for name, stock in mc.stock.items():
            self.assertEqual(stock, 0)

    def test_init_empty_coins(self):
        mc = Machine()
        for value, stock in mc.coins.items():
            self.assertEqual(stock, 0)

    def test_init_empty_log(self):
        mc = Machine()
        self.assertEqual(mc.log, [])  # TODO log d'initialisation?
