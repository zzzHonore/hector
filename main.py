import pygame
import chess

# set up pygame
pygame.init()
window = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Hector Chess - Sint-Pieterscollege, Jette")
clock = pygame.time.Clock()
running = True

to_draw = []

# game loop
while running:
    # ... events for player interaction
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            to_draw.append(mouse_position)

    # ... logic

    # clear the screen before rendering
    window.fill("white")
    # ... rendering the screen
    for coords in to_draw:
        pygame.draw.circle(window,(0,0,255),coords,75)

    pygame.display.flip() # update the screen

    clock.tick(60) # wait until the next frame (60FPS)

pygame.quit()