"""
Om te kunnen tekenen op een window hebben we een externe library of package nodig.
PYGAME zorgt voor:
    Het openen van een window
    Tekenen van lijnen en figuren
    Tekenen van images
    Opvangen van user-events zoals muisedown, mousemove,...
"""


import pygame as pg
pg.init()
win = pg.display.set_mode((800, 600))
pg.display.set_caption("Hector Chess - Sint-Pieterscollege, Jette")

# Om dingen te tekenen spreken we de klasse :draw: van pygame aan. Deze heeft tekenroutines
# Eerste parameter is telkens het venster :win:
# Tweede parameter is telkens een kleur :color:
# Derde parameter is telkens een iets met coordinaten :rect: of :pt:, naargelang het soort figuur
# Teken een rechthoek met dikte 3

# Eerst bepalen we de kleuren die we gebruiken
# Constanten altijd in hoofdletters
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
CYAN = (0, 255, 255)
BURLYWOOD = (222, 184, 135)
CHOCOLATE = (210, 105, 30)
# We bepalen de rechthoeken die we nodig hebben
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
