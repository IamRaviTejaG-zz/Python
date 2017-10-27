def area (leng, brd):
        ar = leng*brd
        if (leng==brd):
                print ("\nArea of the square is " + str(ar) + " square units.")
        else:
                print ("\nArea of the rectangle is " + str(ar) + " square units.")

leng = input("Enter the length: ")
brd = input("\nEnter the breadth: ")
area (leng, brd)

x = raw_input("\nPress any key to exit.")
