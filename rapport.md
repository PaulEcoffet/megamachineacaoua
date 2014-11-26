% Rapport Mega Machine à Caoua
% Paul Ecoffet; Mathieu Seurin
% Vendredi 28 Novembre 2014


Nous allons ici détailler les fonctions utilisées dans notre programme (signature et
axiome) ainsi que faire l'analyse de leur complexité en notation Grand-O
Après chaque fonction, nous indiquerons le fichier correspondant au(x) test(s)
que nous avons effectué, ainsi que les noms des tests.

# Fonctions de Machine, mode fonctionnement #

* order :
	1. signature : $\text{(Monnaie, Commande)} \Rightarrow (Boisson \cup \emptyset \times Monnaie)$
	2. axiome : $  $
	3. Complexité : ON DOIT FAIRE LES AUTRES AVANT
	4. Test : *test_machine.py*
		* test_order_simple()
		* test_order_complex()
		* test_order_fail_not_enough_cash()
		* test_order_fail_not_drink()
		* test_order_fail_no_stock()
		* test_order_cant_get_maxcash()


# Fonctions de Machine, mode Maintenance #

* edit_prices :
	1. signature :$\text{(dictionnaire\_prix)} \Rightarrow \emptyset \cup \text{Error}$
	2. axiome : $$
	3. Complexité :
	4. Test : test_machine.py
		* test_edit_prices

* edit_stocks :
	1. signature :
	2. axiome :
	3. Complexité :
	4. Test : test_machine.py - test_edit_stocks

* refill_stocks :
	1. signature :
	2. axiome :
	3. Complexité :
	4. Test : test_machine.py - test_edit_prices

* edit_coins :
	1. signature :
	2.axiome :
	3. Complexité :
	4. Test : test_machine.py - test_edit_prices

* refill_coins :
	1. signature :
	2.axiome :
	3. Complexité :
	4. Test : test_machine.py - test_edit_prices

* _remove_stocks :
	1. signature :
	2.axiome :
	3. Complexité :
	4. Test : test_machine.py - test_edit_prices

# Fonctions de Coins #
