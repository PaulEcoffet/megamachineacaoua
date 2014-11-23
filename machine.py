import copy
from logs import StockLog
from drink import Drink
from coins import Coins


class InvalidOrderException(Exception): pass

class Machine(object):
    """
    Coffee machine out from factory. Can do anything. Should be put in
    maintenance or usage mode
    """

    MaxCashInput = 200
    CoinsType = [200, 100, 50, 20, 10]
    StocksType = ['coffee', 'tea', 'chocolate', 'milk', 'sugar']
    DefaultPrices = {'coffee': 20, 'tea': 10, 'chocolate': 30,
                     'milk': 5, 'sugar': [0, 5, 15, 15]}  # On peut aussi faire
                                                          # coffee: [0, 20]

    def __init__(self, max_stocks=None, max_coins=None, stock_prices=None):
        if not max_stocks:
            self._max_stocks = {key: 100 for key in Machine.StocksType}
        if not max_coins:
            self._max_coins = Coins({key: 100 for key in Machine.CoinsType})
        if not stock_prices:
            self._stock_prices = copy.copy(Machine.DefaultPrices)
        self._stocks = {key: 0 for key in Machine.StocksType}
        self._cash = Coins({key:0 for key in Machine.CoinsType})
        self._coins = Coins({key:0 for key in Machine.CoinsType})
        self._log = []

    def edit_prices(self, **prices): # TODO SUGAR NOT WORKING WITH THIS CODE
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
        ```
        """
        for type_ in Machine.StocksType:
            try:
                new_val = prices[type_]
            except KeyError:
                pass
            else:
                if new_val > 0:
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
        prev_stocks = self.stocks
        for type_ in Machine.StocksType:
            try:
                new_val = stocks[type_]
            except KeyError:
                pass
            else:
                if self.stocks[type_] < new_val <= self.max_stocks[type_]:
                    self.stocks[type_] = new_val
        self._log.append(StockLog(prev_stocks, self.stocks))


    def order(self, command, coins_in):
        drink = Drink(command, self.stock_price)
        coins = Coins(coins_in, Machine.CoinsType)
        coins_out = self.compute_change(coins, Machine.MaxCashInput)
        coins.subtract(coins_out)
        if coins.value == 0:
            return None, coins_out  # Give all the cash
        if not drink.has_beverage:
            raise InvalidOrderException('You need to choose a beverage')
        for item in drink.stocks:
            if self.stocks[item] - drink.stocks[item] < 0:
                raise NotEnoughStockException(
                        'Not enough {} in stock'.format(item))
        if coins.value < drink.price:
            raise InvalidOrderException('Not Enough change to pay the order')
        coins_out.add(self.give_change(coins, drink.price))
        self.add_to_cash(coins.subtract(coins_out))
        self.remove_stock(drink.stocks)
        return drink, coins_out

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
    def stock_prices(self):
        return self._stock_prices

    def __repr__(self):
        return 'Machine à café d\'usine'



class MachineFunc(object):

    def __init__(self, machine_factory):
        self.m = machine_factory

    def edit_stock(self, *args, **kwargs):
        raise NotImplemented()

    def order(self, *args, **kwargs):
        return self.m.order(*args, **kwargs)

    @property
    def fact(self):
        return self.m
