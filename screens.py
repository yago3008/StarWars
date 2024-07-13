import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Menu Principal')

# Carregar os sons com volumes ajustados
change_song = pygame.mixer.Sound('StarWars/songs/barulhoClick2.wav')
change_song.set_volume(0.2)  # Ajuste o volume conforme necessário
click_song = pygame.mixer.Sound('StarWars/songs/barulhoClick1.wav')
click_song.set_volume(0.5)  # Ajuste o volume conforme necessário

# Função para iniciar o jogo com som
def start_game():
    click_song.play()  # Toca o som
    print("Iniciando o jogo!")

# Função para ir para a loja com som
def go_to_shop():
    click_song.play()  # Toca o som
    print("Indo para a loja!")

# Função para desenhar o fundo do menu
def draw_background():
    surface.fill((0, 0, 0))  # Preenche o fundo com preto

# Criando um tema personalizado
custom_theme = pygame_menu.themes.THEME_DARK.copy()
custom_theme.widget_font = pygame_menu.font.FONT_FRANCHISE
custom_theme.title_font = pygame_menu.font.FONT_FRANCHISE
custom_theme.widget_font_color = (255, 255, 255)
custom_theme.selection_color = (0, 255, 0)  # Cor de seleção
custom_theme.widget_font_size = 40  # Aumenta o tamanho da fonte dos botões
custom_theme.widget_margin = (0, 50)  # Ajusta a margem vertical dos botões (aumentado para 50 pixels)
custom_theme.widget_border_width = 6  # Aumenta a largura da borda dos botões
custom_theme.widget_border_color = (255, 255, 255)  # Cor da borda dos botões
custom_theme.widget_selection_effect = pygame_menu.widgets.HighlightSelection()  # Efeito de seleção
custom_theme.background_color = None  # Define que não terá uma cor de fundo sólida

# Definindo a imagem de fundo
background_image = pygame_menu.baseimage.BaseImage(
    image_path='StarWars/images/background3.jpg',  # Substitua pelo caminho da sua imagem .jfif
    drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL,
)

custom_theme.background_color = background_image

# Criando o menu
menu = pygame_menu.Menu(
    title='Menu Principal',
    width=800,
    height=600,
    theme=custom_theme
)

# Adicionando os botões ao menu com funções associadas
menu.add.button('Ir para o Jogo', start_game)
menu.add.button('Ir para a Loja', go_to_shop)
menu.add.button('Sair', pygame_menu.events.EXIT)

# Função para reproduzir o som de clique ao pressionar teclas
def play_click_sound(event):
    if event.type == pygame.KEYDOWN:
        if event.key in [pygame.K_UP, pygame.K_DOWN]:
            change_song.play()  # Reproduz o som apenas uma vez por evento de tecla

# Loop principal do menu
while True:
    # Desenhar o fundo
    draw_background()
    
    # Gerenciar eventos do pygame
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    # Verificar e reproduzir o som de clique conforme eventos de tecla
    play_click_sound(event)

    # Atualizar o menu com os eventos capturados
    menu.update(events)

    # Desenhar o menu
    menu.draw(surface)
    
    # Atualizar a tela
    pygame.display.flip()
