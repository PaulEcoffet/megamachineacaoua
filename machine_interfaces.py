class MachineFunc(object):

    def __init__(self, machine_factory):
        self.m = machine_factory

    def order(self, *args, **kwargs):
        return self.m.order(*args, **kwargs)

    @property
    def factory(self):
        return self.m

    def __repr__(self):
        return 'Machine à café en fonctionnement'


class MachineMaintenance(object):

    def __init__(self, machine_factory):
        self.m = machine_factory

    def edit_prices(self, **prices):
        self.m.edit_prices(**prices)

    def edit_stocks(self, **stocks):
        self.m.edit_stock(**stocks)

    def refill_stocks(self):
        self.m.refill_stocks()

    def edit_coins(self, coins):
        self.m.edit_coins()

    def refill_coins(self):
        self.m.refill_coins()

    @property
    def max_stocks(self):
        return self.m.max_stocks

    @property
    def max_coins(self):
        return self.m.max_coins

    @property
    def stocks(self):
        return self.m.stocks

    @property
    def coins(self):
        return self.m.coins

    @property
    def log(self):
        return self.m.log

    @property
    def pretty_log(self):
        return self.m.pretty_log

    @property
    def stock_prices(self):
        return self.m.stock_prices

    @property
    def coins(self):
        return self.m.coins

    @property
    def factory(self):
        return self.m

    def __repr__(self):
        return 'Machine à café en maintenance'
