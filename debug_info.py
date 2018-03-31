# -*- coding: utf-8 -*-
import pygame
from utils import Utils


class DebugInfo:
    def __init__(self, screen):
        self.surface = screen
        self.rect = self.surface.get_rect()
        self.line_num = 0
        self.line_height = 32

    def clean(self):
        self.line_num = 0

    def drawLine(self, text):
        utils = Utils.instance()
        line_rect = pygame.Rect(0, self.line_num * self.line_height,
                                self.rect.width, self.line_height)
        utils.drawText(self.surface, line_rect, text, 1)
