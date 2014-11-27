% Rapport Mega Machine à Caoua
% Paul Ecoffet; Mathieu Seurin
% Vendredi 28 Novembre 2014


Nous allons ici détailler les fonctions utilisées dans notre programme (signature
et axiome) ainsi que faire l'analyse de leur complexité en notation **O**.
Après chaque méthode, nous indiquerons le fichier correspondant aux tests
que nous avons effectués, ainsi que les noms des tests.

# Fonctions de Machine, mode fonctionnement #

order : #TODO
---------
1. signature : $\text{(Monnaie, Commande)} \Rightarrow (Boisson \cup \emptyset \times \text{Monnaie})$
2. axiome :
3. Complexité : ON DOIT FAIRE LES AUTRES AVANT
4. Test : *test_machine.py*
	* test_order_simple()
	* test_order_complex()
	* test_order_fail_not_enough_cash()
	* test_order_fail_not_drink()
	* test_order_fail_no_stock()
	* test_order_cant_get_maxcash()


# Fonctions de Machine, mode Maintenance #

reset :
-------
1. signature : $\emptyset \Rightarrow \emptyset$
2. axiome :
	$$\text{machine.reset()} \Rightarrow
	\begin{cases}
		\text{machine.\_stocks[type]} = 0 & \forall \text{type} \in \text{machine.StocksType} \\
		\text{machine.\_coins[type]} = 0 & \forall \text{type} \in \text{machine.CoinssType} \\
		\text{machine.\_cash} = 0 &
	\end{cases}$$

edit_prices :
---------------
1. signature : $\text{(dictionnaire\_prix)} \Rightarrow \emptyset \cup \text{Error}$
2. axiome :
	* $\forall$ stock $\in$ \{'thé', 'café', 'lait', 'chocolat'\}, \
		$\forall$ prix $\geq$ 0\
		edit_prices(stock=prix) $\Rightarrow$ machine._stock_prices[stock] = prix

	* Si stock = 'sucre'
		$\forall$ 0 $\leq\text{prix}_i\leq\text{prix}_{i+1}$, i $\in$ $[0,3]$
			edit_prices(sucre= [$\text{prix}_i$]) \
			machine._stock_prices[stock] = [($\text{prix}_i$)] $\forall$i $\in$ [0,3]
3. Complexité : $O(n)$ avec n le nombre de produits payant
4. Test : *test_machine.py*
	* test_edit_prices

edit_stocks :
---------------
1. signature : $\text{(dictionnaire\_stocks)} \Rightarrow \emptyset \cup \text{Error}$
2. axiome :
	* $\forall$ stock $\in$ \{'thé', 'café', 'lait', 'chocolat', 'sucre'\}, \
		$\forall$ machine.quantite[stock] < quantite $\leq$  machine.quantite_max[stock] \
		machine.edit_stock(stock=quantite) $\Rightarrow$ machine.quantite[stock] = quantite

	* $\forall$ stock $\in$ \{'thé', 'café', 'lait', 'chocolat', 'sucre'\}, \
		$\forall$ quantite $\leq$ machine.quantite[stock] ou quantite > machine.quantite_max[stock] \
		machine.edit_stock(stock, quantite) $\Rightarrow$ machine.quantite[stock] = machine.quantite[stock]

3. Complexité : $O(n)$ avec n le nombre de stocks différents
4. Test : *test_machine.py*
	* test_edit_stocks

refill_stocks :
---------------  
1. signature : $\emptyset \Rightarrow \emptyset$
2. axiome :
	* $\forall$ stock $\in$ Machine.StocksType, \
	machine.refill_stock() $\Rightarrow$ machine.quantite[stock] \
	= machine.quantite_max[stock]
3. Complexité : $O(n)$ avec $n$ le nombre de stocks différents
4. Test : *test_machine.py*
	* test_edit_prices

edit_coins :
---------------
1. signature : $\text{coins}$ $\Rightarrow$ $\emptyset$
2. axiome :
	* $\forall$ pieces $\in$ machine.CoinsType et pieces $\in$ coins, \
		 $\forall$  0 $\leq$ coins[pieces] $\leq$ machine._max_coins[pieces] \
		edit_coins[coins] $\Rightarrow \text{machine.\_coins[pieces] = coins[pieces]},\ \forall \text{pieces}$
3. Complexité : $O(n)$ avec $n$ le nombre de types de pièces différentes gérées par la machine
4. Test : *test_machine.py*
	* test_edit_prices

refill_coins :
---------------
1. signature : $\emptyset \Rightarrow \emptyset$
2. axiome :
	* machine.refill_coins() $\Rightarrow$ $\forall$ valeur $\in$ Machine.CoinsType,\
		machine.coins[valeur] = machine.max_coins[valeur]
3. Complexité : $O(n)$ avec $n$ le nombre de types de pièces différents
4. Test : *test_machine.py*
	* test_edit_prices

remove_stocks :
------------------
1. signature : stock_dict $\Rightarrow \emptyset$
2.axiome :
	* $\forall$ A = $\text{(stock\_type, value)}_i$, $i \in \mathbb{N}$,
	  $\text{stock\_type}_i$ $\in$ Machine.StocksType \
		machine.remove(A) $\Rightarrow$ $\forall$ stock_type, value $\in A$,
		machine._stocks[stock_type] = machine._stocks[stock_type] - value

3. Complexité : $O(n)$ avec $n$ le nombre de types de stocks gérés par la machine
4. Test : *test_machine.py*
	* test_remove_stocks

add_to_cash :
-------------
1. signature: Coins $\Rightarrow \emptyset$
2. axiome :
	* $\forall \text{coins} \in \text{Coins}$, \
		machine.add_to_cash(coins) $\Rightarrow$ $\forall$ type, quantite $\in$ coins, \
		machine.cash[type] = machine.cash[type] + quantite

# Fonctions de Coins #
Coins hérite de collections.Counter.

compute_surplus
---------------
1. signature: value $\Rightarrow$ change $\in$ Coins $\cup$ NoChangePossibleException
2. axiome:
	* $\forall$ coins $in$ Coins, coins.value $\geq$ value, \
	$$\text{coins.compute\_surplus(x)} \Rightarrow
	\begin{cases}
		(\text{coins - change}).\text{value} = \text{value} &\text{if possible} \\
		\text{NoChangePossibleException} &\text{if impossible}
	\end{cases}
	$$
	* $\forall$ coins $in$ Coins, coins.value $\leq$ value, \
	coins.compute_surplus(x) $\Rightarrow$ NoChangePossibleException
3. complexité: $O(2^n)$, $n$ le nombre de pièces dans coins.
	
