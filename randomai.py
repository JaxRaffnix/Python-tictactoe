import player as pl
import random


def aimove(board):
    "Choose a random, valid grid and return the choice."
    selection = []
    for i in board:
        if i != pl.symbol(1) and i != pl.symbol(2):
            selection += i

    if "5" in selection:
        choice = int("5")
    else:
        choice = int(random.choice(selection))

    return (choice - 1)
