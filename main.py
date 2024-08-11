import pygame
from pygame.locals import * # type: ignore
from sys import exit
import random

import pygame.locals

FPS = 10

pygame.init()

morreu = False

largura = 640
altura = 480

x_cobra = largura // 2
y_cobra = altura // 2
comprimento_cobra = 5
lista_cobra = []

x_controle = 20
y_controle = 0

x_comida = random.choice(range(0, 620, 20))
y_comida = random.choice(range(0, 460, 20))

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Snake Game")

relogio = pygame.time.Clock()

fonte = pygame.font.SysFont('arial', 32, True, False)
pontos = 0

efeito_sonoro_colisao = pygame.mixer.Sound('smw_coin.wav')

def aumenta_cobra(lista_cobra):
    for coordenadas in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (coordenadas[0], coordenadas[1], 20, 20))

def reset_game():
    global comprimento_cobra, pontos, x_cobra, y_cobra, lista_cobra, lista_cabeca, y_comida, x_comida, morreu
    comprimento_cobra = 5
    pontos = 0
    x_cobra = largura // 2
    y_cobra = altura // 2
    lista_cabeca = []
    lista_cobra = []
    x_comida = random.choice(range(0, 620, 20))
    y_comida = random.choice(range(0, 460, 20))
    morreu = False


while True:
    relogio.tick(FPS)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == 20:
                    pass
                else:
                    x_controle = -20
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -20:
                    pass
                else:
                    x_controle = 20
                    y_controle = 0
            if event.key == K_w:
                if y_controle == 20:
                    pass
                else:
                    x_controle = 0
                    y_controle = -20
            if event.key == K_s:
                if y_controle == -20:
                    pass
                else:
                    x_controle = 0
                    y_controle = 20

    x_cobra += x_controle
    y_cobra += y_controle
                
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    comida = pygame.draw.rect(tela, (255, 0, 0), (x_comida, y_comida, 20, 20))

    if cobra.colliderect(comida):
        x_comida = random.choice(range(0, 621, 20))
        y_comida = random.choice(range(0, 461, 20))
        pontos += 1
        comprimento_cobra += 1
        efeito_sonoro_colisao.play()


    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        font_morreu = pygame.font.SysFont('arial', 20, True, False)
        mensagem = 'Game Over! Pressione R para reiniciar'
        texto_formatado = font_morreu.render(mensagem, True, (255, 255, 255))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reset_game()

            ret_texto.center = (largura // 2, altura // 2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()
        
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura

    if len(lista_cobra) > comprimento_cobra:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (470, 25))

    pygame.display.update()
