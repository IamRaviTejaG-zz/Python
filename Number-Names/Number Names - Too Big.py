""" NUMBER NAMES -> Designed from scratch by Ravi Teja Gannavarapu. """

from random import randrange

def welcome():
	for i in range (22):
		print ("*"),
	print ("\n*  NUMBER NAMES by Ravi Teja Gannavarapu  *")
	for i in range (22):
		print ("*"),

def numName(n):
	names = {1:"One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve",
				 13: "Thirteen", 14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
				 30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}
	a = str(n)
	b = len(a)
	if (n>=0 and n<=20):
		print ("\n" + names[n])
	elif (n>20 and n<100):
		if (n%10==0):
			print ("\n" + names[((n/10)*10)])
		else:
			print ("\n" + names[((n/10)*10)] + " " + names[n%10])
	if (b==3):
		c = n/100
		d = n%100
		print ("\n" + names[c] + " Hundred " + names[((d/10)*10)] + " " + names[d%10])
	elif (b==4 or b==5):
		c = n/1000
		d = n%1000
		e = d/100
		f = d%100
		if (c>20 and c<100):
			if (f%10==0):
				print ("\n" + names[((c/10)*10)] + " " + names[c%10] + " Thousand(s) " + names[e] + " Hundred " + names[(f/10)*10])
			else:
				print ("\n" + names[((c/10)*10)] + " " + names[c%10] + " Thousand(s) " + names[e] + " Hundred " + names[((f/10)*10)] + " " + names[f%10])
		else:
			if (f%10==0):
				print ("\n" + names[c] + " Thousand(s) " + names[e] + " Hundred " + names[(f/10)*10])
			else:
				print ("\n" + names[c] + " Thousand(s) " + names[e] + " Hundred " + names[((f/10)*10)] + " " + names[f%10])
	elif (b==6 or b==7):
		a = n/100000
		b = n%100000
		c = b/1000
		d = b%1000
		e = d/100
		f = d%100
		if (a>20 and a<100):
			if (c>20 and c<100):
				if (f%10==0):
					print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Lakh(s) " + names[((c/10)*10)] + " " + names[c%10] + " Thousand(s) " + names[e] + " Hundred " + names[(f/10)*10])
				else:
					print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Lakh(s) " + names[((c/10)*10)] + " " + names[c%10] + " Thousand(s) " + names[e] + " Hundred " + names[(f/10)*10] + " " + names[f%10])
			else:
				if (f%10==0):
					print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Lakh(s) " + names[c] + " Thousand(s) " + names[e] + " Hundred " + names[(f/10)*10])
				else:
					print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Lakh(s) " + names[c] + " Thousand(s) " + names[e] + " Hundred " + names[(f/10)*10] + " " + names[f%10])
		else:
			if (c>20 and c<100):
				if (f%10==0):
					print ("\n" + names[a] + " Lakh(s) " + names[((c/10)*10)] + " " + names[c%10] + " Thousand(s) " + names[e] + " Hundred " + names[(f/10)*10])
				else:
					print ("\n" + names[a] + " Lakh(s) " + names[((c/10)*10)] + " " + names[c%10] + " Thousand(s) " + names[e] + " Hundred " + names[(f/10)*10] + " " + names[f%10])
			else:
				if (f%10==0):
					print ("\n" + names[a] + " Lakh(s) " + names[c] + " Thousand(s) " + names[e] + " Hundred " + names[(f/10)*10])
				else:
					print ("\n" + names[a] + " Lakh(s) " + names[c] + " Thousand(s) " + names[e] + " Hundred " + names[(f/10)*10] + " " + names[f%10])
	
	elif (b==8 or b==9):
		a = n/10000000
		b = n%10000000
		c = b/100000
		d = b%100000
		e = d/1000
		f = d%1000
		g = f/100
		h = f%100
		if (a>20 and a<100):
			if (c>20 and c<100):
				if (e>20 and e<100):
					if (h%10==0):
						print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Crore(s) " + names[((c/10)*10)] + " " + names[c%10] + " Lakh(s) " + names[((e/10)*10)] + " " + names[e%10] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10])
					else:
						print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Crore(s) " + names[((c/10)*10)] + " " + names[c%10] + " Lakh(s) " + names[((e/10)*10)] + " " + names[e%10] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10] + " " + names[h%10])
				else:
					if (h%10==0):
						print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Crore(s) " + names[((c/10)*10)] + " " + names[c%10] + " Lakh(s) " + names[e] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10])
					else:
						print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Crore(s) " + names[((c/10)*10)] + " " + names[c%10] + " Lakh(s) " + names[e] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10] + " " + names[h%10])
			else:
				if (e>20 and e<100):
					if (h%10==0):
						print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Crore(s) " + names[c] + " Lakh(s) " + names[((e/10)*10)] + " " + names[e%10] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10])
					else:
						print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Crore(s) " + names[c] + " Lakh(s) " + names[((e/10)*10)] + " " + names[e%10] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10] + " " + names[h%10])
				else:
					if (h%10==0):
						print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Crore(s) " + names[c] + " Lakh(s) " + names[e] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10])
					else:
						print ("\n" + names[((a/10)*10)] + " " + names[a%10] + " Crore(s) " + names[c] + " Lakh(s) " + names[e] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10] + " " + names[h%10])
		else:
			if (c>20 and c<100):
				if (e>20 and e<100):
					if (h%10==0):
						print ("\n" + names[a] + " Crore(s) " + names[((c/10)*10)] + " " + names[c%10] + " Lakh(s) " + names[((e/10)*10)] + " " + names[e%10] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10])
					else:
						print ("\n" + names[a] + " Crore(s) " + names[((c/10)*10)] + " " + names[c%10] + " Lakh(s) " + names[((e/10)*10)] + " " + names[e%10] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10] + " " + names[h%10])
				else:
					if (h%10==0):
						print ("\n" + names[a] + " Crore(s) " + names[((c/10)*10)] + " " + names[c%10] + " Lakh(s) " + names[e] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10])
					else:
						print ("\n" + names[a] + " Crore(s) " + names[((c/10)*10)] + " " + names[c%10] + " Lakh(s) " + names[e] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10] + " " + names[h%10])
			else:
				if (e>20 and e<100):
					if (h%10==0):
						print ("\n" + names[a] + " Crore(s) " + names[c] + " Lakh(s) " + names[((e/10)*10)] + " " + names[e%10] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10])
					else:
						print ("\n" + names[a] + " Crore(s) " + names[c] + " Lakh(s) " + names[((e/10)*10)] + " " + names[e%10] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10] + " " + names[h%10])
				else:
					if (h%10==0):
						print ("\n" + names[a] + " Crore(s) " + names[c] + " Lakh(s) " + names[e] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10])
					else:
						print ("\n" + names[a] + " Crore(s) " + names[c] + " Lakh(s) " + names[e] + " Thousand(s) " + names[g] + " Hundred " + names[(h/10)*10] + " " + names[h%10])

welcome()
x = raw_input("\n\nEnter the number: ")
y = int(x)
numName(y)
z = raw_input("\nPress any key to exit.")
