def symbol(player):
    "return O for the current player True and X for the current player False"
    if player == 1:
        return "O"
    elif player == 2:
        return "X"
    else:
        print("Error, unsupported player number: " + str(player))
        ValueError()

def move(grid, player):
    "change the grid field selected by the player"
    grid[playerinput(grid)] = symbol(player)

def playerinput(grid):
    "get an input field from the player"
    while True:
        selection = int(input("Choose a field: ")) -1
        if selection < 0 or selection > 8:
            print("Error, only fields 1 to 9 are allowed. Try again.")
        elif grid[selection] == symbol(1) or grid[selection] == symbol(2):
            print("Error, field is already filled. Try again.")
        else: 
            return selection

def switch(player):
    if player == 1:
        return 2
    else:
        return 1 