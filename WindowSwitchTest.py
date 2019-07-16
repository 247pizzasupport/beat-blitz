import pygame, keyboard

screen_size = (700,500)
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = ( 255, 255,   0)

pygame.init()
main_screen = pygame.display.set_mode(screen_size)
main_screen.fill(WHITE)
pygame.display.flip()

windowSwitch = 1

def mainWindow():
    print("Main window called!")
    done = False
    main_screen.fill(WHITE)
    titleScreen = pygame.image.load('./Resources/TitleScreen.png')
    main_screen.blit(titleScreen, [0,0])
    pygame.display.flip()
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

        if(pygame.mouse.get_pressed()[0]):
            done = True
            windowSwitch = 2

def secondWindow():
    print("Second window called!")
    done = False
    main_screen.fill(WHITE)
    pygame.draw.circle(main_screen, BLUE, [350,250], 30)
    pygame.display.flip()
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                
        if(keyboard.is_pressed('left')):
           done =True
           windowSwitch = 1

while(1):
    print(windowSwitch)
    if(windowSwitch == 1):
        windowSwitch = 0
        mainWindow()
        windowSwitch = 2
    if(windowSwitch == 2):
        windowSwitch = 0
        secondWindow()
        windowSwitch = 1

pygame.quit()
