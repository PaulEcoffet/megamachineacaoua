import copy
from logs import StockLog, CoinsLog, OrderLog, CashLog, EndOrderLog
from drink import Drink
from coins import Coins, NoChangePossibleException
from machine_interfaces import MachineFunc, MachineMaintenance


class InvalidOrderException(Exception): pass
class NotEnoughStockException(Exception): pass

class Machine(object):
    """
    Coffee machine out from factory. Can do anything. Should be put in
    maintenance or usage mode
    """

    MaxCashInput = 200
    CoinsType = [200, 100, 50, 20, 10, 5]
    CoinsContainers = [50, 20, 10, 5]
    StocksType = ['coffee', 'tea', 'chocolate', 'milk', 'sugar']
    DefaultPrices = {'coffee': 20, 'tea': 10, 'chocolate': 30,
                     'milk': 5, 'sugar': [0, 5, 15, 15]}

    def __init__(self, max_stocks=None, max_coins=None, stock_prices=None):
        if not max_stocks:
            self._max_stocks = {key: 100 for key in Machine.StocksType}
        if not max_coins:
            self._max_coins = Coins({key: 100 for key
                                     in Machine.CoinsContainers})
        if not stock_prices:
            self._stock_prices = copy.copy(Machine.DefaultPrices)
        self.reset()
        self._log = []

    def reset(self):
        """
        Reset the machine, keep the log
        """
        self._stocks = {key: 0 for key in Machine.StocksType}
        self._cash = Coins()
        self._coins = Coins({key:0 for key in Machine.CoinsContainers})

    def edit_prices(self, **prices):
        """
        Edit prices in the coffee machine.
        It allows the user to change the price of one or more products

        Usage:
        ```
        m.edit_prices(coffee=42, tea=30, chocolate=50)
        ```
        ```
        new_prices = {'coffee': 80, 'tea': 50, 'chocolate' : 42}
        m.edit_prices(**new_prices)

        Raises TypeError if prices is not numerical (or list for sugar)
        ```
        """
        for type_ in Machine.StocksType:
            try:
                new_val = prices[type_]
            except KeyError:
                pass
            else:
                if type_ == 'sugar':
                    if isinstance(new_val, list) and len(new_val) == 4:
                        valid = True
                        for i in range(0,3):
                            if not 0 <= new_val[i] <= new_val[i+1]:
                                valid = False
                                break
                        if valid:
                            self.stock_prices['sugar'] = new_val
                    else:
                        raise TypeError('Sugar must be a list of 4 digits')

                elif new_val > 0:
                    self.stock_prices[type_] = new_val

    def edit_stocks(self, **stocks):
        """
        Edit the stocks in the coffee machine.

        If the value is not possible ie less than current stock or over the
        stock limit, then this value is dismissed.

        Usage:
        ```
        m.edit_stocks(coffee=80, tea=50, chocolate=42)
        ```
        ```
        new_stocks = {'coffee': 80, 'tea': 50, 'chocolate' : 42}
        m.edit_stocks(**new_stocks)
        ```
        """
        prev_stocks = copy.copy(self.stocks)
        for type_ in Machine.StocksType:
            try:
                new_val = stocks[type_]
            except KeyError:
                pass
            else:
                if self.stocks[type_] < new_val <= self.max_stocks[type_]:
                    self.stocks[type_] = new_val
        self._log.append(StockLog(prev_stocks, self.stocks))

    def refill_stocks(self):
        """
        Fill all the stock containers to their max values.
        """
        self.edit_stocks(**self._max_stocks)

    def edit_coins(self, coins):
        """
        Change the number of coins available in containers.
        Doesn't change the number if the new value isn't
        between 0 and self._max_coins
        """
        prev_coins = copy.copy(self.coins)
        for type_ in Machine.CoinsType:
            try:
                new_val = coins[type_]
            except KeyError:
                pass
            else:
                if self.coins[type_] < new_val <= self.max_coins[type_]:
                    self.coins[type_] = new_val
        self._log.append(CoinsLog(prev_coins, self.coins))

    def refill_coins(self):
        """
        Fill all the coins containers to their max values.
        """
        self.edit_coins(self._max_coins)

    def _remove_stocks(self, **stocks):
        """
        Remove from the stock the amounts given in `stocks`.
        Doesn't prevent the stock to have a negative value. Be careful
        """
        prev_stocks = copy.copy(self.stocks)
        for type_ in Machine.StocksType:
            try:
                to_remove = stocks[type_]
            except KeyError:
                pass
            else:
                self.stocks[type_] -= to_remove
        self._log.append(StockLog(prev_stocks, self.stocks))


    def order(self, coins_in, command):
        """
        Return the order asked by the customer with his `command` if he has
        given enough money in `coins_in` to pay his drinks.

        Return a drink and the change if possible
        If coins_in > Machine.MaxCashInput, the program will reject coins until
        Machine.MaxCashInput is reached. If it's impossible, it will return all
        the change and no drink.

        Will raise `InvalidOrderException` if the order is invalid or if there
        isn't enough money to pay the drin.
        Will raise `NotEnoughStockException` if there isn't enough stock to
        fulfill the order.
        Will raise `coins.NoChangePossibleException` if there isn't enough
        money in stock to give change back.
        """
        drink = Drink(command, self.stock_prices)
        coins = Coins({key: amount for amount, key
                                   in zip(coins_in, Machine.CoinsType)})
        try:
            coins_out = coins.compute_surplus(Machine.MaxCashInput)
        except NoChangePossibleException:
            return None, copy.copy(coins)  # Abort if 2€ is impossible to get
        coins -= coins_out
        if not drink.has_beverage:
            raise InvalidOrderException('You need to choose a beverage')
        for item in drink.stocks:
            if self.stocks[item] - drink.stocks[item] < 0:
                raise NotEnoughStockException(
                        'Not enough {} in stock'.format(item))
        if coins.value < drink.price:
            raise InvalidOrderException('Not Enough change to pay the order')
        change = self.coins.compute_change(coins.value - drink.price)
        self._log.append(OrderLog(drink, coins))
        self.remove_change(change)
        coins_out += change
        self._remove_stocks(**drink.stocks)
        self.add_to_cash(coins)
        self._log.append(EndOrderLog())
        return drink, coins_out

    def add_to_cash(self, coins):
        """
        Add the Coins `coins` in the box with all the cash.
        It will be logged
        """
        prev = copy.copy(self._cash)
        self._cash.add(coins)
        self._log.append(CashLog(prev, self._cash))

    def remove_change(self, change):
        """
        Remove from the coins container enough money to give the amount `change`
        """
        prev_coins = copy.copy(self._coins)
        self._coins.subtract(change)
        self._log.append(CoinsLog(prev_coins, self._coins))

    @property
    def max_stocks(self):
        return self._max_stocks

    @property
    def max_coins(self):
        return self._max_coins

    @property
    def stocks(self):
        return self._stocks

    @property
    def coins(self):
        return self._coins

    @property
    def log(self):
        return self._log

    @property
    def pretty_log(self):
        return '\n'.join(str(log) for log in self._log)

    @property
    def stock_prices(self):
        return self._stock_prices

    @property
    def coins(self):
        return self._coins

    def __repr__(self):
        return 'Machine à café d\'usine'


# Run the tests on import (as asked in the specs)

import unittest

testsuite = unittest.defaultTestLoader.discover('.')
unittest.TextTestRunner().run(testsuite)
