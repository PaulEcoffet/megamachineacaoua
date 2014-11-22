from collections import Counter

class Coins(Counter):
    """
    Class that represents Coins

    Usage:
    ```
    > coins = Coins([0, 2, 4, 3, 1], [200, 100, 50, 20, 10])
    > coins.value
    470

    > coins2 = Coins([0, 0, 0, 2, 0], [200, 100, 50, 20, 10])
    > coins + coins2
    Coins({200:0, 100:2, 50:4, 20:5, 10:1})

    > coins - coins2
    Coins({200:0, 100:2, 50:4, 20:1, 10:1})
    ```
    Warning: Negative coins amount is not forbidden (yet)

    In place addition and subtraction are also allowed
    ```
    > coins.add(coins2)
    > coins
    Coins({200:0, 100:2, 50:4, 20:5, 10:1})

    ```
    """
    def __init__(self, coins, coins_type):
        super().__init__({value: amount for value, amount
                          in zip(coins_type, coins)})

    @property
    def value(self):
        total = 0
        for value, amount in self.items():
            total += value * amount
        return total

    add = Counter.update  # Update for addition is not clear, addition of
                          # add for symetry with subtract
