# -*- coding: utf-8 -*-
import pygame,sys
from director import *
from param import *

pygame.init()
screen = pygame.display.set_mode((SCR_W, SCR_H))
pygame.display.set_caption("Machine Break")

# 创建导演
director = Director(screen)

while True:
    for event in pygame.event.get():
        director.processEvent(event)

    director.draw()
    pygame.display.update()
