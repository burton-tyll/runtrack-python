#Quelle opération souhaitez vous effectuer

def multiplication(a, b):
	return a * b

def addition(a, b):
	return a + b

def soustraction(a, b):
	return a - b

a = b = ""

# Tant que a et b ne sont pas des nombres, la boucle recommence

while not (a.isdigit() and b.isdigit()):
	opération = input("Quelle opération souhaitez-vous effectuer: ")
	a = input("Entrez un nombre: ")#On demande à l'utilisateur d'entrer deux nombres
	b = input("Entrez un second nombre: ")
	if not (a.isdigit() and b.isdigit()):#On vérifie que les saisies représentent des nombres
		print("Veuillez entrer des nombres corrects")

#Si l'utilisateur a saisi des nombres, on sort de la boucle et on affiche le résultat
if opération == "soustraction":
	print(soustraction(int(a), int(b)))
elif opération == "addition":
	print(addition(int(a), int(b)))
elif opération == "multiplication":
	print(multiplication(int(a), int(b)))

