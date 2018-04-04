# -*- coding: utf-8 -*-
import pygame
import param
from start_window import StartWindow


def main():
    pygame.init()
    screen = pygame.display.set_mode((param.SCR_W, param.SCR_H))
    pygame.display.set_caption("Machine Break")

    sw = StartWindow(screen)
    sw.doModel()


if __name__ == "__main__":
    main()
