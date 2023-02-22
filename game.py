import endgame as eg
import grid as gr
import playeraction as pa
import randomai as rai


def turns(grid, aimode):
    "loop through each players turn."
    turn = 1
    currentplayer = pa.randomstart()
    while True:
        if currentplayer == 2 and aimode:
            field = rai.aimove(grid)
            print("\nTurn", turn, "\t AI")
            print("AI chose field: ", field)
            pa.mark(grid, field, currentplayer)
            # grid[field] = pa.symbol(currentplayer)
        else:
            print("\nTurn" , turn, "\tPlayer", pa.symbol(currentplayer))
            gr.printgrid(grid)
            field = pa.playermove(grid)
            pa.mark(grid, field, currentplayer)

            # if not pa.playermove(grid, currentplayer):
            #     print("Aborting move from player " + str(pa.symbol(currentplayer)) + "! Games has ended.")
            #     break
        if eg.gameend(grid, currentplayer):
            gr.printgrid(grid)
            break
        else:
            turn = turn + 1
            currentplayer = pa.switch(currentplayer)