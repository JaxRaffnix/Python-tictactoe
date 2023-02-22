import endgame as eg
import grid as gr
import player as pl
import randomai as rai
import random


def turn(grid, aimode):
    "loop through each players turn."
    turn = 1
    currentplayer = randomstart()
    while True:
        if currentplayer == 2 and aimode:
            field = rai.aimove(grid)
            print("\nTurn", turn, "\t AI")
            print("AI chose field: ", field)
            mark(grid, field, currentplayer)
        else:
            print("\nTurn", turn, "\tPlayer", pl.symbol(currentplayer))
            gr.printgrid(grid)
            field = pl.playermove(grid)
            if field == "q":
                eg.abort(currentplayer)
                break
            mark(grid, field, currentplayer)
        if eg.gameend(grid, currentplayer):
            gr.printgrid(grid)
            break
        else:
            turn += 1
            currentplayer = switch(currentplayer)


def mark(grid, field, player):
    "Fill the grid field selected by the player with the corresponding mark."
    if field == "q":
        return False
    else:
        grid[field] = pl.symbol(player)
        return True


def switch(player):
    "Switch control over to the other player."
    if player == 1:
        return 2
    else:
        return 1


def randomstart():
    "Choose a random starting player."
    return random.randint(1, 2)
