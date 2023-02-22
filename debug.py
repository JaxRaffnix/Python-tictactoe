grid = ["X", "X", "X", 
        "X", "X", "O", 
        "X", "X", "X",]

# grid = ["X", "X", "O", 
#         "O", "O", "X", 
#         "X", "X", "9",]

def printgrid():
    "print the current grid to the console"
    print(grid[0] + "|" + grid[1] + "|" + grid[2])
    print(grid[3] + "|" + grid[4] + "|" + grid[5])
    print(grid[6] + "|" + grid[7] + "|" + grid[8])

def checkdraw():
    if all( (i == "X") or (i =="O") for i in grid ):
        print("Draw")
    else:
        print("no draw")

checkdraw()


def checkdrawtest():
    if all( (i == "X") or (i == "O") for i in grid ):
        return True
    else:
        return False
    
print(checkdrawtest())