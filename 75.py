def number():
	nl=[]
	for x in range(2000, 3500):
		if (x%7==0) and (x%5!=0):
			nl.append(str(x))
	print (','.join(nl))

print ("NUMBER DIVISIBLE BY 7 BUT ARE NOT MULTIPLE OF 5")
number()
