import pygame
from constants import *
from player import Player
from game_board import GameBoard, PieceColor

#--------------------------------------------------------------------------------------------------------------
# Main Game Loop
#--------------------------------------------------------------------------------------------------------------
def start_game():
    pygame.init()
    clock = pygame.time.Clock()
    board = GameBoard(PieceColor.WHITE)
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Chess")
    board.draw(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.process_click_event(board, screen, pygame.mouse.get_pos())
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

# Main context, enter server CLI between game sessions
player = Player()
player.start()
play_again = True
while play_again:
    play_again = player.enter_CLI()
    if play_again: start_game()

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