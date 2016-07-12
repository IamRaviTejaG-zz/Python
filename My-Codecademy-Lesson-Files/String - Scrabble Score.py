score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

def scrabble_score(word):
    wordlow = str(word.lower());
    score1 = 0;
    leng = len(wordlow);
    for i in range(0, leng):
        score1+=score[wordlow[i]];
    print ("Scrabble score of \"" + str(word) + "\" is " + str(score1) + ".");
    return score1;

inp = raw_input("Enter the word to check its scrabble score: ");
print ("\n");
scrabble_score(inp);
p = raw_input ("\n\nEnter any key to exit.");
