import endgame as eg
import grid as gr
import playeraction as pa

grid = ["0", "1", "2", 
        "X", "X", "X", 
        "6", "7", "8",]

winconditions = [[0,1,2], [3,4,5], [6,7,8],     # horizontal
                 [0,3,6], [1,4,7], [2,5,8],     # vertical
                 [0,4,8], [2,4,6]]              # diagonal

for list in winconditions:
    if all(grid[i] == pa.symbol(1) for i in list) or all(grid[i] == pa.symbol(2) for i in list):
        print(True)
        break

# print(checkwin(grid))
gr.printgrid(grid)
eg.gameend(grid, 1)
