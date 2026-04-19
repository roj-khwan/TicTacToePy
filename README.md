# Tic-Tac-Toe-PY

A simple tic tac toe python module for a fun game, you able to use the module for other reason, such as AI training, Bot Testing, Game Implementation, etc.

## Requirements
- Python >= 3.11

## How to run
- Open Terminal in the project folder
- Run this if you were on Linux
```bash
python -m venv venv
source venv/bin/activate
pip install -e .
python -m TicTacToePy.main
```
- the game board will appear, the first turn will be of O side. play as instruct by the diagram that is show on the screen, and play until any side win!!! <small>or tie I don't care.</small>

## How this work?
> do not be dissapoint but I just make all of this in one shot of coffee...
### Board (board.py)
Board class in board.py will handle normal board logic, hold the piece, check empty, parse data to readable, etc.
### Game (game.py)
Game is the main of the project, Game will handle win/lose logic, play, print board, handle parsing player input to move, etc.
### TicTacToe Main (TicTacToe.main.py)
Main will handle the game cycle for player input and validity of the move base on Game's function.

