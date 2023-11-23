import pygame
import os
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# initialise game
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Chess")
clock = pygame.time.Clock()
# load game assets
king_black = pygame.image.load(os.getcwd() + '/assets/king_black.png')
king_white = pygame.image.load(os.getcwd() + '/assets/king_white.png')
queen_black = pygame.image.load(os.getcwd() + '/assets/queen_black.png')
queen_white = pygame.image.load(os.getcwd() + '/assets/queen_white.png')
rook_black = pygame.image.load(os.getcwd() + '/assets/rook_black.png')
rook_white = pygame.image.load(os.getcwd() + '/assets/rook_white.png')
bishop_black = pygame.image.load(os.getcwd() + '/assets/bishop_black.png')
bishop_white = pygame.image.load(os.getcwd() + '/assets/bishop_white.png')
knight_black = pygame.image.load(os.getcwd() + '/assets/knight_black.png')
knight_white = pygame.image.load(os.getcwd() + '/assets/knight_white.png')
pawn_black = pygame.image.load(os.getcwd() + '/assets/pawn_black.png')
pawn_white = pygame.image.load(os.getcwd() + '/assets/pawn_white.png')
# draw chess pieces
screen.blit(king_black, (0,0))
screen.blit(king_black, (0,0))
# draw overlayed board
#screen.fill(WHITE)
#for x in range(8):
#    for y in range(8):
#        pygame.draw.rect(screen, BLACK, pygame.Rect(100*x + 5, 100*y + 5, 90, 90))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    # next frame
    pygame.display.flip()
    clock.tick(60)

pygame.quit()