from random import randint

board = [];

for x in range(5):
    board.append(["O"] * 5);

def print_board(board):
    print ("\n");
    for row in board:
        print (" ".join(row));

print ("Let's play Battleship!");
print ("\n\nNOTE: Rows & Columns start with 0. So, row 1 is actually row 0.");
print_board(board);

def random_row(board):
    return randint(0, len(board) - 1);

def random_col(board):
    return randint(0, len(board[0]) - 1);

ship_row = random_row(board);
ship_col = random_col(board);

for turn in range(4):
    guess_row = int(raw_input("\nGuess Row: "));
    guess_col = int(raw_input("\nGuess Col: "));

    if guess_row == ship_row and guess_col == ship_col:
        print ("\nCongratulations! You sunk my battleship!");
        break;
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("\nOops, that's not even in the ocean.");
        elif(board[guess_row][guess_col] == "X"):
            print ("\nYou guessed that one already.");
        else:
            print ("\nYou missed my battleship!");
        if (turn == 3):
            print ("\nGame Over");
            print ("\nThe battleship was at: " + str(ship_row) + " row and " + str(ship_col) + " column.");
            x = raw_input("\n\nPress any key to exit.");
        board[guess_row][guess_col] = "X"

    print "\nTurn " , (turn+1);
    print_board(board);
