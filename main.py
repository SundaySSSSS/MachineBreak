# -*- coding: utf-8 -*-
import pygame
from director import Director
import param
from alarm import Alarm
from debug_info import DebugInfo


def main():
    pygame.init()
    screen = pygame.display.set_mode((param.SCR_W, param.SCR_H))
    pygame.display.set_caption("Machine Break")

    # 创建导演
    director = Director(screen)
    # 创建定时器
    alarm = Alarm()
    alarm.setTimeout(1000)
    alarm.start()
    # 创建调试信息
    debugInfo = DebugInfo(screen)

    fps_count = 0
    fps = 0
    while True:
        for event in pygame.event.get():
            director.processEvent(event)
        # 导演类描画主窗体
        director.draw()
        # debug类描画调试信息
        debugInfo.clean()
        debugInfo.drawLine("fps: %d" % fps)

        if alarm.isTimeout():
            fps = fps_count
            fps_count = 0
        else:
            fps_count += 1

        pygame.display.update()


if __name__ == "__main__":
    main()
