import pygame
import time
import random

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
    #text = font.render(msg,True,color)                          #Render Text of Specific Color and Size
    #gameDisplay.blit(text, [displaywidth/4,displayheight/4])    #Render The Message to the gameDisplay
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


#Actual Game Loop
def GameLoop():
    FPS = 12
    game = True
    GameOver =  False
    #snakelegth = 10
    circlex = round(random.randrange(0,displaywidth-blocksize)/20.0)*20
    circley = round(random.randrange(0,displayheight-blocksize)/20.0)*20
    count = 1
    body = []
    bodlength = 5
    score = 0
    x_coordinate = displaywidth/2
    x_coordinate_change = 0
    y_coordinate_change = 0
    y_coordinate = displayheight/2
    while game:
        global direction
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

        if x_coordinate > displaywidth:
            GameOver = True
        if  x_coordinate < 0:
            GameOver = True
        if y_coordinate > displayheight:
            GameOver = True
        if y_coordinate < 0:
            GameOver = True

        x_coordinate += x_coordinate_change
        y_coordinate += y_coordinate_change

        gameDisplay.fill(white)

        if count%5 is 0 and count is not 0:
            applesize = blocksize*2
        else:
            applesize = blocksize
        pygame.draw.rect(gameDisplay,red,[circlex,circley,applesize,applesize])

        head = []
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
                #FPS += 4 
                if count%6 is 0:
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

        #print (x_coordinate , y_coordinate)
        #print(body)
        clock.tick(FPS)                 #specify number of frames per second
    pygame.quit()
    quit()

GameLoop()
