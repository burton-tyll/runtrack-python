

def arrondi(liste):
	i=0
	for nb in liste:
		liste[i] = int(liste[i])
		i+=1
	return liste


def longueur(liste):
	compteur = 0
	for nb in liste:
		compteur+=1
	return(compteur)


def croissant(liste):
	for nb in liste:
		i=0
		while i < longueur(liste)-1:
			while liste[i] > liste[i+1]:
				p=0
				while p < longueur(liste)-1:
					if liste[p] > liste[p+1]:
						liste[p], liste[p+1] = liste[p+1], liste[p]
					p+=1
			i+=1

	return liste

L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

print(arrondi(croissant(L)))



