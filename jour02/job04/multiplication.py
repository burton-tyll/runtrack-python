# L'utilisateur entre une entier N supérieur à zero

N= input("Entrez un nombre supérieur à 0: ")

while int(N) > 10:
	N = input("Veuillez entrer un nombre entre 0 et 10: ")


print("Voici la table de", N)

# Afficher la table demandée

i=0
while i<10:
	i=i+1
	result = i*int(N)
	print(N,"x",i,"=",result)