import pygame
import random
from sys import exit

pygame.init()

# Configurações iniciais
ALTURA = 400
LARGURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Snake Game")

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

# Configurações de tempo
clock = pygame.time.Clock()
FPS = 15

# Configurações da cobra
TAMANHO_BLOCO = 20
COBRA_VELOCIDADE = TAMANHO_BLOCO
cobra_pos = [LARGURA // 2, ALTURA // 2]
cobra_direcao = (0, 0)

# Configuração da comida
comida_pos = (random.randint(0, 580), random.randint(0, 380))

# Loop do jogo
while True:
    for evento in pygame.event.get():
        ...




pygame.quit()