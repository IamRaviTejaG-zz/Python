def oddeven (num):
   snum = str(num)
   if (num<0):
      num = abs(num)
   if (num%2==0):
      print ("\n" + snum + " is even.")
   else:
      print ("\n" + snum + " is odd.")

num = input("Enter a number: ")
oddeven (num)

x = raw_input("\nPress any key to exit.")
