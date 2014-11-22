class Drink(object):

    def __init__(self, command, price):
        self.price = price
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
            total += self.stocks[item]*self.price[item]
        return total

    @property
    def has_beverage(self):
        return (self.stocks['tea'] > 0 or self.stocks['coffee'] > 0 or
                self.stocks['chocolate'] > 0)
