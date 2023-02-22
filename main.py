# Goal: Implement tic tac toe for command line.

grid = ["1", "2", "3", 
        "4", "5", "6", 
        "7", "8", "9",]


def printgrid():
    "print the current grid to the console"
    print(grid[0] + "|" + grid[1] + "|" + grid[2])
    print(grid[3] + "|" + grid[4] + "|" + grid[5])
    print(grid[6] + "|" + grid[7] + "|" + grid[8])

def playersymbol(player):
    "return O for the current player True and X for the current player False"
    if player == 1:
        return "O"
    elif player == 2:
        return "X"
    else:
        print("Error, unsupported player number: " + str(player))
        ValueError()

def playerinput():
    "get an input field from the player"
    while True:
        selection = int(input("Choose a field: ")) -1
        if selection < 0 or selection > 8:
            print("Error, only fields 1 to 9 are allowed. Try again.")
        elif grid[selection] == playersymbol(1) or grid[selection] == playersymbol(2):
            print("Error, field is already filled. Try again.")
        else: 
            return selection

def playeraction(player):
    "change the grid field selected by the player"
    grid[playerinput()] = playersymbol(player)

def switchplayer(player):
    if player == 1:
        return 2
    else:
        return 1 

def checkwin():
    winconditions = [[0,1,2], [3,4,5], [6,7,8],     # horizontal
                     [0,3,6], [1,4,7], [2,5,8],     # vertical
                     [0,4,8], [3,4,6]               # diagonal
    ]
    # for i in winconditions:
    #     if all(j in i for j in):
    #         return True

def checkdraw():
    if all( (i == "X") or (i =="O") for i in grid ):
        return True
    else:
        return False


"loop through each players turn"
turn = 1
currentplayer = 1
while True:
    print("\nTurn" , turn)
    print("Player" , playersymbol(currentplayer))
    printgrid()
    playeraction(currentplayer)
    turn = turn + 1
    currentplayer = switchplayer(currentplayer)
    
    printgrid()
