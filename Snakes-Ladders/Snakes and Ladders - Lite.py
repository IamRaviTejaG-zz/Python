from random import randrange
import os
from urllib import urlopen

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

def welcome():
	print ("Please refer DOCUMENTATION of the source code to understand further how this game works.\n");
	print ("Enter d or D to download the DOCUMENTATION as a python file.\n");
	print ("Source code available at: https://github.com/IamRaviTejaG/Python\n\n");
	for i in range (28):
		print ("*"),;
	print ("\n*                  SNAKES & LADDERS                   *");
	print ("*                                                     *");
	print ("*               PRESS ANY KEY TO START                *");
	for i in range (28):
		print ("*"),;
        print ("\n\n");
	p = raw_input("");
	if (p == "d" or p == "D"):
                resource = urlopen("https://raw.githubusercontent.com/IamRaviTejaG/Python/master/Snakes-Ladders/SnL%20-%20DOCUMENTATION%20ONLY.py");
                output = open("SnL - DOCUMENTATION ONLY.py", "wb");
                output.write(resource.read());
                output.close();

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

def userGen(): 
	userDice = randrange(1, 7);
	return userDice;

def compGen():
	compDice = randrange(1, 7);
	return compDice;

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

def snllist():
	snakes = {29:7, 38:20, 44:14, 55:11, 73:52, 82:60, 93:43, 96:17, 98:48};
	ladders = {3:21, 4:36, 15:48, 24:58, 31:70, 49:90, 60:79, 63:99, 72:91, 77:97};
	print ("\n\nSnake begins at: " + str(snakes.keys()));
	print ("\nSnakes end at: " + str(snakes.values()));
	print ("\nLadders begin at: " + str(ladders.keys()));
	print ("\nLadders end at: " + str(ladders.values()));

def gameOnBoard(x, y):
	print ("\n");
	for i in range (28):
		print ("*"),;
	print ("\n*                  SNAKES & LADDERS                   *");
	print ("*                                                     *");
	print ("*                                                     *");
	c = int(x);
	d = int(y);
	for i in num_list:
		for j in i:
			if (j == c and j == d):
				f = i.index(j);
				i.remove(j);
				i.insert(f, "XY");
			elif (j == c):
				f = i.index(j);
				i.remove(j);
				i.insert(f, "XX");
			elif (j == d):
				f = i.index(j);
				i.remove(j);
				i.insert(f, "YY");
	for i in num_list:
		print ("*\t" + "  ".join(str(j) for j in i) + "\t      *");
	for i in num_list:
		for j in i:
			if (j == "XX"):
				f = i.index(j);
				i.remove(j);
				i.insert(f, c);
			elif (j == "YY"):
				f = i.index(j);
				i.remove(j);
				i.insert(f, d);
			elif (j == "XY"):
				f = i.index(j);
				i.remove(j);
				i.insert(f, d);
	print ("*                                                     *");
	for i in range (28):
		print ("*"),;

def main():
	welcome();
	userScore = 0;
	compScore = 0;
	os.system('cls');
	board();
	snllist();
	a = raw_input("\n\nEnter y or Y to roll dice: ");
	while (a == "y" or a == "Y"):
		if (userScore<100 and compScore<100):
			c = userGen();
			d = compGen();
			userScore = userScore + c;
			compScore = compScore + d;
			text1 = "USER";
			text2 = "COMPUTER";
			print ("\n\nUser Dice: " + str(c));
			print ("\nComputer Dice: " + str(d));
			userScore = snl(userScore, text1);
			compScore = snl(compScore, text2);
			print ("\n\nUser Score: " + str(userScore));
			print ("\nComputer Score: " + str(compScore));
			if (userScore>=100):
				print ("\n\n");
				print ("USER WINS!!!!\n") * 10;
			elif(compScore>=100):
				print ("\n\n");
				print ("COMPUTER WINS!!!!\n") * 10;
			else:
				a = raw_input("\nEnter x or X to see the board. Enter y or Y to roll dice: ");
				while (a == "x" or a == "X"):
					gameOnBoard(userScore, compScore);
					print ("\n\tXX -> User Position\n\tYY -> Computer Position\n\tXY -> User Position = Computer Position.");
					print ("\nNOTE: If the score is <10, then the XX, YY or XY are not shown. Refer documentation for help.");
					a = raw_input("\nEnter y or Y to roll dice: ");

main();
