import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Menu Intergaláctico')

# Função para iniciar o jogo
def start_game():
    print("Iniciando o jogo!")

# Função para ir para a loja
def go_to_shop():
    print("Indo para a loja!")

# Função para desenhar o fundo do menu
def draw_background():
    surface.fill((0, 0, 0))  # Preenche o fundo com preto

# Criando o menu
menu = pygame_menu.Menu(400, 600, 'Menu Intergaláctico', theme=pygame_menu.themes.THEME_DARK)

# Adicionando os botões ao menu
menu.add.button('Ir para o Jogo', start_game)
menu.add.button('Ir para a Loja', go_to_shop)

# Rodando o menu principal
menu.mainloop(surface, bgfun=draw_background)
