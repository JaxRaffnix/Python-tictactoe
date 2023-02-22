import random
import playeraction as pa

def aimove(grid):
    "Choose a random, valid field and return the choice."
    selection = []
    for i in grid:
        if i != pa.symbol(1) and i != pa.symbol(2):     
            selection += i

    if "5" in selection:
        choice = int("5")
    else:
        choice = int(random.choice(selection))
    
    return choice -1
    
    # grid[choice-1] = pa.symbol(player)