from collections import Counter
import copy

class Coins(Counter):
    """
    Class that represents Coins

    Usage:
    ```
    > coins = Coins({200: 0, 100: 2, 50: 4, 20: 3, 10: 1})
    > coins.value
    470

    > coins2 = Coins({200:0, 100:0, 50:0, 20:2, 10:0})
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
    def __init__(self, coins=None):
        """
        Create a Coin object, expect a dict of coins or a list of coins.
        If no argument is given, the coins object is empty

        Usage:
        ```
        > Coins({200:2, 100:5})
        Coins({200:2, 100:5})
        > Coins([200, 200, 100, 100, 100, 100, 100])
        Coins({200:2, 100:5})
        > Coins()
        Coins()
        ```
        """
        if coins:
            if isinstance(coins, dict):
                if (all(isinstance(key, int) for key in coins)
                        and all(isinstance(value, int)
                                for value in coins.values())):
                    super().__init__(coins)
                else:
                    raise ValueError('Coins works only with integers')
            elif isinstance(coins, list):
                if all(isinstance(value, int) for value in coins):
                    super().__init__(coins)
                else:
                    raise ValueError('Coins works only with integers')
            else:
                raise ValueError('Coins works only with integers')
        else:
            super().__init__()

    def compute_surplus(self, change_value):
        """
        Return the amount that exceed 'change_value', if possible

        How to use:

        > coins.Compute_change(200)
        Coins({200:0, 100:1, 50:2, 20:0, 10:0})
        """
        temp = copy.copy(self)
        value = list(self.keys())

        if self.value <= change_value:
            return Coins()

        cost = self.value - change_value
        i = 0
        save = (temp,i)
        saves_a = []

        while True:
            while temp.value > cost and i < len(value):
                if temp[value[i]] >= 1:
                    save = (copy.copy(temp), copy.copy(i))
                    saves_a.append(save)
                i += 1

            if temp.value == cost:
                return temp

            if not saves_a:
                raise Exception

            temp , i = saves_a.pop(len(saves_a)-1)
            temp[value[i]] -= 1

    def compute_change(self, change_value):
        """
        Compute coins so as too reach `change_value`, if possible
        """
        if change_value > self.value:
            raise Exception # Need a more explicit exception
        coins_out = Coins()
        for key in sorted(list(self.keys()), reverse=True):
            coins_out[key] = min(change_value // key, self[key])
            change_value -= coins_out[key]*key
            if change_value == 0:
                break
        if change_value != 0:
            raise Exception("Cannot give money for this amount") # TODO Not explicit
        return coins_out

    @property
    def value(self):
        """
        Return the sum of the values of all the coins in the object

        Usage:
        ```
        > c = Coins({100: 4, 50: 1})
        > c.value
        450
        ```
        """
        total = 0
        for value, amount in self.items():
            total += value * amount
        return total

    add = Counter.update  # Update for addition is not clear, addition of
                          # add for symetry with subtract
