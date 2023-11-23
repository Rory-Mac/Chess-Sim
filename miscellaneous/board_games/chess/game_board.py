from abc import abstractmethod
from enum import Enum
from typing import List

class PieceColor(Enum):
    WHITE = 0
    BLACK = 1

def rank_to_x(rank : int) -> int:
    return 8 - rank
    
def file_to_y(file : str) -> int:
    return ord(file) - ord('a')

class ChessPiece:
    # rank 1-8, file a-h
    def __init__(self, rank : int, file : str, color : PieceColor):
        self.color = color
        self.rank = rank
        self.file = file
        self.x = rank_to_x(rank)
        self.y = file_to_y(file)

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getColor(self):
        return self.color

    def isMoveValid(self, x : int, y : int) -> bool:
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
        dy = abs(self.y - y)
        return (dx == dy) and (dx != 0 or dy != 0)

class GameBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.__add_pieces(
            Rook(0,0, PieceColor.BLACK), Knight(0,1, PieceColor.BLACK), Bishop(0,2, PieceColor.BLACK), Queen(0,3, PieceColor.BLACK),
            King(0,4, PieceColor.BLACK), Bishop(0,5, PieceColor.BLACK), Knight(0,6, PieceColor.BLACK), Rook(0,7, PieceColor.BLACK)
        )
        self.__add_pieces(
            Rook(7,0, PieceColor.WHITE), Knight(7,1, PieceColor.WHITE), Bishop(7,2, PieceColor.WHITE), Queen(7,3, PieceColor.WHITE),
            King(7,4, PieceColor.WHITE), Bishop(7,5, PieceColor.WHITE), Knight(7,6, PieceColor.WHITE), Rook(7,7, PieceColor.WHITE)
        )
        for i in range(8):
            self.__add_piece(Pawn(0,i, PieceColor.BLACK), 0,i)
            self.__add_piece(Pawn(7,i, PieceColor.WHITE), 7,i)

    def __add_piece(self, piece : ChessPiece):
        x, y = piece.getX(), piece.getY()
        if self.board[x][y] != None:
            raise LookupError("Piece already exists at provided tile.")
        self.board[x][y] = piece
    
    def __add_pieces(self, pieces : List[ChessPiece]):
        for piece in pieces:
            x, y = piece.getX(), piece.getY()
            if self.board[x][y] != None:
                raise LookupError("Piece already exists at provided tile.")
            self.board[x][y] = piece

    # returns false if move invalid else returns true
    def makeMove(self, position_from : (int, int), position_to : (int, int)) -> bool:
        from_x, from_y = position_from[0], position_from[1]
        to_x, to_y = position_to[0], position_to[1]
        tile_to, tile_from = self.board[to_x][to_y], self.board[from_x][from_y]
        if not tile_from:
            raise LookupError("Cannot move a piece that doesn't exist.")
        if not tile_from.isMoveValid(): 
            raise ValueError("This piece cannot move in this way")
        if tile_to and tile_from.getColor() == tile_to.getColor():
            raise LookupError("You cannot take your own pieces.")
        self.board[to_x][to_y] = tile_from
        return True