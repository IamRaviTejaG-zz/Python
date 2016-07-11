# Created By G.Ravi Teja in November 2015.
# Updated in May, June 2016.
""" Updated the code with str() and abs() and the use of function. """

def oddeven (num):
   snum = str(num)

   if (num<0):
      num = abs(num)

   if (num%2==0):
      print ("\n" + snum + " is even.");

   else:
      print ("\n" + snum + " is odd.");

num = input("Enter a number: ");
oddeven (num);

x = raw_input("\nPress any key to exit.");
