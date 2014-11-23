import unittest
from machine import Machine
from coins import Coins
import copy

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
        stock = copy.deepcopy(mc.stocks)
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

    @unittest.skip
    def test_parse_order(self):
        mc = Machine()
        drink = {'milk': 1, 'sugar': 3, 'coffee': 1, 'tea': 0, 'chocolate':0}
        self.assertEqual(mc.parse_order((1,1,1,0,1,0)), drink)

        drink = {'milk': 0, 'sugar': 0, 'coffee': 0, 'tea': 0, 'chocolate':0}
        self.assertEqual(mc.parse_order((0,0,0,0,0,0)), drink)

        drink = {'milk': 0, 'sugar': 0, 'tea': 1, 'coffee': 0, 'chocolate':0}
        self.assertEqual(mc.parse_order((0,0,0,1,1,1)), drink)

        drink = {'milk': 0, 'sugar': 0, 'tea': 0, 'coffee': 1, 'chocolate':1}
        self.assertEqual(mc.parse_order((0,0,0,0,1,1)), drink)


    def test_edit_prices(self): #TODO need to test sugar
        mc = Machine()

        prices = copy.deepcopy(mc.stock_prices)
        prices['coffee'] = 30
        mc.edit_prices(coffee=30)
        self.assertEqual(mc.stock_prices,prices)

        mc.edit_prices(coffee=-10)
        self.assertEqual(mc.stock_prices,prices)

        prices['coffee'] = 40
        prices['tea'] = 20
        mc.edit_prices(coffee=40,tea=20)
        self.assertEqual(mc.stock_prices,prices)
