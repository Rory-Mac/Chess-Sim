import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((45 * 8, 45 * 8))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()