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
        str_time = time.strftime('%d %b %H:%M:%S', self.time)
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
                diff=self.cur_stock[key]-self.prev_stock[key]))
        message = ', '.join(items)
        return message


class CoinsLog(StockLog):
    """
    Log the coins operations.
    """

    def __init__(self, prev_coins, cur_coins):
            super().__init__(prev_coins, cur_coins)
            self.type = 'Coins Update'


class OrderLog(Log):
    """Drink Log"""

    def __init__(self, drink, coins_in):
        super().__init__()
        self.type = '** Order **'
        self.drink = copy.copy(drink)
        self.coins = copy.copy(coins_in)

    @property
    def message(self):
        message = str(self.drink) + ' which cost ' + str(self.drink.price)
        message += ', the customer gave ' + str(self.coins.value)
        return message


class EndOrderLog(Log):
    """
    Explicit the end of an order and the logs linked to it.
    """

    def __init__(self):
        super().__init__()
        self.type = '** End of the order **'

    @property
    def message(self):
        return "That's all folks"


class CashLog(Log):
    """
    Log the cash update.
    """

    def __init__(self, previous, current):
        super().__init__()
        self.type = 'Cash Update'
        self.previous = copy.copy(previous)
        self.current = copy.copy(current)

    @property
    def message(self):
        return '{prev} -> {new} ({diff:+d})'.format(prev=self.previous.value,
            new=self.current.value,
            diff=self.current.value-self.previous.value)
