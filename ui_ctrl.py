# -*- coding: utf-8 -*-
import pygame
from utils import Utils

# 当前UICtrl状态
NORMAL_STATE = 0  # 通常状态
SHOW_MACH_INFO_STATE = 1  # 选中某个Machine的状态

BUTTON_STATE_UP = 0
BUTTON_STATE_DOWN = 1


class UICtrl:
    def __init__(self, ui_surface):
        self.surface = ui_surface
        self.rect = ui_surface.get_rect()
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
        Utils.instance().drawText(interRect, caption)

    def showMachineInfo(self, machine):
        # 显示当前machine的信息
        utils = Utils.instance()
        rect = pygame.Rect(10, 30, 150, 35)
        utils.drawText(self.surface, rect, u"代号: %s" % machine.getName(), 1)
        max_hp = machine.getMaxHp()
        hp = machine.getHp()
        atk = machine.getAtk()
        atk_range = machine.getAtkRange()
        rect.move_ip(0, 40)
        utils.drawText(self.surface, rect, u"生命值: %d/%d" % (hp, max_hp), 1)
        rect.move_ip(0, 40)
        utils.drawText(self.surface, rect, u"攻击力: %d" % atk, 1)
        rect.move_ip(0, 40)
        utils.drawText(self.surface, rect, u"攻击范围: %d" % atk_range, 1)
