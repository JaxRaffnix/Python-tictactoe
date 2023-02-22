# Goal: Implement tic tac toe for command line.

grid = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]

def print_grid():
    print(grid[0] + "|" + grid[1] + "|" + grid[2])
    print(grid[3] + "|" + grid[4] + "|" + grid[5])
    print(grid[6] + "|" + grid[7] + "|" + grid[8])

print_grid()