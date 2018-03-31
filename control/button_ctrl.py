# -*- coding: utf-8 -*-
import pygame
import sys
sys.path.append("..")
from utils import Utils

BUTTON_STATE_UP = 0
BUTTON_STATE_DOWN = 1


class ButtonCtrl:
    def __init__(self, surface, rect, text):
        self.surface = surface
        self.rect = rect
        self.text = text
        self.callback = None
        self.state = BUTTON_STATE_UP

    def setCallback(self, callback):
        # 设置点击回调, callback要求是一个无参数, 无返回值的函数
        self.callback = callback

    def isInside(self, pos):
        # 判定pos是否在控件内 pos是一个元组或列表(0, 1)或[2, 3]
        rect = pygame.Rect(pos[0], pos[1], 0, 0)
        return self.rect.contains(rect)

    def mouseDown(self, pos):
        if self.isInside(pos):
            self.state = BUTTON_STATE_DOWN

    def mouseUp(self, pos):
        if self.isInside(pos):
            if self.state == BUTTON_STATE_DOWN:
                self.state = BUTTON_STATE_UP
                self.callback()

    def draw(self):
        rect = self.rect
        frameRect = rect
        interRect = rect.inflate(-6, -6)
        frameColor = pygame.Color(188, 129, 29)
        interColor = pygame.Color(233, 177, 4)
        if self.state == BUTTON_STATE_DOWN:
            interColor = frameColor
        pygame.draw.rect(self.surface, frameColor, frameRect)
        pygame.draw.rect(self.surface, interColor, interRect)
        # 描画文字
        Utils.instance().drawText(self.surface, interRect, self.text)
