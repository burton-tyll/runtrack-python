
num1 = input("Veuillez entrer un nombre: ")

num2 = input("Veuillez entrer un second nombre: ")

operator = input("Quelle opération souhaitez-vous effectuer?: ")


def calcul(num1, operator, num2):
	if operator == "+":
		return int(num1) + int(num2)
	elif operator == "-":
		return int(num1) - int(num2)
	elif operator == "*":
		return int(num1) * int(num2)
	elif operator == "/":
		return int(num1) / int(num2)
	elif operator == "%":
		return int(num1) % int(num2)


aff_calcul = calcul(num1, operator, num2)

print(aff_calcul)






