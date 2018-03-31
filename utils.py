# -*- coding: utf-8 -*-
import pygame
import threading


class Utils:
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if not hasattr(Utils, "_instance"):
            with Utils._instance_lock:
                if not hasattr(Utils, "_instance"):
                    Utils._instance = Utils()
        return Utils._instance

    def drawText(self, surface, rect, text,
                 alignment=0, color=pygame.Color(0, 0, 0)):
        # 描画文字, alignment: 0-居中, 1-左对齐
        font_size = rect.height - 12
        if font_size < 10:
            font_size = 10
        font = pygame.font.Font("res/font/Arial Unicode.ttf", font_size)
        font_sur = font.render(text, True, color)
        # 居中显示文字
        font_rect = font_sur.get_rect()
        if alignment == 0:  # 居中对齐
            font_rect.x = rect.x + (rect.width - font_rect.width) // 2
        else:
            font_rect.x = rect.x
        font_rect.y = rect.y + (rect.height - font_rect.height) // 2
        surface.blit(font_sur, font_rect)
