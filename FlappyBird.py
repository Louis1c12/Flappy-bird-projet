import pygame
import time
import core
import random
import keyboard




largeur = 500
hauteur = 700
gravity = 2
start = 0
bird = [75,200]
obstacle = []
gameOver=False
obstaclesHaut = []
obstaclesBas = []
R = 10 #rayon bird
V = 1 #vitesse
w = 10 #saut
tesNul = pygame.image.load("end.jpg")


def setup():
    print("setup")
    global obstaclesHaut, obstaclesBas,start, hauteur, largeur
    start = time.time()
    core.WINDOW_SIZE=[hauteur,largeur]
    core.fps=30


    for i in range(0,30):
        Vx = 100
        Vy = 150
        y = random.randint(0,100)
        x = random.randint(Vx,Vy)
        s = R*4
        miniHb = 300
        h = hauteur- miniHb

        obstaclesHaut = obstaclesHaut + [[200+i*200,0,40,h-((s+x)+y)]]
        obstaclesBas = obstaclesBas + [[200 + i *200, h-y+s, 40, 800]]

    print("setup end")




def run():

    global bird, gameOver, score, V,y,z,x,w

    score = str(int(time.time() - start))

    bird[1] += gravity   #gravitéSurBird

    if keyboard.is_pressed('space'):
        bird[1] = bird[1] - w           #QuandAppuiBirdVersleHau

    if gameOver == True :
        bird[1] = 200
        bird[0] = 50



    if gameOver != True:
        print('score :' + str(int(time.time() - start)))
        #print(score)

        #while str(int(time.time() - start)) == str(int(time.time() +1)) :
            #V =V+10
            #while start <= 50:
                #Vx = Vx-20
                #Vy = Vy-10

        if bird[1] > hauteur:   #GameOver si on sort de l'écran
            gameOver = True
        if bird[1] <= 0:
            gameOver = True

        for obstacle in obstaclesHaut:  #GameOver si on touche obstacle du haut
            obstacle[0]-=V
            if bird[0]+R  == obstacle[0] and bird[1]+R < obstacle[3] or obstacle[0]< bird[0]+R < obstacle[0]+obstacle[2] and bird[1]-R < obstacle[3] :#collisionRectangleHaut
                gameOver = True


        for obstacle in obstaclesBas:   #GameOver si on touche obstacle du bas
            obstacle[0]-=V
            if bird[0]+R  == obstacle[0] and bird[1]+R > obstacle[1] or obstacle[0]< bird[0]+R<obstacle[0]+obstacle[2] and bird[1]+R > obstacle[1] :#collisionRectangleBas
                gameOver = True




    if gameOver == True :
         core.screen.blit(tesNul, (0, 0))  #ImageGameOver



    pygame.draw.circle(core.screen, (255, 0, 0), (bird[0], bird[1]), R)
    for obstacle in obstaclesHaut:
        pygame.draw.rect(core.screen, (0, 0, 250), (obstacle[0], obstacle[1], obstacle[2], obstacle[3]))
    for obstacle in obstaclesBas:
        pygame.draw.rect(core.screen, (0, 255, 0), (obstacle[0], obstacle[1], obstacle[2], obstacle[3]))


core.main(setup, run)