import pygame
import time
import random
import os

pygame.init()

displayheight = 720                                                     #Make Surface and give name to it
displaywidth = 960                                                      #Make Surface and give name to it
gameDisplay = pygame.display.set_mode((displaywidth,displayheight))     #Make Surface and give name to it
pygame.display.set_caption('Slither')                                   #Make Surface and give name to it
pygame.display.update()

image = pygame.image.load('./snake.png')    #Get The Head

white = (255,255,255)       #give color as a tuple in order RGB
red = (255,0,0)             #give color as a tuple in order RGB
black = (0,0,0)             #give color as a tuple in order RGB

font = pygame.font.SysFont(None,45)         #Make Font Object

blocksize = 24

direction = "right"

def text_object(text,color):
    TextSurface = font.render(text,True,color)
    return TextSurface,TextSurface.get_rect()

#Display Message
def MessageDisplay(msg,color,ydisplace):
    TextSurface, TextRect = text_object(msg,color)                                                #Text Surface Object
    #text = font.render(msg,True,color)                                                           #Render Text of Specific Color and Size
    #gameDisplay.blit(text, [displaywidth/4,displayheight/4])                                     #Render The Message to the gameDisplay
    TextRect.center = (displaywidth/2), (displayheight/2) + ydisplace
    gameDisplay.blit(TextSurface,TextRect) 

clock = pygame.time.Clock()
#make a clock object
def snake(blocksize,snakebody):
    
    if direction == "right":                                    #Rotate The Head
        head = pygame.transform.rotate(image,90)                #Rotate The Head
    if direction == "left":                                     #Rotate The Head
        head = pygame.transform.rotate(image,270)               #Rotate The Head
    if direction == "up":                                       #Rotate The Head
        head = pygame.transform.rotate(image,180)               #Rotate The Head
    if direction == "down":                                     #Rotate The Head
        head = pygame.transform.rotate(image,0)                 #Rotate The Head

    gameDisplay.blit(head, (snakebody[-1][0], snakebody[-1][1]))

    for block in snakebody[:-1]:
        pygame.draw.rect(gameDisplay,black,[block[0],block[1],blocksize,blocksize])

pause = False


def pausegame(pause):                                                 #Function to Pause Game                  
    while pause is True:                                              #Function to Pause Game
        TextSurface, TextRect = text_object("Game Paused Press R to Resume",red)
        TextRect.center = (displaywidth/2), (displayheight/4)
        gameDisplay.blit(TextSurface,TextRect)
        pygame.display.update()
        for event in pygame.event.get():                              #Function to Pause Game  
            print(event)                                              #Function to Pause Game
            if event.key == pygame.K_r:                               #Function to Pause Game
                pause = False                                         #Function to Pause Game
                return                                                #Function to Pause Game

#Actual Game Loop
def GameLoop():
    FPS = 12
    game = True
    GameOver =  False
    #snakelegth = 10
    circlex = round(random.randrange(0,displaywidth-blocksize)/24.0)*24
    circley = round(random.randrange(0,displayheight-blocksize)/24.0)*24
    count = 1
    body = []
    bodlength = 5
    score = 0
    x_coordinate = displaywidth/2
    x_coordinate_change = 0
    y_coordinate_change = 0
    y_coordinate = displayheight/2

    highscore = open("highscore.txt",'r')
    high = highscore.readline()
    #print(high)
    high = int(high)

    while game:
        global direction
        global pause
        while GameOver == True:
            gameDisplay.fill(black)
            MessageDisplay("Game Over",red,-50)
            MessageDisplay(" Enter A to Play Again and Q to Exit",white,50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game = False
                        GameOver = False
                    if event.key == pygame.K_a:
                        GameLoop()
                if event.type == pygame.QUIT:
                    game = False
        

        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                game = False


            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_coordinate_change = -blocksize
                    y_coordinate_change = 0
                    direction = "left"
                if event.key == pygame.K_RIGHT:
                    x_coordinate_change = blocksize
                    y_coordinate_change = 0
                    direction = "right"
                if event.key == pygame.K_UP:
                    y_coordinate_change = -blocksize
                    x_coordinate_change = 0
                    direction = "up"
                if event.key == pygame.K_DOWN:
                    y_coordinate_change = blocksize
                    x_coordinate_change = 0
                    direction = "down"
                if event.key == pygame.K_q:
                    game = False
                if event.key == pygame.K_SPACE:
                    pause = True
                    x_coordinate_change = 0
                    y_coordinate_change = 0
                    pausegame(pause)
                    pause = False
                    if direction == "right":
                        x_coordinate_change = blocksize
                    if direction == "left":
                        x_coordinate_change = -blocksize
                    if direction == "up":
                        y_coordinate_change = -blocksize
                    if direction == "down":
                        y_coordinate_change = blocksize

        #for event in pygame.event.get():
        #    print(event)

        if x_coordinate > displaywidth:
            x_coordinate = 0
        if  x_coordinate < 0:
            x_coordinate = displaywidth
        if y_coordinate > displayheight:
            y_coordinate = 0
        if y_coordinate < 0:
            y_coordinate = displayheight

        x_coordinate += x_coordinate_change
        y_coordinate += y_coordinate_change

        gameDisplay.fill(white)

        if count%5 is 0 and count is not 0:
            applesize = blocksize*2
        else:
            applesize = blocksize
        pygame.draw.rect(gameDisplay,red,[circlex,circley,applesize,applesize])

        head = []

        if pause is False:
            head.append(x_coordinate)
            head.append(y_coordinate)
            body.append(head)
            if len(body) > bodlength:
                del body[0]                 #Remove Last Addition to the list

        if bodlength > 5:
            for element in body[:-1]:
                if element == head:
                    GameOver = True

        snake(blocksize,body)

        if x_coordinate >= circlex and x_coordinate <= circlex + applesize:
            if y_coordinate >= circley and y_coordinate <= circley + applesize:
                circlex = round(random.randrange(0,displaywidth-blocksize)/24.0)*24
                circley = round(random.randrange(0,displayheight-blocksize)/24.0)*24
                count += 1
                bodlength += 1
                FPS += 1 
                if applesize is blocksize*2:
                    score += 20
                else:
                    score += 10

        text = font.render("Score : " + str(score),True,black)
        gameDisplay.blit(text,[0,0])
        #print(score)
            #snakelegth += blocksize
        '''#gameDisplay.fill(red,rect = [x_coordinate,y_coordinate,blocksize,blocksize])
        #faster way to make shape'''


        pygame.display.update()
        if score > high:
            high = score
            highscore1 = open("highscore1.txt",'w')
            highscore1.write(str(high))
            os.system("rm highscore.txt")
            os.system("mv highscore1.txt highscore.txt")
        
        #print(high)
        highest = font.render("Highest Score : " + str(high),True,black)
        gameDisplay.blit(highest,[round(0.6*displaywidth),0])
        pygame.display.update()

        #print (x_coordinate , y_coordinate)
        #print(body)
        clock.tick(FPS)                 #specify number of frames per second
    pygame.quit()
    quit()

GameLoop()
