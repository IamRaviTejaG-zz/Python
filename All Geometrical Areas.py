# Program to calculate the area of geometrical figures.
# Created By G.Ravi Teja initially in November 2015, updated in May, June 2016.

from math import sqrt, pi

print ("Enter 1 to find area of a square.")
print ("Enter 2 to find area of a rectangle.");
print ("Enter 3 to find area of a circle.");
print ("Enter 4 to find area of a right angled triangle.");
print ("Enter 5 to find area of an equilateral triangle.");
print ("Enter 6 to find curved surface area of a cylinder.");
print ("Enter 7 to find lateral surface area of a cylinder.");
print ("Enter 8 to find area of a cone.");
print ("Enter 9 to find area of a trapezium.");
print ("Enter 10 to find area of a parallelogram.");

print ("\nPlease note that the value of Pi is taken as " + str(pi) + ".");

choice = int(raw_input("\nEnter your choice: "));

if (choice==1):
	leng = input("\nEnter the length: ");
	strarea = str(leng**2);
	print ("\nArea of the square is " + strarea + " square units.");
	ex = raw_input("\nPress any key to exit.");

elif (choice==2):
	leng = input("\nEnter the length: ");
	brd = input("\nEnter the breadth: ");
	strarea = str(leng*brd);
	print ("\nArea of the rectangle is " + strarea + " square units.");
	ex = raw_input("\nPress any key to exit.");

elif (choice==3):
	radius = input("\nEnter the radius: ");
	strarea = str(pi*radius*radius);
	print ("\nArea of the circle is " + strarea + " square units.");
	ex = raw_input("\nPress any key to exit.");

elif (choice==4):
	base = input("\nEnter the base length: ");
	height = input("\nEnter the height: ");
	strarea = str(0.5*base*length);
	print ("\nArea of the right angled triangle is " + strarea + " square units.");
	ex = raw_input("\nPress any key to exit.");

elif (choice==5):
	side = input("\nEnter the side length: ");
        l = sqrt(3);
	strarea = str(l*side*side);
	print ("\nArea of the equilateral triangle is " + strarea + " square units.");
	ex = raw_input("\nPress any key to exit.");
        
elif (choice==6):
	radius = input("\nEnter the radius: ");
	height = input("\nEnter the height: ");
	strarea = str(2*pi*radius*(height+radius));
	print ("\nCurved Surface Area of the cylinder is " + strarea + " square units.");
	ex = raw_input("\nPress any key to exit.");

elif (choice==7):
	radius = input("\nEnter the radius: ");
	height = input("\nEnter the height: ");
	strarea = str(2*pi*radius*height);
	print ("\nLateral Surface Area of the cylinder is " + strarea + " square units.");
	ex = raw_input("\nPress any key to exit.");

elif (choice==8):
	slant = input("\nEnter the slant height: ");
	radius = input("\nEnter the radius: ");
	srad = radius+slant;
	strarea = str(pi*radius*srad);
	print ("\nArea of the cone is " + strarea + " square units.");
	ex = raw_input("\nPress any key to exit.");

elif (choice==9):
	a = input("\nEnter the length of first parallel line: ");
	b = input("\nEnter the length of second parallel line: ");
	h = input("\nEnter the distance between the parallel lines: ");
	strarea = str(0.5*(a+b)*h);
	print ("\nArea of the trapezium is " + strarea + " square units.");
	ex = raw_input("\nPress any key to exit.");
  
elif (choice==10):
	leng = input("\nEnter the length: ");
	height = input("\nEnter the height: ");
	strarea = str(leng*height);
	print ("\nArea of the parallelogram is " + strarea + " square units.");
	ex = raw_input("\nPress any key to exit.");

else:
	ex = raw_input("\nInvalid Choice. Press any key to exit.");
