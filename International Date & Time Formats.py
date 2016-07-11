#Program to show date and time in all the international formats.

from datetime import datetime

now = datetime.now();

print ("This program shows date and time in all the international formats.");

print ("\nPress 1 to view date and time in DMY, HH:MM:SS format.");
print ("Press 2 to view date and time in MDY, HH:MM:SS format.");
print ("Press 3 to view date and time in YMD, HH:MM:SS format.");

choice = input("\nEnter your choice: ");

if (choice == 1):
    print ("\nDate: %s-%s-%s" % (now.day, now.month, now.year));
    print ("\nTime: %s:%s:%s" % (now.hour, now.minute, now.second));

elif (choice == 2):
    print ("\nDate: %s-%s-%s" % (now.month, now.day, now.year));
    print ("\nTime: %s:%s:%s" % (now.hour, now.minute, now.second));

elif (choice == 3):
    print ("\nDate: %s-%s-%s" % (now.year, now.month, now.day));
    print ("\nTime: %s:%s:%s" % (now.hour, now.minute, now.second));

else:
    print ("\nInvalid choice.");

print ("\nCreated in 2016 by Ravi Teja Gannavarapu.");
print ("\nDate Time v1.03");

ex = raw_input("\nPress any key to exit.");
