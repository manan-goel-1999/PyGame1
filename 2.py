import pygame
pygame.init()
#Make Surface and give name to it
gameDisplay = pygame.display.set_mode((1280,720))
pygame.display.set_caption('Slither')
pygame.display.update()

#Game Loop Control
gameExit = True

white = (255,255,255)
red = (255,0,0)
#give color as a tuple in order RGB


x_coordinate = 300
y_coordinate = 600
x_coordinate_change = 0
y_coordinate_change = 0


clock = pygame.time.Clock()
#make a clock object

#Actual Game Loop
while gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = False
        
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_coordinate_change = -10
            if event.key == pygame.K_RIGHT:
                x_coordinate_change = 10
            if event.key == pygame.K_UP:
                y_coordinate_change = -10
            if event.key == pygame.K_DOWN:
                y_coordinate_change = 10
        
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: 
                x_coordinate_change = 0
            if event.key == event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_coordinate_change = 0
        #print(event)


    x_coordinate += x_coordinate_change
    y_coordinate += y_coordinate_change
    if x_coordinate > 1280:
        x_coordinate = 0
    if y_coordinate > 720:
        y_coordinate = 0
    if x_coordinate < 0:
        x_coordinate = 1280
    if y_coordinate < 0:
        y_coordinate = 720 


    gameDisplay.fill(white)
    
    
    #pygame.draw.rect(gameDisplay,red,[640,360,10,100])
    #surface,colour,position of top left,width,height    
    
    
    gameDisplay.fill(red,rect = [x_coordinate,y_coordinate,10,10])
    #faster way to make shape
    
    
    pygame.display.update()
    
    
    clock.tick(60)                  
    #specify number of frames per second


pygame.quit()
quit()