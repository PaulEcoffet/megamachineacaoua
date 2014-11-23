class Drink(object):

    def __init__(self, command, prices):
        self.stock_prices = prices
        self.stocks = {}
        self.stocks['tea'] = 0
        self.stocks['coffee'] = 0
        self.stocks['chocolate'] = 0

        self.stocks['sugar'] = command[0] * 2 + command[1]
        self.stocks['milk'] = command[2]
        if command[3]:
            self.stocks['tea'] = 1
        else:
            self.stocks['coffee'] = command[4]
            self.stocks['chocolate'] = command[5]

    @property
    def price(self):
        total = 0
        for item in self.stocks:
            try:
                total += self.stocks[item]*self.stock_prices[item]
            except TypeError:
                total += self.stock_prices[item][self.stocks[item]]
        return total

    @property
    def has_beverage(self):
        return (self.stocks['tea'] > 0 or self.stocks['coffee'] > 0 or
                self.stocks['chocolate'] > 0)

    def __str__(self):
        message = 'A cup of '
        if self.stocks['tea']:
            message += 'tea'
        elif self.stocks['coffee'] and self.stocks['chocolate']:
            if self.stocks['milk']:
                message += 'macciato'
            else:
                message += 'cappucino'
        elif self.stocks['chocolate']:
            message += 'chocolate'
        elif self.stocks['coffee']:
            message += 'coffee'
        else:
            message = 'hot water'
        if self.stocks['milk'] and not (self.stocks['coffee'] and
                self.stocks['chocolate']):
            message += ' with milk '
            if self.stocks['sugar']:
                message += 'and '
        if self.stocks['sugar']:
            message += str(self.stocks['sugar']) + ' sugars'
        message += '.'
        return message
