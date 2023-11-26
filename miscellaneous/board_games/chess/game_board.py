from typing import List
from game_pieces import *

class GameBoard:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.selected_tile = None
        self.orientation = PieceColor.WHITE
        self.__add_pieces([
            Rook(0,0, PieceColor.BLACK), Knight(1,0, PieceColor.BLACK), Bishop(2,0, PieceColor.BLACK), Queen(3,0, PieceColor.BLACK),
            King(4,0, PieceColor.BLACK), Bishop(5,0, PieceColor.BLACK), Knight(6,0, PieceColor.BLACK), Rook(7,0, PieceColor.BLACK)]
        )
        self.__add_pieces([
            Rook(0,7, PieceColor.WHITE), Knight(1,7, PieceColor.WHITE), Bishop(2,7, PieceColor.WHITE), Queen(3,7, PieceColor.WHITE),
            King(4,7, PieceColor.WHITE), Bishop(5,7, PieceColor.WHITE), Knight(6,7, PieceColor.WHITE), Rook(7,7, PieceColor.WHITE)]
        )
        for i in range(8):
            self.__add_piece(Pawn(i,1, PieceColor.BLACK))
            self.__add_piece(Pawn(i,6, PieceColor.WHITE))

    def get_selected_tile(self):
        return self.selected_tile
    
    def set_selected_tile(self, tile: (int, int)):
        self.selected_tile = tile

    def get_orientation(self):
        return self.orientation

    def __add_piece(self, piece : ChessPiece):
        x, y = piece.getX(), piece.getY()
        if self.board[y][x] != None:
            raise LookupError("Piece already exists at provided tile.")
        self.board[y][x] = piece
    
    def __add_pieces(self, pieces : List[ChessPiece]):
        for piece in pieces:
            x, y = piece.getX(), piece.getY()
            if self.board[y][x] != None:
                raise LookupError("Piece already exists at provided tile.")
            self.board[y][x] = piece

    def get_piece(self, tile : (int, int)) -> ChessPiece:
        return self.board[tile[1]][tile[0]]

    # returns false if move invalid else returns true
    def makeMove(self, to_coord : (int, int)) -> bool:
        selected_piece = self.board[self.selected_tile[1]][self.selected_tile[0]]
        if selected_piece == None:
            raise LookupError("Chess piece not found at selected tile")
        valid = selected_piece.isMoveValid(self, to_coord)
        if valid:
            self.board[to_coord[1]][to_coord[0]] = selected_piece
            selected_piece.x, selected_piece.y = to_coord[0], to_coord[1]
            self.board[self.selected_tile[1]][self.selected_tile[0]] = None
            self.selected_tile = None
            selected_piece.move_count += 1
        return valid