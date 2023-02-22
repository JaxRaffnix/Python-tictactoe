import random
import player as pl


def aimove(grid):
    "Choose a random, valid field and return the choice."
    selection = []
    for i in grid:
        if i != pl.symbol(1) and i != pl.symbol(2):
            selection += i

    if "5" in selection:
        choice = int("5")
    else:
        choice = int(random.choice(selection))

    return choice - 1
