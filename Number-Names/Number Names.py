""" NUMBER NAMES by Ravi Teja Gannavarapu """

names = {1:"One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
				 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
				 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}

def welcome():
	for i in range (22):
		print ("*"),
	print ("\n*  NUMBER NAMES by Ravi Teja Gannavarapu  *")
	for i in range (22):
		print ("*"),

def digit2(n):
	if (n<=20):
		return (names[n])
	elif (n>20 and n<100):
		if (n%10==0):
			return (names[((n/10)*10)])
		else:
			return (names[((n/10)*10)] + " " + names[n%10])

def digit3(n):
	c = n/100
	d = n%100
	if (d<=20):
		return (names[c] + " Hundred " + names[d])
	elif (d>20 and d<100):
		return (names[c] + " Hundred " + names[((d/10)*10)] + " " + names[d%10])

def printscr():
	welcome()
	x = raw_input("\n\nEnter the number: ")
	y = len(x)
	z = int(x)
	if (y==1 or y==2):
		print ("\n" + digit2(z))
	elif (y==3):
		print ("\n" + digit3(z))
	elif (y==4):
		a = str(z)
		b = a[0]
		f = int(b)
		g = z%1000
		print ("\n" + digit2(f) + " Thousand " + digit3(g))
	elif (y==5):
		a = str(z)
		b = a[0:2]
		f = int(b)
		g = z%1000
		print ("\n" + digit2(f) + " Thousand " + digit3(g))
	elif (y==6):
		a = str(z)
		b = a[0]
		c = int(b)
		d = z%100000
		e = d/1000
		f = d%1000
		print ("\n" + digit2(c) + " Lakh " + digit2(e) + " Thousand " + digit3(f))
	elif (y==7):
		a = str(z)
		b = a[0:2]
		c = int(b)
		d = z%100000
		e = d/1000
		f = d%1000
		print ("\n" + digit2(c) + " Lakh " + digit2(e) + " Thousand " + digit3(f))
	elif (y==8):
		a = str(z)
		b = a[0]
		c = int(b)
		d = z%10000000
		e = d/100000
		f = d%100000
		g = f/1000
		h = f%1000
		print ("\n" + digit2(c) + " Crore " + digit2(e) + " Lakh " + digit2(g) + " Thousand " + digit3(h))
	elif (y==9):
		a = str(z)
		b = a[0:2]
		c = int(b)
		d = z%10000000
		e = d/100000
		f = d%100000
		g = f/1000
		h = f%1000
		print ("\n" + digit2(c) + " Crore " + digit2(e) + " Lakh " + digit2(g) + " Thousand " + digit3(h))
	elif (y==10):
		a = str(z)
		b = a[0:3]
		c = int(b)
		d = z%10000000
		e = d/100000
		f = d%100000
		g = f/1000
		h = f%1000
		print ("\n" + digit3(c) + " Crore " + digit2(e) + " Lakh " + digit2(g) + " Thousand " + digit3(h))
	if (z>9999999999):
                print ("\nNUMBERS GREATER THAN 9999999999 ARE NOT SUPPORTED.")

printscr()
z = raw_input("\nPress any key to exit.")
