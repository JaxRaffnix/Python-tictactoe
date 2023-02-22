import playeraction as pa

def checkwin(grid):
    winconditions = [[0,1,2], [3,4,5], [6,7,8],     # horizontal
                     [0,3,6], [1,4,7], [2,5,8],     # vertical
                     [0,4,8], [3,4,6]               # diagonal
    ]
    for i in winconditions:
        # if all (j in grid for j in i):
        if grid[winconditions[1][1]] == grid[winconditions[1][2]]:
            return True
        else:
            return False

def checkdraw(grid):
    if all( (i == pa.symbol(1)) or (i == pa.symbol(2)) for i in grid ):
        return True
    else:
        return False

def gameend(grid, currentplayer):
    if checkdraw(grid):
        print("Draw! Game has ended.")
        return True
    if checkwin(grid):
        print("Win for: ", currentplayer, "! Games has ended.")
        return True
    else:
        return False