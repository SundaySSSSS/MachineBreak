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
        self.mousePos = [-1, -1] # 鼠标所在位置, 单位像素, 相对于地图surface
        # 视点所在位置, 单位为地图index, 表示显示的左上角第一个地图块的index. (0, 0)表示从地图左上角进行展示
        self.viewPos = [0, 0]
        # 地图中能在屏幕中显示的瓦片数
        self.visibleTileW = self.surface.get_width() / MAP_TITLE_SIZE + 1
        self.visibleTileH = self.surface.get_height() / MAP_TITLE_SIZE + 1
        print(self.visibleTileH)

    def loadMap(self, map_path):
        with open(map_path) as fp:
            map_file_content = fp.read()
            map_json = json.loads(map_file_content)
            self.mapInfo = MapInfo(map_json)
            fp.close()

    # 设置当前鼠标位置
    def setMousePos(self, pos):
        self.mousePos = pos

    # 移动地图
    def down(self, step):
        if self.viewPos[1] + self.visibleTileH < self.mapInfo.h + 1:
            self.viewPos[1] += step

    def up(self, step):
        if self.viewPos[1] > 0:
            self.viewPos[1] -= step

    def right(self, step):
        if self.viewPos[0] + self.visibleTileW < self.mapInfo.w + 1:
            self.viewPos[0] += step

    def left(self, step):
        if self.viewPos[0] > 0:
            self.viewPos[0] -= step
    # 描画相关
    def drawLowerItem(self):
        grass = self.resCtrl.getImgGrass()
        water = self.resCtrl.getImgWater()
        #self.surface.blit(grass, (0, 0))
        mapTileNum = self.mapInfo.w * self.mapInfo.h
        count = 0
        while count < mapTileNum:
            index = self.mapInfo.data[count]
            # 计算在地图中的坐标
            map_x = (count % self.mapInfo.w) - self.viewPos[0]
            map_y = (count / self.mapInfo.w) - self.viewPos[1]
            # 计算在surface中的坐标(单位: 像素)
            sur_x = map_x * MAP_TITLE_SIZE
            sur_y = map_y * MAP_TITLE_SIZE
            if index == 1:
                self.surface.blit(grass, (sur_x, sur_y))
            elif index == 2:
                self.surface.blit(water, (sur_x, sur_y))
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
        self.surface.fill((0,0,0))
        self.drawLowerItem()
        self.drawUpperItem()
        self.drawMachine()
        self.drawTarget()
