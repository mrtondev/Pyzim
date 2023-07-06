import pygame
import random

# Configurações do jogo
largura_tela = 800
altura_tela = 400
cor_fundo = (0, 0, 0)
fps = 60

# Configurações da raquete
largura_raquete = 10
altura_raquete = 60
cor_raquete = (255, 255, 255)
velocidade_raquete = 5

# Configurações da bola
tamanho_bola = 10
cor_bola = (255, 255, 255)
velocidade_bola = 3
direcao_bola = [random.choice([-1, 1]), random.choice([-1, 1])]

# Pontuação inicial
pontuacao_esquerda = 0
pontuacao_direita = 0

# Inicialização do Pygame
pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()
fonte = pygame.font.Font(None, 36)

# Função para desenhar as raquetes
def desenhar_raquetes(x1, y1, x2, y2):
    pygame.draw.rect(tela, cor_raquete, (x1, y1, largura_raquete, altura_raquete))
    pygame.draw.rect(tela, cor_raquete, (x2, y2, largura_raquete, altura_raquete))

# Função para desenhar a bola
def desenhar_bola(x, y):
    pygame.draw.circle(tela, cor_bola, (x, y), tamanho_bola)

# Função para exibir o menu inicial
def exibir_menu():
    tela.fill(cor_fundo)
    texto_titulo = fonte.render("PONG - Escolha a velocidade da bola", True, cor_raquete)
    tela.blit(texto_titulo, (largura_tela // 2 - texto_titulo.get_width() // 2, altura_tela // 2 - 50))
    texto_opcao1 = fonte.render("1 - Lenta", True, cor_raquete)
    tela.blit(texto_opcao1, (largura_tela // 2 - texto_opcao1.get_width() // 2, altura_tela // 2))
    texto_opcao2 = fonte.render("2 - Média", True, cor_raquete)
    tela.blit(texto_opcao2, (largura_tela // 2 - texto_opcao2.get_width() // 2, altura_tela // 2 + 50))
    texto_opcao3 = fonte.render("3 - Rápida", True, cor_raquete)
    tela.blit(texto_opcao3, (largura_tela // 2 - texto_opcao3.get_width() // 2, altura_tela // 2 + 100))
    texto_opcao4 = fonte.render("4 - Muito Rápida", True, cor_raquete)
    tela.blit(texto_opcao4, (largura_tela // 2 - texto_opcao4.get_width() // 2, altura_tela // 2 + 150))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 1
                elif event.key == pygame.K_2:
                    return 2
                elif event.key == pygame.K_3:
                    return 3
                elif event.key == pygame.K_4:
                    return 4

# Função principal do jogo
def jogo_pong():
    global velocidade_bola
    global direcao_bola

    velocidade_opcao = exibir_menu()

    if velocidade_opcao == 1:
        velocidade_bola = 2
    elif velocidade_opcao == 2:
        velocidade_bola = 3
    elif velocidade_opcao == 3:
        velocidade_bola = 5
    elif velocidade_opcao == 4:
        velocidade_bola = 8

    # Posições iniciais das raquetes
    raquete_esquerda_y = altura_tela // 2 - altura_raquete // 2
    raquete_direita_y = altura_tela // 2 - altura_raquete // 2

    # Posições iniciais da bola
    bola_x = largura_tela // 2
    bola_y = altura_tela // 2

    direcao_bola = [random.choice([-1, 1]), random.choice([-1, 1])]

    pontuacao_esquerda = 0
    pontuacao_direita = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Movimentação das raquetes
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and raquete_esquerda_y > 0:
            raquete_esquerda_y -= velocidade_raquete
        if keys[pygame.K_s] and raquete_esquerda_y < altura_tela - altura_raquete:
            raquete_esquerda_y += velocidade_raquete
        if keys[pygame.K_UP] and raquete_direita_y > 0:
            raquete_direita_y -= velocidade_raquete
        if keys[pygame.K_DOWN] and raquete_direita_y < altura_tela - altura_raquete:
            raquete_direita_y += velocidade_raquete

        # Atualização da posição da bola
        bola_x += velocidade_bola * direcao_bola[0]
        bola_y += velocidade_bola * direcao_bola[1]

        # Verificação de colisões com as raquetes
        if bola_x <= largura_raquete and raquete_esquerda_y <= bola_y <= raquete_esquerda_y + altura_raquete:
            direcao_bola[0] = 1
        if bola_x >= largura_tela - largura_raquete - tamanho_bola and raquete_direita_y <= bola_y <= raquete_direita_y + altura_raquete:
            direcao_bola[0] = -1
        if bola_y <= 0 or bola_y >= altura_tela - tamanho_bola:
            direcao_bola[1] = -direcao_bola[1]

        # Verificação de colisões com as paredes laterais
        if bola_x <= 0:
            pontuacao_direita += 1
            bola_x = largura_tela // 2
            bola_y = altura_tela // 2
            direcao_bola = [random.choice([-1, 1]), random.choice([-1, 1])]
        if bola_x >= largura_tela - tamanho_bola:
            pontuacao_esquerda += 1
            bola_x = largura_tela // 2
            bola_y = altura_tela // 2

        # Desenho na tela
        tela.fill(cor_fundo)
        desenhar_raquetes(0, raquete_esquerda_y, largura_tela - largura_raquete, raquete_direita_y)
        desenhar_bola(bola_x, bola_y)

        # Exibição da pontuação
        texto_pontuacao = fonte.render(str(pontuacao_esquerda) + " : " + str(pontuacao_direita), True, cor_raquete)
        tela.blit(texto_pontuacao, (largura_tela // 2 - texto_pontuacao.get_width() // 2, 10))

        pygame.display.update()
        clock.tick(fps)


# Inicialização do jogo
jogo_pong()
