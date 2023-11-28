import pygame
import os
from game_board import GameBoard, PieceColor, King, Queen, Bishop, Knight, Rook, Pawn

#--------------------------------------------------------------------------------------------------------------
# Initialisation
#--------------------------------------------------------------------------------------------------------------
# game constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
# initialise game
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
# initialise game components
board = GameBoard(PieceColor.WHITE)
# game asset dictionary
game_assests = {
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
# draw overlayed board
screen.fill(BLACK)
for x in range(8):
    for y in range(8):
        pygame.draw.rect(screen, WHITE, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))
# draw pieces to screen
default_piece_order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
for i, piece in enumerate(default_piece_order):
    if board.get_orientation() == PieceColor.BLACK:
        screen.blit(game_assests[PieceColor.WHITE][piece], (i*100, 0))
        screen.blit(game_assests[PieceColor.WHITE][Pawn], (i*100, 100))
        screen.blit(game_assests[PieceColor.BLACK][Pawn], (i*100, 600))
        screen.blit(game_assests[PieceColor.BLACK][piece], (i*100, 700))
    else:
        screen.blit(game_assests[PieceColor.BLACK][piece], (i*100, 0))
        screen.blit(game_assests[PieceColor.BLACK][Pawn], (i*100, 100))
        screen.blit(game_assests[PieceColor.WHITE][Pawn], (i*100, 600))
        screen.blit(game_assests[PieceColor.WHITE][piece], (i*100, 700))

#--------------------------------------------------------------------------------------------------------------
# Helper functions
#--------------------------------------------------------------------------------------------------------------
def draw_tile(tile : (int, int)):
    x, y = tile[0], tile[1]
    pygame.draw.rect(screen, WHITE, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))
    piece = board.get_piece(tile)
    if piece:
        sprite = game_assests[piece.getColor()][piece.__class__]
        screen.blit(sprite, (100*x,100*y))

def highlight_tile(tile : (int, int)):
    x, y = tile[0], tile[1]
    pygame.draw.rect(screen, GREEN, pygame.Rect(100*x, 100*y, 100, 100))
    pygame.draw.rect(screen, WHITE, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))
    draw_tile(tile)

def unhighlight_tile(tile : (int, int)):
    x, y = tile[0], tile[1]
    pygame.draw.rect(screen, BLACK, pygame.Rect(100*x, 100*y, 100, 100))
    pygame.draw.rect(screen, WHITE, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))
    draw_tile(tile)

def process_click_event(click_coord : (int, int)):
    clicked_tile = (click_coord[0] // 100, click_coord[1] // 100)
    clicked_piece = board.get_piece(clicked_tile)
    selected_tile = board.get_selected_tile()
    if selected_tile == clicked_tile:
        unhighlight_tile(selected_tile)
        board.set_selected_tile(None)
    elif clicked_piece and clicked_piece.getColor() == board.get_orientation():
        if selected_tile: unhighlight_tile(selected_tile)
        board.set_selected_tile(clicked_tile)
        highlight_tile(clicked_tile)
    elif selected_tile and board.makeMove(clicked_tile):
        unhighlight_tile(selected_tile)
        draw_tile(clicked_tile)

#--------------------------------------------------------------------------------------------------------------
# Main Game Loop
#--------------------------------------------------------------------------------------------------------------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            process_click_event(pygame.mouse.get_pos())
    # next frame
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

# TODO
# run application with two clients
#   IPC (with threads for simultaneous client and listener)
#   try sockets instead
#   test sending/receiving player moves, visualise opponent moves
#   make turn-based
# add check with red highlighting
#   if notified that king is in check, highlight red
#   if king in check and proposed move does not put king out of check, invalidate
#   if proposed move puts own king in check, invalidate
#   if proposed move is valid and puts own king out of check, unhighlight
#   if proposed move is valid and puts opponents king in check, notify opponent
# more features
#   pawn promotion, castling, en passant, audio
# write project report (licensing, state machine, fix projects page) 
# FIX BUGS
#   initial pawn movement of 2 spaces can jump over pieces