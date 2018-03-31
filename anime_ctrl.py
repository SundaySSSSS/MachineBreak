# -*- coding: utf-8 -*-
import threading
from animation import Animation
from res_ctrl import ResCtrl


class AnimeCtrl:
    _instance_lock = threading.Lock()

    def __init__(self):
        self.explodingAnime = None

    @classmethod
    def instance(cls):
        if not hasattr(AnimeCtrl, "_instance"):
            with AnimeCtrl._instance_lock:
                if not hasattr(AnimeCtrl, "_instance"):
                    AnimeCtrl._instance = AnimeCtrl()
        return AnimeCtrl._instance

    def getExplodingAnime(self, surface, pos, duration=500):
        if self.explodingAnime is None:
            resCtrl = ResCtrl.instance()
            exploderList = []
            for stage in range(3):
                exploderImg = resCtrl.getImgExploder(stage)
                exploderList.append(exploderImg)
            explodingAnime = Animation(exploderList)
            explodingAnime.setFrameDuration(duration)
            explodingAnime.setPostion(surface, pos)
            self.explodingAnime = explodingAnime
        return self.explodingAnime
