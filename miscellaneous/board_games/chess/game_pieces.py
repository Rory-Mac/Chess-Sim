from abc import abstractmethod
from enum import Enum

class PieceColor(Enum):
    WHITE = 0
    BLACK = 1

class ChessPiece:
    def __init__(self, x : int, y : str, color : PieceColor):
        self.color = color
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getColor(self):
        return self.color

    def isMoveValid(self, to_coord : (int, int)) -> bool:
        x, y = to_coord[0], to_coord[1]
        if not (0 <= x <= 7 and 0 <= y <= 7):
            raise ValueError("Cannot move piece to tile that does not exist.")
        return self.inRange(x, y)

    @abstractmethod
    def inRange(self, x : int, y : int) -> bool:
        pass

class King(ChessPiece):
    def inRange(self, x : int, y : int) -> bool:
        dx = abs(self.x - x)
        dy = abs(self.y - y)
        return 0 <= dx <= 1 and 0 <= dy <= 1 and (dx != 0 or dy != 0)

class Queen(ChessPiece):
    def inRange(self, x : int, y : int) -> bool:
        dx = abs(self.x - x)
        dy = abs(self.y - y)
        return (dx == 0 and dy != 0) or (dy == 0 and dx != 0) or (dx == dy)

class Knight(ChessPiece):
    def inRange(self, x : int, y : int) -> bool:
        dx = abs(self.x - x)
        dy = abs(self.y - y)
        return (dx == 1 and dy == 2) or (dy == 1 and dx == 2)

class Rook(ChessPiece):
    def inRange(self, x : int, y : int) -> bool:
        dx = abs(self.x - x)
        dy = abs(self.y - y)
        return (dx == 0 and dy != 0) or (dy == 0 and dx != 0)

class Bishop(ChessPiece):
    def inRange(self, x : int, y : int) -> bool:
        dx = abs(self.x - x)
        dy = abs(self.y - y)
        return (dx == dy) and (dx != 0 or dy != 0)

class Pawn(ChessPiece):
    def inRange(self, x : int, y : int) -> bool:
        dx = abs(self.x - x)
        return (self.y - y == 1) and dx <= 1
