i=0
while i<100:
	i=i+1
	if i%3 == 0  and not i%5==0:
		print("fizz")
	elif i%5 == 0 and not i%3==0:
		print("buzz")
	elif i%5==0 and i%3==0:
		print("fizzbuzz")
	else:
		print(i)