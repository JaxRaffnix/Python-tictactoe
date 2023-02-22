import player as pl


def checkwin(grid):
    "Check if a win condition is met."
    winconditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],     # horizontal
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],     # vertical
                     [0, 4, 8], [2, 4, 6]]              # diagonal

    for list in winconditions:
        if all(grid[i] == pl.symbol(1) for i in list) or all(grid[i] == pl.symbol(2) for i in list):
            return True


def checkdraw(grid):
    "check if every field is filled out."
    if all((i == pl.symbol(1)) or (i == pl.symbol(2)) for i in grid):
        return True
    else:
        return False


def gameend(grid, player):
    "Return True if the game is either a win or a draw."
    if checkwin(grid):
        print("\nWin for Player: " + str(pl.symbol(player)) + "! Games has ended.")
        return True
    if checkdraw(grid):
        print("\nDraw! Game has ended.")
        return True
    else:
        return False


def abort(player):
    print("Aborting move from player " +
          str(pl.symbol(player)) + "! Games has ended.")
    # break
