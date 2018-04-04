# -*- coding: utf-8 -*-
import pygame
from director import Director
from alarm import Alarm
from debug_info import DebugInfo


class BattleWindow():
    def __init__(self, screen):
        self.screen = screen
        self.ctrlList = []
        # 创建导演
        self.director = Director(self.screen)
        # 创建定时器
        self.alarm = Alarm()
        self.alarm.setTimeout(1000)
        self.alarm.start()
        # 创建调试信息
        self.debugInfo = DebugInfo(screen)
        # fps相关
        self.fps_count = 0
        self.fps = 0

    def processEvent(self, event):
        pass

    def doModel(self):
        while True:
            for event in pygame.event.get():
                self.director.processEvent(event)
            # 导演类描画主窗体
            self.director.draw()
            # debug类描画调试信息
            self.debugInfo.clean()
            self.debugInfo.drawLine("fps: %d" % self.fps)

            if self.alarm.isTimeout():
                self.fps = self.fps_count
                self.fps_count = 0
            else:
                self.fps_count += 1

            pygame.display.update()
