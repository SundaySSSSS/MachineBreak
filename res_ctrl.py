# -*- coding: utf-8 -*-
import pygame, sys

class ResCtrl:
    def __init__(self):
        # 底层图块
        self.imgGrass = None
        self.imgWater = None
        self.imgLower = pygame.image.load("res/img/ground.png").convert_alpha()
        # target相关
        self.imgNormalTarget = None
        self.imgTarget = pygame.image.load("res/img/target.png").convert_alpha()
        
    def getImgGrass(self):
        if self.imgGrass == None:
            self.imgGrass = self.imgLower.subsurface(pygame.Rect(0,0,48,48)).copy()
        return self.imgGrass.copy()

    def getImgWater(self):
        if self.imgWater == None:
            self.imgWater = self.imgLower.subsurface(pygame.Rect(48,0,48,48)).copy()
        return self.imgWater.copy()
    
    def getImgNormalTarget(self):
        if self.imgNormalTarget == None:
            self.imgNormalTarget = self.imgTarget.subsurface(pygame.Rect(48, 0, 48, 48)).copy()
        return self.imgNormalTarget.copy()
        
