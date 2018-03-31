# -*- coding: utf-8 -*-
import pygame
from director import Director
import param


def main():
    pygame.init()
    screen = pygame.display.set_mode((param.SCR_W, param.SCR_H))
    pygame.display.set_caption("Machine Break")

    # 创建导演
    director = Director(screen)

    while True:
        for event in pygame.event.get():
            director.processEvent(event)
            director.draw()
            pygame.display.update()


if __name__ == "__main__":
    main()
