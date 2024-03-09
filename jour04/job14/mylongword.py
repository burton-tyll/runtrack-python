
BreakingBad = "Je ne suis pas en danger Skyler, c'est moi le danger. Si quelqu'un ouvre sa porte et se fait descendre tu crois que ce sera moi?! Non, je suis l'homme qui frappe à la porte! "


# ---------------------------On créé une fonction len------------------------------

def longueur(chaine):
	compteur = 0
	for _ in chaine:
		compteur+=1
	return(compteur)

# ---------------------------On créé une fonction split------------------------

def split(chaine):
	liste = []
	mot = ""
	for lettre in chaine:
		if lettre != " ":
			mot += lettre
		else:
			liste += [mot]
			mot = ""
	return liste

# --------------On utilise les fonctions split et len dans la fonction my_long_word----------------

def my_long_word(nb, chaine):
	phrase = ""
	for mot in split(chaine):
		if longueur(mot) > nb:
			phrase += mot+" "
	return phrase


# ----------------On affiche le résultat-----------------------------

print(my_long_word(2, BreakingBad))




