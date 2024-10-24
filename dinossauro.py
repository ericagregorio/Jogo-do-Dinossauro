import pygame
from pygame.locals import QUIT, K_LEFT, K_RIGHT, K_SPACE

# Inicializa o pygame
pygame.init()

# Dimensões da tela
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo Estilo Dinossauro Chrome")

# Definindo cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # Cor para obstáculos

# Variáveis do jogador
player_size = (40, 60)
player_pos = [100, HEIGHT - player_size[1]]
player_vel = 0
is_jumping = False
gravity = 1

# Plataforma
ground_height = 30
platform = pygame.Rect(0, HEIGHT - ground_height, WIDTH, ground_height)

# Obstáculos
obstacle_width = 50
obstacle_height = 50
obstacle_pos = [WIDTH, HEIGHT - ground_height - obstacle_height]  # Posição inicial do obstáculo
obstacle_speed = 5  # Velocidade do obstáculo

# Taxa de FPS
clock = pygame.time.Clock()

# Loop principal do jogo
running = True
while running:
    clock.tick(60)  # 60 FPS
    screen.fill(WHITE)

    # Eventos
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Movimentação do jogador
    keys = pygame.key.get_pressed()

    if keys[K_LEFT]:
        player_pos[0] -= 5
    if keys[K_RIGHT]:
        player_pos[0] += 5
    if not is_jumping and keys[K_SPACE]:
        is_jumping = True
        player_vel = -15

    # Aplicar gravidade
    if is_jumping:
        player_pos[1] += player_vel
        player_vel += gravity
        if player_pos[1] >= HEIGHT - player_size[1] - ground_height:
            player_pos[1] = HEIGHT - player_size[1] - ground_height
            is_jumping = False
            player_vel = 0

    # Movimentação do obstáculo
    obstacle_pos[0] -= obstacle_speed  # Move o obstáculo para a esquerda
    if obstacle_pos[0] < -obstacle_width:  # Se o obstáculo sair da tela
        obstacle_pos[0] = WIDTH  # Reseta a posição do obstáculo

    # Desenhar chão
    pygame.draw.rect(screen, BLACK, platform)

    # Desenhar jogador (um retângulo simples)
    pygame.draw.rect(screen, BLACK, (*player_pos, *player_size))

    # Desenhar obstáculo
    pygame.draw.rect(screen, RED, (*obstacle_pos, obstacle_width, obstacle_height))

    # Verificação de colisão (simples)
    player_rect = pygame.Rect(*player_pos, *player_size)
    obstacle_rect = pygame.Rect(*obstacle_pos, obstacle_width, obstacle_height)

    if player_rect.colliderect(obstacle_rect):
        print("Colidiu com o obstáculo!")  # Apenas uma mensagem por enquanto

    # Atualiza a tela
    pygame.display.flip()

# Fecha o pygame
pygame.quit()
