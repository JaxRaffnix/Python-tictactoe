# Goal: Implement tic tac toe for the command line.
#       Incldues win/draw-detection and random starting player selection.
#       Switch between two player mode and pc, includes AI that does random moves
# Requirements: python random package

import game as pt
import grid as gr

games = 1
aimode = True
print("Welcome to tic-tac-toe!")
print("You have the following options:\n- two player modus\t'twoplayer'\n- one player modus\t'oneplayer'\n- start a game\t\t'start'\n- exit a game and take a Loose\t'q'\n- end the program\t'exit'")

while True:
    prompt = input("\nGame Options: ")
    if prompt == "oneplayer":
        aimode = True
    if prompt == "twoplayer":
        aimode = False
    if prompt == "start":
        print("\nGAME", games)
        grid = gr.creategrid()
        pt.turns(grid, aimode)
        games += 1
        continue
    if prompt == "exit":
        print("Games has been terminated.")
        break
    else:
        print("Error, wrong input. Try again.")

