# -*- coding: utf-8 -*-
import datetime


class Alarm:
    def __init__(self):
        self.timout_msec = 0
        self.last_alarm_time = -1

    def setTimeout(self, msec):
        # 设定超时时间, 单位毫秒
        self.timout_msec = msec

    def start(self):
        # 开始定时器
        self.last_alarm_time = datetime.datetime.now()

    def isTimeout(self):
        # 检查是否到达超时时间, 到达返回True, 否则返回False
        now = datetime.datetime.now()
        duration = now - self.last_alarm_time
        if duration.total_seconds() * 1000 > self.timout_msec:
            self.last_alarm_time = now
            return True
        return False
