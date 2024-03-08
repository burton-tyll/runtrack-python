L = [7, 19, 3, 12, 109, 1]

def croissant(liste):
	while not liste[0]==min(liste):
		p=0
		while p < len(liste)-1:
			if liste[p] > liste[p+1]:
				liste[p], liste[p+1] = liste[p+1], liste[p]
			p+=1
	return liste


print(croissant(L))




