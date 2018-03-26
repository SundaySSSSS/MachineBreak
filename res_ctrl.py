# -*- coding: utf-8 -*-
import pygame, sys

class ResCtrl:
    def __init__(self):
        self.imgGrass = None
        self.imgWater = None
        self.imgGround = pygame.image.load("res/img/ground.png").convert_alpha()
        
    def getImgGrass(self):
        if self.imgGrass == None:
            self.imgGrass = self.imgGround.subsurface(pygame.Rect(0,0,48,48)).copy()
        return self.imgGrass.copy()

    def getImgWater(self):
        if self.imgWater == None:
            self.imgWater = self.imgGround.subsurface(pygame.Rect(48,0,48,48)).copy()
        return self.imgWater.copy()
        
