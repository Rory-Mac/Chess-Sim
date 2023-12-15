import os
import pygame
import winsound
from game_pieces import *
from constants import *


class GameBoard:
    def __init__(self, orientation):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.selected_tile = None
        self.player_prev_move = ((-1,-1),(-1,-1)) # dummy initialisation
        self.opponent_prev_move = ((-1,-1),(-1,-1)) # dummy initialisation
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
                King : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/king_black.svg'), (45, 45)),
                Queen : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/queen_black.svg'), (45, 45)),
                Rook : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/rook_black.svg'), (45, 45)),
                Bishop : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/bishop_black.svg'), (45, 45)),
                Knight : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/knight_black.svg'), (45, 45)),
                Pawn : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/pawn_black.svg'), (45, 45))
            },
            PieceColor.WHITE : {
                King : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/king_white.svg'), (45, 45)),
                Queen : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/queen_white.svg'), (45, 45)),
                Rook : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/rook_white.svg'), (45, 45)),
                Bishop : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/bishop_white.svg'), (45, 45)),
                Knight : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/knight_white.svg'), (45, 45)),
                Pawn : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/pawn_white.svg'), (45, 45))
            }
        }

    def get_tile_color(self, tile : (int, int)):
        x, y = tile
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
            return LIGHT_TILE
        if (x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1):
            return DARK_TILE

    def draw(self, screen):
        # draw overlayed board
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(screen, self.get_tile_color((x,y)), pygame.Rect(45*x, 45*y, 45, 45))
        # draw pieces to screen
        white_oriented_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        black_oriented_order = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]
        if self.orientation == PieceColor.WHITE:
            for i, piece in enumerate(white_oriented_order):
                screen.blit(self.game_assets[PieceColor.BLACK][piece], (i*45, 0))
                screen.blit(self.game_assets[PieceColor.BLACK][Pawn], (i*45, 45))
                screen.blit(self.game_assets[PieceColor.WHITE][Pawn], (i*45, 6*45))
                screen.blit(self.game_assets[PieceColor.WHITE][piece], (i*45, 7*45))
        elif self.orientation == PieceColor.BLACK:
            for i, piece in enumerate(black_oriented_order):
                screen.blit(self.game_assets[PieceColor.WHITE][piece], (i*45, 0))
                screen.blit(self.game_assets[PieceColor.WHITE][Pawn], (i*45, 45))
                screen.blit(self.game_assets[PieceColor.BLACK][Pawn], (i*45, 6*45))
                screen.blit(self.game_assets[PieceColor.BLACK][piece], (i*45, 7*45))

    def draw_tile(self, screen, tile : (int, int), highlight=False):
        x, y = tile
        tile_color = self.get_tile_color(tile)
        if highlight:
            tile_color = HIGHLIGHTED_DARK_TILE if tile_color == DARK_TILE else HIGHLIGHTED_LIGHT_TILE
        pygame.draw.rect(screen, tile_color, pygame.Rect(45*x, 45*y, 45, 45))
        piece = self.get_piece(tile)
        if piece:
            sprite = self.game_assets[piece.getColor()][piece.__class__]
            screen.blit(sprite, (45*x,45*y))

    def __add_piece(self, piece : ChessPiece):
        x, y = piece.getX(), piece.getY()
        if self.board[y][x] != None:
            raise LookupError("Piece already exists at provided tile.")
        self.board[y][x] = piece

    def get_piece(self, tile) -> ChessPiece:
        if 0 <= tile[0] <= 7 and 0 <= tile[1] <= 7:
            return self.board[tile[1]][tile[0]]
        return None

    # returns false if move invalid else returns true
    def makeMove(self, from_coord : (int, int), to_coord : (int, int)) -> bool:
        selected_piece = self.board[from_coord[1]][from_coord[0]]
        captured_piece = self.board[to_coord[1]][to_coord[0]]
        move_valid = selected_piece.isMoveValid(self, to_coord)
        if move_valid:
            self.board[to_coord[1]][to_coord[0]] = selected_piece
            selected_piece.x, selected_piece.y = to_coord[0], to_coord[1]
            self.board[from_coord[1]][from_coord[0]] = None
            selected_piece.move_count += 1
        if not move_valid: return False
        # if move places king in check, cancel move
        in_check = self.in_danger(self.king)
        if in_check:
            self.board[from_coord[1]][from_coord[0]] = selected_piece
            self.board[to_coord[1]][to_coord[0]] = captured_piece
            selected_piece.x, selected_piece.y = from_coord[0], from_coord[1]
            selected_piece.move_count -= 1
        return not in_check

    def makeOpponentMove(self, from_coord : (int, int), to_coord : (int, int)) -> bool:
        selected_piece = self.board[from_coord[1]][from_coord[0]]
        self.board[to_coord[1]][to_coord[0]] = selected_piece
        selected_piece.x, selected_piece.y = to_coord[0], to_coord[1]
        self.board[from_coord[1]][from_coord[0]] = None

    # if click event triggers a move on player's turn, return that move, else return none
    def process_click_event(self, screen, click_coord : (int, int)):
        clicked_tile = (click_coord[0] // 45, click_coord[1] // 45)
        clicked_piece = self.get_piece(clicked_tile)
        if self.selected_tile == clicked_tile and self.selected_tile not in self.player_prev_move: # unselect tile
            self.draw_tile(screen, self.selected_tile)
            self.selected_tile = None
        elif self.selected_tile and clicked_piece and clicked_piece.getColor() == self.orientation: # select tile (own piece)
            # check for special case where player selects king and then castles
            selected_piece = self.get_piece(self.selected_tile)
            if isinstance(selected_piece, King) and isinstance(clicked_piece, Rook):
                self.castle_if_valid(clicked_piece)
            # unhighlight previously selected tile, highlight newly selected tile
            if self.selected_tile and self.selected_tile not in self.player_prev_move: self.draw_tile(screen, self.selected_tile)
            self.selected_tile = clicked_tile
            self.draw_tile(screen, clicked_tile, highlight=True)
        elif self.selected_tile and self.turn == self.orientation and self.makeMove(self.selected_tile, clicked_tile): # select a move
            # check for special case of pawn promotion
            selected_piece = self.board[clicked_tile[1]][clicked_tile[0]]
            if isinstance(selected_piece, Pawn) and selected_piece.y == 0:
                self.board[selected_piece.y][selected_piece.x] = Queen(selected_piece.x, selected_piece.y, self.orientation)
            # play sound to user
            winsound.PlaySound(os.getcwd() + '\\assets\player_move.wav', winsound.SND_FILENAME)
            # highlight player move
            self.draw_tile(screen, self.selected_tile, highlight=True)
            self.draw_tile(screen, clicked_tile, highlight=True)
            # unhighlight opponent's last move
            self.draw_tile(screen, self.opponent_prev_move[0])
            self.draw_tile(screen, self.opponent_prev_move[1])
            # turn-over, return player move
            self.player_prev_move = (self.selected_tile, clicked_tile)
            self.opponent_prev_move = ((-1,-1),(-1,-1))
            self.turn = PieceColor.BLACK if self.turn == PieceColor.WHITE else PieceColor.WHITE
            move = (self.selected_tile, clicked_tile)
            self.selected_tile = None
            return move
        return None
    
    def process_opponent_move(self, screen, move : ((int, int), (int, int))):
        # process received opponent move
        from_coord, to_coord = move
        self.makeOpponentMove(from_coord, to_coord)
        # check for special case of pawn promotion
        selected_piece = self.board[to_coord[1]][to_coord[0]]
        if isinstance(selected_piece, Pawn) and selected_piece.y == 7: 
            self.board[selected_piece.y][selected_piece.x] = Queen(selected_piece.x, selected_piece.y, self.turn)
        # play sound to user
        winsound.PlaySound(os.getcwd() + '\\assets\opponent_move.wav', winsound.SND_FILENAME)
        # highlight opponent move
        self.draw_tile(screen, from_coord, highlight=True)
        self.draw_tile(screen, to_coord, highlight=True)
        # unhighlight player's previous move
        self.draw_tile(screen, self.player_prev_move[0])
        self.draw_tile(screen, self.player_prev_move[1])
        # turn-over
        self.opponent_prev_move = (from_coord, to_coord)
        self.player_prev_move = ((-1,-1),(-1,-1))
        self.turn = PieceColor.BLACK if self.turn == PieceColor.WHITE else PieceColor.WHITE

    def in_danger(self, piece):
        x, y = piece.x, piece.y
        # determine if piece is endangered by adjacent king
        if abs(x - self.opponent_king.x) < 2 and abs(y - self.opponent_king.y) < 2:
            return True
        # determine if piece is endangered by adjacent knight
        positions = [(x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2), (x - 1, y - 2), (x + 1, y + 2), (x + 1, y - 2)]
        for position in positions:
            piece = self.get_piece(position)
            if piece and isinstance(piece, Knight) and piece.getColor() != self.orientation:
                return True
        # determine if piece is endangered by adjacent pawns
        positions = [(x - 1, y - 1), (x + 1, y - 1)]
        for position in positions:
            piece = self.get_piece(position)
            if piece and isinstance(piece, Pawn) and piece.getColor() != self.orientation:
                return True
        # determine if piece is endangered vertically or horizontally by rook or queen
        left, right, up, down = [x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]
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
        type_list = [type(piece) for piece in [left_piece, right_piece, up_piece, down_piece] \
                     if piece and piece.getColor() != self.orientation]
        if Rook in type_list or Queen in type_list:
            return True
        # determine if piece is endangered diagonally by bishop or queen
        left_up, right_up, left_down, right_down = [x - 1, y - 1], [x + 1, y - 1], [x - 1, y + 1], [x + 1, y + 1]
        left_up_piece = right_up_piece = left_down_piece = right_down_piece = None
        while left_up_piece == None and left_up[0] >= 0 and left_up[1] >= 0:
            left_up_piece = self.get_piece(left_up)
            left_up[0] -= 1
            left_up[1] -= 1
        while right_up_piece == None and right_up[0] <= 7 and right_up[1] >= 0 :
            right_up_piece = self.get_piece(right_up)
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
        type_list = [type(piece) for piece in [left_up_piece, right_up_piece, left_down_piece, right_down_piece] \
                     if piece and piece.getColor() != self.orientation]
        if Bishop in type_list or Queen in type_list:
            return True
        return False
    
    def castle_if_valid(self, rook):
        if not (self.king.move_count == 0 and rook.move_count == 0): 
            return
        positions = []
        if rook.x < self.king.x:
            for i in range(rook.x + 1, self.king.x):
                positions.append((i, 7))
        elif rook.x > self.king.x:
            for i in range(self.king.x + 1, rook.x):
                positions.append((i, 7))
        # check that each position is empty and not being attacked by an opponent piece
        for position in positions:
            if self.get_piece(position) or self.in_danger(position):
                return
        # otherwise, castling is valid, move castle adjacent to king, hop king over castle
        self.board[rook.y][rook.x] = None
        self.board[7][self.king.x] = None
        if rook.x < self.king.x:
            self.board[7][self.king.x - 1] = rook
            rook.x = self.king.x - 1
            self.board[7][self.king.x - 2] = self.king
            self.king.x -= 2
            # draw over previous king and rook positions
            self.draw_tile((0, 7))
            self.draw_tile((self.king.x + 2, 7))
        elif rook.x > self.king.x:
            self.board[7][self.king.x + 1] = rook
            rook.x = self.king.x + 1
            self.board[7][self.king.x + 2] = self.king
            self.king.x += 2
            # draw over previous king and rook positions
            self.draw_tile((7, 7))
            self.draw_tile((self.king.x - 2, 7))
        # draw new positions of king and rook
        self.draw_tile((rook.x, rook.y))
        self.draw_tile((self.king.x, self.king.y))
