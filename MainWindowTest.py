import pygame, time
from rhythm import *

screen_size = (700,500)
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = ( 255, 255,   0)

main_screen = pygame.display.set_mode(screen_size)
done = False

start_time = time.time()
while not done:
    for event in pygame.event.get(): #Pygame events are only used for handling window close
        if event.type == pygame.QUIT:
            done = True

    main_screen.fill(WHITE)
    pygame.draw.circle(main_screen, RED, [100,100], 30)
    pygame.draw.circle(main_screen, GREEN, [600, 200], 30)
    pygame.draw.circle(main_screen, BLUE, [300, 400], 30)
    pygame.display.flip()

pygame.quit()
