import pygame
import chess

# set up pygame
pygame.init()
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hector Chess - Sint-Pieterscollege, Jette")
clock = pygame.time.Clock()
running = True

to_draw = []

def create_grid(position=(WINDOW_WIDTH//2,WINDOW_HEIGHT//2),width=400):
    """
    This function creates a grid of rects to serve as a background for all the pieces.
    Accepts
        position (tuple): x and y coords of the middle of the grid
        width (int): the width of the grid
    Returns
        grid_rects (list): list with pygame rects that represent a grid when drawn
    """
    grid_rects = []
    for x in range(0,width,width//8):
        for y in range(0,width,width//8):
            grid_rects.append(pygame.Rect(x+position[0]-width//2,y+position[1]-width//2,width/8,width/8))
    return grid_rects

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
    window.fill("black")
    # ... rendering the screen

    # the background
    grid = create_grid()
    colors = ["gray","white"]
    color_counter = 1
    for i in range(len(grid)):
        pygame.draw.rect(window,colors[color_counter%2],grid[i])
        if not (i+1)%8 == 0:
            color_counter += 1


    pygame.display.flip() # update the screen

    clock.tick(60) # wait until the next frame (60FPS)

