# Goal: Implement tic tac toe for command line.

grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]
def print_grid():
    "print the current grid to the console"
    print(grid[0] + "|" + grid[1] + "|" + grid[2])
    print(grid[3] + "|" + grid[4] + "|" + grid[5])
    print(grid[6] + "|" + grid[7] + "|" + grid[8])


p0_symbol = "O"
p1_symbol = "X"
def playersymbol():
    if player0_turn == True:
        return p0_symbol
    else:
        return p1_symbol


def playerinput():
    "get an input field from the player"
    while True:
        selection = int(input("Choose a field: "))
        if selection < 1 or selection > 9:
            print("Error, only fields 1 to 9 are allowed. Try again.")
        elif grid[selection-1] == p0_symbol or grid[selection-1] == p1_symbol:
            print("Error, field is already filled. Try again.")
        else: 
            return selection


def playeraction():
    if player0_turn == True:
        grid[playerinput()-1] = p1_symbol
    elif player0_turn == False:
        grid[playerinput()-1] = p0_symbol


player0_turn = True
tracker = 1
while True:
    print()
    print("Round" , tracker, )
    print("Player" , playersymbol(), "Turn:")
    print_grid()
    playeraction()
    tracker = tracker + 1
    player0_turn = not player0_turn