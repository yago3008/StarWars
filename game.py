import pygame, time as t
from entities import Player, Boss, Game, draw_pixel_art, color, heart_pattern, speed_pattern

pygame.init()

# Configurações de tela
display_W = 800
display_H = 600
display = pygame.display.set_mode((display_W, display_H))
pygame.display.set_caption('StarWars Game')
clock = pygame.time.Clock()
font_style = pygame.font.SysFont("bahnschrift", 22)

# Variáveis globais
player = Player()
game = Game(player.score)
boss = Boss()

def draw_hearts(times, display):
    for i in range(times):
        draw_pixel_art(heart_pattern, 800 * i - (770 * i), 5, 3, display)

def cleanScreen(display):
    display.fill(color('black'))

def updateScreen():
    pygame.display.update()

def message(msg, color, x, y, display, font_style):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [x, y])

def lose(player):
    return player.life <= 0

def main():  
    alive = True

    while alive:
        cleanScreen(display)

        if lose(player):
            alive = False
            #chamar tela final

        draw_hearts(player.life, display)
        message(f"Score: {player.score}", color('white'), 685, 3, display, font_style)
        player.draw(display)
        player.shoot(display)
        game.apply_buffs(player, display)
  
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                alive = False
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_ESCAPE:
                    alive = False
                if event.key == pygame.K_SPACE:
                    player.ammo.append([player.x + player.size // 2 - 2, player.y])
        
        if not game.boss_fight:
            game.spawn_enemy(player, boss, display)
        else:
            game.spawn_boss(boss, player, display)
        
        
        updateScreen()
        player.update_buffs()
        player.move()
        game.spawn_enemies(player)
        clock.tick(60)
    pygame.quit()
    quit()
main()