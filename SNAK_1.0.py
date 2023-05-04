import pygame, sys          #
from pygame.locals import * # Bibliotecas utilizadas
import random               # 


WINDOW = (400,400) # Tamanho da janela 
pixel = 10 


def collision(pos1,pos2): # Função de colição de objetos 
    return pos1 == pos2   #


def limition(pos):                                        #
    if 0 <=pos[0] < WINDOW[0] and 0 <= pos[1] < WINDOW[1]:#
        return False                                      # Limite da borda do jogo 
    else:                                                 #
        return True                                       #
    
    
def sort_apple():                                      #
    x = random.randint(0,WINDOW[0])                    # Sortiar onde a maça vai aparecer 
    y = random.randint(0,WINDOW[1])                    # 
    return (x // pixel * pixel, y // pixel * pixel)    #
        

pygame.init()                            #
screen = pygame.display.set_mode(WINDOW) # Janela principal
pygame.display.set_caption('Snake')      #


SNAK_pos = [(250,50),(260,50),(270,50)]   # A posição de onde a snake aparece 
SNAK_surface = pygame.Surface((9.5,9.5))  # A surperficie 
SNAK_surface.fill((124,252,0))              # A cor da snake
SNAK_direction = K_LEFT                   # Pra onde a snake vai no inicio do jogo

apple_surface = pygame.Surface((pixel,pixel))   # A surperficie 
apple_surface.fill((255,0,0))                   # A cor 
apple_pos = sort_apple()                        # coloca a apple em um local aleatorio

def restart_game():                         #
    global SNAK_pos                         #
    global apple_pos                        # 
    global SNAK_direction                   # restart jogo 
    SNAK_pos = [(250,50),(260,50),(270,50)] # 
    SNAK_direction = K_LEFT                 #
    apple_pos = sort_apple()                #


while True: #principal loop
    pygame.time.Clock().tick(15)
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
        
        elif event.type == KEYDOWN:                      #
            if event.key in [K_UP,K_DOWN,K_LEFT,K_RIGHT]:# criar os  botões
                SNAK_direction = event.key               # 
                
    screen.blit(apple_surface, apple_pos)
    
    if collision(apple_pos,SNAK_pos[0]):
        SNAK_pos.append((pixel,pixel))  
        apple_pos = sort_apple()         
    
    for pos in SNAK_pos:
        screen.blit(SNAK_surface,pos)
            
    for i in range(len(SNAK_pos) -1,0,-1):
        if collision(SNAK_pos[0],SNAK_pos[i]):
            restart_game()
        SNAK_pos[i] = SNAK_pos[i-1]
        
    if limition(SNAK_pos[0]):
        restart_game()
        
    if SNAK_direction == K_UP:
        SNAK_pos[0] = (SNAK_pos[0][0],SNAK_pos[0][1] - pixel )
        
    elif SNAK_direction == K_DOWN:
        SNAK_pos[0] = (SNAK_pos[0][0],SNAK_pos[0][1] + pixel )
        
    elif SNAK_direction == K_LEFT:
        SNAK_pos[0] = (SNAK_pos[0][0] - pixel ,SNAK_pos[0][1])
    
    elif SNAK_direction == K_RIGHT:
        SNAK_pos[0] = (SNAK_pos[0][0] + pixel ,SNAK_pos[0][1])
    
        
    pygame.display.update()
        
    
    
