import random
from util import draw_pixel_art, display_H, display_W
from pattern import enemy_pattern

class Enemy:
    def __init__(self, score):
        self.x = random.randint(50, display_W - 100)
        self.y = random.randint(-150, -50)
        self.width = 15
        self.passed = False
        self.update_speed(score)

    def update_speed(self, score):
        self.speed = 2 + (score / 20)

    def move(self):
        self.y += self.speed
        if self.y > display_H:
            self.reset_position()

    def draw(self, display):
        draw_pixel_art(enemy_pattern, self.x, self.y, 4, display)

    def outOfScreen(self, player):
        if self.y > 599 - self.width and not self.passed:
            player.life -= 1
            self.passed = True

    def reset_position(self):
        self.y = random.randint(-150, -50)
        self.x = random.randint(50, display_W - 50)
        self.passed = False