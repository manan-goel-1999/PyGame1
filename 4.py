import pygame
import time
import random
'''displayheight = input("Enter Height of Screen")
displaywidth = input("Enter Width of Screen")'''
pygame.init()
#Make Surface and give name to it
displayheight = 720
displaywidth = 1280
gameDisplay = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('Slither')
pygame.display.update()

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
#give color as a tuple in order RGB

#Make Font Object
font = pygame.font.SysFont(None,45)

FPS = 45
blocksize = 10

#Display Message
def MessageDisplay(msg,color):
    text = font.render(msg,True,color)                          #Render Text of Specific Color and Size
    gameDisplay.blit(text, [displaywidth/2,displayheight/2])    #Render The Message to the gameDisplay

clock = pygame.time.Clock()
#make a clock object

#Actual Game Loop
def GameLoop():
    game = True
    GameOver =  False

    x_coordinate = displaywidth/2
    x_coordinate_change = 0
    y_coordinate_change = 0
    y_coordinate = displayheight/2
    while game:
        while GameOver == True:
            gameDisplay.fill(black)
            MessageDisplay("Game Over, Enter A to Play Again and Q to Exit",white)
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
                if event.key == pygame.K_RIGHT:
                    x_coordinate_change = blocksize
                    y_coordinate_change = 0
                if event.key == pygame.K_UP:
                    y_coordinate_change = -blocksize
                    x_coordinate_change = 0
                if event.key == pygame.K_DOWN:
                    y_coordinate_change = blocksize
                    x_coordinate_change = 0


            '''if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                    x_coordinate_change = 0
                if event.key == event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_coordinate_change = 0
            #print(event)'''


        x_coordinate += x_coordinate_change
        y_coordinate += y_coordinate_change

        if x_coordinate > displaywidth:
            GameOver = True
        if  x_coordinate < 0:
            GameOver = True
        if y_coordinate > displayheight:
            GameOver = True
        if y_coordinate < 0:
            GameOver = True
        gameDisplay.fill(white)


        pygame.draw.rect(gameDisplay,red,[x_coordinate,y_coordinate,blocksize,blocksize])
        #surface,colour,position of top left,width,height    
        circlex = random.randrange(0,displaywidth)
        circley = random.randrange(0,displayheight)
        pygame.draw.circle(gameDisplay,black,[circlex,circley],int(blocksize/2))

        #gameDisplay.fill(red,rect = [x_coordinate,y_coordinate,blocksize,blocksize])
        #faster way to make shape


        pygame.display.update()


        clock.tick(FPS)                  
        #specify number of frames per second
    
    pygame.quit()
    quit()

GameLoop()