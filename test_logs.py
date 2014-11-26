import unittest
import copy
import time

from coins import Coins
from drink import Drink

from logs import Log, StockLog, CoinsLog, OrderLog, EndOrderLog, CashLog

prev_stock = {'coffee': 40, 'tea': 20, 'sugar': 0, 'chocolate': 4,
              'milk': 3}
new_stock = {'coffee': 30, 'tea': 40, 'sugar': 0, 'chocolate': 14,
             'milk': 0}

prev_coins = Coins({5: 10, 10: 3})
new_coins = Coins({5: 5, 10: 4})

stock_prices = {'coffee': 20, 'tea': 10, 'chocolate': 30,
                'milk': 5, 'sugar': [0, 5, 15, 15]}

class LogTestCase(unittest.TestCase):

    def test_log(self):
        log = Log('Gibi')
        ftime =  time.strftime('%d %b %H:%M:%S', log.time)
        self.assertEqual(str(log), '[' + ftime + '] General Log: Gibi')

    def test_stock_log_no_changes(self):
        new_stock_modif = copy.deepcopy(new_stock)
        new_stock_no_modif = copy.deepcopy(new_stock)
        log = StockLog(prev_stock, new_stock_modif)
        new_stock_modif = 'Yolo'
        self.assertEqual(log.cur_stock, new_stock_no_modif)

    def test_stock_log_message(self):
        log = StockLog(prev_stock, new_stock)
        message = 'chocolate: 4 -> 14 (+10), coffee: 40 -> 30 (-10), '
        message += 'milk: 3 -> 0 (-3), sugar: 0 -> 0 (+0), tea: 20 -> 40 (+20)'
        self.assertEqual(log.message, message)

    def test_stock_log_str(self):
        log = StockLog(prev_stock, new_stock)
        message = 'chocolate: 4 -> 14 (+10), coffee: 40 -> 30 (-10), '
        message += 'milk: 3 -> 0 (-3), sugar: 0 -> 0 (+0), tea: 20 -> 40 (+20)'
        ftime =  time.strftime('%d %b %H:%M:%S', log.time)
        self.assertEqual(str(log), '[' + ftime + '] Stock Update: ' + message)

    def test_coins_log_message(self):
        log = CoinsLog(prev_coins, new_coins)
        message = '5: 10 -> 5 (-5), 10: 3 -> 4 (+1)'
        self.assertEqual(log.message, message)

    def test_order_log_message(self):
        drink = Drink((0, 1, 0, 1, 0, 0), stock_prices)
        coins = Coins({100: 1, 50: 1, 20: 1})
        log = OrderLog(drink, coins)
        message = 'A cup of tea with 1 sugars which cost 15, the customer gave 170'
        self.assertEqual(log.message, message)

    def test_end_order_log_message(self):
        log = EndOrderLog()
        ftime =  time.strftime('%d %b %H:%M:%S', log.time)
        self.assertEqual(str(log),
            '['+ ftime + '] ** End of the order **: That\'s all folks')

    def test_cash_log_message(self):
        log = CashLog(prev_coins, new_coins)
        message = '80 -> 65 (-15)'
        self.assertEqual(log.message, message)
