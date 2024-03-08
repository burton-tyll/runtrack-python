L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

def suppr_doublons(liste):
	liste_simple = []
	for valeur in liste:
		if not valeur in liste_simple:
			liste_simple.append(valeur)
	return liste_simple


print(suppr_doublons(L))
