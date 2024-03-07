
def moyenne(note1, note2, note3):
	return ((note1 + note2 + note3)/3)

saisie = print("Veuillez entrer les notes ci-dessous:")
note1 = float(input("1: "))
note2 = float(input("2: "))
note3 = float(input("3: "))


moyenne_etudiant = moyenne(note1, note2, note3)

if 15<= moyenne_etudiant <=20:
	print(str(moyenne_etudiant) +" Très bon élève")
elif 11<= moyenne_etudiant <=14:
	print(str(moyenne_etudiant)+" Bon élève")
elif 8<= moyenne_etudiant <=10:
	print(str(moyenne_etudiant)+" Elève moyen")
elif 0<= moyenne_etudiant <=7:
	print(str(moyenne_etudiant)+" Elève nul à chier")




