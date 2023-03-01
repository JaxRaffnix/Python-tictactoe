import time
import endgame as eg
import board as bd
import player as pl
import randomai as rai


AI_TIME = 2
def game(board, aimode, startplayer):
    "loop through each players turn. Return the winner or a 0 in case of draw."
    turn = 1
    currentplayer = startplayer
    while True:
        if currentplayer == 2 and aimode:
            grid = rai.aimove(board)
            print("\nTurn", turn, "\t AI")
            bd.printboard(board)
            print("AI chose grid: ", grid + 1)
            time.sleep(AI_TIME)
            mark(board, grid, currentplayer)
            deleteboard()
        else:
            print("\nTurn", turn, "\tPlayer", pl.symbol(currentplayer))
            bd.printboard(board)
            grid = pl.playermove(board)
            deleteboard()
            if eg.checkabort(grid):
                print("Abort from player " +
                      str(pl.symbol(currentplayer)) + "! Win for player " + str(pl.symbol(switch(currentplayer))) + "! Games has ended.")
                # return the other player as winner if games has been aborted
                return switch(currentplayer)
            else:
                mark(board, grid, currentplayer)
        if eg.checkwin(board):
            print("")
            bd.printboard(board)
            print("\nWin for player " +
                  str(pl.symbol(currentplayer)) + "! Games has ended.")
            return currentplayer
        elif eg.checkdraw(board):
            print("")
            bd.printboard(board)
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
    if player == 2:
        return 1
    else:
        print("Error, unsupported player number: " + str(player))
        ValueError()


def deleteboard():
    LINE_UP = "\033[1A"
    LINE_CLEAR = "\x1b[2K"
    LINES = 6
    i = 0
    while i < LINES:
        print(LINE_UP, end=LINE_CLEAR)
        i += 1