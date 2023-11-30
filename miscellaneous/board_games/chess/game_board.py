import pygame
from game_pieces import *
from constants import *

class GameBoard:
    def __init__(self, orientation):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.selected_tile = None
        self.orientation = orientation
        default_piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece in enumerate(default_piece_order):
            if self.orientation == PieceColor.BLACK:
                self.__add_piece(piece(i, 0, PieceColor.WHITE))
                self.__add_piece(Pawn(i, 1, PieceColor.WHITE))
                self.__add_piece(Pawn(i, 6, PieceColor.BLACK))
                self.__add_piece(piece(i, 7, PieceColor.BLACK))
            else:
                self.__add_piece(piece(i, 0, PieceColor.BLACK))
                self.__add_piece(Pawn(i, 1, PieceColor.BLACK))
                self.__add_piece(Pawn(i, 6, PieceColor.WHITE))
                self.__add_piece(piece(i, 7, PieceColor.WHITE))

    def draw(self, screen, game_assets):
        # draw overlayed board
        screen.fill(BLACK)
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(screen, WHITE, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))
        # draw pieces to screen
        default_piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece in enumerate(default_piece_order):
            if self.get_orientation() == PieceColor.BLACK:
                screen.blit(game_assets[PieceColor.WHITE][piece], (i*100, 0))
                screen.blit(game_assets[PieceColor.WHITE][Pawn], (i*100, 100))
                screen.blit(game_assets[PieceColor.BLACK][Pawn], (i*100, 600))
                screen.blit(game_assets[PieceColor.BLACK][piece], (i*100, 700))
            else:
                screen.blit(game_assets[PieceColor.BLACK][piece], (i*100, 0))
                screen.blit(game_assets[PieceColor.BLACK][Pawn], (i*100, 100))
                screen.blit(game_assets[PieceColor.WHITE][Pawn], (i*100, 600))
                screen.blit(game_assets[PieceColor.WHITE][piece], (i*100, 700))

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