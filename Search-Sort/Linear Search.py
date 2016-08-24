""" LINEAR SEARCH by Ravi Teja Gannavarapu """

a = []

def linSearch(n):
	for i in range(len(a)):
		if (n == a[i]):
			return ("\n\n" + str(n) + " was found at index " + str(i+1) + ".")
	else:
		return ("\n\n" + str(n) + " was not found at any index.")

def inp():
	c = raw_input("Enter the number of entries in the list: ")
	d = int(c)
	for i in range(d):
		e = raw_input("\nEnter number " + str(i+1) + " : ")
		a.insert(i, int(e))

def srch():
	f = raw_input("\n\nEnter the item to search for: ")
	g = int(f)
	print linSearch(g)

inp()
srch()