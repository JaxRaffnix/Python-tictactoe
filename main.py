# Goal: Implement tic tac toe for command line.
#       Incldues win/draw-detection and random starting player selection.

import playeraction as pa
import endgame as eg
import grid as gr

# gr.creategrid()
grid = ["1", "2", "3", 
        "4", "5", "6", 
        "7", "8", "9",]
# grid = ["X", "O", "X", 
#         "X", "O", "X", 
#         "O", "8", "9",]
        

"loop through each players turn."
turn = 1
currentplayer = pa.randomstart()
while True:
    print("\nTurn" , turn, "\tPlayer", pa.symbol(currentplayer))
    gr.printgrid(grid)
    pa.playermove(grid, currentplayer)
    if eg.gameend(grid, currentplayer):
        break
    else:
        turn = turn + 1
        currentplayer = pa.switch(currentplayer)
