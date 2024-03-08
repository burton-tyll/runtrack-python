L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]

def pair(liste):
	i=0
	for nb in liste:
		if nb % 2==0:
			i+=1
			print(nb)
		else:
			pass
	else:
		print(f"\n______________________________________\n")
		print(f"Il y a {i} nombres pairs dans la liste")

pair(L)