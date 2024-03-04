produit = "Samsung Galaxy S22 Ultra", "IphoneX", "Redmi12"

euro = "€"

prix_unitaire = [900, 1200, 750]

stock = [350, 200, 800]

prix_euro = str(prix_unitaire[0]) + (euro)

print("le prix de "+(produit[0])+" est de "+(prix_euro)+". "+"Il en reste "+str(stock[0])+" en stock")

demande = input("Quelle quantité souhaitez-vous?: ")

prixfinal = (prix_unitaire[0]) * int(demande)

print("Vous avez demandé "+(demande)+" "+(produit[0])+" pour un prix de "+str(prixfinal))

stock = (stock[0]) - int(demande)

print("Il en reste "+str(stock)+" en stock")

inflation = 1.1

nouveau_prix = (prix_unitaire[0]) * (inflation)

print("Il semblerait que le prix de ce produit ait évolué. Son nouveau prix est de "+str(round(nouveau_prix, 1))+"€ . Souhaitez-vous toujours passer commande?")

continuer = input("Oui/non?: ")

nouveau_prix_final = nouveau_prix * int(demande)

if continuer=="oui":
	print("Veuillez régler la somme de " + str(round(nouveau_prix_final, 1))+(euro))
else: print("bye")

	

