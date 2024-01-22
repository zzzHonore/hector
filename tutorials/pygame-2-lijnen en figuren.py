"""
Om te kunnen tekenen op een window hebben we een externe library of package nodig.
Wij kiezen voor PYGAME (je zal pygame eerst moeten installeren voor je deze tutorial doet)
PYGAME zorgt voor:
    Het openen van een window met bepaalde grootte en titel(caption)
    Tekenen van lijnen en figuren (al dan niet opgevuld)
    Opladen, herschalen en tekenen van images (bmp,png,jpeg,...)
    Opvangen van user-events zoals mousedown, mousemove,...

Tutorial-pygame-deel-2: Tekenen van lijnen en figuren
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

# Om dingen te tekenen spreken we het object :draw: van pygame aan.
# Het object :draw: heeft tekenroutines

# Tekenroutine 1: de functie pg.draw.rect tekent een rechthoek
#    pg.draw.rect(surface, color, rect, width=0)
#        :surface: Het oppervlak waarop je wilt tekenen, dus :win:
#        :color: de kleur waarin je wil tekenen, bvb RED
#        :rect: de coordinaten van de rechthoek, (left,top,width,height)
#        :width=0: geeft de dikte van de lijnen (0 wil zeggen opvullen)
#            =0 wil zeggen dat als je de parameter niet meegeeft, 0 wordt gebruikt als parameter
#     Rechthoeken: We gebruiken geen standaard rechthoeken, maar pygame recthoeken
#         rect = (left,top,width,height) is een standaard rechthoek, maar heeft weinig mogelijkheden
#         rect = pg.Rect((left,top,width,height)) zet die standaard rechthoek om naar een OBJECT
#            Nu kan je rect.top, rect.left, rect.width, rect.height, rect.bottom, rect.right gebruiken
# Teken een rode rechthoek met lijndikte 4
rect1 = pg.Rect((40, 80, 200, 75))  # (left,top,width,height)
pg.draw.rect(win, RED, rect1, 4)
# De lijn komt nooit buiten de rechthoek. We tekenen dus de 4 pixels vanaf de rand naar binnen toe

# Tekenroutine 2: de functie pg.draw.line tekent een lijn
#    pygame.draw.line(surface, color, start_pos, end_pos, width=1)
#        :surface: Het oppervlak waarop je wilt tekenen.(:win:)
#        :color: De kleur van de lijn.
#        :start_pos: Een tuple/koppel (x, y) met de coördinaten van het startpunt van de lijn.
#        :end_pos: Een tuple/koppel (x, y) met de coördinaten van het eindpunt van de lijn.
#        :width (optioneel): Lijndikte. =1 als je niets specifieert
# Teken een groene lijn met lijndikte 2 op een diagonaal van de rechthoek
pg.draw.line(win, GREEN, (rect1.left, rect1.top), (rect1.right, rect1.bottom),2)

# Tekenroutine 3: de functie pg.draw.circle tekent een cirkel
#    pygame.draw.circle(surface, color, center, radius, width=0)
#        :surface: Het oppervlak waarop je wilt tekenen. (:win:)
#        :color: De kleur van de cirkel.
#        :center: Een tuple (x, y) met de coördinaten van het middelpunt van de cirkel.
#        :radius: De straal van de cirkel.
#        :width (optioneel): Lijndikte. Als 0, wordt de cirkel gevuld.
# We tekenen een blauwe cirkel met straal 45, rond de rechteronderhoek van de rectangle, met dikte 3
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
