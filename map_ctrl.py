# -*- coding: utf-8 -*-
import pygame, sys
from res_ctrl import *
from param import *
import json

class MapInfo:
    def __init__(self, map_json):
        self.data = map_json['layers'][0]['data']
        self.w = map_json['layers'][0]['width']
        self.h = map_json['layers'][0]['height']
    
class MapCtrl:
    def __init__(self, map_surface, resCtrl):
        self.surface = map_surface
        self.resCtrl = resCtrl
        self.mousePos = (-1, -1) # 鼠标所在位置

    def loadMap(self, map_path):
        with open(map_path) as fp:
            map_file_content = fp.read()
            map_json = json.loads(map_file_content)
            self.mapInfo = MapInfo(map_json)
            fp.close()

    # 设置当前鼠标位置
    def setMousePos(self, pos):
        self.mousePos = pos
    
    def drawLowerItem(self):
        grass = self.resCtrl.getImgGrass()
        water = self.resCtrl.getImgWater()
        #self.surface.blit(grass, (0, 0))
        mapTileNum = self.mapInfo.w * self.mapInfo.h
        count = 0
        while count < mapTileNum:
            index = self.mapInfo.data[count]
            x = (count % self.mapInfo.w) * MAP_TITLE_SIZE
            y = (count / self.mapInfo.w) * MAP_TITLE_SIZE
            if index == 1:
                self.surface.blit(grass, (x, y))
            elif index == 2:
                self.surface.blit(water, (x, y))
            count += 1
            
    
    def drawUpperItem(self):
        pass
    
    def drawMachine(self):
        pass

    def drawTarget(self):
        # 描画鼠标target
        #mouse_x = self.mousePos[0] / MAP_TITLE_SIZE
        #mouse_y = self.mousePos[1] / MAP_TITLE_SIZE
        #print("mouse x = %d, y = %d" % (mouse_x, mouse_y))
        normal_target = self.resCtrl.getImgNormalTarget()
        mouse_draw_pos = (self.mousePos[0] / MAP_TITLE_SIZE * MAP_TITLE_SIZE, self.mousePos[1] / MAP_TITLE_SIZE * MAP_TITLE_SIZE)
        self.surface.blit(normal_target, mouse_draw_pos)
    
    def draw(self):
        self.drawLowerItem()
        self.drawUpperItem()
        self.drawMachine()
        self.drawTarget()
