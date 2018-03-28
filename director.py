# -*- coding: utf-8 -*-
import pygame
import sys
from ui_ctrl import UICtrl
from map_ctrl import MapCtrl
from res_ctrl import ResCtrl
import param


class Director:
    def __init__(self, screen):
        self.rect = screen.get_rect()
        self.screen = screen
        resCtrl = ResCtrl()
        # 创建UI区域
        uiRect = pygame.Rect(param.UI_AREA_X, param.UI_AREA_Y,
                             param.UI_AREA_W, param.UI_AREA_H)
        ui_surface = screen.subsurface(uiRect)
        self.uiCtrl = UICtrl(ui_surface, resCtrl)
        # 创建地图区域
        mapRect = pygame.Rect(param.MAP_AREA_X, param.MAP_AREA_Y,
                              param.MAP_AREA_W, param.MAP_AREA_H)
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
            key = event.key
            if key == pygame.K_DOWN or key == pygame.K_s:
                self.mapCtrl.down(1)
            if key == pygame.K_UP or key == pygame.K_w:
                self.mapCtrl.up(1)
            if key == pygame.K_LEFT or key == pygame.K_a:
                self.mapCtrl.left(1)
            if key == pygame.K_RIGHT or key == pygame.K_d:
                self.mapCtrl.right(1)
        elif event.type == pygame.MOUSEMOTION:
            # 鼠标移动
            # 转化为地图surface的坐标
            posInSurface = (event.pos[0] - param.MAP_AREA_X, event.pos[1])
            self.mapCtrl.setMousePos(posInSurface)
        elif event.type == pygame.MOUSEBUTTONUP:
            # 鼠标抬起
            # 转化为地图surface的坐标
            posInSurface = (event.pos[0] - param.MAP_AREA_X, event.pos[1])
            select_thing = self.mapCtrl.selectSomething(posInSurface)
            if select_thing == param.SELECT_MACHINE:
                machine = self.mapCtrl.getSelectMachine()
                self.uiCtrl.stateShowMachineInfo(machine)   

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("[MOUSEBUTTONDOWN]:", event.pos, event.button)

