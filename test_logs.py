import unittest
import copy
import time

from logs import Log, StockLog

prev_stock = {'coffee': 40, 'tea': 20, 'sugar': 0, 'chocolate': 4,
              'milk': 3}
new_stock = {'coffee': 30, 'tea': 40, 'sugar': 0, 'chocolate': 14,
             'milk': 0}

class LogTestCase(unittest.TestCase):

    def test_log(self):
        log = Log('Gibi')
        ftime =  time.strftime('%a %d %b %H:%M:%S', log.time)
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
        ftime =  time.strftime('%a %d %b %H:%M:%S', log.time)
        self.assertEqual(str(log), '[' + ftime + '] Stock Update: ' + message)
