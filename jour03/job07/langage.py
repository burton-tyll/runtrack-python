langage = input("Quel langage de programmation utilisez-vous?: ")



def lang(langage):
	if langage == "JavaScript":
		print("Tu es un développeur web")
	elif langage == "python":
		print("Tu es un développeur IA")
	elif langage == "java":
		print("Tu es un développeur logiciel")
	elif langage == "reactjs":
		print("Tu es un développeur mobile")
	else:
		print("Un jour, je serai le meilleur développeur...")


lang(langage)