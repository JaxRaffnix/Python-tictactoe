import random
import playeraction as pa

def aimove(grid, player):
    "Fill the grid field selected by ai with the corresponding mark."
    selection = []
    for i in grid:
        if i != pa.symbol(1) and i != pa.symbol(2): 
            selection += i

    choice = int(random.choice(selection)) -1
    grid[choice] = pa.symbol(player)