"""
Om te kunnen tekenen op een window hebben we een externe library of package nodig.
Wij kiezen voor PYGAME (je zal pygame eerst moeten installeren voor je deze tutorial doet)
PYGAME zorgt voor:
    Het openen van een window met bepaalde grootte en titel(caption)
    Tekenen van lijnen en figuren (al dan niet opgevuld)
    Opladen, herschalen en tekenen van images (bmp,png,jpeg,...)
    Opvangen van user-events zoals mousedown, mousemove,...

Tutorial-pygame-deel-1: Openen van een venster
"""

# stap 1: importeer pygame. 
# Door te importeren as pg, moet je niet telkens pygame voluit schrijven
import pygame as pg
# stap 2: roep pg.init() op.
# Doe je dit niet dan zijn er functies van pygame die niet correct werken
pg.init()
# Je kan nu de functies van pygame gebruiken

# Stap 2: We openen een venster (window) met pygame
# pygame bevat een object :pg.display: dat daar functies voor heeft
# We roepen de functie :pg.display.set_mode(width,height) op die dat voor je doet
win = pg.display.set_mode((800, 600))
# Het resultaat steken we in de variabele :win:
# De variabele :win: zal je later doorgeven aan alle functies die iets op het window moeten tekenen.
# We zien later dat :win: eigenlijk een OBJECT is met eigen functies

# Stap 3: We geven het venster een gepaste titel
# Ook daarvoor heeft het OBJECT pg.display een functie, namelijk pg.display.set_caption(titel)
pg.display.set_caption("Hector Chess - Sint-Pieterscollege, Jette")

# Stap 4: Je mag nu dit programma uitvoeren en het resultaat bekijken

keep_running = True
while keep_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keep_running = False

# Als het game klaar is roep je best pg.quit() op zodat alle geheugen wordt vrijgegeven
pg.quit()
