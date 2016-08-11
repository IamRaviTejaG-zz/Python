from random import randrange

charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz~`!@#$%^&*()-_=+{}[]<>.,\/?|;:"
str1 = []

def rsg(x):
    for i in range(x):
        stri = int(i)
        int1 = int(randrange(0, 92))
        str1.insert (stri, charset[int1])
    a = ''.join(str1)
    print ("\n\n" + str(a))

print ("Mini Random String Generator by Ravi Teja Gannavarapu\n\n")
c = raw_input("Enter the random string length: ")
e = int(c)
rsg(e)
d = raw_input("\n\n\nGeneration Complete. Press any key to exit.")
