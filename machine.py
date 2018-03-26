# -*- coding: utf-8 -*-
import pygame, sys
from param import *

class Machine:
    def __init__(self, pos, resCtrl):
        self.pos = pos # 位置, 例如[2, 3]
        self.actionAblity = 3 # 行动力
        self.actionLeft = 3 # 剩余行动力
        self.img = resCtrl.getImgMachine()
        
    def moveTo(pos):
        distance = math.abs(self.pos[0] - pos[0]) + math.abs(self.pos[1] - self.pos[1])
        if distance < self.actionLeft:
            self.pos = pos
            self.actionLeft -= distance

    def getImg(self):
        return self.img.copy()
        
        

    
