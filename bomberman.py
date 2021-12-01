# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
import time
from pygame.font import Font

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
title = pygame.font.SysFont(None,80)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


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
bonecobig_img = pygame.image.load('assets/hulk.png').convert_alpha()
bonecobig_img = pygame.transform.scale(bonecobig_img, (300, 300))
boneco1big_img = pygame.image.load('assets/chewbaca.png').convert_alpha()
boneco1big_img = pygame.transform.scale(boneco1big_img, (300, 300))


# ----- Configura a tela inicial
click = False

def main_menu():
    while True:

        window.fill((0, 255, 100))
        window.blit(bomb_img, (160,80))
        draw_text('Bombinha', title, (0, 0, 0), window, 235, 100)
        window.blit(bomb_img, (500,80))

        draw_text('CONTROLES P1', font, (0, 0, 0), window, 10, 175)
        draw_text('SETAS', font, (0, 0, 0), window, 10, 260)
        draw_text('BOMBA: SHIFT', font, (0, 0, 0), window, 10, 300)

        draw_text('CONTROLES P2', font, (0, 0, 0), window, 450, 175)
        draw_text('WASD', font, (0, 0, 0), window, 450, 260)
        draw_text('BOMBA: ESPAÇO', font, (0, 0, 0), window, 450, 300)


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

            #condicoes de tempo para soltar a bomba
            self.last_update = pygame.time.get_ticks()
            self.frame_ticks = 10
            self.last_shot = pygame.time.get_ticks()
            self.shoot_ticks = 3000
        



        def update(self):
            # Atualização da posição do boneco
            self.rect.x = self.x*BRICK_WIDTH
            self.rect.y = self.y*BRICK_HEIGHT

        
        
        def shoot(self):
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            now = pygame.time.get_ticks()

            elapsed_ticks = now - self.last_shot

            if elapsed_ticks > self.shoot_ticks:
                

                self.last_shot = now

                new_bomb = Bomb(self.bomb_img, self.rect.bottom+17, self.rect.centerx+2, self.x, self.y)
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

            #condicoes de tempo bomba
            self.last_update = pygame.time.get_ticks()
            self.frame_ticks = 10
            self.last_shot = pygame.time.get_ticks()
            self.shoot_ticks = 3000

        def update(self):
            # Atualização da posição do boneco
            self.rect.x = self.x*BRICK_WIDTH
            self.rect.y = self.y*BRICK_HEIGHT


            
        def shoot(self):
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            now = pygame.time.get_ticks()

            elapsed_ticks = now - self.last_shot

            if elapsed_ticks > self.shoot_ticks:

                self.last_shot = now

                new_bomb = Bomb(self.bomb_img, self.rect.bottom+17, self.rect.centerx+2, self.x, self.y)
                self.all_sprites.add(new_bomb)
                self.all_bombs.add(new_bomb)

    class Bomb(pygame.sprite.Sprite):
        # Construtor da classe.
        def __init__(self, img, bottom, centerx,i,j):
            # Construtor da classe mãe (Sprite).
            pygame.sprite.Sprite.__init__(self)

            self.image = img
            self.rect = self.image.get_rect()

            # Coloca no lugar inicial definido em x, y do constutor
            self.rect.centerx = centerx
            self.rect.bottom = bottom
            self.tempo = 150

            self.i = j
            self.j = i

        def update(self):
            self.tempo -= 2 
        
            if self.tempo <= 0:
                #print('oi')
                center = self.rect.center
                self.rect.width *= 1 
                self.rect.height *= 1 
                self.rect.center = center

                hits = pygame.sprite.groupcollide(all_bombs,all_woods,False,False)
                for bomba, woods in hits.items():
                    possiveis = [(self.i + 1, self.j), (self.i - 1, self.j), (self.i, self.j+ 1), (self.i, self.j - 1)]
                    # self.kill()
                    for wood in woods:
                        #print(wood)
                        # print((wood.y, wood.x))
                        # print((self.i, self.j))
                        if (wood.y, wood.x) in possiveis:
                            print('oi')
                            LAYOUT[wood.y][wood.x] = 0
                            wood.kill()

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

        # hits = pygame.sprite.groupcollide(all_bombs,all_woods,False,False)
        
        # for bomba, woods in hits.items():
            
        #         bomba.kill()
        #         for wood in woods:

        #             LAYOUT[wood.y][wood.x] = 0

        #             wood.kill()


        

        # ----- Gera saídas
        window.fill((0, 255, 100))  # Preenche com a cor verde
        # Desenhando sprites
        all_sprites.draw(window)

        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

    # ----- Configura as telas finais
def win_p1():
    while True:

        window.fill((0, 255, 100))
        draw_text('O JOGADOR 1 VENCEU!', title, (0, 0, 0), window, 50, 100)
        window.blit(bonecobig_img, (200, 300))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(20, 200, 320, 50)
        button_2 = pygame.Rect(400, 200, 320, 50)


        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.QUIT()
        pygame.draw.rect(window, (255, 0, 0), button_1)
        pygame.draw.rect(window, (255, 0, 0), button_2)
        draw_text('JOGAR DE NOVO?', font, (0, 0, 0), window, 30, 210)
        draw_text('SAIR', font, (0, 0, 0), window, 520, 210)

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
        draw_text('O JOGADOR 2 VENCEU!', title, (0, 0, 0), window, 50, 100)
        window.blit(boneco1big_img, (200, 300))

        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(20, 200, 320, 50)
        button_2 = pygame.Rect(400, 200, 320, 50)


        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.QUIT()
        pygame.draw.rect(window, (255, 0, 0), button_1)
        pygame.draw.rect(window, (255, 0, 0), button_2)
        draw_text('JOGAR DE NOVO?', font, (0, 0, 0), window, 30, 210)
        draw_text('SAIR', font, (0, 0, 0), window, 520, 210)

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
