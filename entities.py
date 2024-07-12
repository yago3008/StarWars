import pygame, random, time

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

test_pattern = [
    "111111",
    "111111",
    "111111",
    "111111",
    "111111",
    "111111",
]

boss_pattern = [

    "           3366cc           ",
    "        32266ccdddee        ",
    "       32366ccdddeeee       ",
    "   54433366ccdddeeeeee445   ",
    "baa54444446ccddeee4444445aab",
    "bbbff555554444444455555ffbbb",
    "bbbbaa5555555555555555aabbbb",
    "  bbbbaff5555555555ffabbbb  ",
    "    bbbbaaaaaffaaaaabbbb    ",
    "         bbbbbbbbbb         "
]

laser_patternPT1 = [
 "    eedd22ddee    ",
 "    eedd22ddee    ",
 "    eedd22ddee    ",
 "    eedd22ddee    ",
 "    eedd22ddee    ",
 "    eedd22ddee    ",
 "    eedd22ddee    ",
 "    eedd22ddee    ",
 "    eedd22ddee    ",
 "    eedd22ddee    ",
]

laser_patternPT2 = [
 "   eedd2222ddee   ",
 "e  eedd2222ddee  e",
 "eeeddd222222dddeee",
 "eeeddd222222dddeee",
]

bullet_pattern = [
    "      e      ",
    "     ede     ",
    "     ede     ",
    "    eddde    ",
    "    ed2de    ",
    "   edd2dde   ",
    "   ed222de   ",
    "  edd222dde  ",
    "  edd222dde  ",
    "eedd22222ddee",
    "eedd22222ddee",
    " edd22222dde ",
    "  edd222dde  ",
    "  eddd2ddde  ",
    "   edd2dde   ",
    "    eddde    ",
    "     eee"

]

bullet_pattern1 = [
    "      1      ",
    "     1g1     ",
    "     1g1     ",
    "    1ggg1    ",
    "    1g8g1    ",
    "   1gg8gg1   ",
    "   1g888g1   ",
    "  1gg888gg1  ",
    "  1gg888gg1  ",
    "11gg88888gg11",
    "11gg88888gg11",
    " 1gg88888gg1 ",
    "  1gg888gg1  ",
    "  1ggg8ggg1  ",
    "   1gg8gg1   ",
    "    1ggg1    ",
    "     111"

]

angry_pattern = [
"  000         000        ",
" 01110       01110       ",
"   011110   0110         ",
"     01110  01110        ",
"     01110  0 01110      ",
"    01110  010  01110    ",
"  011110  01110   011110 ",
"01110   011100110    0110",
" 000  01110   01110   00 ",
"    01110        0110    ",
"     000          00     ",
]

exclamation_pattern = [
"  000000    ",
" 01111110   ",
" 01111110   ",
" 01111110   ",
" 01111110   ",
"  01111110  ",
"   01111110 ",
"   01111110 ",
"     0000   ",
"    011110  ",
"   01111110 ",
"    011110  ",
"     0000   "
]
def color(op):
    colors = {
        'white': (235, 235, 235),
        'yellow': (255, 255, 102),
        'dyellow': (214, 153, 0),
        'black': (0, 0, 0),
        'red': (255, 50, 50),
        'lred': (255, 107, 25),
        'dred': (198, 0, 0),
        'blue': (133, 209, 255),
        'dblue': (134, 199, 255),
        'dblue1': (135, 189, 255),
        'dblue2': (136, 179, 255),
        'dblue3': (134, 169, 255),
        'gray': (128, 128, 128),
        'dgray': (108, 108, 108),
        'dgray1': (98, 98, 98),
        'dgray2': (88, 88, 88),
        'dgray3': (87, 78, 88),
    }
    return colors.get(op)


def draw_pixel_art(pattern, x, y, ps, display):
    for row_index, row in enumerate(pattern):
        for col_index, pixel in enumerate(row):
            if pixel == '0':
                pygame.draw.rect(display, color('black'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '1':
                pygame.draw.rect(display, color('red'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '2':
                pygame.draw.rect(display, color('white'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '3':
                pygame.draw.rect(display, color('blue'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '6':
                pygame.draw.rect(display, color('dblue'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '4':
                pygame.draw.rect(display, color('gray'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '5':
                pygame.draw.rect(display, color('dgray'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '7':
                pygame.draw.rect(display, color('dred'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '8':
                pygame.draw.rect(display, color('yellow'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '9':
                pygame.draw.rect(display, color('dyellow'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'a':
                pygame.draw.rect(display, color('dgray1'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'b':
                pygame.draw.rect(display, color('dgray2'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'c':
                pygame.draw.rect(display, color('dblue1'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'd':
                pygame.draw.rect(display, color('dblue2'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'e':
                pygame.draw.rect(display, color('dblue3'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'f':
                pygame.draw.rect(display, color('dgray3'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'g':
                pygame.draw.rect(display, color('lred'), (x + col_index * ps, y + row_index * ps, ps, ps))

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
        self.width = 12
        self.speed = 2
        self.ammo = []
        self.delay = 0
        self.bullet_speed = 0
        self.shooting = True
        self.minigun = False
        self.cannon = False
        self.laser = False
        self.stop = False
        self.change_direction = False

    def draw(self, display):
        draw_pixel_art(boss_pattern, self.x, self.y, self.width, display)

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
                    draw_pixel_art(laser_patternPT1, self.x + 124, (self.y + 120) + (50 * i), 5, display)
                draw_pixel_art(laser_patternPT2, self.x + 124, self.y + 550, 5, display)
                if (self.delay // 20) % 2 == 0:
                    draw_pixel_art(angry_pattern, self.x + 210, self.y, 4, display)
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
    

class Game:
    def __init__(self, score):
        self.enemies = [Enemy(score)]
        self.buffs = []
        self.boss_fight = False

    def spawn_enemies(self, player):
        if len(self.enemies) < player.score // 50 + 1:
            self.enemies.append(Enemy(player.score))

    def create_buff(self, enemy):
        n = random.randint(0, 20)
        if n <= 10:
            return Buff(1, "heal", enemy[0], enemy[1], heart_pattern)
        if n > 10:
            return Buff(90, "speed", enemy[0], enemy[1], speed_pattern)
        return None
    
    def checkEnemyCollision(self, bullet, enemy_pos):
        bullet_rect = pygame.Rect(bullet[0] - 22, bullet[1] - 20, 5, 5)
        hitbox_size = 45
        enemy_rect = pygame.Rect(enemy_pos[0] - hitbox_size // 2, enemy_pos[1] - hitbox_size // 2, hitbox_size, hitbox_size)
        return bullet_rect.colliderect(enemy_rect)
    
    def spawn_enemy(self, player, boss, display):
        for enemy in self.enemies:
            enemy.draw(display)
            enemy.move()
            enemy.outOfScreen(player)
            for bullet in player.ammo:
                for enemy in self.enemies:
                    if self.checkEnemyCollision(bullet, (enemy.x, enemy.y)):
                        player.score += 10
                        player.ammo.remove(bullet)
                        buff = self.create_buff((enemy.x, enemy.y))
                        if buff:
                            self.buffs.append(buff)
                        self.boss_round(player)
                        enemy.reset_position()
                        enemy.update_speed(player.score)
    
    def boss_round(self, player):
        if len(self.enemies) < player.score // 50 + 1:
            self.boss_fight = True

    def spawn_boss(self, boss, player, display):
        boss.draw(display)
        boss.shoot(display, player)
        if not boss.stop:
            boss.move()
    
    def apply_buffs(self, player, display):
        for buff in self.buffs:
            buff.draw(display, 3)
            buff.move()
            if buff.check_collision(player):
                player.apply_buff(buff)
                self.buffs.remove(buff)

    