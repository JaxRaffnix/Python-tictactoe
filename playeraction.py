import random

def symbol(player):
    "return O for player 1 and X for  player 2."
    if player == 1:
        return "O"
    elif player == 2:
        return "X"
    else:
        print("Error, unsupported player number: " + str(player))
        ValueError()

def playermove(grid, player):
    "Fill the grid field selected by the player with the corresponding mark."
    grid[playerinput(grid)] = symbol(player)

def playerinput(grid):
    "prompt the user for a valid field."
    while True:
        selection = int(input("Choose a field: ")) -1
        if selection < 0 or selection > 8:
            print("Error, only fields 1 to 9 are allowed. Try again.")
        elif grid[selection] == symbol(1) or grid[selection] == symbol(2):
            print("Error, field is already filled. Try again.")
        else: 
            return selection

def randomstart():
    "Choose a random starting player."
    return random.randint(1,2)

def switch(player):
    "Switch control over to the other player."
    if player == 1:
        return 2
    else:
        return 1 