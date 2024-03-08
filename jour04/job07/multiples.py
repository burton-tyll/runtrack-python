L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]

# Je défini une fonction capable de reconnaître un multiple de 3


def multiple(nb, liste):
	i=0
	for cle in liste:
		if cle % nb==0:
			print(f"{cle} est un multiple de 3")
			i+=1
		else:
			pass
	else:
		print("\n__________________________________________\n")
		print(f"Il y a {i} multiples de {nb} dans la liste")

print(multiple(3, L))






