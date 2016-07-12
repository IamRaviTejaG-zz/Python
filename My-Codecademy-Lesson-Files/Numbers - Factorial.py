def factorial(x):
    i=x-1;
    a=x;
    while i>0:
        a*=i;
        i-=1;
    print a;

print ("Enter the number to find its factorial.");
p = raw_input("\n\nEnter the number: ");
x = int(p);
print ("\n\n");
factorial(x);
y = raw_input ("\n\nPress any key to exit.");
