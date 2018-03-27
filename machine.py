# -*- coding: utf-8 -*-


class Machine:
    def __init__(self, pos, resCtrl):
        self.pos = pos  # 位置, 例如[2, 3]
        self.actionAblity = 3  # 行动力
        self.actionLeft = 3  # 剩余行动力
        self.img = resCtrl.getImgMachine()

    def moveTo(self, pos, action_cost):
        # 移动到指定地点, action_cost为消耗的行动力
        self.pos = pos
        self.actionLeft -= action_cost
        if self.actionLeft < 0:
            print("Error, action left < 0")

    def turnStart(self):
        # 回合开始时调用, 刷新Machine的状态
        self.actionLeft = self.actionAblity

    def getImg(self):
        return self.img.copy()

    def getPos(self):
        return self.pos

    def getActionAbility(self):
        # 获取行动力
        return self.actionAblity

    def getActionAbilityLeft(self):
        # 获取剩余行动力
        return self.actionLeft
