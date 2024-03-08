fruits = ["pomme", "cerise", "orange"]

def addmelon():
	fruits.append("melon")
	return fruits

print(fruits)

# Ici on rajoute deux fois melon à la liste
addmelon()
addmelon()

print(fruits)