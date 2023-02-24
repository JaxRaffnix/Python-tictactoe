import endgame as eg
import board as bd
import player as pl
import randomai as rai
import random


def game(board, aimode):
    "loop through each players turn. Return the winner or a 0 in case of draw."
    turn = 1
    currentplayer = randomstart()
    while True:
        if currentplayer == 2 and aimode:
            grid = rai.aimove(board)
            print("\nTurn", turn, "\t AI")
            print("AI chose grid: ", grid + 1)
            mark(board, grid, currentplayer)
        else:
            print("\nTurn", turn, "\tPlayer", pl.symbol(currentplayer))
            bd.printboard(board)
            grid = pl.playermove(board)
            if eg.checkabort(grid):
                print("Abort from player " +
                      str(pl.symbol(currentplayer)) + "! Win for player " + str(pl.symbol(switch(currentplayer))) + "! Games has ended.")
                # return the other player as winner if games has been aborted
                return switch(currentplayer)
            else:
                mark(board, grid, currentplayer)
        if eg.checkwin(board):
            bd.printboard(board)
            print("\nWin for player " +
                  str(pl.symbol(currentplayer)) + "! Games has ended.")
            return currentplayer
        elif eg.checkdraw(board):
            print("\nDraw! Game has ended.")
            return 0
        else:
            turn += 1
            currentplayer = switch(currentplayer)


def mark(board, grid, player):
    "Set the board position chosen by the player with the corresponding marker."
    board[grid] = pl.symbol(player)


def switch(player):
    "Switch control over to the other player."
    if player == 1:
        return 2
    else:
        return 1


def randomstart():
    "Choose a random starting player."
    return random.randint(1, 2)

