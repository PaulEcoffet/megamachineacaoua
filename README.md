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
>>>
```
