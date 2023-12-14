import os
import pygame
from game_pieces import *
from constants import *

class GameBoard:
    def __init__(self, orientation):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.selected_tile = None
        self.orientation = orientation
        white_oriented_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        black_oriented_order = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]
        self.king = None # later initialised for quicker retrieval
        self.opponent_king = None # later initialised for quicker retrieval
        self.turn = PieceColor.WHITE
        if self.orientation == PieceColor.WHITE:
            for i, piece in enumerate(white_oriented_order):
                self.__add_piece(piece(i, 0, PieceColor.BLACK))
                self.__add_piece(Pawn(i, 1, PieceColor.BLACK))
                self.__add_piece(Pawn(i, 6, PieceColor.WHITE))
                self.__add_piece(piece(i, 7, PieceColor.WHITE))
                self.king = self.get_piece((4,7))
                self.opponent_king = self.get_piece((4,0))
        elif self.orientation == PieceColor.BLACK:
            for i, piece in enumerate(black_oriented_order):            
                self.__add_piece(piece(i, 0, PieceColor.WHITE))
                self.__add_piece(Pawn(i, 1, PieceColor.WHITE))
                self.__add_piece(Pawn(i, 6, PieceColor.BLACK))
                self.__add_piece(piece(i, 7, PieceColor.BLACK))
                self.king = self.get_piece((3,7))
                self.opponent_king = self.get_piece((3,0))
        self.game_assets = {
            PieceColor.BLACK : {
                King : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/king_black.png'), (100, 100)),
                Queen : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/queen_black.png'), (100, 100)),
                Rook : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/rook_black.png'), (100, 100)),
                Bishop : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/bishop_black.png'), (100, 100)),
                Knight : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/knight_black.png'), (100, 100)),
                Pawn : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/pawn_black.png'), (100, 100))
            },
            PieceColor.WHITE : {
                King : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/king_white.png'), (100, 100)),
                Queen : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/queen_white.png'), (100, 100)),
                Rook : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/rook_white.png'), (100, 100)),
                Bishop : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/bishop_white.png'), (100, 100)),
                Knight : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/knight_white.png'), (100, 100)),
                Pawn : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/pawn_white.png'), (100, 100))
            }
        }

    def draw(self, screen):
        # draw overlayed board
        screen.fill(BLACK)
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(screen, WHITE, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))
        # draw pieces to screen
        white_oriented_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        black_oriented_order = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]
        if self.orientation == PieceColor.WHITE:
            for i, piece in enumerate(white_oriented_order):
                screen.blit(self.game_assets[PieceColor.BLACK][piece], (i*100, 0))
                screen.blit(self.game_assets[PieceColor.BLACK][Pawn], (i*100, 100))
                screen.blit(self.game_assets[PieceColor.WHITE][Pawn], (i*100, 600))
                screen.blit(self.game_assets[PieceColor.WHITE][piece], (i*100, 700))
        elif self.orientation == PieceColor.BLACK:
            for i, piece in enumerate(black_oriented_order):
                screen.blit(self.game_assets[PieceColor.WHITE][piece], (i*100, 0))
                screen.blit(self.game_assets[PieceColor.WHITE][Pawn], (i*100, 100))
                screen.blit(self.game_assets[PieceColor.BLACK][Pawn], (i*100, 600))
                screen.blit(self.game_assets[PieceColor.BLACK][piece], (i*100, 700))

    def draw_tile(self, screen, tile : (int, int)):
        x, y = tile
        pygame.draw.rect(screen, WHITE, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))
        piece = self.get_piece(tile)
        if piece:
            sprite = self.game_assets[piece.getColor()][piece.__class__]
            screen.blit(sprite, (100*x,100*y))

    def highlight_tile(self, screen, tile : (int, int)):
        x, y = tile
        pygame.draw.rect(screen, GREEN, pygame.Rect(100*x, 100*y, 100, 100))
        pygame.draw.rect(screen, WHITE, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))
        self.draw_tile(screen, tile)

    def unhighlight_tile(self, screen, tile : (int, int)):
        x, y = tile
        pygame.draw.rect(screen, BLACK, pygame.Rect(100*x, 100*y, 100, 100))
        pygame.draw.rect(screen, WHITE, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))
        self.draw_tile(screen, tile)

    def __add_piece(self, piece : ChessPiece):
        x, y = piece.getX(), piece.getY()
        if self.board[y][x] != None:
            raise LookupError("Piece already exists at provided tile.")
        self.board[y][x] = piece

    def get_piece(self, tile : (int, int)) -> ChessPiece:
        return self.board[tile[1]][tile[0]]

    # returns false if move invalid else returns true
    def makeMove(self, from_coord : (int, int), to_coord : (int, int)) -> bool:
        selected_piece = self.board[from_coord[1]][from_coord[0]]
        valid = selected_piece.isMoveValid(self, to_coord)
        if valid:
            self.board[to_coord[1]][to_coord[0]] = selected_piece
            selected_piece.x, selected_piece.y = to_coord[0], to_coord[1]
            self.board[from_coord[1]][from_coord[0]] = None
            selected_piece.move_count += 1
        return valid

    def makeOpponentMove(self, from_coord : (int, int), to_coord : (int, int)) -> bool:
        selected_piece = self.board[from_coord[1]][from_coord[0]]
        self.board[to_coord[1]][to_coord[0]] = selected_piece
        selected_piece.x, selected_piece.y = to_coord[0], to_coord[1]
        self.board[from_coord[1]][from_coord[0]] = None

    # if click event triggers a move on player's turn, return that move, else return none
    def process_click_event(self, screen, click_coord : (int, int)):
        clicked_tile = (click_coord[0] // 100, click_coord[1] // 100)
        clicked_piece = self.get_piece(clicked_tile)
        if self.selected_tile == clicked_tile: # unselect tile
            self.unhighlight_tile(screen, self.selected_tile)
            self.selected_tile = None
        elif clicked_piece and clicked_piece.getColor() == self.orientation: # select tile (own piece)
            if self.selected_tile: self.unhighlight_tile(screen, self.selected_tile)
            self.selected_tile = clicked_tile
            self.highlight_tile(screen, clicked_tile)
        elif self.selected_tile and self.turn == self.orientation and self.makeMove(self.selected_tile, clicked_tile): # select a move
            self.unhighlight_tile(screen, self.selected_tile)
            self.draw_tile(screen, clicked_tile)
            self.turn = PieceColor.BLACK if self.turn == PieceColor.WHITE else PieceColor.WHITE
            print(f"move made, turn is now {self.turn}")
            move = (self.selected_tile, clicked_tile)
            self.selected_tile = None
            return move
        return None
    
    def process_opponent_move(self, screen, move : ((int, int), (int, int))):
        from_coord, to_coord = move
        self.makeOpponentMove(from_coord, to_coord)
        self.draw_tile(screen, from_coord)
        self.draw_tile(screen, to_coord)
        self.turn = PieceColor.BLACK if self.turn == PieceColor.WHITE else PieceColor.WHITE
        print(f"opponent made move turn is now {self.turn}")
        
    def inCheck(self):
        x, y = self.king.x, self.king.y
        # determine if king is checked by adjacent king
        if abs(x - self.opponent_king.x) < 2 and abs(y - self.opponent_king.y) < 2:
            return True
        # determine if king is checked by adjacent knight
        positions = [(x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2), (x - 1, y - 2), (x + 1, y + 2), (x + 1, y - 2)]
        for position in positions:
            piece = self.get_piece(position)
            if piece and isinstance(piece, Knight) and piece.getColor() != self.orientation:
                return True
        # determine if king is checked by adjacent pawns
        positions = [(x - 1, y - 1), (x + 1, y - 1)]
        for position in positions:
            piece = self.get_piece(position)
            if piece and isinstance(piece, Pawn) and piece.getColor() != self.orientation:
                return True
        # determine if king is checked vertically or horizontally by rook or queen
        left, right, up, down = (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)
        left_piece = right_piece = up_piece = down_piece = None
        while left_piece == None and left[0] >= 0:
            left_piece = self.get_piece(left)
            left[0] -= 1
        while right_piece == None and right[0] <= 7:
            right_piece = self.get_piece(right)
            right[0] += 1
        while up_piece == None and up[1] >= 0:
            up_piece = self.get_piece(up)
            up[1] -= 1
        while down_piece == None and down[1] <= 7:
            down_piece = self.get_piece(down)
            down[1] += 1
        type_list = [type(piece) for piece in [left_piece, right_piece, up_piece, down_piece] if piece.getColor() != self.orientation]
        if Rook in type_list or Queen in type_list:
            return True
        # determine if king is checked diagonally by bishop or queen
        left_up, right_up, left_down, right_down = (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)
        left_up_piece = right_up_piece = left_down_piece = right_down_piece = None
        while left_up_piece == None and left_up[0] >= 0 and left_up[1] >= 0:
            left_piece = self.get_piece(left_up)
            left_up[0] -= 1
            left_up[1] -= 1
        while right_up_piece == None and right_up[0] <= 7 and right_up[1] >= 0 :
            right_piece = self.get_piece(right_up)
            right_up[0] += 1
            right_up[1] -= 1
        while left_down_piece == None and left_down[0] >= 0 and left_down[1] <= 7:
            left_down_piece = self.get_piece(left_down)
            left_down[0] -= 1
            left_down[1] += 1
        while right_down_piece == None and right_down[0] <= 7 and right_down[1] <= 7:
            right_down_piece = self.get_piece(right_down)
            right_down[0] += 1
            right_down[1] += 1
        type_list = [type(piece) for piece in [left_up_piece, right_up_piece, left_down_piece, right_down_piece] if piece.getColor() != self.orientation]
        if Bishop in type_list or Queen in type_list:
            return True