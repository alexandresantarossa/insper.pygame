# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time
from pygame.font import Font

pygame.init()

# ----- Toca e define a músicaS
musica =pygame.mixer.Sound('assets/matue.mp3')
musica.set_volume(0.1)
musica.play(-1)

explosao = pygame.mixer.Sound("assets/explosao.mp3")
explosao.set_volume(0.2)

# ----- Gera tela principal
WIDTH = 750
HEIGHT = 650
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Bomber Smash')

# ----- Inicia assets
# Define o nosso mapa, onde 0 são espaços livres e 1 são tijolos, 5 e 6 são os jogadores
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

# ----- Define as constantes
BONECO_WIDTH = 45
BONECO_HEIGHT = 40
BRICK_WIDTH=50
BRICK_HEIGHT=50
WOOD_WIDTH=50
WOOD_HEIGHT=50
BOMB_WIDTH=90
BOMB_HEIGHT=90
EXP_WIDTH=100
EXP_HEIGHT=100

# ----- Configura a fonte
font = pygame.font.SysFont(None, 48)
title = pygame.font.SysFont(None,80)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# ----- Carrega e muda o tamanho das imagens
boneco_img = pygame.image.load('assets/hulk verde.png').convert_alpha()
boneco_img = pygame.transform.scale(boneco_img, (BONECO_WIDTH, 45))
boneco1_img = pygame.image.load('assets/hulk.png').convert_alpha()
boneco1_img = pygame.transform.scale(boneco1_img, (BONECO_WIDTH, BONECO_HEIGHT))
brick_img = pygame.image.load('assets/bricks.png').convert_alpha()
brick_img = pygame.transform.scale(brick_img, (BRICK_WIDTH, BRICK_HEIGHT)) 
wood_img = pygame.image.load('assets/wood.png').convert_alpha()
wood_img = pygame.transform.scale(wood_img, (WOOD_WIDTH, WOOD_HEIGHT))
bomb_img=pygame.image.load('assets/bomb.png').convert_alpha()
bomb_img = pygame.transform.scale(bomb_img, (BOMB_WIDTH, BOMB_HEIGHT))
bonecobig_img = pygame.image.load('assets/hulk verde.png').convert_alpha()
bonecobig_img = pygame.transform.scale(bonecobig_img, (300, 300))
boneco1big_img = pygame.image.load('assets/hulk.png').convert_alpha()
boneco1big_img = pygame.transform.scale(boneco1big_img, (300, 300))
sand_img = pygame.image.load('assets/sand.png').convert_alpha()
sand_img = pygame.transform.scale(sand_img, (750, 650))
bg_img = pygame.image.load('assets/bg.jpeg').convert_alpha()
bg_img = pygame.transform.scale(bg_img, (750, 650))
exp1_img=pygame.image.load('assets/exp1.png').convert_alpha()
exp1_img = pygame.transform.scale(exp1_img, (EXP_WIDTH, EXP_HEIGHT))
exp2_img=pygame.image.load('assets/exp2.png').convert_alpha()
exp2_img = pygame.transform.scale(exp2_img, (EXP_WIDTH, EXP_HEIGHT))
exp3_img=pygame.image.load('assets/exp3.png').convert_alpha()
exp3_img = pygame.transform.scale(exp3_img, (EXP_WIDTH, EXP_HEIGHT))
imagem=[bomb_img,exp1_img,exp2_img,exp3_img]

# ----- Configura a tela inicial
click = False

def main_menu():
    while True:

        window.fill((0, 255, 100))
        window.blit(bg_img, (0,0))
        window.blit(boneco1_img, (140,80))
        window.blit(boneco_img, (530,80))
        draw_text('Bomber Smash', title, (255, 255, 255), window, 155, 100)

        draw_text('CONTROLES P1', font, (255, 255, 255), window, 10, 175)
        draw_text('SETAS', font, (255, 255, 255), window, 10, 260)
        draw_text('BOMBA: SHIFT', font, (255, 255, 255), window, 10, 300)

        draw_text('CONTROLES P2', font, (255, 255, 255), window, 450, 175)
        draw_text('WASD', font, (255, 255, 255), window, 450, 260)
        draw_text('BOMBA: ESPAÇO', font, (255, 255, 255), window, 450, 300)

        # ----- Configura os botões clicáveis
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(275, 400, 200, 50)
        button_2 = pygame.Rect(275, 500, 200, 50)


        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.QUIT()
        pygame.draw.rect(window, (255, 0, 0), button_1)
        pygame.draw.rect(window, (255, 0, 0), button_2)
        draw_text('JOGAR', font, (0, 0, 0), window, 310, 410)
        draw_text('SAIR', font, (0, 0, 0), window, 330, 510)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

# ----- Configura o jogo

def game():
    game = True
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

            self.x = x
            self.y =y 
        



    class Player1(pygame.sprite.Sprite):
        def __init__(self, img, all_sprites, all_bombs,x,y,imagem):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x*BRICK_WIDTH
            self.rect.y = y*BRICK_HEIGHT
            self.all_sprites = all_sprites
            self.all_bombs = all_bombs
            self.imagem = imagem
            
            self.x = x
            self.y = y

            #condicoes iniciais de tempo para soltar a bomba
            self.last_update = pygame.time.get_ticks()
            self.frame_ticks = 10
            self.last_shot = pygame.time.get_ticks()
            self.shoot_ticks = 3000
        



        def update(self):
            # Atualização da posição do boneco
            self.rect.x = self.x*BRICK_WIDTH
            self.rect.y = self.y*BRICK_HEIGHT

        
        
        def shoot(self):
            # A nova bomba vai ser criada logo acima do personagem com um cooldown de 3 segundos
            now = pygame.time.get_ticks()

            elapsed_ticks = now - self.last_shot

            if elapsed_ticks > self.shoot_ticks:
                

                self.last_shot = now

                new_bomb = Bomb(self.imagem, self.rect.bottom+17, self.rect.centerx+2, self.x, self.y)
                self.all_sprites.add(new_bomb)
                self.all_bombs.add(new_bomb)

                

    

    class Player2(pygame.sprite.Sprite):
        def __init__(self, img, all_sprites, all_bombs,x,y,imagem):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.x = x*BRICK_WIDTH
            self.rect.y = y*BRICK_HEIGHT
            self.all_sprites = all_sprites
            self.all_bombs = all_bombs
            self.imagem = imagem

            self.x = x
            self.y = y 

            #condicoes iniciais de tempo da bomba
            self.last_update = pygame.time.get_ticks()
            self.frame_ticks = 10
            self.last_shot = pygame.time.get_ticks()
            self.shoot_ticks = 3000

        def update(self):
            # Atualização da posição do boneco
            self.rect.x = self.x*BRICK_WIDTH
            self.rect.y = self.y*BRICK_HEIGHT


            
        def shoot(self):
            # A nova bomba vai ser criada logo acima do personagem com um cooldown de 3 segundos
            now = pygame.time.get_ticks()

            elapsed_ticks = now - self.last_shot

            if elapsed_ticks > self.shoot_ticks:

                self.last_shot = now

                new_bomb = Bomb(self.imagem, self.rect.bottom+17, self.rect.centerx+2, self.x, self.y)
                self.all_sprites.add(new_bomb)
                self.all_bombs.add(new_bomb)

    class Bomb(pygame.sprite.Sprite):
        # Construtor da classe.
        def __init__(self, img, bottom, centerx,i,j):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img[0]
            self.rect = self.image.get_rect()
            self.types=img

            # Coloca no lugar inicial definido em x, y do constutor
            self.rect.centerx = centerx
            self.rect.bottom = bottom
            self.tempo = 150
            self.expc=centerx
            self.expb=bottom

            self.i = j
            self.j = i

        # Configura a animação da explosão da bomba
        def update(self):
            self.tempo -= 2 


            if self.tempo>30 and self.tempo<=40:
                self.image=self.types[1]
                centerx=self.expc
                bottom=self.expb
                self.rect.centerx = centerx
                self.rect.bottom = bottom

            if self.tempo ==30:
                explosao.play()

                
            if self.tempo<=30 and self.tempo>20:
                self.image=self.types[2]
                centerx=self.expc
                bottom=self.expb
                self.rect.centerx = centerx
                self.rect.bottom = bottom

                
            if self.tempo<=20 and self.tempo>10:
                self.image=self.types[3]
                centerx=self.expc
                bottom=self.expb
                self.rect.centerx = centerx
                self.rect.bottom = bottom 
        
            if self.tempo <= 5:
                
                centerx =self.expc
                bottom = self.expb
                self.rect.width *= 1 
                self.rect.height *= 1 
                self.rect.centerx = centerx
                self.rect.bottom = bottom

                # explodindo as caixas 
                hits = pygame.sprite.groupcollide(all_bombs,all_woods,False,False)
                for bomba, woods in hits.items():
                    possiveis = [(self.i + 1, self.j), (self.i - 1, self.j), (self.i, self.j+ 1), (self.i, self.j - 1)]
                    # self.kill()
                    for wood in woods:
                        #os comentarios abaixo foram feitos para nos ajudar a achar o erro na matriz(invertemos linha e coluna), caso queira ver tambem
                        #print(wood)
                        # print((wood.y, wood.x))
                        # print((self.i, self.j))
                        if (wood.y, wood.x) in possiveis:
                
                            LAYOUT[wood.y][wood.x] = 0
                            wood.kill()
   
                # bomba matando o jogador 
                kill = pygame.sprite.groupcollide(all_bombs,all_players,False,False)
        
                for bomba,players in kill.items():
                    possiveis = [(self.i + 1, self.j), (self.i - 1, self.j), (self.i, self.j+ 1), (self.i, self.j - 1),(self.i,self.j)]

                    for player in players: 
                            if (player.y,player.x) in possiveis:
                                LAYOUT[player.y][player.x] = 0
                                if player == player1:
                                    win_p2()
                                if player == player2:
                                    win_p1()

                                player.kill()
                
                self.kill()

                                
      

                


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
    all_players = pygame.sprite.Group()

    # Criando os blocos do mapa
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
                player1 = Player1(boneco_img, all_sprites, all_bombs,c,l,imagem)
                
            
            if item == 6:
                LAYOUT[l][c] =0
                player2 = Player2(boneco1_img,all_sprites, all_bombs,c,l,imagem)
                
    # adicionando aos grupos de sprites
    all_sprites.add(player1)
    all_sprites.add(player2)
    all_sprites.add(all_bricks)
    all_sprites.add(all_woods)
    all_blocks.add(all_bricks)
    all_blocks.add(all_woods)
    all_players.add(player1)
    all_players.add(player2)



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

        window.blit(sand_img,(0,0))


        # Desenhando sprites
        all_sprites.draw(window)

        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

# ----- Configura as telas finais de vitória de cada jogador
def win_p1():
    while True:

        window.fill((0, 255, 100))
        window.blit(bg_img, (0,0))

        draw_text('O JOGADOR 1 VENCEU!', title, (255, 255, 255), window, 50, 100)
        window.blit(bonecobig_img, (200, 300))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(250, 200, 230, 40)


        if button_1.collidepoint((mx, my)):
            if click:
                pygame.QUIT()
        pygame.draw.rect(window, (255, 0, 0), button_1)
        draw_text('SAIR', font, (0, 0, 0), window, 330, 205)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def win_p2():
    while True:

        window.fill((0, 255, 100))
        window.blit(bg_img, (0,0))

        draw_text('O JOGADOR 2 VENCEU!', title, (255, 255, 255), window, 50, 100)
        window.blit(boneco1big_img, (200, 300))

        mx, my = pygame.mouse.get_pos()


        button_1 = pygame.Rect(250, 200, 230, 40)

        if button_1.collidepoint((mx, my)):
            if click:
                pygame.QUIT()
        pygame.draw.rect(window, (255, 0, 0), button_1)
        draw_text('SAIR', font, (0, 0, 0), window, 330, 205)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

# ----- Abre o jogo
main_menu()
