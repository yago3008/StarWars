from enemy import Enemy
from buff import Buff
import random, pygame
from pattern import heart_pattern, speed_pattern

class Game:
    def __init__(self, score):
        self.enemies = [Enemy(score)]
        self.buffs = []
        self.boss_fight = False
        self.playing = True

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
    
    def checkBossCollision(self, bullet, boss_pos):
        bullet_rect = pygame.Rect(bullet[0] - 22, bullet[1] - 20, 5, 5)
        hitbox_sizeY = 200
        hitbox_sizeX = 280
        enemy_rect = pygame.Rect(boss_pos[0] - (hitbox_sizeX // 2) + 110 , boss_pos[1] - hitbox_sizeY // 2, hitbox_sizeX + (hitbox_sizeX // 4) - 25, hitbox_sizeY)
        return bullet_rect.colliderect(enemy_rect)

    def spawn_enemy(self, player, display):
        for enemy in self.enemies:
            enemy.draw(display)
            enemy.move()
            enemy.outOfScreen(player)
            for bullet in player.ammo:
                for enemy in self.enemies:
                    if self.checkEnemyCollision(bullet, (enemy.x, enemy.y)):
                        player.score += 7
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
        boss.draw_bossLife(display)
        boss.shoot(display, player)
        if not boss.stop:
            boss.move()
        self.boss_alive(player, boss)

    def apply_buffs(self, player, display):
        for buff in self.buffs:
            buff.draw(display, 3)
            buff.move()
            if buff.check_collision(player):
                player.apply_buff(buff)
                self.buffs.remove(buff)

    def boss_alive(self, player, boss):
        for bullet in player.ammo:
            if self.boss_fight:
                if self.checkBossCollision(bullet, (boss.x, boss.y)):
                    player.ammo.remove(bullet)
                    boss.life -= 1
                    print(boss.life)
    
    def gameover(self, player, boss):
        if player.life <= 0 or boss.life <= 0:
            self.playing = False
            print("Game Over!")
    