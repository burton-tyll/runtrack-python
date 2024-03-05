import string

alphabet= string.ascii_lowercase*10

nb = 1

i=0

while i<14:
	nb+=2
	i=i+1
	racourci = alphabet[:nb]
	print(racourci)


