# -*- coding: utf-8 -*-
import pygame, sys
from res_ctrl import *

class UICtrl:
    def __init__(self, ui_surface, resCtrl):
        self.surface = ui_surface
        self.rect = ui_surface.get_rect()
        self.resCtrl = resCtrl
    def draw(self):
        pygame.draw.rect(self.surface, pygame.Color("red"), self.rect)
