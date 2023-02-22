import random
import endgame as eg

class color:
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    END = "\033[0m"

def symbol(player):
    "return O for player 1 and X for  player 2."
    if player == 1:
        return color.BLUE + "O" + color.END
    elif player == 2:
        return color.YELLOW + "X" + color.END
    else:
        print("Error, unsupported player number: " + str(player))
        ValueError()

def playermove(grid, player):
    "Fill the grid field selected by the player with the corresponding mark."
    grid[playerinput(grid, player)] = symbol(player)
    
def playerinput(grid, player):
    "prompt the user for a valid field."
    while True:
        try:
            selection = input("Choose a field: ")
            if selection == "q":
                eg.abort(player)
            selection = int(selection) -1
            if selection < 0 or selection > 8:
                print("Error, only fields 1 to 9 are allowed. Try again.")
            elif grid[selection] == symbol(1) or grid[selection] == symbol(2):
                print("Error, field is already filled. Try again.")
            else: 
                return selection
        except ValueError:
            print("Error, only numbers 1 to 9 are allowed. Try again.")
        # else:
            

def randomstart():
    "Choose a random starting player."
    return random.randint(1,2)

def switch(player):
    "Switch control over to the other player."
    if player == 1:
        return 2
    else:
        return 1 