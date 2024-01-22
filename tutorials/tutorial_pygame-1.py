"""
Om te kunnen tekenen op een window hebben we een externe library of package nodig.
PYGAME zorgt voor:
    Het openen van een window
    Tekenen van lijnen en figuren
    Tekenen van images
    Opvangen van user-events zoals muisedown, mousemove,...
"""

# stap 1: importeer pygame. Je kan nu de functies van pygame gebruiken
import pygame as pg

# stap 2: roep pg.init() op.
# Doe je dit niet dan zijn er functies van pygame die niet correct werken
pg.init()

# Eerst openen we een venster met pygame
# De variabele win zal je moeten meegeven met elke routine die iets op het window moet tekenen
# we spreken hiervoor de pygame klasse :display: aan
win = pg.display.set_mode((800, 600))

# We geven het venster een gepaste titel
pg.display.set_caption("Hector Chess - Sint-Pieterscollege, Jette")

keep_running = True
while keep_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keep_running = False

# Als het game klaar is roep je best pg.quit() op zodat alle geheugen wordt vrijgegeven
pg.quit()
