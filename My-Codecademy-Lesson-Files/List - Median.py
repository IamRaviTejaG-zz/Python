def median(inp):
    sortedList = sorted(inp);
    a = len(sortedList);
    if (a%2==0):
        a1 = a/2;
        a2 = a1-1;
        median = ((sortedList[a1] + sortedList[a2])/2.0);
    elif (a==1):
        median = sortedList[0];
    elif (a%2==1):
        a1 = (a-1)/2;
        median = sortedList[a1]*1.0;
    return median;

x = raw_input("Enter the number of items in the list: ");
y = int(x);
a = [];
for i in range(y):
    c = raw_input("\nEnter number " + str(i+1) + ": ");
    d = int(c);
    a.append(d);
print ("\n\nMedian of your data set is: " + str(median (a)) + ".");
e = raw_input("\n\nPress any key to exit.");
