# Program created by G.Ravi Teja on 15 June 2016.

""" Program to convert the input string into completely lower or upper case. """

print ("Enter 1 to convert input string into lower case.")
print ("\nEnter 2 to convert input string into upper case.")
chce = raw_input("\n\nEnter your choice: ")

if (int(chce) == 1):
   inp1 = raw_input("\nEnter the string to be converted to lowercase: ")
   low = inp1.lower()
   print ("\n\n" + low)

elif (int(chce) == 2):
   inp2 = raw_input("\nEnter the string to be converted to uppercase: ")
   upp = inp2.upper()
   print ("\n\n" + upp)

else:
   print ("\nGO HOME. YOU ARE DRUNK !!!!")

inp3 = raw_input("\nPress any key to exit.")
