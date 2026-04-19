from TicTacToePy.board import Board

class Game():
    
    def __init__(self):
        self.board = Board()
        self.turn = 0 # counter
        self.side = 0 # 0 : O | 1 : X

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

        if self.board.CheckCellFilled(move): return False, "cell filled"

        return True, move
    
    def CheckWin(self):
        patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]

        for pattern in patterns:
            align, piece = self.board.CheckPattern(*pattern)

            if piece != 0 and align:
                return True, piece
            
        return False, None

    def CheckSideWin(self, side : int):
        win, piece = self.CheckWin()
        
        return win and piece == side + 1
    
    def Reset(self):
        self.board = Board()
        self.turn = 0 # counter
        self.side = 0 # 0 : O | 1 : X
