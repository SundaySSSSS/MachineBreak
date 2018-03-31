# -*- coding: utf-8 -*-
import pygame
import threading


class ResCtrl:
    _instance_lock = threading.Lock()

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
        # 爆炸相关
        self.imgExploderSmall = None
        self.imgExploderMiddle = None
        self.imgExploderBig = None
        self.imgExploder = \
            pygame.image.load("res/img/exploder.png").convert_alpha()

    @classmethod
    def instance(cls):
        if not hasattr(ResCtrl, "_instance"):
            with ResCtrl._instance_lock:
                if not hasattr(ResCtrl, "_instance"):
                    ResCtrl._instance = ResCtrl()
        return ResCtrl._instance

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

    def getImgExploder(self, stage):
        # 获取爆炸图片, stage: 0 - small 1-middle 2-big
        if self.imgExploderSmall is None:
            self.imgExploderSmall = \
                self.imgExploder.subsurface(pygame.Rect(0, 0, 48, 48)).copy()
        if self.imgExploderMiddle is None:
            self.imgExploderMiddle = \
                self.imgExploder.subsurface(pygame.Rect(48, 0, 48, 48)).copy()
        if self.imgExploderBig is None:
            self.imgExploderBig = \
                self.imgExploder.subsurface(pygame.Rect(96, 0, 48, 48)).copy()

        if stage == 0:
            return self.imgExploderSmall.copy()
        elif stage == 1:
            return self.imgExploderMiddle.copy()
        else:
            return self.imgExploderBig.copy()
