# -*- coding: utf-8 -*-
import pygame
from res_ctrl import ResCtrl

# 当前UICtrl状态
NORMAL_STATE = 0 # 通常状态
SHOW_MACH_INFO_STATE = 1 # 选中某个Machine的状态

BUTTON_STATE_UP = 0
BUTTON_STATE_DOWN = 1


class UICtrl:
    def __init__(self, ui_surface, resCtrl):
        self.surface = ui_surface
        self.rect = ui_surface.get_rect()
        self.resCtrl = resCtrl
        self.state = NORMAL_STATE

    def stateShowMachineInfo(self, machine):
        # 切换到显示Machine信息状态
        self.state = SHOW_MACH_INFO_STATE
        self.machine = machine

    def stateNormal(self):
        # 切换到通常状态
        self.state = NORMAL_STATE
        self.machine = None
        
    def draw(self):
        pygame.draw.rect(self.surface, pygame.Color(3, 136, 239), self.rect)
        pygame.draw.rect(self.surface, pygame.Color(7, 89, 175),
                         self.rect.inflate(-10, -10))
        # self.drawButton(pygame.Rect(10, 20, 150, 50), "caption", 1)
        # self.drawButton(pygame.Rect(10, 100, 150, 50), "test", 0)
        if self.state == SHOW_MACH_INFO_STATE:
            self.showMachineInfo(self.machine)
        

    def drawButton(self, rect, caption, state):
        frameRect = rect
        interRect = rect.inflate(-6, -6)
        frameColor = pygame.Color(188, 129, 29)
        interColor = pygame.Color(233, 177, 4)
        if state == BUTTON_STATE_DOWN:
            interColor = frameColor
        pygame.draw.rect(self.surface, frameColor, frameRect)
        pygame.draw.rect(self.surface, interColor, interRect)
        # 描画文字
        font_size = interRect.height - 12
        if font_size < 10:
            font_size = 10
        font = pygame.font.Font("res/font/Arial Unicode.ttf", font_size)
        font_sur = font.render(caption, True, (255, 255, 255))
        self.drawText(interRect, caption)

    def drawText(self, rect, text, color = pygame.Color(0, 0, 0)):
        font_size = rect.height - 12
        if font_size < 10:
            font_size = 10
        font = pygame.font.Font("res/font/Arial Unicode.ttf", font_size)
        font_sur = font.render(text, True, color)
        # 居中显示文字
        font_rect = font_sur.get_rect()
        font_rect.x = rect.x + (rect.width - font_rect.width) // 2
        font_rect.y = rect.y + (rect.height - font_rect.height) // 2
        self.surface.blit(font_sur, font_rect)

    def showMachineInfo(self, machine):
        # 显示当前machine的信息
        rect = pygame.Rect(10, 30, 150, 50)
        self.drawText(rect, machine.getName())
