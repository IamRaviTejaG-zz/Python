def digit_sum(n):
    word = str(n);
    sum1=0;
    for i in word:
        sum1+=int(i);
    return sum1;

p = raw_input("Enter number to find the sum of its digits: ");
q = int(p);
print ("\n\nSum of the digits of " + str(q) + " is " + str(digit_sum(q)) + ".");
x = raw_input("\n\nPress any key to exit.");
