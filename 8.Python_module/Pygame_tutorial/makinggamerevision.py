# import pygame
import pygame
import random
pygame.init()
screen=pygame.display.set_mode((800,500))
pygame.display.set_caption("Amrit panta")
icon=pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)
background=pygame.image.load('background.png')
# player
PlayerImg=pygame.image.load('mero.png')
playerX=200
playerY=420
player_change=0

# enemy
enemyImg=pygame.image.load('cartoon.png')
enemyX=random.randint(0,800)
enemyY=random.randint(10,100)
enemyX_change=1.5
# enemyY_change=0
# bullet
bulletImg=pygame.image.load('bullet.png')
bulletX=0
bulletY=420
bulletX_change=0
bulletY_change=40
bullet_state="Ready"



def player(x,y):
    screen.blit(PlayerImg,(x,y))

def enemy(x,y):
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))
    print(f'{x}and{y}')



running=True
while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                # print("a key is pressed")
                if event.key==pygame.K_LEFT:
                    # print("Left key")
                    player_change=-2.5
                if event.key==pygame.K_RIGHT:
                    # print("right key")
                    player_change=2.5
                if event.key==pygame.K_SPACE:   
                    print("1")
                    if bullet_state is "Ready":
                        print("2\n\n")
                        bulletX=playerX
                        fire_bullet(bulletX,bulletY) 
                        print("3\n")


            if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                        # print("Key have been released")
                        player_change=0
            # if event.key==pygame.K_SPACE:
            

                           
             


        # screen.fill((0,0,0))
        screen.blit(background,(0,0))
        playerX+=player_change
        if playerX<=0:
            playerX=0
        elif playerX>=736:
            playerX=736
        enemyX+=enemyX_change
        # enemyX_change=1.5
        enemyY_change=40
        if enemyX<=0:
            enemyX_change=1.5
            enemyY+=enemyY_change
        elif enemyX>=736:
            enemyX_change=-1.5
            enemyY+=enemyY_change
        if bullet_state is "fire":
            print("Panta")
            fire_bullet(bulletX,bulletY)
            print("Amrit")
            bulletY-=bulletY_change
            
            



        player(playerX,playerY)
        enemy(enemyX,enemyY)
        pygame.display.update()


