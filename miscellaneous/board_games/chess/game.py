import os
import pygame
from constants import *
from player import Player
from game_board import GameBoard, PieceColor, King, Queen, Bishop, Knight, Rook, Pawn

#--------------------------------------------------------------------------------------------------------------
# Initialisation
#--------------------------------------------------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess")
game_assets = {
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
clock = pygame.time.Clock()
board = GameBoard(PieceColor.WHITE)
player = Player()
#--------------------------------------------------------------------------------------------------------------
# Helper functions
#--------------------------------------------------------------------------------------------------------------
def draw_tile(tile : (int, int)):
    x, y = tile[0], tile[1]
    pygame.draw.rect(screen, WHITE, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))
    piece = board.get_piece(tile)
    if piece:
        sprite = game_assets[piece.getColor()][piece.__class__]
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

def exit_game():
    pygame.quit()
    exit(0)

# run initial CLI between player and player directory
def player_CLI():
    while True:
        cmd = input("Input command: ")
        cmd_words = cmd.split()
        if cmd_words[0] == "help":
            print("\thelp : list all commands")
            print("\tlist : list all available players")
            print("\trequest [player]: list all available players")
            print("\texit : exit command-line interface")
        elif cmd_words[0] == "list":
            player.list_players()
        elif cmd_words[0] == "request":
            if player.game_request(cmd_words[1]): 
                print("Request Accepted.")
                break
            else:
                print("Request Denied.")
        elif cmd == "exit":
            player.leave_player_directory()
            exit_game()
        else:
            print("Commant not found. Type 'help' for list of commands.")

#--------------------------------------------------------------------------------------------------------------
# Main Game Loop
#--------------------------------------------------------------------------------------------------------------
player.set_user_handle(input("Enter username: "))
player.join_player_directory()
player_CLI()
board.draw(screen, game_assets)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            process_click_event(pygame.mouse.get_pos())
    pygame.display.flip()
    clock.tick(60)
exit_game()

# TODO
# finish connection routes between player, opponent and player directory
# finish exchange between connected player and opponent (make move, notify opponent, wait to receive move, receive, visualise, repeat)
# update threading (how to handle traffic if there are more connections than there are threads)
# add check with red highlighting
#   if notified that king is in check, highlight red
#   if king in check and proposed move does not put king out of check, invalidate
#   if proposed move puts own king in check, invalidate
#   if proposed move is valid and puts own king out of check, unhighlight
#   if proposed move is valid and puts opponents king in check, notify opponent
# more features
#   pawn promotion, castling, en passant, audio, board style, resolution of 45x45px
# update markdown with code segments
# write project report (licensing, state machine, fix projects page)
# FIX BUGS
#   initial pawn movement of 2 spaces can jump over pieces