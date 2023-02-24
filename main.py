# Goal: Implement tic tac toe for the command line.
#       Incldues win/draw-detection and random starting player selection.
#       Switch between two player mode and pc, includes AI that does random moves
# Requirements: python random plckage

import game as game
import board as bd
import player as pl

def gamehelp():
    print("Solo mode is the default. The AI plays random.\n" + 
          "You have the following options:\n" +
          "- help text\t\t'help'\n" + 
          "- switch symbols\t'switchmark'\n" +
          "- two player mode\t'twoplayer'\n" + 
          "- solo mode vs AI\t'singleplayer'\n" +
          "- start a game\t\t'start'\n" + 
          "- exit a game in grid prompt\t'q'\n" + 
          "- end the program\t'exit'")

def scoreboard(wincounter):
    print("\nScoreboard\n" + 
          "Draws\tPlayer " + str(pl.symbol(1)) + "\tPlayer " + str(pl.symbol(2)) + "\n" +
          str(wincounter[0]) + "\t" + str(wincounter[1]) + "\t\t" + str(wincounter[2]))

# defaults
games = 1
aimode = True
wincounter = [0,0,0]
print("Welcome to tic-tac-toe!")
gamehelp()
while True:
    scoreboard(wincounter)
    prompt = input("Choose an option: ")
    if prompt == "help":
        gamehelp()
        continue
    if prompt == "singleplayer":
        aimode = True
        continue
    if prompt == "twoplayer":
        aimode = False
        continue
    if prompt == "switchmark":
        pl.switchmark()
        continue
    if prompt == "start":
        print("\nGAME", games)
        board = bd.createboard()
        gameresult = game.game(board, aimode)
        wincounter[gameresult] += 1
        games += 1
        continue
    if prompt == "exit":
        print("Program has been terminated.")
        break
    else:
        print("Error, unknown input. Try again.")
