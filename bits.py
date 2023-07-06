import pygame
from pygame.locals import *

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura_janela = 800
altura_janela = 600
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Meu Jogo de Plataforma")

# Cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)

# Loop principal do jogo
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            executando = False

    # Limpeza da tela
    janela.fill(PRETO)

    # Desenhe a primeira fase em estilo 8 bits
    # Aqui você pode desenhar seus sprites, blocos, personagens, etc.

    # Atualize a tela
    pygame.display.flip()

# Encerramento do Pygame
pygame.quit()
