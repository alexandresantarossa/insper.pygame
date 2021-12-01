# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time
pygame.init()

#Toca o hino
musica =pygame.mixer.Sound('assets/matue.mp3')
musica.set_volume(0.1)
musica.play()

# ----- Gera tela principal
WIDTH = 750
HEIGHT = 650
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bombinha')

# ----- Inicia assets
LAYOUT = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1],
    [1, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,-1,6,1,],
    [1, -1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,-1,1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0,1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0,1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,0,1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0,1],
    [1, -1 , 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,-1,1],
    [1, 5, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1,-1,1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1,1,1],
        ]
BONECO_WIDTH = 45
BONECO_HEIGHT = 40
BRICK_WIDTH=50
BRICK_HEIGHT=50
WOOD_WIDTH=50
WOOD_HEIGHT=50
BOMB_WIDTH=90
BOMB_HEIGHT=90
font = pygame.font.SysFont(None, 48)
boneco_img = pygame.image.load('assets/hulk.png').convert_alpha()
boneco_img = pygame.transform.scale(boneco_img, (BONECO_WIDTH, BONECO_HEIGHT))
boneco1_img = pygame.image.load('assets/chewbaca.png').convert_alpha()
boneco1_img = pygame.transform.scale(boneco1_img, (BONECO_WIDTH, BONECO_HEIGHT))
brick_img = pygame.image.load('assets/bricks.png').convert_alpha()
brick_img = pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT)) 
wood_img = pygame.image.load('assets/wood.png').convert_alpha()
wood_img = pygame.transform.scale(wood_img, (WOOD_WIDTH, WOOD_HEIGHT))
bomb_img=pygame.image.load('assets/bomb.png').convert_alpha()
bomb_img = pygame.transform.scale(bomb_img, (BOMB_WIDTH, BOMB_HEIGHT))

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class brick(pygame.sprite.Sprite):
    def __init__(self, img,x,y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x*BRICK_WIDTH
        self.rect.y = y*BRICK_HEIGHT

class wood(pygame.sprite.Sprite):
    def __init__(self, img,x,y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x*WOOD_WIDTH
        self.rect.y = y*WOOD_HEIGHT
       



class Player1(pygame.sprite.Sprite):
    def __init__(self, img, all_sprites, all_bombs, bomb_img,x,y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x*BRICK_WIDTH
        self.rect.y = y*BRICK_HEIGHT
        self.all_sprites = all_sprites
        self.all_bombs = all_bombs
        self.bomb_img = bomb_img
        
        self.x = x
        self.y = y

    



    def update(self):
        # Atualização da posição do boneco
        self.rect.x = self.x*BRICK_WIDTH
        self.rect.y = self.y*BRICK_HEIGHT

    
    
    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_bomb = Bomb(self.bomb_img, self.rect.bottom+17, self.rect.centerx+2)
        self.all_sprites.add(new_bomb)
        self.all_bombs.add(new_bomb)


class Player2(pygame.sprite.Sprite):
    def __init__(self, img, all_sprites, all_bombs, bomb_img,x,y):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x*BRICK_WIDTH
        self.rect.y = y*BRICK_HEIGHT
        self.all_sprites = all_sprites
        self.all_bombs = all_bombs
        self.bomb_img = bomb_img

        self.x = x
        self.y = y 

    def update(self):
        # Atualização da posição do boneco
        self.rect.x = self.x*BRICK_WIDTH
        self.rect.y = self.y*BRICK_HEIGHT

       
        
        
    def shoot(self):
        # A nova bala vai ser criada logo acima e no centro horizontal da nave
        new_bomb = Bomb(self.bomb_img, self.rect.bottom+17, self.rect.centerx+2)
        self.all_sprites.add(new_bomb)
        self.all_bombs.add(new_bomb)

class Bomb(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, img, bottom, centerx):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()

        # Coloca no lugar inicial definido em x, y do constutor
        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = 0  
        self.speedx = 0 

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando um grupo de blocos 
all_woods = pygame.sprite.Group()
all_bricks = pygame.sprite.Group()

# Criando um grupo de sprites
all_sprites = pygame.sprite.Group()
all_bombs = pygame.sprite.Group()
all_blocks = pygame.sprite.Group()

# Criando os blocos
for l in range (len(LAYOUT)):
    for c in range (len(LAYOUT[l])):
        item = LAYOUT[l][c]
        
        if item == 1:
            pedra = brick(brick_img,c,l)
            all_bricks.add(pedra)
        
        if item == 0:
            r= random.randint(2,4)
            if r ==3 or r==4:
                madeira =wood(wood_img,c,l)
                all_woods.add(madeira)
                LAYOUT[l][c] =1
            else:
                LAYOUT[l][c] =0

        if item == 5 :

            LAYOUT[l][c] =0 
            player1 = Player1(boneco_img, all_sprites, all_bombs, bomb_img,c,l)
            
        
        if item == 6:
             LAYOUT[l][c] =0
             player2 = Player2(boneco1_img,all_sprites, all_bombs, bomb_img,c,l)
            
# adicionando aos grupos de sprites
all_sprites.add(player1)
all_sprites.add(player2)
all_sprites.add(all_bricks)
all_sprites.add(all_woods)
all_blocks.add(all_bricks)
all_blocks.add(all_woods)

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
            # AÇÕES PLAYER 1
           
            if event.key == pygame.K_LEFT:
                if LAYOUT[player1.y][player1.x - 1] in[0,-1] :
                    player1.x -= 1 
           
            if event.key == pygame.K_RIGHT: 
                if LAYOUT[player1.y][player1.x + 1] in[0,-1]:
                    player1.x += 1 
           
            if event.key == pygame.K_UP:
                if LAYOUT[player1.y - 1][player1.x] in[0,-1]:
                    player1.y -=1
            
            if event.key == pygame.K_DOWN:
                if LAYOUT[player1.y + 1][player1.x] in[0,-1]:
                    player1.y +=1
                
            if event.key == pygame.K_RSHIFT:
                player1.shoot()
            
            #AÇÕES PLAYER 2

            if event.key == pygame.K_a:
                if LAYOUT[player2.y][player2.x - 1] in[0,-1] :
                    player2.x -= 1 
            
            if event.key == pygame.K_d: 
                if LAYOUT[player2.y][player2.x + 1] in[0,-1]:
                    player2.x += 1 
            
            if event.key == pygame.K_w:
                if LAYOUT[player2.y - 1][player2.x] in[0,-1]:
                    player2.y -=1
            
            if event.key == pygame.K_s:
                if LAYOUT[player2.y + 1][player2.x] in[0,-1]:
                    player2.y +=1
                
            if event.key == pygame.K_SPACE:
                player2.shoot()
     
  

    # ----- Atualiza estado do jogo
    # Atualizando a posição das sprites
    all_sprites.update()


    

    # ----- Gera saídas
    window.fill((0, 255, 100))  # Preenche com a cor verde
    # Desenhando sprites
    all_sprites.draw(window)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

