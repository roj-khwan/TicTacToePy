from TicTacToePy.board import Board

class Game():
    turn = 0
    side = 0
    board = None

    def __init__(self):
        self.board = Board()

    def Display(self):
        print(self.board.Print())

    def Run(self, slot : int):
        self.board.Insert(slot, self.side)
        self.turn += 1
        self.SwitchTurn()

    def RunForceSide(self, slot : int, side : int):
        if not (0 <= side <= 1):
            raise ValueError
        
        self.side = side
        self.Run(slot)

    def SwitchTurn(self):
        self.side = 1 - self.side #swtiching 0 -> 1, 1 -> 0

    def TryParseMove(self, move:str):
        try:
            move = int(move)
        except ValueError:
            return False, "not integer"
        
        if not (1 <= move <= 9): return False, "out of bound (1 - 9)"

        move = move - 1 # turn 1 - 9 to 0 - 8

        if self.board.CheckFilled(move): return False, "cell filled"

        return True, move