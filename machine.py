class WrongModeException(Exception): pass

class Machine(object):
    """
    Machine à café doc bla bla
    """

    def __init__(self, stocks_max):
        self._maintenance = True
        self._stocks_max = stocks_max


    def edit_stocks(self, stocks):
        pass
