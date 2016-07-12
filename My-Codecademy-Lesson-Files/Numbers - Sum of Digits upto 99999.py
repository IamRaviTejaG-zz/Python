def digit_sum(n):
    if (n>=0 and n<=9):
        print n;
    elif (n>=10 and n<=99):
        x=n%10;
        y=int(n/10);
        print ("Sum of digits: " + str(x+y));
    elif (n>=100 and n<=999):
        x=int(n/100);
        a=int(n/10);
        y=a%10;
        z=int(n%10);
        print ("Sum of digits: " + str(x+y+z));
    elif (n>=1000 and n<=9999):
        w=int(n/1000);
        a=n%1000;
        x=int(a/100);
        b=n%100;
        y=int(b/10);
        z=b%10;
        print ("Sum of digits: " + str(w+x+y+z));
    elif (n>=10000 and n<=99999):
        v=int(n/10000);
        a=n%10000;
        w=int(a/1000);
        b=n%1000;
        x=int(b/100);
        c=n%100;
        y=int(c/10);
        z=c%10;
        print ("Sum of digits: " + str(v+w+x+y+z));
    else:
        print ("Sorry, but numbers greater than 10000 are currently not supported!");

print ("Enter the number to find the sum of its digits. Note that the number should be less than 100000.");
p = raw_input("\n\nEnter the number: ");
x = int(p);
print ("\n");
digit_sum(x);
y = raw_input ("\n\nPress any key to exit.");
