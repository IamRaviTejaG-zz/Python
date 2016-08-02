""" SNAKES AND LADDERS -> Designed from scratch by Ravi Teja Gannavarapu. """

print ("DOCUMENTATION FOR THE GAME - SNAKES AND LADDERS by Ravi Teja Gannavarapu\n\n\n\
\
\
\
NOTE: This code was written on a monitor with a resolution 1440x900px. Any bad indentation is likely to happen with change in the monitor resolution.\n\n\n\
\
\
\
IMPORTS AT A GLANCE:\n\
\
1. from random import randrange: This function was imported because the program required a random integer to be generated between 1 and 6.\n\
2. import os: Contains os.system('cls') which is required to clear the console screen.\n\
3. from urllib import urlopen: This was imported because the program needs to open and download the DOCUMENTATION file from Github on user demand.\n\n\n\
\
\
\
FUNCTIONS AT A GLANCE:\n\
\
1. welcome(): This function draws a smaller board and shows the text \"PRESS ANY KEY TO START\". Welcome to the game people, thanks to this function. :P.\n\
2. board(): This function draws the board and prints the numbers to the screen. All the extra spaces in the function are just for nice indentation of the text.\n\
\t2.1. NOTE FOR board(): The board printed is in accordance with a 1440x900px resolution monitor.\n\
\tThough the way it is designed, it should look good on any resolution.\n\
3. userGen(): This function generates and returns a random number between 1 and 6 to simulate a dice roll for the user.\n\
4. compGen(): This function is similar to the userGen() above. Except that, this function simulates a dice roll for the computer.\n\
5. snl(): This function takes the score as input and changes its value accordingly if the user/computer hits a snake or a ladder.\n\
6. snllist(): This function prints the list of snakes and ladders at the beginning of the game.\n\
7. gameOnBoard(): This function generates the board while the gameplay is on. XX is shown for the user score and YY for computer score.\n\
\t7.1. XXYY Note 1: This function compares the user score and computer score and accordingly replaces the numbers in the list with XX, YY or XY respectively.\n\
\t7.2. XXYY Note 2: This function replaces the XX and YY back with the original numbers.\n\
8. main(): The function calls all other function and is responsible for the gameplay. Thank it once you are done with gameplay.\n\
\t8.1. ALLERGEN NOTICE FOR THE C/C++ PEOPLE: To all those people knowing only C/C++ (or freshmen to Python), please note that unlike in C/C++,\n\
\tmain is not a keyword in python. So, yes, the name is correct and acceptable.\n\
\t8.2. XX, YY NOT BEING SHOWN if SCORE <10: This error occurs because the numbers below 10 are 1, 2, 3, etc. for python. So, keeping indentation\n\
\tin mind, the data for the numbers in the list was entered as strings instead of numbers as 01, 02, etc make no sense in python. And since this\n\
\twas done, comparing a string and an integer wasn't possible. Hence, XX, YY positions are not shown if the score is less than 10.\n\
9. main() -> IT WAS JUST A FUNCTION CALL. NOW RELAX, AND ENJOY THE GAME!!!\n\n\n\n\
\
\
\
\
DESIgned from scratch by Ravi Teja Gannavarapu WITH TONS OF LOVE in INDIA.\n\n")

x = raw_input("Press any key to exit.")
