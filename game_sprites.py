# -*- coding: UTF-8 -*-
import random
import pygame
import plane_war

HERO_SHOOT_EVENT = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, speed=0):
        super(GameSprite, self).__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self, *args):
        self.rect.y += self.speed


class BackgroundSprite(GameSprite):

    def update(self, *args):
        super(BackgroundSprite, self).update()
        if self.rect.y >= self.rect.height:
            self.rect.y = -self.rect.height


class EnemySprite(GameSprite):

    def __init__(self, image_path):
        super(EnemySprite, self).__init__(image_path, random.randint(1, 3))
        x_max_position = plane_war.SCREEN_SIZE.width - self.rect.width
        self.rect.bottom = 0
        self.rect.x = random.randint(0, x_max_position)

    def update(self, *args):
        super(EnemySprite, self).update()
        # 判断是否超出屏幕范围
        if self.rect.y >= plane_war.SCREEN_SIZE.height:
            self.kill()


class HeroSprite(pygame.sprite.Sprite):
    hero_image_flag = True
    hero_image1 = pygame.image.load("./images/hero1.png")
    hero_image2 = pygame.image.load("./images/hero2.png")

    def __init__(self, game_screen):
        super(HeroSprite, self).__init__()
        self.image = self.hero_image2
        self.rect = self.image.get_rect()
        self.x_speed = 0
        self.y_speed = 0
        self.game_screen = game_screen

        # 设置飞机出场位置
        self.rect.x = (plane_war.SCREEN_SIZE.width / 2) - (self.rect.width / 2)
        self.rect.y = plane_war.SCREEN_SIZE.height - self.rect.height - self.rect.height / 2

    def update(self, *args):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= plane_war.SCREEN_SIZE.width - self.rect.width:
            self.rect.x = plane_war.SCREEN_SIZE.width - self.rect.width

        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= plane_war.SCREEN_SIZE.height - self.rect.height:
            self.rect.y = plane_war.SCREEN_SIZE.height - self.rect.height

        self.x_speed = 0
        self.y_speed = 0

    def shoot(self):
        bullet = BulletSprite()
        bullet.rect.centerx = self.rect.centerx
        bullet.rect.y = self.rect.y - 10
        self.game_screen.bullet_group.add(bullet)


class BulletSprite(GameSprite):
    def __init__(self):
        super(BulletSprite, self).__init__("./images/bullet1.png", -10)

    def update(self, *args):
        super(BulletSprite, self).update()
        if self.rect.y <= 0:
            self.kill()
