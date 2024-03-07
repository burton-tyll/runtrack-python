import sys

LISTE = []

MENU = """Choisissez parmi les 5 options suivantes:
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉Votre choix: """

MENU_CHOICES = ["1", "2", "3", "4", "5"]

while True:
	user_choice = ""
	while user_choice not in MENU_CHOICES:
		user_choice = input(MENU)
		if user_choice not in MENU_CHOICES:
			print("\nVeuillez entrer un choix valide...")
			print("_" * 50)


	if user_choice == "1": #Ajouter un élément
		item = input("\nEntrer le nom d'un élément à ajouter à la liste de courses: ")
		LISTE.append(item)
		print(f"\nL'élément, {item} a bien été ajouté à la liste")
	elif user_choice == "2": #Retirer un élément
		item = input("\nVeuillez entrer le nom de l'élément que vous souhaitez retirer de la liste de courses: ")
		if item in LISTE:
			LISTE.remove(item)
			print(f"\nL'élément {item} a bien été retiré de la liste")
		else:
			print("Veuillez entrer un élément de la liste")
	elif user_choice == "3": #Afficher la liste
		if LISTE:
			print("\nVoici le contenu de la liste:")
			for i, item in enumerate(LISTE, 1):
				print(f"{i}. {item}")
		else:
			print("\nLa liste est vide")
	elif user_choice == "4": #Vider la liste
		LISTE.clear()
		print('\nLa liste a été vidée')
	elif user_choice == "5": #Quitter le menu
		print("\nA bientôt!")
		sys.exit()

	print("_" * 50)





