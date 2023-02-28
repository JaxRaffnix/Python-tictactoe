class color:
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"
player1_symbol = color.BLUE + "O" + color.END
player2_symbol = color.YELLOW + "X" + color.END

markswitch = False
def switchmark(): 
    "switches mark for player 1 and 2"
    global markswitch 
    markswitch = not markswitch

def symbol(player):
    "return colored O for player 1 and X for player 2."
    if player == 1:
        if markswitch:
            return player2_symbol
        else:
            return player1_symbol
    if player == 2:
        if markswitch:
            return player1_symbol
        else:
            return player2_symbol
    else:
        print("Error, unsupported player number" + str(player))
        ValueError()

abort_sequence = "q"
def playermove(board):
    "prompt the user for a valid grid."
    while True:
        try:
            choice = input("Choose a grid: ")
            if choice == abort_sequence:
                return choice
            choice = int(choice) - 1
            if choice < 0 or choice > 8:
                print("Error, only grids 1 to 9 are allowed. Try again.")
            elif board[choice] == symbol(1) or board[choice] == symbol(2):
                print("Error, grid is already filled. Try again.")
            else:
                return choice
        except ValueError:
            print("Error, only numbers 1 to 9 are allowed. Try again.")
