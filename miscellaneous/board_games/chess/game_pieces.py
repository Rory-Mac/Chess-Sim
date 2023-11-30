from abc import abstractmethod
from constants import *

class ChessPiece:
    def __init__(self, x : int, y : str, color : PieceColor):
        self.color = color
        self.move_count = 0
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getColor(self):
        return self.color

    def isMoveValid(self, board, to_coord : (int, int)) -> bool:
        return self.isValid(board, to_coord) and self.isInRange(to_coord) and not self.isBlocked(board, to_coord)

    # default method, overriden by class Pawn
    def isValid(self, board, to_coord : (int, int)) -> bool:
        target_piece = board.get_piece(to_coord)
        return not target_piece or (target_piece and target_piece.getColor() != board.get_orientation())

    @abstractmethod
    def isInRange(self, to_coord : (int, int)) -> bool:
        pass

    # default method, overriden by classes King, Knight, Pawn  
    def isBlocked(self, board, coord : (int, int)) -> bool:
        target_x, target_y = coord
        # if moving vertically
        if self.x == target_x:
            initial_y, final_y = (self.y + 1, target_y) if self.y < target_y else (target_y + 1, self.y)
            for current_y in range(initial_y, final_y):
                if board.get_piece((self.x, current_y)):
                    return True
            return False
        # if moving horizontally 
        if self.y == target_y:
            initial_x, final_x = (self.x + 1, target_x) if self.x < target_x else (target_x + 1, self.x)
            for current_x in range(initial_x, final_x):
                if board.get_piece((current_x, self.y)):
                    return True
            return False
        # if moving diagonally (towards upper-left)
        if self.x > target_x and self.y > target_y:
            curr_x = self.x - 1
            curr_y = self.y - 1
            while curr_x != target_x and curr_y != target_y:
                if board.get_piece((curr_x, curr_y)):
                    return True
                curr_x -= 1
                curr_y -= 1
        # if moving diagonally (towards upper-right)
        elif self.x < target_x and self.y > target_y:
            curr_x = self.x + 1
            curr_y = self.y - 1
            while curr_x != target_x and curr_y != target_y:
                if board.get_piece((curr_x, curr_y)):
                    return True
                curr_x += 1
                curr_y -= 1
        # if moving diagonally (towards lower-left)
        elif self.x > target_x and self.y < target_y:
            curr_x = self.x - 1
            curr_y = self.y + 1
            while curr_x != target_x and curr_y != target_y:
                if board.get_piece((curr_x, curr_y)):
                    return True
                curr_x -= 1
                curr_y += 1
        # if moving diagonally (towards lower-right)
        elif self.x < target_x and self.y < target_y:
            curr_x = self.x + 1
            curr_y = self.y + 1
            while curr_x != target_x and curr_y != target_y:
                if board.get_piece((curr_x, curr_y)):
                    return True
                curr_x += 1
                curr_y += 1
        return False

class King(ChessPiece):
    def isInRange(self, coord : (int, int)) -> bool:
        dx = abs(self.x - coord[0])
        dy = abs(self.y - coord[1])
        return 0 <= dx <= 1 and 0 <= dy <= 1 and (dx != 0 or dy != 0)

    def isBlocked(self, board, coord : (int, int)) -> bool:
        return False

class Queen(ChessPiece):
    def isInRange(self, coord : (int, int)) -> bool:
        dx = abs(self.x - coord[0])
        dy = abs(self.y - coord[1])
        return (dx == 0 and dy != 0) or (dy == 0 and dx != 0) or (dx == dy)

class Knight(ChessPiece):
    def isInRange(self, coord : (int, int)) -> bool:
        dx = abs(self.x - coord[0])
        dy = abs(self.y - coord[1])
        return (dx == 1 and dy == 2) or (dy == 1 and dx == 2)
    
    def isBlocked(self, board, coord : (int, int)) -> bool:
        return False

class Rook(ChessPiece):
    def isInRange(self, coord : (int, int)) -> bool:
        dx = abs(self.x - coord[0])
        dy = abs(self.y - coord[1])
        return (dx == 0 and dy != 0) or (dy == 0 and dx != 0)

class Bishop(ChessPiece):
    def isInRange(self, coord : (int, int)) -> bool:
        dx = abs(self.x - coord[0])
        dy = abs(self.y - coord[1])
        return (dx == dy) and (dx != 0 or dy != 0)

class Pawn(ChessPiece):
    def isValid(self, board, to_coord : (int, int)) -> bool:
        target_piece = board.get_piece(to_coord)
        same_column = self.x == to_coord[0]
        # move is valid if moving forward one tile to empty tile, moving forward two tiles if pawn's first move, 
        # or one tile diagonally to take opponent's piece 
        return (not target_piece and same_column and self.y - to_coord[1] == 1) or \
        (not target_piece and same_column and self.move_count == 0 and self.y - to_coord[1] == 2) or \
        (target_piece and abs(self.x - to_coord[0]) == 1)

    def isInRange(self, coord : (int, int)) -> bool:
        dx = abs(self.x - coord[0])
        return (dx <= 1 and self.y - coord[1] == 1) or (dx == 0 and self.y - coord[1] == 2)

    def isBlocked(self, board, coord : (int, int)) -> bool:
        return False
    
