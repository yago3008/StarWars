import pygame, random
from entities import Player, Enemy, Buff, draw_pixel_art, color, heart_pattern

pygame.init()

# Configurações de tela
display_W = 800
display_H = 600
display = pygame.display.set_mode((display_W, display_H))
pygame.display.set_caption('Shoot Game')
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 22)

# Variáveis globais
playing = True
shooting = False
ammo = []
score = 0
player = Player(375, 570, 30)
enemy = Enemy()
buff = Buff(0,'', 0 , 0)




def draw_hearts(times):
    for i in range(times):
        draw_pixel_art(heart_pattern, 800 * i - (770 * i), 5, 3, display)

def shoot():
    global ammo
    for bullet in ammo:
        bullet[1] -= 10
        pygame.draw.circle(display, color('white'), (bullet[0] + 14, bullet[1]), 3)
        if bullet[1] < 0:
            ammo.remove(bullet)

def cleanScreen():
    display.fill(color('black'))

def updateScreen():
    pygame.display.update()

def buff_exists(x, y):
    n = random.randint(0, 20)
    heart_pattern = [
    " 011011 ",
    "01211111",
    "01111111",
    " 011111 ",
    "  0111  ",
    "   01   "
]
    if  n < 100:
        #if n <= 10:
        #    buff.draw('speed_pattern', display)
        if n > 0 and n <= 20:
            buff.x = x
            buff.y = y
            print(f'x = {x}, y = {y}')
            #buff.draw('heart_pattern', display)
            draw_pixel_art(heart_pattern, x + 20, y + 20, 4, display)




def checkEnemyCollision(bullet, enemy_pos):
    bullet_rect = pygame.Rect(bullet[0] - 22, bullet[1] - 20, 5, 5)
    hitbox_size = 45 
    enemy_rect = pygame.Rect(enemy_pos[0] - hitbox_size // 2, enemy_pos[1] - hitbox_size // 2, hitbox_size, hitbox_size)
    return bullet_rect.colliderect(enemy_rect)

def message(msg, color, x, y):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x, y])

def lose():
    global playing
    if player.life <= 0:
        playing = False

def game():
    global playing, ammo, score
    
    while playing:
        cleanScreen()
        lose()
        draw_hearts(player.life)
        message(f"Score: {score}", color('white'), 685, 3)
        player.draw(display)
        shoot()
        
        enemy.draw(display)
        enemy.move()
        enemy.outOfScreen(player)
        updateScreen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playing = False
                if event.key == pygame.K_SPACE:
                    ammo.append([player.x + player.size // 2 - 2, player.y])
        for bullet in ammo:
            if checkEnemyCollision(bullet, (enemy.x, enemy.y)):      
                score += 1
                ammo.remove(bullet)
                buff_exists(enemy.x, enemy.y)
                #enemy.reset_position()
                updateScreen()
                
                
        buff.move()
        player.update_buffs()
        player.move()
        clock.tick(60)

game()
pygame.quit()
quit()