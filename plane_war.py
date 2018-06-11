# -*- coding: UTF-8 -*-
from game_judge import *
from game_screen import *
from game_sprites import *
import pygame

"""
首先初始化游戏，创建游戏裁判系统，并初始化PyGame
在主函数中调创建游戏对象并开始游戏
"""

SCREEN_SIZE = pygame.Rect(0, 0, 480, 680)
FRAME_PER_SEC = 60


class PlaneWar(object):

    def __init__(self):
        pygame.display.init()
        # 初始化游戏显示体系
        self.__game_screen = GameScreen()
        # 初始化游戏裁判体系
        self.__game_judge = GameJudge(self.__game_screen)
        # 初始化游戏时钟
        self.__game_clock = pygame.time.Clock()
        pygame.display.update()

    def star_game(self):
        # 建立游戏循环
        while True:
            # 设置游戏帧率
            self.__game_clock.tick(FRAME_PER_SEC)
            # 将游戏事件交由裁判体系
            self.__game_judge.check_events(pygame.event.get())
            # 使用游戏显示体系更新游戏画面
            self.__game_screen.update_sprites()
            # 重新绘制游戏界面
            pygame.display.update()


if __name__ == '__main__':
    plane_game = PlaneWar()
    plane_game.star_game()
