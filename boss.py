from util import draw_pixel_art, display_W, display_H
from pattern import boss_pattern, exclamation_pattern, laser_patternPT1, laser_patternPT2, angry_pattern, bullet_pattern, bullet_pattern1
from pattern import bossLifeStart_pattern, bossLifeMid_pattern, bossLifeEnd_pattern, bossEmptyLifeStart_pattern, bossEmptyLifeMid_pattern, bossEmptyLifeEnd_pattern
import pygame, random

class Boss:
    def __init__(self):
        self.x = 250
        self.y = 50
        self.life = 10
        self.maxLife = 10
        self.width = 12
        self.speed = 2
        self.ammo = []
        self.delay = 0
        self.bullet_speed = 0
        self.shooting = False
        self.minigun = False
        self.cannon = False
        self.laser = True
        self.stop = False
        self.change_direction = False
        self.shaking = True
        self.shake_duration = 0
        self.shake_intensity = 0
        self.original_y = self.y
        self.shake_direction = 1

    def draw(self, display):
        draw_pixel_art(boss_pattern, self.x, self.y, self.width, display)

    
    def draw_bossLife(self, display):
        x = 240
        y = 5
        width = 7
        positionTail = x + ((x // 6) * 8)

        if (self.life / self.maxLife) >= 0.1:
            draw_pixel_art(bossLifeStart_pattern, x - 40, y, width, display)
        else:
            draw_pixel_art(bossEmptyLifeStart_pattern, x - 40, y, width, display)

        for i in range(int(self.maxLife * 0.8)):
            if self.life > (i + 1) * (self.maxLife * 0.1):
                draw_pixel_art(bossLifeMid_pattern, x + ((x // 6) * i), y, width, display)
            else:
                draw_pixel_art(bossEmptyLifeMid_pattern, x + ((x // 6) * i), y, width, display)

                
        if self.life > (int(self.maxLife * 0.1) * 9):
            draw_pixel_art(bossLifeEnd_pattern, positionTail, y, width, display)
        else:
            draw_pixel_art(bossEmptyLifeEnd_pattern, positionTail, y, width, display)

    def move(self):
        if not self.stop:
            if self.x < display_W - 338 and not self.change_direction:
                self.x += self.speed
                if self.x == display_W -338:
                    self.change_direction = True

            elif self.change_direction:
                self.x -= self.speed
                if self.x == 0:
                    self.change_direction = False

    def draw_shoot(self, bullet_sz, pattern, display, player):
        for bullet in self.ammo:
            bullet[1] += self.bullet_speed
            draw_pixel_art(pattern, bullet[0], bullet[1], bullet_sz, display)
            if self.check_collision(player, bullet[0], bullet[1] , bullet_sz + 10, bullet_sz+ 10):
                player.life -= 1
                self.ammo.remove(bullet)
            if bullet[1] > display_H:
                self.ammo.remove(bullet)


    def shoot(self, display, player):
        if self.laser:
            if (self.delay // 20) % 2 == 0 and self.x != 250:
                draw_pixel_art(exclamation_pattern, self.x + 240, self.y - 10, 5, display)
            self.delay += 1
            if self.x < 250:
                self.x += self.speed
            elif self.x > 250:
                self.x -= self.speed
            self.stop = True
            if self.x == 250:
                for i in range(12):
                    draw_pixel_art(laser_patternPT1, self.x + 124, (50 + 120) + (50 * i), 5, display)
                draw_pixel_art(laser_patternPT2, self.x + 124, 50 + 530, 5, display)
                draw_pixel_art(angry_pattern, self.x + 210, 50, 4, display)
                if self.delay % 300 == 0:
                    self.laser = False
                    self.shooting = True
                    self.delay = 0
                    self.stop = False

        if self.shooting:
            self.bullet_speed = 3
            self.delay += 1
            if self.delay % 30 == 0:
                self.ammo.append([self.x + self.width + random.randint(80, 200), self.y + 120])
            self.draw_shoot(4,bullet_pattern, display, player)
            if self.delay % 300 == 0:
                self.shooting = False
                self.minigun = True
                self.delay = 0
            
        if self.minigun:
            self.bullet_speed = 10
            self.delay += 1
            if self.delay % 17 == 0:
                self.ammo.append([self.x + self.width + random.randint(100, 220), self.y + 120])
            self.draw_shoot(2, bullet_pattern1, display, player)
            if self.delay % 300 == 0:
                self.minigun = False
                self.laser = True
                self.delay = 0

    def check_collision(self, player, x, y , sz1, sz2):
        bullet_rect = pygame.Rect(x, y, sz1, sz2)
        player_rect = pygame.Rect(player.x, player.y, player.size, player.size)
        return bullet_rect.colliderect(player_rect)
    