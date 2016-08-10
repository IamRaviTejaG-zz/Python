from random import randrange


print ("RANDOM PASSWORD GENERATOR by Ravi Teja Gannavarapu\n\n")
c = raw_input("Enter the random string length: ")
e = int(c)
f = raw_input("\n\nEnter number of strings of length " + str(e) + " to be generated: ")
g = int(f)
k = raw_input("\n\nDo you want to save the strings to a file? Y/N: ")
charset1 = "0123456789"
charset2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
charset3 = "abcdefghijklmnopqrstuvwxyz"
charset4 = "~`!@#$%^&*()-_=+{}[]<>.,\/?|;:"
str1 = []
l = open ("Random Strings.txt", "a")
u = "RANDOM PASSWORD GENERATOR by Ravi Teja Gannavarapu"
v = "===== OUTPUT BEGINS =====\n\n"
w = "\n\n===== OUTPUT ENDS ====="
n = "\n\n"
l.write(u)
l.write(n)
l.write(v)
l.write(n)
for h in range(g):
    for i in range(e):
        stri = int(i)
        int1 = int(randrange(0, 10))
        int2 = int(randrange(0, 26))
        int3 = int(randrange(0, 29))
        ch = int(randrange(1, 5))
        if (ch==1):
            str1.insert (i, charset1[int1])
        elif (ch==2):
            str1.insert (i, charset2[int2])
        elif (ch==3):
            str1.insert (i, charset3[int2])
        elif (ch==4):
            str1.insert (i, charset4[int3])
    a = ''.join(str1)
    print ("\n\n" + str(a))
    if (k == "y" or k == "Y"):
         l.write(a)
         l.write(n)
    del str1[::]

l.write(w)
l.close()
d = raw_input()
