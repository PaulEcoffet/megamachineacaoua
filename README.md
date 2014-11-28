Mega Machine à Café
===================

Exemple d'utilisation de la *Méga Machine à Café*:

```
>>> import machine
..................................
----------------------------------------------------------------------
Ran 34 tests in 0.012s

OK
>>> m = machine.Machine()
>>> f = machine.MachineFunc(m)
>>> maintenance = machine.MachineMaintenance(f.factory)
>>> maintenance.refill_coins()
>>> maintenance.refill_stocks()
>>> drink, coins = f.order((0,0,1,1,4), (1,1,0,0,1,1))
>>> str(drink)
'A cup of cappucino with 3 sugars'
>>> coins
Coins({20: 2, 5: 1})

>>> maintenance.order((0,0,1,1,4), (1,1,0,0,1,1))  # machine en maintenance ne peut rien commander
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'MachineMaintenance' object has no attribute 'order'

>>> maintenance.stocks
{'milk': 100, 'sugar': 97, 'coffee': 99, 'tea': 100, 'chocolate': 99}
>>> maintenance.edit_stocks(sugar=50)
>>> maintenance.stocks
{'milk': 100, 'sugar': 97, 'coffee': 99, 'tea': 100, 'chocolate': 99}
>>> maintenance.edit_stocks(sugar=100)
>>> maintenance.stocks
{'milk': 100, 'sugar': 100, 'coffee': 99, 'tea': 100, 'chocolate': 99}
>>> print(maintenance.pretty_log)
[42 Jan 42:42:37] Coins Update: 5: 0 -> 100 (+100), 10: 0 -> 100 (+100), 20: 0 -> 100 (+100), 50: 0 -> 100 (+100)
[42 Jan 42:42:40] Stock Update: chocolate: 0 -> 100 (+100), coffee: 0 -> 100 (+100), milk: 0 -> 100 (+100), sugar: 0 -> 100 (+100), tea: 0 -> 100 (+100)
[42 Jan 42:42:42] ** Order **: A cup of cappucino with 3 sugars which cost 65, the customer gave 110
[42 Jan 42:42:42] Coins Update: 5: 100 -> 99 (-1), 10: 100 -> 100 (+0), 20: 100 -> 98 (-2), 50: 100 -> 100 (+0)
[42 Jan 42:42:42] Stock Update: chocolate: 100 -> 99 (-1), coffee: 100 -> 99 (-1), milk: 100 -> 100 (+0), sugar: 100 -> 97 (-3), tea: 100 -> 100 (+0)
[42 Jan 42:42:42] Cash Update: 0 -> 110 (+110)
[42 Jan 42:42:42] ** End of the order **: That's all folks
[42 Jan 42:42:46] Stock Update: chocolate: 99 -> 99 (+0), coffee: 99 -> 99 (+0), milk: 100 -> 100 (+0), sugar: 97 -> 97 (+0), tea: 100 -> 100 (+0)
[42 Jan 42:42:47] Stock Update: chocolate: 99 -> 99 (+0), coffee: 99 -> 99 (+0), milk: 100 -> 100 (+0), sugar: 97 -> 100 (+3), tea: 100 -> 100 (+0)
```
