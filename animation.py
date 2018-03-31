# -*- coding: utf-8 -*-
from alarm import Alarm

# 定义动画运行的状态
ANIME_READY = 0  # 就绪状态, 可以开始
ANIME_RUNNING = 1  # 动画正在播放状态
ANIME_FINISHED = 2  # 动画已经播放完毕


class Animation:
    def __init__(self, frameList):
        self.frameList = frameList  # 设置帧列表, frameList为一个list, 每一个成员均为surface
        self.maxFrame = len(self.frameList)  # 动画帧数量
        self.currentFrameIdx = 0  # 当前动画帧id
        self.frameDurationMsec = 0  # 播放动画时使用的帧间隔
        self.pos = [0, 0]  # 动画发生地点, 单位为像素
        self.surface = None  # 动画发生的surface
        self.repeat = 0  # 循环次数 0-无限循环
        self.state = ANIME_READY  # 动画就绪
        self.alarm = Alarm()
        self.playTimes = 0  # 动画被播放的次数

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
        if self.state == ANIME_READY:
            self.state = ANIME_RUNNING
            self.alarm.setTimeout(self.frameDurationMsec)
            self.alarm.start()
        elif self.state == ANIME_RUNNING:
            if self.alarm.isTimeout():
                self.currentFrameIdx += 1
                if self.currentFrameIdx == self.maxFrame:
                    self.currentFrameIdx = 0
                    if self.repeat != 0:
                        # 不是无限循环
                        self.playTimes += 1
                        if self.playTimes == self.repeat:
                            # 到达播放次数
                            self.state = ANIME_FINISHED
            self.surface.blit(self.frameList[self.currentFrameIdx], self.pos)
        else:
            pass  # 不做任何事

    def isAlive(self):
        # 判断动画是否存活
        if self.state == ANIME_FINISHED:
            return False
        return True
