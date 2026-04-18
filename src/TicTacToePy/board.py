size = 3

class Board:
    cells = []

    def __init__(self):
        self.cells = [0] * (size * size)
        pass

    def Insert(self, slot : int, piece : int):
        if not 0 <= slot <= size*size - 1:
            raise IndexError
        if not 0 <= piece <= 1:
            raise ValueError
        
        self.cells[slot] = piece + 1

    def CheckFilled(self, slot : int):
        if not (0 <= slot <= size*size - 1):
            raise IndexError
        
        return self.cells[slot] != 0

    def Print(self):
        pieceMap = {
            0 : '_',
            1 : 'O',
            2 : 'X'
        }

        result = ""
        for i in range(0, size)[::-1]:
            for j in range(size):
                result += f'{pieceMap[self.cells[i * size + j]]}'
                result += ' | ' if j != size - 1 else ''
            result += '\n' if i != 0 else ''

        return result