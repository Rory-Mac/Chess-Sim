import os
import pygame
from game_pieces import *
from constants import *

class GameBoard:
    def __init__(self, screen, player_color):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.screen = screen
        self.player_color = player_color
        self.opponent_color = PieceColor.DARK if self.player_color == PieceColor.LIGHT else PieceColor.LIGHT
        self.selected_tile = None
        self.player_prev_move = ((-1,-1),(-1,-1)) # dummy initialisation
        self.opponent_prev_move = ((-1,-1),(-1,-1)) # dummy initialisation
        light_oriented_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        dark_oriented_order = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]
        self.king = None # later initialised for quicker retrieval
        self.opponent_king = None # later initialised for quicker retrieval
        self.turn = PieceColor.LIGHT
        if self.player_color == PieceColor.LIGHT:
            for i, piece in enumerate(light_oriented_order):
                self.__add_piece(piece(i, 0, PieceColor.DARK))
                self.__add_piece(Pawn(i, 1, PieceColor.DARK))
                self.__add_piece(Pawn(i, 6, PieceColor.LIGHT))
                self.__add_piece(piece(i, 7, PieceColor.LIGHT))
                self.king = self.get_piece((4,7))
                self.opponent_king = self.get_piece((4,0))
        elif self.player_color == PieceColor.DARK:
            for i, piece in enumerate(dark_oriented_order):            
                self.__add_piece(piece(i, 0, PieceColor.LIGHT))
                self.__add_piece(Pawn(i, 1, PieceColor.LIGHT))
                self.__add_piece(Pawn(i, 6, PieceColor.DARK))
                self.__add_piece(piece(i, 7, PieceColor.DARK))
                self.king = self.get_piece((3,7))
                self.opponent_king = self.get_piece((3,0))
        self.game_assets = {
            PieceColor.DARK : {
                King : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/king_dark.png'), (TILE_WIDTH, TILE_WIDTH)),
                Queen : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/queen_dark.png'), (TILE_WIDTH, TILE_WIDTH)),
                Rook : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/rook_dark.png'), (TILE_WIDTH, TILE_WIDTH)),
                Bishop : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/bishop_dark.png'), (TILE_WIDTH, TILE_WIDTH)),
                Knight : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/knight_dark.png'), (TILE_WIDTH, TILE_WIDTH)),
                Pawn : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/pawn_dark.png'), (TILE_WIDTH, TILE_WIDTH))
            },
            PieceColor.LIGHT : {
                King : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/king_light.png'), (TILE_WIDTH, TILE_WIDTH)),
                Queen : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/queen_light.png'), (TILE_WIDTH, TILE_WIDTH)),
                Rook : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/rook_light.png'), (TILE_WIDTH, TILE_WIDTH)),
                Bishop : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/bishop_light.png'), (TILE_WIDTH, TILE_WIDTH)),
                Knight : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/knight_light.png'), (TILE_WIDTH, TILE_WIDTH)),
                Pawn : pygame.transform.scale(pygame.image.load(os.getcwd() + '/assets/pawn_light.png'), (TILE_WIDTH, TILE_WIDTH))
            }
        }

    def get_tile_color(self, tile : (int, int)):
        x, y = tile
        if (x % 2 == 0 and y % 2 == 0) or (x % 2 == 1 and y % 2 == 1):
            return LIGHT_TILE
        if (x % 2 == 1 and y % 2 == 0) or (x % 2 == 0 and y % 2 == 1):
            return DARK_TILE

    def draw(self):
        # draw overlayed board
        for x in range(8):
            for y in range(8):
                pygame.draw.rect(self.screen, self.get_tile_color((x,y)), pygame.Rect(TILE_WIDTH*x, TILE_WIDTH*y, TILE_WIDTH, TILE_WIDTH))
        # draw pieces to screen
        light_oriented_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        dark_oriented_order = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]
        if self.player_color == PieceColor.LIGHT:
            for i, piece in enumerate(light_oriented_order):
                self.screen.blit(self.game_assets[PieceColor.DARK][piece], (i*TILE_WIDTH, 0))
                self.screen.blit(self.game_assets[PieceColor.DARK][Pawn], (i*TILE_WIDTH, TILE_WIDTH))
                self.screen.blit(self.game_assets[PieceColor.LIGHT][Pawn], (i*TILE_WIDTH, 6*TILE_WIDTH))
                self.screen.blit(self.game_assets[PieceColor.LIGHT][piece], (i*TILE_WIDTH, 7*TILE_WIDTH))
        elif self.player_color == PieceColor.DARK:
            for i, piece in enumerate(dark_oriented_order):
                self.screen.blit(self.game_assets[PieceColor.LIGHT][piece], (i*TILE_WIDTH, 0))
                self.screen.blit(self.game_assets[PieceColor.LIGHT][Pawn], (i*TILE_WIDTH, TILE_WIDTH))
                self.screen.blit(self.game_assets[PieceColor.DARK][Pawn], (i*TILE_WIDTH, 6*TILE_WIDTH))
                self.screen.blit(self.game_assets[PieceColor.DARK][piece], (i*TILE_WIDTH, 7*TILE_WIDTH))

    def draw_tile(self, tile : (int, int), highlight=False):
        x, y = tile
        tile_color = self.get_tile_color(tile)
        if highlight:
            tile_color = HIGHLIGHTED_DARK_TILE if tile_color == DARK_TILE else HIGHLIGHTED_LIGHT_TILE
        pygame.draw.rect(self.screen, tile_color, pygame.Rect(TILE_WIDTH*x, TILE_WIDTH*y, TILE_WIDTH, TILE_WIDTH))
        piece = self.get_piece(tile)
        if piece:
            sprite = self.game_assets[piece.color][piece.__class__]
            self.screen.blit(sprite, (TILE_WIDTH*x,TILE_WIDTH*y))

    def __add_piece(self, piece : ChessPiece):
        x, y = piece.x, piece.y
        if self.board[y][x] != None:
            raise LookupError("Piece already exists at provided tile.")
        self.board[y][x] = piece

    def on_board(self, tile) -> bool:
        if 0 <= tile[0] <= 7 and 0 <= tile[1] <= 7:
            return True
        return False

    def get_piece(self, tile) -> ChessPiece:
        if 0 <= tile[0] <= 7 and 0 <= tile[1] <= 7:
            return self.board[tile[1]][tile[0]]
        return None

    # returns if move was valid
    def make_move_if_valid(self, move : ((int, int), (int,int))) -> bool:
        from_coord, to_coord = move
        selected_piece = self.board[from_coord[1]][from_coord[0]]
        captured_piece = self.board[to_coord[1]][to_coord[0]]
        if selected_piece.move_is_valid(self, to_coord): 
            self.make_move(move)
            if self.in_danger((self.king.x, self.king.y), self.opponent_color):
                self.cancel_move(move, selected_piece, captured_piece)
                return False
            return True
        return False
    
    def make_move(self, move):
        from_coord, to_coord = move
        selected_piece = self.board[from_coord[1]][from_coord[0]]
        self.board[to_coord[1]][to_coord[0]] = selected_piece
        selected_piece.x, selected_piece.y = to_coord[0], to_coord[1]
        selected_piece.move_count += 1
        self.board[from_coord[1]][from_coord[0]] = None

    def cancel_move(self, move, selected_piece, captured_piece):
        from_coord, to_coord = move
        self.board[from_coord[1]][from_coord[0]] = selected_piece
        self.board[to_coord[1]][to_coord[0]] = captured_piece
        selected_piece.x, selected_piece.y = from_coord[0], from_coord[1]
        selected_piece.move_count -= 1

    def end_player_move(self, move):
        self.player_prev_move = move
        self.opponent_prev_move = ((-1,-1),(-1,-1))
        self.turn = PieceColor.DARK if self.turn == PieceColor.LIGHT else PieceColor.LIGHT
        self.selected_tile = None

    def end_opponent_move(self, move):        
        self.player_prev_move = ((-1,-1),(-1,-1))
        self.opponent_prev_move = move
        self.turn = PieceColor.DARK if self.turn == PieceColor.LIGHT else PieceColor.LIGHT

    def highlight_player_move(self, move):
        # unhighlight opponent's last move
        self.draw_tile(self.opponent_prev_move[0])
        self.draw_tile(self.opponent_prev_move[1])
        # highlight player move
        self.draw_tile(move[0], highlight=True)
        self.draw_tile(move[1], highlight=True)

    def highlight_opponent_move(self, move):
        # unhighlight player's previous move
        self.draw_tile(self.player_prev_move[0])
        self.draw_tile(self.player_prev_move[1])
        # highlight opponent move
        self.draw_tile(move[0], highlight=True)
        self.draw_tile(move[1], highlight=True)

    def highlight_end_game(self):
        checkmated_tile = (self.king.x, self.king.y) if self.in_check_mate() else (self.opponent_king.x, self.opponent_king.y)
        pygame.draw.rect(self.screen, CHECKMATE_TILE, pygame.Rect(TILE_WIDTH*checkmated_tile[0], TILE_WIDTH*checkmated_tile[1], TILE_WIDTH, TILE_WIDTH))
        king = self.get_piece(checkmated_tile)
        sprite = self.game_assets[king.color][King]
        self.screen.blit(sprite, (TILE_WIDTH*king.x, TILE_WIDTH*king.y))

    # if click event triggers a move on player's turn, return that move, else return none
    def process_click_event(self, click_coord : (int, int)):
        clicked_tile = (click_coord[0] // TILE_WIDTH, click_coord[1] // TILE_WIDTH)
        clicked_piece = self.get_piece(clicked_tile)
        if self.selected_tile == clicked_tile and self.selected_tile not in self.player_prev_move: # unselect player piece
            self.draw_tile(self.selected_tile)
            self.selected_tile = None
        elif clicked_piece and clicked_piece.color == self.player_color: # select player piece
            # check for special case where player selects king and then castles
            if self.selected_tile:
                selected_piece = self.get_piece(self.selected_tile)
                if isinstance(selected_piece, King) and isinstance(clicked_piece, Rook) and self.castle_is_valid(clicked_piece):
                    self.castle(clicked_piece)
                    self.draw_tile(self.opponent_prev_move[0])
                    self.draw_tile(self.opponent_prev_move[1])
                    # player move recorded as king and rook's final rather than initial position
                    move = (self.selected_tile, clicked_tile)
                    self.end_player_move(((selected_piece.x, selected_piece.y), (clicked_piece.x, clicked_piece.y)))
                    return move
            # unhighlight previously selected piece, highlight newly selected piece
            if self.selected_tile and self.selected_tile not in self.player_prev_move:
                self.draw_tile(self.selected_tile)
            self.selected_tile = clicked_tile
            self.draw_tile(clicked_tile, highlight=True) 
        elif self.selected_tile and self.turn == self.player_color and self.make_move_if_valid((self.selected_tile, clicked_tile)):
            # check for special case of pawn promotion
            selected_piece = self.board[clicked_tile[1]][clicked_tile[0]]
            if isinstance(selected_piece, Pawn) and selected_piece.y == 0:
                self.board[selected_piece.y][selected_piece.x] = Queen(selected_piece.x, selected_piece.y, self.player_color)
            # turn-over, highlight and return player move
            move = (self.selected_tile, clicked_tile)
            self.highlight_player_move(move)
            self.end_player_move(move)
            return move
        return None

    def process_opponent_move(self, move : ((int, int), (int, int))) -> bool:
        # check for and process the special case of an opponent castling
        rook = self.get_piece(move[1])
        if rook and rook.color != self.player_color:
            self.castle(rook)
            self.draw_tile(self.player_prev_move[0])
            self.draw_tile(self.player_prev_move[1])
            # player move recorded as king and rook's final rather than initial position
            self.end_opponent_move(((self.opponent_king.x, self.opponent_king.y),(rook.x, rook.y)))
            return
        # in all other cases, board is updated in standard way
        self.make_move(move)
        # check for special case of pawn promotion
        selected_piece = self.get_piece(move[1])
        if isinstance(selected_piece, Pawn) and selected_piece.y == 7: 
            self.board[selected_piece.y][selected_piece.x] = Queen(selected_piece.x, selected_piece.y, self.turn)
        # turn-over, highlight and end opponent move
        self.highlight_opponent_move(move)
        self.end_opponent_move(move)
        return

    # return a list of pieces of a give color currently attacking a given tile 
    def in_danger(self, tile, attacking_color):
        x, y = tile
        attacking_pieces = []
        # determine if tile is endangered by adjacent king
        if attacking_color == self.player_color and abs(x - self.king.x) < 2 and abs(y - self.king.y) < 2:
            attacking_pieces.append(self.king)        
        elif attacking_color != self.player_color and abs(x - self.opponent_king.x) < 2 and abs(y - self.opponent_king.y) < 2:
            attacking_pieces.append(self.opponent_king)
        # determine if tile is endangered by adjacent knight
        for position in [(x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2), (x - 1, y - 2), (x + 1, y + 2), (x + 1, y - 2)]:
            piece = self.get_piece(position)
            if piece and isinstance(piece, Knight) and piece.color == attacking_color:
                attacking_pieces.append(piece)
        # determine if tile is endangered by adjacent pawns
        if attacking_color != self.player_color:
            for position in [(x - 1, y - 1), (x + 1, y - 1)]:
                piece = self.get_piece(position)
                if piece and isinstance(piece, Pawn) and piece.color == attacking_color:
                    attacking_pieces.append(piece)
        elif attacking_color == self.player_color:
            for position in [(x - 1, y + 1), (x + 1, y + 1)]:
                piece = self.get_piece(position)
                if piece and isinstance(piece, Pawn) and piece.color == attacking_color:
                    attacking_pieces.append(piece)
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
        for piece in [left_piece, right_piece, up_piece, down_piece]:
            if (isinstance(piece, Rook) or isinstance(piece, Queen)) and piece.color == attacking_color:
                attacking_pieces.append(piece)
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
        for piece in [left_up_piece, right_up_piece, left_down_piece, right_down_piece]:
            if (isinstance(piece, Bishop) or isinstance(piece, Queen)) and piece.color == attacking_color:
                attacking_pieces.append(piece)
        return attacking_pieces
    
    # return list of pieces of a given color that can move to given tile
    def get_pieces_in_range(self, tile : (int, int)):
        x, y = tile
        pieces_in_range = []
        # determine if tile can be reached by adjacent kings
        if abs(x - self.king.x) < 2 and abs(y - self.king.y) < 2:
            pieces_in_range.append(self.king)        
        if abs(x - self.opponent_king.x) < 2 and abs(y - self.opponent_king.y) < 2:
            pieces_in_range.append(self.opponent_king)
        # determine if tile can be reached by adjacent knights
        for position in [(x - 2, y - 1), (x - 2, y + 1), (x - 1, y + 2), (x - 1, y - 2), (x + 1, y + 2), (x + 1, y - 2)]:
            piece = self.get_piece(position)
            if piece and isinstance(piece, Knight):
                pieces_in_range.append(piece)
        # determine if tile can be reached by adjacent pawns
        piece = self.get_piece((x, y - 1))
        if isinstance(piece, Pawn) and piece.color != self.player_color:
            pieces_in_range.append(piece)
        piece = self.get_piece((x, y - 2))
        if isinstance(piece, Pawn) and piece.move_count == 0 and piece.color != self.player_color:
            pieces_in_range.append(piece)
        piece = self.get_piece((x, y + 1))
        if isinstance(piece, Pawn) and piece.color == self.player_color:
            pieces_in_range.append(piece)
        piece = self.get_piece((x, y + 2))
        if isinstance(piece, Pawn) and piece.move_count == 0 and piece.color == self.player_color:
            pieces_in_range.append(piece)
        # determine if tile can be reached vertically or horizontally by rook or queen
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
        for piece in [left_piece, right_piece, up_piece, down_piece]:
            if (isinstance(piece, Rook) or isinstance(piece, Queen)):
                pieces_in_range.append(piece)
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
        for piece in [left_up_piece, right_up_piece, left_down_piece, right_down_piece]:
            if (isinstance(piece, Bishop) or isinstance(piece, Queen)):
                pieces_in_range.append(piece)
        return pieces_in_range

    def castle_is_valid(self, rook) -> bool:
        if not (self.king.move_count == 0 and rook.move_count == 0): 
            return False
        positions = []
        if rook.x < self.king.x:
            for i in range(rook.x + 1, self.king.x):
                positions.append((i, 7))
        elif rook.x > self.king.x:
            for i in range(self.king.x + 1, rook.x):
                positions.append((i, 7))
        # check that each position is empty and not being attacked by an opponent piece
        for position in positions:
            if self.get_piece(position) or self.in_danger(position, self.opponent_color):
                return False
        return True

    # function processes and renders to screen castling by player or opponent
    def castle(self, rook):
        # determine if processing player or opponent castling
        if rook.color == self.player_color:
            king = self.king
            y_index = 7
        else:
            king = self.opponent_king
            y_index = 0
        # otherwise, castling is valid, move castle adjacent to king, hop king over castle
        self.board[rook.y][rook.x] = None
        self.board[y_index][king.x] = None
        if rook.x < king.x:
            self.board[y_index][king.x - 1] = rook
            rook.x = king.x - 1
            self.board[y_index][king.x - 2] = king
            king.x -= 2
            # draw over previous king and rook positions
            self.draw_tile((0, y_index))
            self.draw_tile((king.x + 2, y_index))
        elif rook.x > king.x:
            self.board[y_index][king.x + 1] = rook
            rook.x = king.x + 1
            self.board[y_index][king.x + 2] = king
            king.x += 2
            # draw over previous king and rook positions
            self.draw_tile((7, y_index))
            self.draw_tile((king.x - 2, y_index))
        # draw new positions of king and rook
        self.draw_tile((rook.x, rook.y), highlight=True)
        self.draw_tile((king.x, king.y), highlight=True)

    # return list of tiles that exist between two horizontally, vertically or diagonally separated tiles
    def tiles_between(from_tile : (int, int), to_tile : (int, int)):
        tiles = []
        from_x, from_y = from_tile
        to_x, to_y = to_tile
        if from_y == to_y: # find horizontal tiles
            start_x = from_x if from_x < to_x else to_x
            end_x = to_x if to_x > from_x else from_x
            start_x += 1
            while start_x < end_x:
                tiles.append((start_x, to_y))
                start_x += 1
        elif from_x == to_x: # find vertical tiles
            start_y = from_y if from_y < to_y else to_y
            end_y = to_y if to_y > from_y else from_y
            start_y += 1
            while start_y < end_y:
                tiles.append((to_x, start_y))
                start_y += 1
        elif (from_x < to_x and from_y < to_y) or (from_x > to_x and from_y > to_y): # find diagonal tiles (top-left/bottom-right)
            start_x = from_x if from_x < to_x else to_x
            start_y = from_y if from_y < to_y else to_y
            end_x = to_x if to_x > from_x else from_x
            end_y = to_y if to_y > from_y else from_y
            while start_x < end_x and start_y < end_y:
                tiles.append((start_x, start_y))
                start_x += 1
                start_y += 1
        elif (from_x < to_x and from_y > to_y) or (from_x > to_x and from_y < to_y): # find diagonal tiles (top-right/bottom-left)
            start_x = from_x if from_x < to_x else to_x
            start_y = from_y if from_y > to_y else to_y
            end_x = to_x if to_x > from_x else from_x
            end_y = to_y if to_y < from_y else from_y
            while start_x < end_x and start_y > end_y:
                tiles.append((start_x, start_y))
                start_x += 1
                start_y -= 1
        return tiles

    def in_check_mate(self) -> bool:
        x, y = self.king.x, self.king.y
        attacking_pieces = self.in_danger((x, y), self.opponent_color)
        if not attacking_pieces:
            return False
        # if king can move to any adjacent tile, king is not in checkmate  
        for tile in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:
            if not self.on_board(tile): continue
            captured_piece = self.get_piece(tile)
            if self.make_move_if_valid(((self.king.x, self.king.y), tile)):
                self.cancel_move(((self.king.x, self.king.y), tile), self.king, captured_piece)
                return False
        # if there is more than one piece attacking king and king cannot move to adjacent tile, checkmate
        if len(attacking_pieces) > 1:
            return True
        # if king is only attacked by one piece, check if attacking piece can be captured or blocked
        attacking_piece = attacking_pieces[0]
        can_capture = self.in_danger((attacking_piece.x, attacking_piece.y), self.player_color)
        if can_capture:
            if can_capture == [self.king]: # edge case where king is only piece that can capture, but attacking piece is protected
                if self.make_move_if_valid(((self.king.x, self.king.y), (attacking_piece.x, attacking_piece.y))):
                    self.cancel_move(((self.king.x, self.king.y), tile), self.king, captured_piece)
                    return False
                return True
            return False # there exists a move to capture opponent's attacking piece
        if isinstance(attacking_piece, Bishop) or isinstance(attacking_piece, Rook) or isinstance(attacking_piece, Queen):
            blocking_tiles = self.tiles_between((attacking_piece.x, attacking_piece.y), (self.king.x, self.king.y))
            for tile in blocking_tiles:
                if [piece for piece in self.get_pieces_in_range(tile) if piece.color == self.player_color]:
                    return False # there exists a move to block opponent's attacking piece
        return True