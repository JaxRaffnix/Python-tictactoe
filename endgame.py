import player as pl


def checkwin(board):
    "Check if a win condition is met."
    winconditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8],   # horizontal
                     [0, 3, 6], [1, 4, 7], [2, 5, 8],   # vertical
                     [0, 4, 8], [2, 4, 6]]              # diagonal
    for list in winconditions:
        if all(board[i] == pl.symbol(1) for i in list) or all(board[i] == pl.symbol(2) for i in list):
            return True


def checkdraw(board):
    "check if every grid is filled out."
    if all((i == pl.symbol(1)) or (i == pl.symbol(2)) for i in board):
        return True


def checkabort(grid):
    "Return True if argument is abort sequence"
    if grid == pl.abort_sequence:
        return True
