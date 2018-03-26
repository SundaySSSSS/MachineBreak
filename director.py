# -*- coding: utf-8 -*-
import pygame, sys
from ui_ctrl import *
from map_ctrl import *
#from event_ctrl import *
from res_ctrl import *
from param import *


class Director:
    def __init__(self, screen):
        self.rect = screen.get_rect()
        self.screen = screen
        resCtrl = ResCtrl()
        # 创建UI区域
        uiRect = pygame.Rect(UI_AREA_X, UI_AREA_Y, UI_AREA_W, UI_AREA_H)
        ui_surface = screen.subsurface(uiRect)
        self.uiCtrl = UICtrl(ui_surface, resCtrl)
        # 创建地图区域
        mapRect = pygame.Rect(MAP_AREA_X, MAP_AREA_Y, MAP_AREA_W, MAP_AREA_H)
        map_surface = screen.subsurface(mapRect)
        self.mapCtrl = MapCtrl(map_surface, resCtrl)
        
        # 加载地图
        self.mapCtrl.loadMap("res/map/test.json")

    def draw(self):
        self.uiCtrl.draw()
        self.mapCtrl.draw()

    def processEvent(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN]:", "#", event.key, event.mod)
            else:
                print("[KEYDOWN]:", event.unicode, event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            # 转化为地图区域的坐标
            mousePosInMap = (event.pos[0] - MAP_AREA_X, event.pos[1])
            self.mapCtrl.setMousePos(mousePosInMap)
        elif event.type == pygame.MOUSEBUTTONUP:
            print("[MOUSEBUTTONUP]:", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MOUSEBUTTONDOWN]:", event.pos, event.button)
        
