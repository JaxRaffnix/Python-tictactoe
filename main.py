# Goal: Implement tic tac toe for command line.

import playeraction as pa
import gameend as ge
import grid as gr

# gr.creategrid()
grid = ["1", "2", "3", 
        "4", "5", "6", 
        "7", "8", "9",]
        

"loop through each players turn"
turn = 1
currentplayer = 1
while True:
    print("\nTurn" , turn, "\tPlayer", pa.symbol(currentplayer))
    gr.printgrid(grid)
    pa.move(grid, currentplayer)
    turn = turn + 1
    currentplayer = pa.switch(currentplayer)
    if ge.checkdraw(grid) == True:
        break
