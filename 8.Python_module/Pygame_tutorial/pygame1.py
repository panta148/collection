import pygame 
pygame.init()
screen=pygame.display.set_mode((600,400))
pygame.display.set_caption("Amrit panta")
icon=pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)
# player
PlayerImg=pygame.image.load('mero.png')
playerX=200
playerY=300
player_change=0
def player(x,y):
    screen.blit(PlayerImg,(x,y))


running=True
while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if event.type==pygame.KEYDOWN:
                # print("a key is pressed")
                if event.key==pygame.K_LEFT:
                    # print("Left key")
                    player_change=-0.1
                if event.key==pygame.K_RIGHT:
                    # print("right key")
                    player_change=0.1
            if event.type==pygame.KEYUP:
                    if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                        # print("Key have been released")
                        player_change=0
             


        screen.fill((0,0,0))
        playerX+=player_change
        if playerX<=0:
            playerX=0
        elif playerX>=550:
            playerX=550



        player(playerX,playerY)
        pygame.display.update()


