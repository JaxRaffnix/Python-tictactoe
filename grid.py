def creategrid():
    "return the default starting grid"
    defaultgrid = ["1", "2", "3",
                   "4", "5", "6",
                   "7", "8", "9",]
    return defaultgrid


def printgrid(grid):
    "print the current grid to the console"
    print(grid[0] + "|" + grid[1] + "|" + grid[2])
    print(grid[3] + "|" + grid[4] + "|" + grid[5])
    print(grid[6] + "|" + grid[7] + "|" + grid[8])
