class WrongModeException(Exception): pass

class Machine(object):
    """
    Machine's docs string, need to be filled
    """

    def __init__(self, stocks_max):
        self._maintenance = True
        self._stocks_max = stocks_max


    def edit_stocks(self, stocks):
        pass

class Order(object):
    """
    Order's docs string, need to be filled
    """

    def __init__(self, base,supp_choco=False,supp_milk=False,supp_sugar=0): #need setter, getter
        self.drink = Drink(base, supp_choco, supp_milk, supp_sugar)
        self._aMoney = []

class Drink(object):
    """
    Drink's docs string, need to be filled
    """

    def __init__(self, base,supp_choco=False,supp_milk=False,supp_sugar=0):
        self.base = base
        self.supp_choco = supp_choco
        self.supp_milk = supp_milk
        self.supp_sugar = supp_sugar
        self.price = cal_price()

    def cal_price(self):
        pass
