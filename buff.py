from util import draw_pixel_art, display_H
import pygame

class Buff:
    def __init__(self, duration, effect, x, y, pattern):
        self.duration = duration
        self.effect = effect
        self.active = True
        self.x = x
        self.y = y
        self.speed = 3
        self.pattern = pattern

    def draw(self, display, ps):
        draw_pixel_art(self.pattern, self.x, self.y, ps, display)

    def move(self):
        self.y += self.speed
        if self.y > display_H:
            pass
    
    def apply(self, player):
        if self.effect == "speed":
            player.speed += 10
        elif self.effect == "heal":
            if player.life < player.max_life:
                player.life += 1
        elif self.effect == "invulnerability":
            player.invulnerable = True
        elif self.effect == "double shoot":
            player.doubleshoot = True

    def remove(self, player):
        if self.effect == "speed":
            player.speed -= 10
        elif self.effect == "heal":
            pass
        elif self.effect == "invulnerability":
            player.invulnerable = False

    def update(self, player):
        self.move()
        if self.duration > 0:
            self.duration -= 1
        else:
            if self.active:
                self.remove(player)
                self.active = False
            return False
        return True

    def check_collision(self, player):
        buff_rect = pygame.Rect(self.x, self.y, 24, 24)
        player_rect = pygame.Rect(player.x, player.y, player.size, player.size)
        return buff_rect.colliderect(player_rect)