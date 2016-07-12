from random import randint

random_number = randint(1, 10);

guesses_left = 3;

while (guesses_left>0):
    guess = int(raw_input("Enter your guess: "));
    if (guess == random_number):
        print ("You win!");
        break;
    else:
        print ("Wrong guess!");
        print ("Guesses left: " + str(guesses_left-1));
    guesses_left-=1;
else:
    print ("You lose!");

x = raw_input("\n\nPress any key to exit.");
