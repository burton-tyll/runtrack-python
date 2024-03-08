L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

def mult(liste):
	produit = 1
	for nb in liste:
		if 25 <= nb <= 90:
			produit *= nb
	return produit


print(mult(L))
