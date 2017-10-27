num = raw_input("Enter a three digit number to check if its a armstrong number: ")
a = str(num)
b = int(num)
if (b>=100 and b<=999):
    dig1 = int(a[0])
    dig2 = int(a[1])
    dig3 = int(a[2])
    sum1 = (dig1**3) + (dig2**3) + (dig3**3)
    print ("\n\nSum of cubes of digits is: " + str(sum1))
    if (b == sum1):
        print ("\n\n" + num + " is an armstrong number.")
    else:
        print ("\n\n" + num + " is not an armstrong number.")

else:
    print ("\n\n" + num + " is not an three digit number.")

x = raw_input("\n\nPress any key to exit.")
