class color:
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    END = "\033[0m"


player1_symbol = color.BLUE + "O" + color.END
player2_symbol = color.YELLOW + "X" + color.END


def symbol(player):
    "return colored O for player 1 and X for player 2."
    if player == 1:
        return player1_symbol
    elif player == 2:
        return player2_symbol
    else:
        print("Error, unsupported player number: " + str(player))
        ValueError()


def playermove(grid):
    "prompt the user for a valid field."
    while True:
        try:
            choice = input("Choose a field: ")
            if choice == "q":
                return choice
            choice = int(choice) - 1
            if choice < 0 or choice > 8:
                print("Error, only fields 1 to 9 are allowed. Try again.")
            elif grid[choice] == symbol(1) or grid[choice] == symbol(2):
                print("Error, field is already filled. Try again.")
            else:
                return choice
        except ValueError:
            print("Error, only numbers 1 to 9 are allowed. Try again.")
