import pygame
import chess

# set up pygame
pygame.init()
window = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Hector Chess - Sint-Pieterscollege, Jette")
clock = pygame.time.Clock()
running = True

# this loop always runs
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    render()
    pygame.display.flip()
    clock.tick(60) #limiteer FPS tot 60

pygame.quit()