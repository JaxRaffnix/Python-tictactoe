# Goal: Implement tic tac toe for the command line.
#       Incldues win/draw-detection and random starting player selection.
#       Switch between two player mode and pc, includes AI that does random moves
# Requirements: python random plckage

import game as game
import grid as gr

def gamehelp():
    print("Solo modus is the default. The AI plays random.\n" + 
          "You have the following options:\n" +
          "- help text\t\t'help'\n" + 
          "- swap the symbols for player 1 and 2\t'symbolselect'\n" +
          "- two player modus\t'twoplayer'\n" + 
          "- solo modus vs AI\t'oneplayer'\n" +
          "- start a game\t\t'start'\n" + 
          "- exit a game \t\t'q'\n" + 
          "- end the program\t'exit'")
    
def playerselect():
    "prompt the user to pick a color"

games = 1
aimode = True

print("Welcome to tic-tac-toe!")
gamehelp()
while True:
    prompt = input("\nGame Options: ")
    if prompt == "help":
        gamehelp()
        continue
    if prompt == "oneplayer":
        aimode = True
        continue
    if prompt == "twoplayer":
        aimode = False
        continue
    if prompt == "start":
        print("\nGAME", games)
        grid = gr.creategrid()
        game.turn(grid, aimode)
        games += 1
        continue
    if prompt == "exit":
        print("Program has been terminated.")
        break
    else:
        print("Error, wrong input. Try again.")
