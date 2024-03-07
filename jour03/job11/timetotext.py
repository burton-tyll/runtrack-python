
def time_to_text(a):
	if a > 0:
		heure = a/ 60
		minutes = a % 60
		#On vérifie que le nombre correspond à plus d'une heure
		if (a / 60) > 1:
			return(f"{int(heure)} heures et {minutes} minutes")
		else:
			return(f"{minutes} minutes")
	else:
		print("Veuillez entrer un nombre positif")


a = int(input("Entrez un nombre de minutes: "))


result = time_to_text(a)

print(result)
