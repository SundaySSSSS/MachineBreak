# -*- coding: utf-8 -*-
import pygame


class ResCtrl:
    def __init__(self):
        # 底层图块
        self.imgGrass = None
        self.imgWater = None
        self.imgLower = pygame.image.load("res/img/ground.png").convert_alpha()
        # target相关
        self.imgNormalTarget = None
        self.imgMovableTarget = None
        self.imgAttackableTarget = None  # 可攻击的目标(备选)
        self.imgAttackTaget = None  # 要攻击的目标
        self.imgTarget = \
            pygame.image.load("res/img/target.png").convert_alpha()
        # machine相关
        self.imgMachine = None

    def getImgGrass(self):
        if self.imgGrass is None:
            self.imgGrass = \
                self.imgLower.subsurface(pygame.Rect(0, 0, 48, 48)).copy()
        return self.imgGrass.copy()

    def getImgWater(self):
        if self.imgWater is None:
            self.imgWater = \
                self.imgLower.subsurface(pygame.Rect(48, 0, 48, 48)).copy()
        return self.imgWater.copy()

    def getImgNormalTarget(self):
        # 获取普通目标标记图(鼠标滑过时的标记)
        if self.imgNormalTarget is None:
            self.imgNormalTarget = \
                self.imgTarget.subsurface(pygame.Rect(48, 0, 48, 48)).copy()
        return self.imgNormalTarget.copy()

    def getImgMovableTarget(self):
        # 获取可移动目标标记图
        if self.imgMovableTarget is None:
            self.imgMovableTarget = \
                self.imgTarget.subsurface(pygame.Rect(0, 48, 48, 48)).copy()
        return self.imgMovableTarget.copy()

    def getImgAttackableTarget(self):
        # 获取可攻击目标标记图
        if self.imgAttackableTarget is None:
            self.imgAttackableTarget = \
                self.imgTarget.subsurface(pygame.Rect(48, 48, 48, 48)).copy()
        return self.imgAttackableTarget.copy()

    def getImgAttackTarget(self):
        # 获取攻击目标标记图
        if self.imgAttackTaget is None:
            self.imgAttackTaget = \
                self.imgTarget.subsurface(pygame.Rect(0, 0, 48, 48)).copy()
        return self.imgAttackTaget.copy()

    def getImgMachine(self):
        if self.imgMachine is None:
            self.imgMachine = \
                pygame.image.load("res/img/machine.png").convert_alpha()
        return self.imgMachine.copy()
