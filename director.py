# -*- coding: utf-8 -*-
import pygame, sys
from ui_ctrl import *
from map_ctrl import *
#from event_ctrl import *
from res_ctrl import *

class Director:
    def __init__(self, screen):
        self.rect = screen.get_rect()
        self.screen = screen
        resCtrl = ResCtrl()
        # 创建UI区域
        uiRect = pygame.Rect(0, 0, self.rect.width / 4, self.rect.height)
        ui_surface = screen.subsurface(uiRect)
        self.uiCtrl = UICtrl(ui_surface, resCtrl)
        # 创建地图区域
        mapRect = pygame.Rect(self.rect.width / 4, 0, self.rect.width - self.rect.width / 4, self.rect.height)
        map_surface = screen.subsurface(mapRect)
        self.mapCtrl = MapCtrl(map_surface, resCtrl)
        
        #self.eventCtrl = eventCtrl()
        # 加载地图
        self.mapCtrl.loadMap("res/map/test.json")

    def draw(self):
        self.uiCtrl.draw()
        self.mapCtrl.draw()
        pass

    def processEvent(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == "":
                print("[KEYDOWN]:", "#", event.key, event.mod)
            else:
                print("[KEYDOWN]:", event.unicode, event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            #print("[MOUSEMOTION]:", event.pos, event.rel, event.buttons)
            pass
        elif event.type == pygame.MOUSEBUTTONUP:
            print("[MOUSEBUTTONUP]:", event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MOUSEBUTTONDOWN]:", event.pos, event.button)
        
