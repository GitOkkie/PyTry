#!/usr/bin/env python3

import pygame
import kaprekar

size_x = 8
size_y = 6

mode=(size_x*100, size_y*100)

background=(64,64,64)
colours=[(0,0,0), (0,0,255), (0,255,0), (0,255,255),
         (255,0,0), (255,0,255), (255,255,0), (255,255,255)]

pygame.init()
screen = pygame.display.set_mode(mode)
screen.fill(background)

for x,y in kaprekar.grid:
    val = kaprekar.grid[x,y]
    if val != None:
        blokje = pygame.Rect((x*size_x, y*size_y, size_x, size_y))
        pygame.draw.rect(screen, colours[val], blokje)

pygame.display.update()

while True:
    event=pygame.event.wait()
    print(event)
    if event.type == pygame.QUIT:
        break
    else:
        pygame.display.update()
