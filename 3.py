import pygame
displayheight = input("Enter Height of Screen")
displaywidth = input("Enter Width of Screen")
pygame.init()
#Make Surface and give name to it
displayheight = int(displayheight)
displaywidth = int(displaywidth)
gameDisplay = pygame.display.set_mode((displaywidth,displayheight))
pygame.display.set_caption('Slither')
pygame.display.update()

#Game Loop Control
gameExit = True

white = (255,255,255)
red = (255,0,0)
#give color as a tuple in order RGB


x_coordinate = displaywidth/2
y_coordinate = displayheight/2
x_coordinate_change = 0
y_coordinate_change = 0

FPS = 45
blocksize = 10

clock = pygame.time.Clock()
#make a clock object

#Actual Game Loop
while gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = False
        
        
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
        x_coordinate = 0
    if  x_coordinate < 0:
        x_coordinate = displaywidth
    if y_coordinate > displayheight:
        y_coordinate = 0  
    if y_coordinate < 0:
        y_coordinate = displayheight
    gameDisplay.fill(white)
    
    
    #pygame.draw.rect(gameDisplay,red,[640,360,10,100])
    #surface,colour,position of top left,width,height    
    
    
    gameDisplay.fill(red,rect = [x_coordinate,y_coordinate,blocksize,blocksize])
    #faster way to make shape
    
    
    pygame.display.update()
    
    
    clock.tick(FPS)                  
    #specify number of frames per second


pygame.quit()
quit()