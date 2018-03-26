# -*- coding: utf-8 -*-
import pygame, sys
from res_ctrl import *
import json

MAP_TILE_SIZE = 48

class MapInfo:
    def __init__(self, map_json):
        self.data = map_json['layers'][0]['data']
        self.w = map_json['layers'][0]['width']
        self.h = map_json['layers'][0]['height']
        print(self.data)
        #print(self.mapW)
        #print(self.mapH)
    
class MapCtrl:
    def __init__(self, map_surface, resCtrl):
        self.surface = map_surface
        self.resCtrl = resCtrl

    def loadMap(self, map_path):
        with open(map_path) as fp:
            map_file_content = fp.read()
            map_json = json.loads(map_file_content)
            self.mapInfo = MapInfo(map_json)
            fp.close()
        
    
    def drawLowerItem(self):
        grass = self.resCtrl.getImgGrass()
        water = self.resCtrl.getImgWater()
        #self.surface.blit(grass, (0, 0))
        mapTileNum = self.mapInfo.w * self.mapInfo.h
        count = 0
        while count < mapTileNum:
            index = self.mapInfo.data[count]
            x = (count % self.mapInfo.w) * MAP_TILE_SIZE
            y = (count / self.mapInfo.w) * MAP_TILE_SIZE
            if index == 1:
                self.surface.blit(grass, (x, y))
            elif index == 2:
                self.surface.blit(water, (x, y))
            count += 1
            
        
    def drawUpperItem(self):
        pass
    
    def drawMachine(self):
        pass
    
    def draw(self):
        self.drawLowerItem()
        self.drawUpperItem()
        self.drawMachine()
