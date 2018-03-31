# -*- coding: utf-8 -*-
import pygame
import sys
from control.button_ctrl import ButtonCtrl


class StartWindow():
    def __init__(self, screen):
        self.screen = screen
        self.btnMachineDesigner = \
            ButtonCtrl(screen, pygame.Rect(20, 30, 400, 50),
                       "Machine Designer")
        self.btnMachineDesigner.setCallback(self.machineDesignerBtnClick)
        self.btnFightSim = \
            ButtonCtrl(screen, pygame.Rect(20, 100, 400, 50),
                       "Fight Sim")
        self.btnFightSim.setCallback(self.fightSimBtnClick)
        self.ctrlList = []
        self.ctrlList.append(self.btnMachineDesigner)
        self.ctrlList.append(self.btnFightSim)

    def processEvent(self, event):
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass
        elif event.type == pygame.MOUSEMOTION:
            pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ctrl in self.ctrlList:
                ctrl.mouseDown(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            for ctrl in self.ctrlList:
                ctrl.mouseUp(event.pos)

    def doModel(self):
        while True:
            for event in pygame.event.get():
                # 鼠标按下事件
                # 判定是否在控件内, 如果是, 调用相应回调
                self.processEvent(event)
            # 描画所有控件
            for ctrl in self.ctrlList:
                ctrl.draw()
            pygame.display.update()

    def machineDesignerBtnClick(self):
        print("click Machine Designer")

    def fightSimBtnClick(self):
        print("click Fight Sim")
