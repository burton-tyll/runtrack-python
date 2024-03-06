# Définir les longueurs du triangle

a = input("Saisissez la longueur de ab: ")
b = input("Saisissez la longueur de ac: ")
c = input("Saisissez la longueur de bc: ")

# Est-ce que c'est un triangle?
a= int(a)
b= int(b)
c= int(c)

if a+b > c or a+c > b or b+c > a:
	print("La figure est un triangle")
else:
	pass

# Est-ce un triangle rectangle?

if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
	print("La figure est un triangle rectangle")

# Est-ce un triangle isocèle?

if (a==b or a==c or b==c) and not (a==b==c):
	print("La figure est un triangle isocèle")
else:
	pass

# Est-ce un triangle équilatéral

if a==b==c:
	print("La figure est un triangle équilatéral")

