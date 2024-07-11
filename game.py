import pygame, random, time as t
from entities import Player, Enemy, Buff, Boss, draw_pixel_art, color, heart_pattern, speed_pattern

pygame.init()

# Configurações de tela
display_W = 800
display_H = 600
display = pygame.display.set_mode((display_W, display_H))
pygame.display.set_caption('StarWars Game')
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 22)

# Variáveis globais

shooting = False
ammo = []
score = 0
player = Player()
enemies = [Enemy(score)]
buffs = []
boss_fight = False
boss = Boss()

def draw_hearts(times, display):
    for i in range(times):
        draw_pixel_art(heart_pattern, 800 * i - (770 * i), 5, 3, display)

def shoot(ammo, display):
    for bullet in ammo:
        bullet[1] -= 10
        pygame.draw.circle(display, color('white'), (bullet[0] + 14, bullet[1]), 3)
        if bullet[1] < 0:
            ammo.remove(bullet)

def cleanScreen(display):
    display.fill(color('black'))

def updateScreen():
    pygame.display.update()

def create_buff(x, y):
    n = random.randint(0, 20)
    if n <= 10:
        return Buff(1, "heal", x, y, heart_pattern)
    if n > 10:
        return Buff(90, "speed", x, y, speed_pattern)
    return None

def checkEnemyCollision(bullet, enemy_pos):
    bullet_rect = pygame.Rect(bullet[0] - 22, bullet[1] - 20, 5, 5)
    hitbox_size = 45
    enemy_rect = pygame.Rect(enemy_pos[0] - hitbox_size // 2, enemy_pos[1] - hitbox_size // 2, hitbox_size, hitbox_size)
    return bullet_rect.colliderect(enemy_rect) 

def message(msg, color, x, y, display, font_style):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x, y])

def lose(player):
    return player.life <= 0

def spawn_enemies():
        if len(enemies) < score // 50 + 1:
            enemies.append(Enemy(score))

def spawn_enemy():
    global score 
    for enemy in enemies:
        enemy.draw(display)
        enemy.move()
        enemy.outOfScreen(player)
        for bullet in ammo:
            for enemy in enemies:
                if checkEnemyCollision(bullet, (enemy.x, enemy.y)):
                    score += 50
                    ammo.remove(bullet)
                    buff = create_buff(enemy.x, enemy.y)
                    if buff:
                        buffs.append(buff)
                    boss_round()
                    enemy.reset_position()
                    enemy.update_speed(score)

def boss_round():
    global boss_fight

    if len(enemies) < score // 50 + 1:
        boss_fight = True

def spawn_boss():
    boss.draw(display)

def apply_buffs():
    for buff in buffs:
        buff.draw(display, 3)
        buff.move()
        if buff.check_collision(player):
            player.apply_buff(buff)
            buffs.remove(buff)

def game():  
    global boss_fight
    alive = True

    while alive:
        cleanScreen(display)

        if lose(player):
            alive = False
            #chamar tela final

        draw_hearts(player.life, display)
        message(f"Score: {score}", color('white'), 685, 3, display, font_style)
        player.draw(display)
        shoot(ammo, display)

        apply_buffs()
  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    alive = False
                if event.key == pygame.K_SPACE:
                    ammo.append([player.x + player.size // 2 - 2, player.y])
        
        if not boss_fight:
            spawn_enemy()
        else:
            spawn_boss()
        
        
        updateScreen()
        player.update_buffs()
        player.move()
        spawn_enemies()
        clock.tick(60)
    pygame.quit()
    quit()
game()