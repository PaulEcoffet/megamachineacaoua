import copy
import time

class Log(object):
    """General log class"""

    def __init__(self, message=''):
        self.type = 'General Log'
        self.time = time.localtime()
        self._message = message

    @property
    def message(self):
        return self._message

    def __str__(self):
        str_time = time.strftime('%a %d %b %H:%M:%S', self.time)
        return '[' + str_time + '] ' + self.type + ': ' + self.message

class StockLog(Log):
    """Log Stock edition"""

    def __init__(self, prev_stock, cur_stock):
        super().__init__()
        self.type = 'Stock Update'
        self.prev_stock = copy.deepcopy(prev_stock)
        self.cur_stock = copy.deepcopy(cur_stock)

    @property
    def message(self):
        items = []
        for key in sorted(self.prev_stock):
            items.append('{key}: {prev} -> {new} ({diff:+d})'.format(
                key=key, prev=self.prev_stock[key], new=self.cur_stock[key],
                diff=self.cur_stock[key]-self.prev_stock[key]
            ))
        message = ', '.join(items)
        return message

class CoinsLog(StockLog):
    pass
