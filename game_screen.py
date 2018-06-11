# -*- coding: UTF-8 -*-
import game_sprites
import pygame
import plane_war

BACKGROUND_RES_PATH = "./images/background.png"


class GameScreen(object):
    def __init__(self):
        self.game_screen = pygame.display.set_mode(plane_war.SCREEN_SIZE.size)
        background_1 = game_sprites.BackgroundSprite(BACKGROUND_RES_PATH, 3)
        background_2 = game_sprites.BackgroundSprite(BACKGROUND_RES_PATH, 3)
        background_1.rect.y = 0
        background_2.rect.y = -background_2.rect.height
        self.hero = game_sprites.HeroSprite(self)
        # 游戏背景精灵组
        self.background_group = pygame.sprite.Group((background_1, background_2))
        # 敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 英雄战机精灵组
        self.hero_group = pygame.sprite.Group(self.hero)
        # 子弹精灵组
        self.bullet_group = pygame.sprite.Group()

    def update_sprites(self):
        """更新游戏精灵"""
        self.background_group.update()
        self.background_group.draw(self.game_screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.game_screen)

        self.hero_group.update()
        self.hero_group.draw(self.game_screen)

        self.bullet_group.update()
        self.bullet_group.draw(self.game_screen)

    def add_enemy(self, enemy_sprite):
        """添加敌机"""
        self.enemy_group.add(enemy_sprite)
