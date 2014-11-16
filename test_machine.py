import unittest
from machine import Machine


class MachineTestCase(unittest.TestCase):
    """
    Test for MMC, to test use in cmd: python.exe -m unittest test_XXXXX.py
                             in bash: python3 -m unittest test_XXXXX.py
    """

    def test_init_default_maxstock(self):
        mc = Machine()
        for key in Machine.StocksType:
            self.assertEqual(mc.max_stocks[key], 100)

    def test_init_default_maxcoins(self):
        mc = Machine()
        for key in Machine.CoinsType:
            self.assertEqual(mc.max_coins[key], 100)

    def test_init_empty_stocks(self):
        mc = Machine()
        for key in Machine.StocksType:
            self.assertEqual(mc.stocks[key], 0)

    def test_init_empty_coins(self):
        mc = Machine()
        for key in Machine.CoinsType:
            self.assertEqual(mc.coins[key], 0)

    def test_init_empty_log(self):
        mc = Machine()
        self.assertEqual(mc.log, [])  # TODO log d'initialisation?

    def test_edit_stocks(self):
        mc = Machine()
        stock = mc.stocks
        mc.edit_stocks(coffee=50)
        stock['coffee'] = 50
        self.assertEqual(mc.stocks, stock)
        mc.edit_stocks(coffee=49)
        self.assertEqual(mc.stocks, stock)
        mc.edit_stocks(coffee=mc.max_stocks['coffee']+1)
        self.assertEqual(mc.stocks, stock)
        mc.edit_stocks(coffee=mc.max_stocks['coffee'])
        stock['coffee'] = mc.max_stocks['coffee']
        self.assertEqual(mc.stocks, stock)
