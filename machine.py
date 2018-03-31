# -*- coding: utf-8 -*-
from res_ctrl import ResCtrl


class Machine:
    def __init__(self, name, pos):
        self.pos = list(pos)  # 位置, 例如[2, 3]
        self.actionAblity = 3  # 行动力
        self.actionLeft = 3  # 剩余行动力
        self.atk = 3  # 攻击力
        self.atk_range = 3  # 攻击范围
        self.hp = 10  # 生命值
        self.max_hp = 10  # 最大生命值
        self.name = name  # Machine代号
        self.img = ResCtrl.instance().getImgMachine()

    def moveTo(self, pos, action_cost):
        # 移动到指定地点, action_cost为消耗的行动力
        self.pos = pos
        self.actionLeft -= action_cost
        if self.actionLeft < 0:
            print("Error, action left < 0")

    def attackMachine(self, target_machine):
        # 攻击指定Machine
        target_machine.hp -= self.atk
        if target_machine.hp < 0:
            target_machine.hp = 0

    def turnStart(self):
        # 回合开始时调用, 刷新Machine的状态
        self.actionLeft = self.actionAblity

    def getHp(self):
        return self.hp

    def getMaxHp(self):
        return self.max_hp

    def getAtk(self):
        return self.atk

    def getAtkRange(self):
        return self.atk_range

    def getName(self):
        return self.name

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
