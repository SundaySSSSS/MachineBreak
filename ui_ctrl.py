# -*- coding: utf-8 -*-
import pygame
from res_ctrl import ResCtrl

BUTTON_STATE_UP = 0
BUTTON_STATE_DOWN = 1


class UICtrl:
    def __init__(self, ui_surface, resCtrl):
        self.surface = ui_surface
        self.rect = ui_surface.get_rect()
        self.resCtrl = resCtrl

    def draw(self):
        pygame.draw.rect(self.surface, pygame.Color(3, 136, 239), self.rect)
        pygame.draw.rect(self.surface, pygame.Color(7, 89, 175),
                         self.rect.inflate(-10, -10))
        self.drawButton(pygame.Rect(10, 20, 150, 50), "caption", 1)
        self.drawButton(pygame.Rect(10, 100, 150, 50), "test", 0)

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
        font_sur = font.render(caption, True, (255, 0, 0))
        self.surface.blit(font_sur, interRect)
