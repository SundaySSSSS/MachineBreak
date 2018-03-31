# -*- coding: utf-8 -*-
import param
from machine import Machine
from res_ctrl import ResCtrl
from animation import Animation
import json

# MapCtrl的状态
NORMAL_STATE = 0  # 通常状态
MACH_SELETED_STATE = 1  # 选中了某个Machine的状态


class MapInfo:
    def __init__(self, map_json):
        self.data = map_json['layers'][0]['data']
        self.w = map_json['layers'][0]['width']
        self.h = map_json['layers'][0]['height']


class MapCtrl:
    def __init__(self, map_surface):
        self.state = NORMAL_STATE  # 当前状态
        self.surface = map_surface

        self.mousePos = [-1, -1]  # 鼠标所在位置, 单位像素, 相对于地图surface
        # 视点所在位置, 单位为地图index, 表示显示的左上角第一个地图块的index. (0, 0)表示从地图左上角进行展示
        self.viewPos = [0, 0]
        # 地图中能在屏幕中显示的瓦片数
        self.visibleTileW = \
            self.surface.get_width() // param.MAP_TILE_SIZE + 1
        self.visibleTileH = \
            self.surface.get_height() // param.MAP_TILE_SIZE + 1
        # Machine列表
        self.machineList = []
        self.machineList.append(Machine("Tom", [2, 3]))
        self.machineList.append(Machine("Jerry", [5, 5]))
        self.selectMachine = None  # 当前选中的Machine
        self.movableList = []  # 选中Machine的可移动地图块列表
        self.attackableList = []  # 选中Machine的可攻击目标列表

        # 初始化动画
        self.animeList = []
        resCtrl = ResCtrl.instance()
        exploderList = []
        for stage in range(3):
            exploderImg = resCtrl.getImgExploder(stage)
            exploderList.append(exploderImg)
        explodingAnime = Animation(exploderList)
        explodingAnime.setFrameDuration(500)
        explodingAnime.setPostion(self.surface, (0, 0))
        self.animeList.append(explodingAnime)

    def getSelectMachine(self):
        # 获取当前选中的Machine
        return self.selectMachine

    def loadMap(self, map_path):
        with open(map_path) as fp:
            map_file_content = fp.read()
            map_json = json.loads(map_file_content)
            self.mapInfo = MapInfo(map_json)
            fp.close()
        return

    def isHaveMachineAt(self, mapPos):
        # 检查输入位置是否存在machine(pos为地图坐标)
        for mach in self.machineList:
            machPos = mach.getPos()
            if machPos[0] == list(mapPos)[0] and machPos[1] == list(mapPos)[1]:
                return True
        return False

    def getMachineByMapPos(self, mapPos):
        # 通过地图坐标找到对应的machine
        for mach in self.machineList:
            machPos = mach.getPos()
            if machPos[0] == list(mapPos)[0] and machPos[1] == list(mapPos)[1]:
                return mach
        return None

    def mapPos2SurPos(self, mapPos):
        # 从地图坐标转化为surface坐标
        surPos = [0, 0]
        surPos[0] = (mapPos[0] - self.viewPos[0]) * param.MAP_TILE_SIZE
        surPos[1] = (mapPos[1] - self.viewPos[1]) * param.MAP_TILE_SIZE
        return surPos

    def surPos2MapPos(self, surPos):
        # 从surface坐标转化为地图坐标
        mapPos = [0, 0]
        mapPos[0] = (surPos[0] // param.MAP_TILE_SIZE) + self.viewPos[0]
        mapPos[1] = (surPos[1] // param.MAP_TILE_SIZE) + self.viewPos[1]
        return mapPos

    def setMousePos(self, surPos):
        # 设置当前鼠标位置
        self.mousePos = surPos

    def selectSomething(self, surPos):
        # 在地图上选择了某个地图块(一般是鼠标左键抬起)
        select_thing = param.SELECT_MAP_TILE  # 标记当前选中了什么
        mapPos = self.surPos2MapPos(surPos)
        if self.state == NORMAL_STATE:
            if self.isHaveMachineAt(mapPos):
                self.selectMachine = self.getMachineByMapPos(mapPos)
                self.state = MACH_SELETED_STATE  # 选中了某个Machine, 切换状态
                select_thing = param.SELECT_MACHINE
                # 选中了一个Machine, 计算可以移动的范围
                self.movableList = self.getMovableTile(
                    self.selectMachine.getPos(),
                    self.selectMachine.getActionAbilityLeft())
                self.attackableList = self.getAttackableTile(
                    self.selectMachine.getPos(),
                    self.selectMachine.getAtkRange())
        elif self.state == MACH_SELETED_STATE:
            if tuple(mapPos) in self.movableList:
                # 选中的目标在可移动范围内, 移动到目标位置
                self.selectMachine.moveTo(mapPos, self.getDistance(
                    mapPos, self.selectMachine.getPos()))
            if tuple(mapPos) in self.attackableList:
                # 选中的目标在攻击范围内, 进行攻击
                target_machine = self.getMachineByMapPos(mapPos)
                self.selectMachine.attackMachine(target_machine)
            self.state = NORMAL_STATE  # 什么也没选中, 切换到通常状态
            self.selectMachine.turnStart()  # 仅用于测试, 实装回合切换后去除
            self.selectMachine = None
            self.movableList = []
            self.attackableList = []
        return select_thing

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
        grass = ResCtrl.instance().getImgGrass()
        water = ResCtrl.instance().getImgWater()
        mapTileNum = self.mapInfo.w * self.mapInfo.h
        count = 0
        while count < mapTileNum:
            index = self.mapInfo.data[count]
            # 计算在surface中的坐标(单位: 像素)
            mapPos = [count % self.mapInfo.w, count // self.mapInfo.w]
            surPos = self.mapPos2SurPos(mapPos)
            if index == 1:
                self.surface.blit(grass, surPos)
            elif index == 2:
                self.surface.blit(water, surPos)
            count += 1

    def drawUpperItem(self):
        for anime in self.animeList:
            anime.draw()

    def drawMachine(self):
        # Machine层描画
        for machine in self.machineList:
            machineImg = machine.getImg()
            machinePos = self.mapPos2SurPos(machine.getPos())
            self.surface.blit(machineImg, machinePos)

    def getDistance(self, mapPos1, mapPos2):
        # 获取地图上两个点的距离
        distance_x = abs(mapPos1[0] - mapPos2[0])
        distance_y = abs(mapPos1[1] - mapPos2[1])
        return distance_x + distance_y

    def getNearByTile(self, centerMapPos, radius):
        # 获取指定中心附近的地图块列表
        nearByList = []
        # 获取可移动的大致范围
        min_x = centerMapPos[0] - radius
        if min_x < 0:
            min_x = 0
        max_x = centerMapPos[0] + radius
        if max_x >= self.mapInfo.w:
            max_x = self.mapInfo.w - 1
        min_y = centerMapPos[1] - radius
        if min_y < 0:
            min_y = 0
        max_y = centerMapPos[1] + radius
        if max_y >= self.mapInfo.h:
            max_y = self.mapInfo.h - 1
        # 在较小的范围内遍历所有点
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                distance = self.getDistance((x, y), centerMapPos)
                if (distance <= radius):
                    nearByList.append((x, y))
        return nearByList

    def getMovableTile(self, startMapPos, actionAblity):
        # 获取可移动的位置列表
        delList = []
        movableList = self.getNearByTile(startMapPos, actionAblity)
        # 剔除存在障碍的点
        for mapPos in movableList:
            if self.isHaveMachineAt(mapPos):
                # 如果目标地点有machine, 将该图块加入剔除列表
                delList.append(mapPos)
        for mapPos in delList:
            movableList.remove(mapPos)
        return movableList

    def getAttackableTile(self, attackerPos, atkRange):
        # 获取可攻击位置列表
        nearbyList = self.getNearByTile(attackerPos, atkRange)
        attackableList = []
        # 从中筛选存在攻击目标的项
        for mapPos in nearbyList:
            if self.isHaveMachineAt(mapPos):
                attackableList.append(mapPos)
        # 去除中心(自己)
        attackableList.remove(tuple(attackerPos))
        return attackableList

    def drawTarget(self):
        # Target层描画
        # 描画可选目标target(当选中machine后显示可移动范围)
        if self.state == MACH_SELETED_STATE:
            if self.selectMachine is not None:
                # 在可移动地点上描画标记
                movableTarget = ResCtrl.instance().getImgMovableTarget()
                for mapPos in self.movableList:
                    surPos = self.mapPos2SurPos(mapPos)
                    self.surface.blit(movableTarget, surPos)
                # 在可攻击地点上描画攻击标记
                attackableTarget = ResCtrl.instance().getImgAttackableTarget()
                for mapPos in self.attackableList:
                    surPos = self.mapPos2SurPos(mapPos)
                    self.surface.blit(attackableTarget, surPos)

        # 描画鼠标target
        mouse_draw_pos = \
            (self.mousePos[0] // param.MAP_TILE_SIZE * param.MAP_TILE_SIZE,
             self.mousePos[1] // param.MAP_TILE_SIZE * param.MAP_TILE_SIZE)
        mouse_map_pos = (self.mousePos[0] // param.MAP_TILE_SIZE,
                         self.mousePos[1] // param.MAP_TILE_SIZE)
        if mouse_map_pos in self.attackableList:
            mouse_target = ResCtrl.instance().getImgAttackTarget()
        else:
            mouse_target = ResCtrl.instance().getImgNormalTarget()
        self.surface.blit(mouse_target, mouse_draw_pos)

    def draw(self):
        # 地图描画, 地图从下到上依次为:
        # Lower层: 草地, 水面等
        # Upper层: 草, 树, 山等
        # Machine层: machines
        # Target层: 描画目标, 如鼠标位置, 可移动区域等, 用于指示操作
        self.surface.fill((0, 0, 0))
        self.drawLowerItem()
        self.drawUpperItem()
        self.drawMachine()
        self.drawTarget()
