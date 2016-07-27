""" For FULL FLEDGED DOCUMENTATION REGARDING THE IMPORTS AND THE PROGRAM, GO TO THE BOTTOM OF THE CODE. """


""" IMPORTS BEGIN """
from random import randrange
import os
""" IMPORTS END """


""" DATA & VARIABLES BEGIN """
""" The board numbers data. """
list_90 = ["1H", 99, 98, 97, 96, 95, 94, 93, 92, 91];
list_80 = [81, 82, 83, 84, 85, 86, 87, 88, 89, 90];
list_70 = [80, 79, 78, 77, 76, 75, 74, 73, 72, 71];
list_60 = [61, 62, 63, 64, 65, 66, 67, 68, 69, 70];
list_50 = [60, 59, 58, 57, 56, 55, 54, 53, 52, 51];
list_40 = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50];
list_30 = [40, 39, 38, 37, 36, 35, 34, 33, 32, 31];
list_20 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30];
list_10 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11];
list_00 = ["01", "02", "03", "04", "05", "06", "07", "08", "09", 10];
num_list = [list_90, list_80, list_70, list_60, list_50, list_40, list_30, list_20, list_10, list_00];
""" DATA & VARIABLES END """


""" FUNCTION DEFINITIONS BEGIN """
""" Generates the welcome screen. """
def welcome():
        for i in range (28):
                print ("*"),;
        print ("\n*                  SNAKES & LADDERS                   *");
        print ("*                                                     *");
        print ("*               PRESS ANY KEY TO START                *");
        for i in range (28):
                print ("*"),;
        p = raw_input();

""" Generates board design. """
def board():
        for i in range (28):
                print ("*"),;
        print ("\n*                  SNAKES & LADDERS                   *");
        print ("*                                                     *");
        print ("*                                                     *");
        for i in num_list:
                print ("*\t" + "  ".join(str(j) for j in i) + "\t      *");
        print ("*                                                     *");
        for i in range (28):
                print ("*"),;

""" Generates random dice number for the user. """
def userGen(): 
	userDice = randrange(6) + 1;
        return userDice;

""" Generates random dice number for the computer. """
def compGen():
	compDice = randrange(6) + 1;
        return compDice;

""" Implements the snakes and ladders thrill into the user score. """
def snl(score, text):
        snakes = {29:7, 38:20, 44:14, 55:11, 73:52, 82:60, 93:43, 96:17, 98:48};
        ladders = {3:21, 4:36, 15:48, 24:58, 31:70, 49:90, 60:79, 63:99, 72:91, 77:97};
        for w in ladders:
                if (score == w):
                        print ("\n\n" + str(text) + " hit a ladder. " + str(text) + ", HIT A LADDER!!!! WOOOHHHHOOOOOO !!!!");
                        score = ladders[score];
        for w in snakes:
                if (score == w):
                        print ("\n\n" + str(text) + " stepped on a snake. " + str(text) + ", DOWN YOU GO GO GO!!!!");
                        score = snakes[score];
	return score;

""" Generates board design during gameplay is on. """
def gameOnBoard(x, y):
        print ("\n");
        for i in range (28):
                print ("*"),;
        print ("\n*                  SNAKES & LADDERS                   *");
        print ("*                                                     *");
        print ("*                                                     *");
        c = int(x);
        d = int(y);
        for i in num_list: # Refer XXYY Note 1 under point 6 (point 6.1) of gameOnBoard() in Documentation for help.
                for j in i:
                        if (j == c):
                                f = i.index(j);
                                i.remove(j);
                                i.insert(f, "XX");
                        elif (j == d):
                                f = i.index(j);
                                i.remove(j);
                                i.insert(f, "YY");
                                         
        for i in num_list:
                print ("*\t" + "  ".join(str(j) for j in i) + "\t      *");
        for i in num_list: # Refer XXYY Note 2 under point 6 (point 6.2) of gameOnBoard() in Documentation for help.
                for j in i:
                        if (j == "XX"):
                                f = i.index(j);
                                i.remove(j);
                                i.insert(f, c);
                        elif (j == "YY"):
                                f = i.index(j);
                                i.remove(j);
                                i.insert(f, d);
        print ("*                                                     *");
        for i in range (28):
                print ("*"),;

""" The MAIN GAME function. Calls all other functions and runs the game. """
def main():
        welcome();
        userScore = 0;
        compScore = 0;
        os.system('cls');
        board();
        a = raw_input("\n\nEnter y or Y to roll dice: ");
        while (a == "y" or a == "Y"):
                if (userScore<100 and compScore<100):
                        c = userGen();
                        d = compGen();
                        userScore = userScore + c;
                        compScore = compScore + d;
                        text1 = "USER";
                        text2 = "COMPUTER";
                        userScore = snl(userScore, text1);
                        compScore = snl(compScore, text2);
                        print ("\n\nUser Dice: " + str(c));
                        print ("\nComputer Dice: " + str(d));
                        print ("\n\nUser Score: " + str(userScore));
                        print ("\nComputer Score: " + str(compScore));
                        if (userScore>100):
                                print ("\n\n");
                                print ("USER WINS!!!!\n") * 10;
                        elif(compScore>100):
                                print ("\n\n");
                                print ("COMPUTER WINS!!!!\n") * 10;
                        else:
                                a = raw_input("\nEnter x or X to see the board. Enter y or Y to roll dice: ");
                                while (a == "X" or a == "x"):
                                        gameOnBoard(userScore, compScore);
                                        print ("\nXX -> User Position\nYY -> Computer Position.");
                                        # To know why the below error occurs, refer point 7.2 of *FUNCTIONS AT A GLANCE* section of Documentation.
                                        print ("\nNOTE: If the score is <10, then the XX or YY are not shown. Sorry for the inconvenience.");
                                        a = raw_input("\nEnter y or Y to roll dice: ");
                                
""" FUNCTION DEFINITIONS END """


""" FUNCTION CALLS BEGIN """
main();
""" FUNCTION CALLS END """


""" DOCUMENTATION BEGINS """
""" DETAILED DOCUMENTATION FOR THE PROGRAM """
""" NOTE: This code was written on a monitor with a resolution 1440x900px. Any bad indentation is likely to happen with change in the monitor resolution. """

""" IMPORTS AT A GLANCE:
1. from random import randrange: This function was imported because the program required a random integer to be generated between 1 and 6.
2. import os: This was imported because at few points the program needs to clear the console screen."""

""" FUNCTIONS AT A GLANCE:
1. welcome(): This function draws a smaller board and shows the text "PRESS ANY KEY TO START". Welcome to the game people, thanks to this function. :P.
2. board(): This function draws the board and prints the numbers to the screen. All the extra spaces in the function are just for nice indentation of the text.
	2.1. NOTE FOR board(): The board printed is in accordance with a 1440x900px resolution monitor.
	Though the way it is designed, it should look good on any resolution.
3. userGen(): This function generates and returns a random number between 1 and 6 to simulate a dice roll for the user.
4. compGen(): This function is similar to the userGen() above. Except that, this function simulates a dice roll for the computer.
5. snl(): This function takes the score as input and changes its value accordingly if the user/computer hits a snake or a ladder.
6. gameOnBoard(): This function generates the board while the gameplay is on. XX is shown for the user score and YY for computer score.
        6.1. XXYY Note 1: This function compares the user score and computer score and accordingly replaces the numbers in the list with XX and YY respectively.
        6.2. XXYY Note 2: This function replaces the XX and YY back with the original numbers.
7. main(): The function calls all other function and is responsible for the gameplay. Thank it once you are done with gameplay.
	7.1. ALLERGEN NOTICE FOR THE C/C++ PEOPLE: To all those people knowing only C/C++ (or freshmen to Python), please note that unlike in C/C++,
	main is not a keyword in python. So, yes, the name is correct and acceptable.
	7.2. XX, YY NOT BEING SHOWN FOR SCORE <10: This error occurs because the numbers below 10 are 1, 2, 3, etc. for python. So, keeping indentation
	in mind, the data for the numbers in the list was entered as strings instead of numbers as 01, 02, etc make no sense in python. And since this
	was done, comparing a string and an integer wasn't possible. Hence, XX, YY positions are not shown if the score is less than 10.
8. main(); -> ENOUGH FOLKS, IT WAS JUST A FUNCTION CALL. THAT'S IT. NOW RELAX, AND ENJOY THE GAME!!!"""


""" DESIgned from scratch by Ravi Teja Gannavarapu with love in INDIA. (MAKE IN INDIA). :P. """
""" DOCUMENTATION ENDS """
