# -*- coding: utf-8 -*-
import threading
from animation import Animation
from res_ctrl import ResCtrl


class AnimeCtrl:
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if not hasattr(AnimeCtrl, "_instance"):
            with AnimeCtrl._instance_lock:
                if not hasattr(AnimeCtrl, "_instance"):
                    AnimeCtrl._instance = AnimeCtrl()
        return AnimeCtrl._instance

    def getExplodingAnime(self, surface, pos, duration=500, repeat=0):
        resCtrl = ResCtrl.instance()
        exploderList = []
        # 获取爆炸阶段的图片
        exploderSmallImg = resCtrl.getImgExploder(0)
        exploderMiddleImg = resCtrl.getImgExploder(1)
        exploderBigImg = resCtrl.getImgExploder(2)
        # 将图片插入图片列表
        exploderList.append(exploderSmallImg)
        exploderList.append(exploderMiddleImg)
        exploderList.append(exploderBigImg)
        # 生成动画
        explodingAnime = Animation(exploderList)
        explodingAnime.setFrameDuration(duration)
        explodingAnime.setPostion(surface, pos)
        explodingAnime.setRepeat(repeat)
        return explodingAnime
