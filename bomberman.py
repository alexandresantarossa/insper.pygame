# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Bomberman')

# ----- Inicia assets
BONECO1_W = 50
BONECO1_H = 38

boneco1 = pygame.image.load('assets/hulk.png').convert_alpha()
boneco1 = pygame.transform.scale(boneco1, (BONECO1_W, BONECO1_H))

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((100, 255, 100))  # Preenche com a cor branca
    window.blit(boneco1, (10,10))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

