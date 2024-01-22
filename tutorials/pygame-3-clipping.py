"""
Om te kunnen tekenen op een window hebben we een externe library of package nodig.
Wij kiezen voor PYGAME (je zal pygame eerst moeten installeren voor je deze tutorial doet)
PYGAME zorgt voor:
    -Het openen van een window met bepaalde grootte en titel(caption)
    -Tekenen van lijnen en figuren (al dan niet opgevuld)
    -Opladen, herschalen en tekenen van images (bmp,png,jpeg,...)
    -Opvangen van user-events zoals mousedown, mousemove,...

Tutorial-pygame-deel-3: C
"""

import pygame as pg
pg.init()
win = pg.display.set_mode((800, 600))
pg.display.set_caption("Hector Chess - Sint-Pieterscollege, Jette")

# Onze kleuren
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
CYAN = (0, 255, 255)
BURLYWOOD = (222, 184, 135)
CHOCOLATE = (210, 105, 30)

# Overzicht van de gebruikte functies (zie Tutorial Deel 2)
#    pg.draw.rect(surface, color, rect, width=0)
#    pg.draw.circle(surface, color, center, radius, width=0)
# Door 1 maal de figuren te tekenen met width=0 krijgen we een opgevulde figuur
# Door dan 1 maal de figuren te tekenen met width=2 krijgen we een rand
# Eerst tekenen we een rode rechthoek met groene rand
rect1 = pg.Rect((40, 280, 200, 75))  # (left,top,width,height)
pg.draw.rect(win, RED, rect1,0)  # Eerst de rode achtergrond
pg.draw.rect(win, GREEN, rect1,4)  # Dan de groenekader
# Dan tekenen we een witte cirkel met straal 45, met blauwe rand
pg.draw.circle(win, WHITE, (rect1.right, rect1.bottom), 45, 0)
pg.draw.circle(win, BLUE, (rect1.right, rect1.bottom), 45, 3)




# Als we pg.Rect gebruiken om een rechthoek te definieren kunnen we ook rect.top, rect.width,... gebruiken
# De functie pg.Rect zet de python rect (40, 80, 200, 75) om naar een pg.Rect
rect1 = pg.Rect((40, 80, 200, 75))  # (left,top,width,height)
pg.draw.rect(win, RED, rect1,4)
pg.draw.line(win, GREEN, (rect1.left, rect1.top), (rect1.right, rect1.bottom))
# We tekenen een cirkel met straal 45, rond de rechteronderhoek van de rectangle, met dikte 3
pg.draw.circle(win, BLUE, (rect1.right, rect1.bottom), 45, 3)

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
