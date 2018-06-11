# -*- coding: UTF-8 -*-
from game_sprites import *
import pygame
import game_sprites

CREATE_ENEMY_EVENT = pygame.USEREVENT


class GameJudge(object):
    """游戏总裁判系统
    按功能对裁判系统进行不同模块的划分
    """

    def __init__(self, game_screen):
        self.__judge_system = JudgeSystem(game_screen)
        self.__control_system = ControlSystem(game_screen)
        self.__game_screen = game_screen

    def check_events(self, events):
        # 游戏事件处理
        self.__control_system.check_events(events)
        self.__judge_system.check_collide()


class ControlSystem(object):
    """游戏控制系统
    1. 检测定时器时间、玩家操作等
    2. 生成敌人等
    """

    def __init__(self, game_screen):
        self.__game_screen = game_screen
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 2000)
        pygame.time.set_timer(game_sprites.HERO_SHOOT_EVENT, 300)

    def check_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                game_over()

            if event.type == CREATE_ENEMY_EVENT:
                self.__create_enemy()

            if event.type == game_sprites.HERO_SHOOT_EVENT:
                self.__game_screen.hero.shoot()

        self.__hero_control()

    def __create_enemy(self):
        self.__game_screen.add_enemy(EnemySprite("./images/enemy1.png"))

    def __hero_control(self):
        key_pressed = pygame.key.get_pressed()

        if key_pressed[pygame.K_UP]:
            self.__game_screen.hero.y_speed = -9

        if key_pressed[pygame.K_DOWN]:
            self.__game_screen.hero.y_speed = 9

        if key_pressed[pygame.K_LEFT]:
            self.__game_screen.hero.x_speed = -7

        if key_pressed[pygame.K_RIGHT]:
            self.__game_screen.hero.x_speed = 7


class JudgeSystem(object):
    """裁判系统
    用来检测敌机是否被摧毁、玩家战机是否被击毁
    """

    def __init__(self, game_screen):
        self.game_screen = game_screen

    def check_collide(self):
        pygame.sprite.groupcollide(self.game_screen.bullet_group, self.game_screen.enemy_group, True, True)
        enemies = pygame.sprite.groupcollide(self.game_screen.enemy_group, self.game_screen.hero_group, True, False)
        if len(enemies) > 0:
            self.game_screen.hero.kill()
            game_over()


def game_over():
    """结束游戏"""
    pygame.quit()
    print("玩家阵亡，游戏结束！")
    exit()
