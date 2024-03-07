type = input("choisissez un type entre 'fruits' et 'légumes': ")
saison = input("choisissez une saison: ")

def primeur(type, saison):
	if type=="fruits" and saison=="hiver":#...
		print("orange, mandarine, kiwi")
	elif type=="fruits" and saison=="été":#...
		print("poire, fraise,cassis")
	elif type=="légumes" and saison=="hiver":#...
		print("carotte, topinambour, endive")
	elif type=="légumes" and saison=="été":#...
		print("artichaut, aubergine, navet")


primeur(type, saison)