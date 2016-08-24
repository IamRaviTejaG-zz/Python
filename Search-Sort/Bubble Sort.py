""" BUBBLE SORT IN PYTHON by Ravi Teja Gannavarapu """

a = []

def inp():
	c = raw_input("Enter the number of entries in the list: ")
	d = int(c)
	for i in range(d):
		e = raw_input("\nEnter number " + str(i+1) + " : ")
		a.insert(i, int(e))
	bubble(a)
	print ("\n\n\nSorted List is as follows: \n\n")
	for i in range(len(a)):
		print (str(a[i])+ "\t")

def bubble(a):
	for i in range(len(a)):
		for j in range(len(a)-1):
			if (a[j] > a[j+1]):
				a[j], a[j+1] = a[j+1], a[j]

inp()
x = raw_input("\n\nBubble Sorting complete. Press any key to exit.")
