import endgame as ge
import grid as gr
import playeraction as pa

grid = ["O", "O", "O", 
        "X", "X", "O", 
        "7", "8", "9",]

winconditions = [[0,1,2], [3,4,5], [6,7,8],     # horizontal
                     [0,3,6], [1,4,7], [2,5,8],     # vertical
                     [0,4,8], [3,4,6]               # diagonal
    ]


for j in winconditions:
    if all( grid[i] == "X" for i in j) or all( grid[i] == "O" for i in j) :
        print(True)
    else:
        print(False)

# for j in wincon:
#     if all( (grid[i] == "X") or (grid[i] == "O") for i in j):

# gr.printgrid(grid)
