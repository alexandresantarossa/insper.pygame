# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 600
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bombinha')

# ----- Inicia assets

BONECO_WIDTH = 45
BONECO_HEIGHT = 40
font = pygame.font.SysFont(None, 48)
boneco_img = pygame.image.load('assets/hulk.png').convert_alpha()
boneco_img = pygame.transform.scale(boneco_img, (BONECO_WIDTH, BONECO_HEIGHT))

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Player1(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 0
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        # Atualização da posição da nave
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de meteoros
all_sprites = pygame.sprite.Group()
# Criando o jogador
player1 = Player1(boneco_img)
all_sprites.add(player1)


# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:    
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player1.speedx -= 3
            if event.key == pygame.K_RIGHT:
                player1.speedx += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player1.speedx = 0
            if event.key == pygame.K_RIGHT:
                player1.speedx = 0            
    
            


    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    all_sprites.update()

    # ----- Gera saídas
    window.fill((0, 255, 100))  # Preenche com a cor branca
    # Desenhando meteoros
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

