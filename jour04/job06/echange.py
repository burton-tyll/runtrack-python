L = [1, 2, 3, 4, 5]

print(L)

def echange():
	newlist = L[-1], L[1], L[2], L[3], L[0]
	return list(newlist)


print(echange())