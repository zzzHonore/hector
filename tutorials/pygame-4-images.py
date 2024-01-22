"""
Om te kunnen tekenen op een window hebben we een externe library of package nodig.
Wij kiezen voor PYGAME (je zal pygame eerst moeten installeren voor je deze tutorial doet)
PYGAME zorgt voor:
    -Het openen van een window met bepaalde grootte en titel(caption)
    -Tekenen van lijnen en figuren (al dan niet opgevuld)
    -Opladen, herschalen en tekenen van images (bmp,png,jpeg,...)
    -Opvangen van user-events zoals mousedown, mousemove,...

Tutorial-pygame-deel-4: werken met images
"""

import pygame as pg
pg.init()
win = pg.display.set_mode((800, 600))
pg.display.set_caption("Hector Chess - Sint-Pieterscollege, Jette")

# Voordat we beginnen met tekenen bepalen we de kleuren die we gaan gebruiken
# Constanten altijd in hoofdletters
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
CYAN = (0, 255, 255)
BURLYWOOD = (222, 184, 135)
CHOCOLATE = (210, 105, 30)

#Nog te verwerken, nu eten!

# We doen nog eens hetzelfde met een andere rect, maar nu zetten we de lijndikte gelijk aan 0
rect1 = pg.Rect((340, 80, 200, 75))  # (left,top,width,height)
pg.draw.rect(win, RED, rect1,0)
pg.draw.line(win, GREEN, (rect1.left, rect1.top), (rect1.right, rect1.bottom))
# We tekenen een cirkel met straal 45, rond de rechteronderhoek van de rectangle, met dikte 0
pg.draw.circle(win, BLUE, (rect1.right, rect1.bottom), 45, 0)

# Wil je gevulde figuren met een rand? Dan combineer je beiden
rect1 = pg.Rect((40, 280, 200, 75))  # (left,top,width,height)
pg.draw.rect(win, RED, rect1,0)  # Eerst de achtergrond
pg.draw.rect(win, GREEN, rect1,4)  # Dan de kader
# We tekenen een cirkel met straal 45, rond de rechteronderhoek van de rectangle
pg.draw.circle(win, WHITE, (rect1.right, rect1.bottom), 45, 0)
pg.draw.circle(win, BLUE, (rect1.right, rect1.bottom), 45, 3)

# Als je tekening te groot is en je wil er iets afknippen dan moet je clippen
# je wil bijvoorbeeld een stuk van je tekening gebruiken om een vlag te tekenen
clip_rect = pg.Rect((420, 320, 140, 64))  # (left,top,width,height)
# set_clip is een functie van je window
win.set_clip(clip_rect)
# We vullen de clip_rect even op met roze
pg.draw.rect(win, PINK, clip_rect,0)  # de achtergrond
# Nu tekenen we gewoon
rect1 = pg.Rect((340, 280, 200, 75))  # (left,top,width,height)
pg.draw.rect(win, RED, rect1,0)  # Eerst de achtergrond
pg.draw.rect(win, GREEN, rect1,4)  # Dan de kader
# We tekenen een cirkel met straal 45, rond de rechteronderhoek van de rectangle
pg.draw.circle(win, WHITE, (rect1.right, rect1.bottom), 45, 0)
pg.draw.circle(win, BLUE, (rect1.right, rect1.bottom), 45, 3)
# Nu nog een kader rond de clip_rect
pg.draw.rect(win, CYAN, clip_rect,2)  # de achtergrond
# Vergeet niet om de clip_rect terug te herstellen
win.set_clip((0, 0, win.get_width(), win.get_height()))
# En nog een flag-pole
pg.draw.rect(win, BURLYWOOD, (clip_rect.left-10,clip_rect.top-10,10,200),0)  # Eerst de achtergrond

# Uitsmijter: het window object van pygame kan ook een :image: tonen, via blit functie
queen_image = pg.image.load("assets/pieces/W_Queen.png")
rect1 = pg.Rect((100, 440, 64, 64))  # (left,top,width,height)
pg.draw.rect(win, CHOCOLATE, rect1,0)  # Eerst de achtergrond
win.blit(queen_image, rect1)
# is je image te groot kan je hem transformen
rect1 = pg.Rect((180, 460, 32, 32))  # (left,top,width,height)
scaled_queen_image = pg.transform.scale(queen_image,(32, 32))
pg.draw.rect(win, CHOCOLATE, rect1,0)  # Eerst de achtergrond
win.blit(scaled_queen_image, rect1)


# Alles wordt getekend op een onzichtbaar venster
# pg.display.update() kopieert alles naar het zichtbare scherm in 1 stap
pg.display.update()

keep_running = True
while keep_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keep_running = False

# Als het game klaar is roep je best pg.quit() op zodat alle geheugen wordt vrijgegeven
pg.quit()
