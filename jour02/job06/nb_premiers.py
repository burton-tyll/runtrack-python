# Déterminer si un nombre est un nombre premier
# Strictement supérieur ou égal à 2 (>=2)
# Divisible par lui meme (ex: 1%1==0)
# Non divisible par le reste (ex: 10%reste!=0)

# Afficher chaque élément de la liste
# for cle in nombres:
#     # print(cle)


# -----------------CREATION DE LA FONCTION CHIFFRE_PREMIER----------
def is_prime(nb):
	if nb < 2:
		return False

	for d in range(2, nb):
		if nb % d==0:
			return False
	return True

# --------------AFFICHAGE LISTE------------

for chiffre in range(0, 1000):
	if is_prime(chiffre)== True:
		print(chiffre, "est un nombre premier")













