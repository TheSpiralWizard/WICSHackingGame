import pygame

pygame.init() # Initializes pygame


screenWidth = 1000 
screenHeight = 1000 
screenDimensions = (screenWidth, screenHeight)
win = pygame.display.set_mode(screenDimensions) # Sets the dimensions of the window based on the tuple to 500x500

pygame.display.set_caption("First game") # Sets the title of the window that the game is running in to "First Game"

# Variables to control the position and dimensions of our "character":
 
width = 40 
height = 60 
vel = 5  
y = screenHeight - height - vel 
x = vel 
isJump = False
jumpCount = 10

mapList = [pygame.image.load('MapImages/usa.png'), pygame.image.load('MapImages/india.png'), pygame.image.load('MapImages/china.png'),
           pygame.image.load('MapImages/russia.png'), pygame.image.load('MapImages/uk.png') ]

index = 0

def redrawGameWindow():
    global index, mapList

    win.fill((0, 0, 0))
    win.blit(mapList[index], (0, 0))
    pygame.display.update()

run = True 
while run: # While loop to keep the window persisting until the window is closed 
    pygame.time.delay(100) # Kind of like the clock in pygame

    for event in pygame.event.get(): # Gets a list of the events in pygame, then you can act on an event based on the "event" variable 

        if event.type == pygame.QUIT: # Closes the window without causing an error  
            run = False 
    
    keys = pygame.key.get_pressed() 
    mouse = pygame.mouse.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel 

    if keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel         

    if mouse[0]: 
        index += 1
        if(index >= len(mapList)):
            index = 0
        
        

    if not(isJump):
        
        if keys[pygame.K_UP] and y > vel:
            y -= vel 

        if keys[pygame.K_DOWN] and y < screenHeight - height - vel:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            neg = 1 
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2)/2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10


    # win.fill((0, 0, 0))
    redrawGameWindow()
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) 

    pygame.display.update() 



pygame.quit() 
