# -*- coding: utf-8 -*-
from res_ctrl import ResCtrl
import param
from machine import Machine
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
        self.mousePos = [-1, -1]  # 鼠标所在位置, 单位像素, 相对于地图surface
        # 视点所在位置, 单位为地图index, 表示显示的左上角第一个地图块的index. (0, 0)表示从地图左上角进行展示
        self.viewPos = [0, 0]
        # 地图中能在屏幕中显示的瓦片数
        self.visibleTileW = self.surface.get_width() / param.MAP_TITLE_SIZE + 1
        self.visibleTileH = self.surface.get_height() / param.MAP_TITLE_SIZE + 1
        # Machine列表
        self.machineList = []
        self.machineList.append(Machine([2, 3], self.resCtrl))

    def loadMap(self, map_path):
        with open(map_path) as fp:
            map_file_content = fp.read()
            map_json = json.loads(map_file_content)
            self.mapInfo = MapInfo(map_json)
            fp.close()
        return

    def mapPos2SurPos(self, mapPos):
        # 从地图坐标转化为surface坐标
        surPos = [0, 0]
        surPos[0] = (mapPos[0] - self.viewPos[0]) * param.MAP_TITLE_SIZE
        surPos[1] = (mapPos[1] - self.viewPos[1]) * param.MAP_TITLE_SIZE
        return surPos

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
        mapTileNum = self.mapInfo.w * self.mapInfo.h
        count = 0
        while count < mapTileNum:
            index = self.mapInfo.data[count]
            # 计算在surface中的坐标(单位: 像素)
            mapPos = [count % self.mapInfo.w, count / self.mapInfo.w]
            surPos = self.mapPos2SurPos(mapPos)
            if index == 1:
                self.surface.blit(grass, surPos)
            elif index == 2:
                self.surface.blit(water, surPos)
            count += 1

    def drawUpperItem(self):
        pass

    def drawMachine(self):
        for machine in self.machineList:
            machineImg = machine.getImg()
            machinePos = self.mapPos2SurPos(machine.getPos())
            self.surface.blit(machineImg, machinePos)

    def drawTarget(self):
        # 描画鼠标target
        normal_target = self.resCtrl.getImgNormalTarget()
        mouse_draw_pos = \
            (self.mousePos[0] / param.MAP_TITLE_SIZE * param.MAP_TITLE_SIZE,
             self.mousePos[1] / param.MAP_TITLE_SIZE * param.MAP_TITLE_SIZE)
        self.surface.blit(normal_target, mouse_draw_pos)

    def draw(self):
        self.surface.fill((0, 0, 0))
        self.drawLowerItem()
        self.drawUpperItem()
        self.drawMachine()
        self.drawTarget()
