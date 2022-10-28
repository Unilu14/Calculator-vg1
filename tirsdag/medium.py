import random as rn
import pygame as pg

# Oppgave 1
pg.init()

w = 600
h = 650

surface = pg.display.set_mode((400,300))
color = (255,0,0)

background = pg.display.set_mode((w,h))
pg.display.set_caption = ('Oppgave_medium')

pg.draw.rect(surface, color, pg.Rect(30, 30, 60, 60), 2)
pg.draw.rect(surface, color, pg.Rect(80, 80, 40, 40))
pg.display.flip()

a = rn.randint(1,30)
b = rn.randint(30,40)
coord1=(a,b)

run = True
while run:
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False