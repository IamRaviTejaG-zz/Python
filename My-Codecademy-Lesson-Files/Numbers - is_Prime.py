def is_prime(x):
    count=0;
    for i in range(1, x+1):
        if (x%i==0):
            count+=1;
    if (count==2):
        return True;
    else:
        return False;

inp = raw_input("Enter a number to find out if its prime: ");
a = int(inp);
if (is_prime(a)==True):
    print ("\n\n" + str(a) + " is prime.");
else:
    print ("\n\n" + str(a) + " is not prime.");

d = raw_input("\n\nPress any key to exit.");
