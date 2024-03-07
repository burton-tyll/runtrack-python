def pairimpair(a):
	if a > 0:
		if a % 2 ==0:
			print(f"{a} est un nombre pair")
		else:
			print(f"{a} est un nombre impair")

	else: print("Veuillez entrer un nombre entier/positif")


pairimpair(2)

pairimpair(3)

pairimpair(19)

pairimpair(30)