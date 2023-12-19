from abc import abstractmethod
from constants import *

class ChessPiece:
    def __init__(self, x : int, y : str, color : PieceColor):
        self.color = color
        self.move_count = 0
        self.x = x
        self.y = y

    def move_is_valid(self, board, to_coord : (int, int)) -> bool:
        return self.is_valid(board, to_coord) and self.is_in_range(to_coord) and not self.is_blocked(board, to_coord)

    # default method, overriden by class Pawn
    def is_valid(self, board, to_coord : (int, int)) -> bool:
        target_piece = board.get_piece(to_coord)
        return not target_piece or (target_piece and target_piece.color != board.player_color)

    @abstractmethod
    def is_in_range(self, to_coord : (int, int)) -> bool:
        pass

    # default method, overriden by classes King, Knight, Pawn  
    def is_blocked(self, board, coord : (int, int)) -> bool:
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
    def is_in_range(self, coord : (int, int)) -> bool:
        dx = abs(self.x - coord[0])
        dy = abs(self.y - coord[1])
        return 0 <= dx <= 1 and 0 <= dy <= 1 and (dx != 0 or dy != 0)

    def is_blocked(self, board, coord : (int, int)) -> bool:
        return False

class Queen(ChessPiece):
    def is_in_range(self, coord : (int, int)) -> bool:
        dx = abs(self.x - coord[0])
        dy = abs(self.y - coord[1])
        return (dx == 0 and dy != 0) or (dy == 0 and dx != 0) or (dx == dy)

class Knight(ChessPiece):
    def is_in_range(self, coord : (int, int)) -> bool:
        dx = abs(self.x - coord[0])
        dy = abs(self.y - coord[1])
        return (dx == 1 and dy == 2) or (dy == 1 and dx == 2)
    
    def is_blocked(self, board, coord : (int, int)) -> bool:
        return False

class Rook(ChessPiece):
    def is_in_range(self, coord : (int, int)) -> bool:
        dx = abs(self.x - coord[0])
        dy = abs(self.y - coord[1])
        return (dx == 0 and dy != 0) or (dy == 0 and dx != 0)

class Bishop(ChessPiece):
    def is_in_range(self, coord : (int, int)) -> bool:
        dx = abs(self.x - coord[0])
        dy = abs(self.y - coord[1])
        return (dx == dy) and (dx != 0 or dy != 0)

class Pawn(ChessPiece):
    def is_valid(self, board, coord : (int, int)) -> bool:
        dx = coord[0] - self.x
        dy = self.y - coord[1]
        target_piece = board.get_piece(coord)
        # if moving diagonally one space to capture
        if abs(dx) == 1 and dy == 1 and target_piece:
            return True
        # if moving forward one space
        if dx == 0 and dy == 1 and not board.get_piece((self.x, self.y - 1)):
            return True
        # if moving forward two spaces on first move
        if dx == 0 and dy == 2 and not board.get_piece((self.x, self.y - 1)):
            return True
        return False

    def is_in_range(self, coord : (int, int)) -> bool:
        return True

    def is_blocked(self, board, coord : (int, int)) -> bool:
        return False
