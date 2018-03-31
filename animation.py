# -*- coding: utf-8 -*-
from alarm import Alarm


class Animation:
    def __init__(self, frameList):
        self.frameList = frameList  # 设置帧列表, frameList为一个list, 每一个成员均为surface
        self.maxFrame = len(self.frameList)  # 动画帧数量
        self.currentFrameIdx = 0  # 当前动画帧id
        self.frameDurationMsec = 0  # 播放动画时使用的帧间隔
        self.pos = [0, 0]  # 动画发生地点, 单位为像素
        self.surface = None  # 动画发生的surface
        self.repeat = 0  # 循环次数 0-无限循环
        self.isStart = False  # 动画是否开始显示
        self.alarm = Alarm()

    def setFrameDuration(self, duration_msec):
        self.frameDurationMsec = duration_msec

    def setPostion(self, surface, pos):
        # 设置动画发生的地点
        self.pos = pos
        self.surface = surface

    def setRepeat(self, repeat):
        # 设置循环模式, 0-无限循环, >0-循环几次
        self.repeat = repeat

    def draw(self):
        # 周期性的调用此函数即可进行动画描画
        if not self.isStart:
            self.isStart = True
            self.alarm.setTimeout(self.frameDurationMsec)
            self.alarm.start()
        if self.alarm.isTimeout():
            self.currentFrameIdx += 1
            if self.currentFrameIdx == self.maxFrame:
                self.currentFrameIdx = 0
        self.surface.blit(self.frameList[self.currentFrameIdx], self.pos)
