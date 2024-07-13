import pygame
from pattern import player_pattern
from util import display_W, draw_pixel_art, color


class Player:
    def __init__(self):
        self.x = 375
        self.y = 570
        self.size = 30
        self.pattern = player_pattern
        self.speed = 6
        self.buffs = []
        self.life = 5
        self.max_life = 10
        self.invulnerable = False
        self.doubleShoot = False
        self.ammo = []
        self.score = 0

    def draw(self, display):
        draw_pixel_art(self.pattern, self.x, self.y, 4, display)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < display_W - self.size + 10:
            self.x += self.speed

    def apply_buff(self, buff):
        self.buffs.append(buff)
        buff.apply(self)

    def update_buffs(self):
        for buff in self.buffs[:]:
            if not buff.update(self):
                self.buffs.remove(buff)

    def shoot(self, display):
        for bullet in self.ammo:
            bullet[1] -= 10
            pygame.draw.circle(display, color('white'), (bullet[0] + 14, bullet[1]), 3)
            if bullet[1] < 0:
                self.ammo.remove(bullet)






    

    

    