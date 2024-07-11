import pygame
import random

display_W = 800
display_H = 600


enemy_pattern = [
    "  7 1  1 7  ",
    "   11  11   ",
    " 1 161161 1 ",
    " 1 121121 1 ",
    " 1111111111 ",
    "   117711   ",
    "   11  11   ",
    "  1      1  "
]

player_pattern = [
       "      45      ",
       "     4235     ",
       "     4335     ",
       " 5   4335   5 ",
       "445  4445  445",
       "445  4445  445",
       "44444444444445 ",
]

speed_pattern = [
    "        8 ",
    "       89 ",
    "      89  ",
    "     889  ",
    "    889   ",
    "   8889   ",
    "  8889    ",
    "  888889  ",
    "    8889  ",
    "    889   ",
    "   889    ",
    "   89     ",
    "  89      ",
    " 8        "
]

heart_pattern = [
    " 011011 ",
    "01211111",
    "01111111",
    " 011111 ",
    "  0111  ",
    "   01   "
]

buff_pattern = [
    "111111",
    "111111",
    "111111",
    "111111",
    "111111",
    "111111",
]

boss_pattern = [
    "            3333            "
    "           333333           ",
    "         3233333333         ",
    "        322333333333        ",
    "   4443333333333333333444   ",
    "4444454555333333335554544444",
    "4444444444555555554444444444",
    "4444444544444444444454444444",
    "  444444444445444444444444  ",
    "    44444444444444444444    ",
    "         4444444444         "
]
background_pattern = [
    "000111000",
    "001222100",
    "012333210",
    "123444321",
    "123444321",
    "012333210",
    "001222100",
    "000111000"
]

def color(op):
    colors = {
        'white': (255, 255, 255),
        'yellow': (255, 255, 102),
        'dyellow': (214, 153, 0),
        'black': (0, 0, 0),
        'red': (255, 50, 50),
        'dred': (198, 0, 0),
        'blue': (173, 216, 230),
        'gray': (128, 128, 128),
        'dgray': (108, 108, 108)
    }
    return colors.get(op)

def draw_pixel_art(pattern, x, y, ps, display):
    for row_index, row in enumerate(pattern):
        for col_index, pixel in enumerate(row):
            if pixel == '1':
                pygame.draw.rect(display, color('red'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '2':
                pygame.draw.rect(display, color('white'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '3':
                pygame.draw.rect(display, color('blue'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '4':
                pygame.draw.rect(display, color('gray'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '5':
                pygame.draw.rect(display, color('dgray'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '6':
                pygame.draw.rect(display, color('black'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '7':
                pygame.draw.rect(display, color('dred'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '8':
                pygame.draw.rect(display, color('yellow'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '9':
                pygame.draw.rect(display, color('dyellow'), (x + col_index * ps, y + row_index * ps, ps, ps))


class Player:
    def __init__(self):
        self.x = 375
        self.y = 570
        self.size = 30
        self.pattern = player_pattern
        self.speed = 6
        self.buffs = []
        self.life = 3
        self.invulnerable = False
        self.doubleShoot = False

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



class Boss:
    def __init__(self):
        self.x = 250
        self.y = 30 
        self.life = 200
        self.width = 15
        self.speed = 2

    def move(self):
        self.y += self.speed
        if self.y > display_H:
            pass

    def draw(self, display):
        draw_pixel_art(boss_pattern, self.x, self.y, self.width, display)
        

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
            if player.life < 5:
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
