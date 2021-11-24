# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
WIDTH = 1000
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bombinha')

# ----- Inicia assets

BONECO_WIDTH = 45
BONECO_HEIGHT = 40
BRICK_WIDTH=100
BRICK_HEIGHT=100
WOOD_WIDTH=52
WOOD_HEIGHT=52
font = pygame.font.SysFont(None, 48)
boneco_img = pygame.image.load('assets/hulk.png').convert_alpha()
boneco_img = pygame.transform.scale(boneco_img, (BONECO_WIDTH, BONECO_HEIGHT))
boneco1_img = pygame.image.load('assets/chewbaca.png').convert_alpha()
boneco1_img = pygame.transform.scale(boneco1_img, (BONECO_WIDTH, BONECO_HEIGHT))
brick_img = pygame.image.load('assets/brick.png').convert_alpha()
brick_img = pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT)) 
wood_img = pygame.image.load('assets/wood.png').convert_alpha()
wood_img = pygame.transform.scale(wood_img, (WOOD_WIDTH, WOOD_HEIGHT))


# ----- Inicia estruturas de dados
# Definindo os novos tipos
class brick(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(25,WIDTH - 25)
        self.rect.bottom = random.randint(80,HEIGHT - 25)

class wood(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(25,WIDTH-25)
        self.rect.bottom = random.randint(80,HEIGHT-25)
        




class Player1(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 40
        self.rect.bottom = HEIGHT - 25
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # Atualização da posição do boneco
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
class Player2(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.centerx = 760
        self.rect.bottom =  50
        self.speedx = 0
        self.speedy = 0

    def update(self):
        # Atualização da posição do boneco
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30
# Criando um grupo de blocos 
all_woods = pygame.sprite.Group()
all_bricks = pygame.sprite.Group()
# Criando os blocos
for i in range(8):

    pedra = brick(brick_img)
    all_bricks.add(pedra)

    madeiras=wood(wood_img)
    all_woods.add(madeiras)

# Criando um grupo de sprites
all_sprites = pygame.sprite.Group()
# Criando o jogador

player1 = Player1(boneco_img)
player2 = Player2(boneco1_img)
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(all_bricks)
all_sprites.add(all_woods)

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
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:    
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_UP:
                player1.speedy -= 3
            if event.key == pygame.K_DOWN:
                player1.speedy += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player1.speedy = 0
            if event.key == pygame.K_DOWN:
                player1.speedy = 0      
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:    
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_a:
                player2.speedx -= 3
            if event.key == pygame.K_d:
                player2.speedx += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                player2.speedx = 0
            if event.key == pygame.K_d:
                player2.speedx = 0            
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:    
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_w:
                player2.speedy -= 3
            if event.key == pygame.K_s:
                player2.speedy += 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player2.speedy = 0
            if event.key == pygame.K_s:
                player2.speedy = 0                  


    # ----- Atualiza estado do jogo
    # Atualizando a posição das sprites
    all_sprites.update()

    # verifica colisões entre os blocos, se o bloco de madeira ou pedra encostar em outro ele adiciona em outro lugar 
    colisao_p_m = pygame.sprite.groupcollide(all_bricks, all_woods, True, True)
    
    for p in colisao_p_m:
        p = brick(brick_img)
        all_sprites.add(p)
        all_bricks.add(p)
    
    for m in colisao_p_m:
        m = wood(wood_img)
        all_sprites.add(m)
        all_woods.add(m)

    # colisao_m_m =  pygame.sprite.groupcollide(all_woods, all_woods, True, False)
    
    # for i in colisao_m_m:
    #     i = wood(wood_img)
    #     all_sprites.add(i)
    #     all_woods.add(i)

    # colisao_p_p =  pygame.sprite.groupcollide(all_bricks, all_bricks,False, True)

    # for j in colisao_p_p:
    #     j = brick(brick_img)
    #     all_sprites.add(j)
    #     all_bricks.add(j)

# TESTA AI TIRAR ESSES COMETARIOS DE CIMA DA FORMA DE COMENTARIO KKKKKKKKKKKKKKKKKK
        


    # ----- Gera saídas
    window.fill((0, 255, 100))  # Preenche com a cor verde
    # Desenhando sprites
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

