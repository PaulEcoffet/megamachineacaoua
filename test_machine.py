import unittest
from machine import Machine, InvalidOrderException, NotEnoughStockException
from drink import Drink
from coins import Coins, NoChangePossibleException
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
        for key in Machine.CoinsContainers:
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
        self.assertEqual(mc._stocks, stock)
        mc.edit_stocks(coffee=49)
        self.assertEqual(mc.stocks, stock)
        mc.edit_stocks(coffee=mc.max_stocks['coffee']+1)
        self.assertEqual(mc.stocks, stock)
        mc.edit_stocks(coffee=mc.max_stocks['coffee'])
        stock['coffee'] = mc.max_stocks['coffee']
        self.assertEqual(mc.stocks, stock)

        mc = Machine()
        mc.refill_stocks()
        self.assertEqual(mc.stocks, mc.max_stocks)

    @unittest.skip  # Should be move in test_drink
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


    def test_edit_prices(self):
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

        prices['sugar'] = [5,5,15,20]
        mc.edit_prices(sugar=[5,5,15,20])
        self.assertEqual(mc.stock_prices,prices)

        mc.edit_prices(sugar=[10,5,15,20])
        self.assertEqual(mc.stock_prices,prices)

        mc.edit_prices(sugar=[-10,5,15,20])
        self.assertEqual(mc.stock_prices,prices)

    def test_order_simple(self):
        mc = Machine()
        mc.refill_stocks()
        mc.refill_coins()
        coins_stock = copy.copy(mc.coins)

        drink, change = mc.order((0,0,0,0,1,0), (0,1,0,0,0))
        self.assertEqual(drink.stocks, Drink((0,0,0,0,1,0),
                                              mc.stock_prices).stocks)
        self.assertEqual(change.value, 80)
        self.assertEqual(mc.stocks, {'milk': 100, 'sugar':100, 'tea': 100,
                                     'coffee': 99, 'chocolate': 100})
        self.assertEqual(mc._cash.value, 100)
        self.assertEqual(mc.coins.value, coins_stock.value - change.value)

    def test_order_complex(self):
        mc = Machine()
        mc.refill_stocks()
        mc.refill_coins()
        coins_stock = copy.copy(mc.coins)

        drink, change = mc.order((1,1,1,0,1,1), (1,1,0,0,0))
        expected = Drink((1,1,1,0,1,1), mc.stock_prices)
        self.assertEqual(drink.stocks, expected.stocks)
        self.assertEqual(change.value, 300 - expected.price)
        self.assertEqual(mc.stocks, {'milk': 99, 'sugar':97, 'tea': 100,
                                     'coffee': 99, 'chocolate': 99})
        self.assertEqual(mc._cash.value, 200)
        # + 100 for next line because 100 is from user coins input
        self.assertEqual(mc.coins.value, coins_stock.value - change.value + 100)
        print(mc.pretty_log)

    def test_order_fail_not_enough_cash(self):
        mc = Machine()
        mc.refill_stocks()
        mc.refill_coins()
        coins_stock = copy.copy(mc.coins)

        self.assertRaises(InvalidOrderException, mc.order,(1,1,1,0,1,1),
                          (0,0,0,1,0))
        self.assertEqual(mc.stocks, {'milk': 100, 'sugar':100, 'tea': 100,
                                     'coffee': 100, 'chocolate': 100})
        self.assertEqual(mc._cash.value, 0)
        # + 100 for next line because 100 is from user coins input
        self.assertEqual(mc.coins.value, coins_stock.value)

    def test_order_fail_not_drink(self):
        mc = Machine()
        mc.refill_stocks()
        mc.refill_coins()
        coins_stock = copy.copy(mc.coins)

        self.assertRaises(InvalidOrderException, mc.order,(1,0,1,0,0,0),
                          (0,0,0,1,0))
        self.assertEqual(mc.stocks, {'milk': 100, 'sugar': 100, 'tea': 100,
                                     'coffee': 100, 'chocolate': 100})
        self.assertEqual(mc._cash.value, 0)
        # + 100 for next line because 100 is from user coins input
        self.assertEqual(mc.coins.value, coins_stock.value)

    def test_order_fail_no_stock(self):
        mc = Machine()
        mc.refill_coins()
        coins_stock = copy.copy(mc.coins)

        self.assertRaises(NotEnoughStockException, mc.order,(1,0,1,1,0,0),
                          (0,0,0,1,0))
        self.assertEqual(mc.stocks, {'milk': 0, 'sugar': 0, 'tea': 0,
                                     'coffee': 0, 'chocolate': 0})
        self.assertEqual(mc._cash.value, 0)
        # + 100 for next line because 100 is from user coins input
        self.assertEqual(mc.coins.value, coins_stock.value)

    def test_order_cant_get_maxcash(self):
        mc = Machine()
        mc.refill_stocks()
        mc.refill_coins()
        coins_stock = copy.copy(mc.coins)
        drink, change = mc.order((1,1,1,0,1,1), (0,0,1,8,0))
        self.assertIsNone(drink)
        self.assertEqual(change, Coins({200:0, 100: 0, 50:1, 20:8, 10: 0}))
        self.assertEqual(mc.stocks, {'milk': 100, 'sugar': 100, 'tea': 100,
                                     'coffee': 100, 'chocolate': 100})
        self.assertEqual(mc._cash.value, 0)
        # + 100 for next line because 100 is from user coins input
        self.assertEqual(mc.coins.value, coins_stock.value)

    def test_order_cant_give_money_back(self):
        mc = Machine()
        mc.refill_stocks()
        self.assertRaises(NoChangePossibleException, mc.order,(0,0,0,0,1,0),
                          (0,1,0,0,0))
