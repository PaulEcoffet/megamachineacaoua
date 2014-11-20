import copy

class InvalidOrderException(Exception): pass

class Machine(object):
    """
    Coffee machine out from factory. Can do anything. Should be put in
    maintenance or usage mode
    """

    CoinsType = [200, 100, 50, 20, 10]
    StocksType = ['coffee', 'tea', 'chocolate', 'milk', 'sugar']
    DefaultPrices = {'coffee': 20, 'tea': 10, 'chocolate': 30,
                     'milk': 5, 'sugar': [0, 5, 15, 15]}  # On peut aussi faire
                                                          # coffee: [0, 20]

    def __init__(self, max_stocks=None, max_coins=None, stock_price=None):
        if not max_stocks:
            self._max_stocks = {key: 100 for key in Machine.StocksType}
        if not max_coins:
            self._max_coins = {key: 100 for key in Machine.CoinsType}
        if not stock_price:
            self._stock_price = copy.copy(Machine.DefaultPrices)
        self._stocks = {key: 0 for key in Machine.StocksType}
        self._cash = {key: 0 for key in Machine.CoinsType}
        self._coins = {key: 0 for key in Machine.CoinsType}
        self._log = []
        self._prices = DefaultPrices

    def edit_prices(self, **prices):
        pass

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

    def parse_order(self, command):
        drink = {}
        drink['sugar'] = command[0] * 2 + command[1]
        drink['milk'] = command[2]
        if command[3]:
            drink['tea'] = 1
            drink['coffee'] = 0
            drink['chocolate'] = 0
        else:
            drink['tea'] = 0
            drink['coffee'] = command[4]
            drink['chocolate'] = command[5]
        return drink

    def order(self, command):
        drink = self.parse_order(command)
        if not drink['beverage']:
            raise InvalidOrderException('You need to choose a beverage')
        for key in self.stocks:
            pass # Test if enough stock or raise error            
        
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
    def prices(self):
        return self._prices

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
