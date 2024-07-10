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

buff_pattern = [
    "111111",
    "111111",
    "111111",
    "111111",
    "111111",
    "111111"
]

heart_pattern = [
    " 011011 ",
    "01211111",
    "01111111",
    " 011111 ",
    "  0111  ",
    "   01   "
]

def color(op):
    colors = {
        'white': (255, 255, 255),
        'yellow': (255, 255, 102),
        'black': (0, 0, 0),
        'red': (255, 50, 50),
        'dred': (198, 0, 0),
        'blue': (173, 216, 230),
        'gray': (148, 128, 128),
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


class Player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.pattern = player_pattern
        self.speed = 6
        self.buffs = []
        self.life = 300
        self.invulnerable = False

    def draw(self, display):
        draw_pixel_art(self.pattern, self.x, self.y, 4, display)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < display_W - self.size:
            self.x += self.speed

    def apply_buff(self, buff):
        self.buffs.append(buff)
        buff.apply(self)

    def update_buffs(self):
        for buff in self.buffs[:]:
            if not buff.update(self):
                self.buffs.remove(buff)


class Enemy:
    def __init__(self):
        self.x = random.randint(50, display_W - 50)
        self.y = random.randint(-150, -50)
        self.speed = 1
        self.width = 15
        self.passed = False

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


class Buff:
    def __init__(self, duration, effect, x, y):
        self.duration = duration
        self.effect = effect
        self.active = True  # Para rastrear se o buff ainda está ativo
        self.x = x
        self.y = y
        self.speed = random.randint(3, 6)

    def draw(self, pattern, display):
        draw_pixel_art(pattern, self.x, self.y, 4, display)

    def move(self):
        print(f"movendo posicion {self.y}")
        self.y += self.speed
        if self.y > display_H:
            self.reset_position()

    def reset_position(self):
        self.y = random.randint(-150, -50)
        self.x = random.randint(50, display_W - 50)
        self.speed = random.randint(3, 6)

    def apply(self, player):
        if self.effect == "speed":
            player.speed += 10  # Exemplo de aplicação de buff de velocidade
        elif self.effect == "heal":
            if player.life < 5:
                player.life += 1
        elif self.effect == "invulnerability":
            player.invulnerable = True

    def remove(self, player):
        if self.effect == "speed":
            player.speed -= 10  # Ajuste aqui para remover o buff corretamente
        elif self.effect == "heal":
            pass  # Adicione lógica de remoção de buff de cura, se necessário
        elif self.effect == "invulnerability":
            player.invulnerable = False

    def update(self, player):
        self.move()  # Movimenta o buff
        if self.duration > 0:
            self.duration -= 1
        else:
            if self.active:  # Remover o buff apenas uma vez quando o tempo acabar
                self.remove(player)
                self.active = False
            return False  # Indicar que o buff não está mais ativo após removê-lo
        return True  # Indicar que o buff ainda está ativo enquanto a duração for maior que zero

    def checkBuffCollision(self, player):
        player_rect = pygame.Rect(player.x + 10, player.y, 40, 40)
        buff_rect = pygame.Rect(self.x, self.y, 25, 25)
        return buff_rect.colliderect(player_rect)
