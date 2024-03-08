L = [1, 2, 3, 4, 5]

print(L)

print(L[1])

def rep_list():
	somme = L[2]+L[4]
	L[3] = somme
	print(L)
	print(L[-1])

rep_list()
