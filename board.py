def createboard():
    "return the default starting board"
    defaultboard = ["1", "2", "3",
                   "4", "5", "6",
                   "7", "8", "9",]
    return defaultboard


def printboard(board):
    "print the current board to the console"
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])
