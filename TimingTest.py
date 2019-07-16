import time, keyboard, pygame
from rhythm import *

screen_size = (700,500)
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = ( 255, 255,   0)

pygame.init()
pygame.mixer.init()

mychart = Chart("./SampleChart.txt", 276, 11)
mysong = Song("Test Song", "./Bad Apple.mp3", "2:01", 276, mychart)

note_period = 1.0/(float(mychart.bpm)/60.0)
note_counter = -1

x_pressed = False
n_pressed = False
input_period = 0.001

main_screen = pygame.display.set_mode(screen_size)
font = pygame.font.SysFont('Calibri', 18, True, False)
done = False
main_screen.fill(WHITE)
pygame.display.flip()

pygame.mixer.music.load(mysong.filepath)
pygame.mixer.music.play()
last_note = time.time()
last_input = time.time()
while(note_counter <= mychart.chart_len):
    if(time.time() - last_input > input_period):
        #POLL FOR X
        if(not x_pressed and keyboard.is_pressed('x')):
            x_pressed = True
        elif(x_pressed and not keyboard.is_pressed('x')):
            x_pressed = False

        #POLL FOR N
        if(not n_pressed and keyboard.is_pressed('n')):
            n_pressed = True
        elif(n_pressed and not keyboard.is_pressed('n')):
            n_pressed = False
        last_input = time.time()
        
    if(time.time() - last_note > note_period):
        if(note_counter < mychart.chart_len):
            upcoming_notes = mychart.get_notes(note_counter+1)
            if(upcoming_notes != "-"):
                for note in upcoming_notes:
                    note_pos = note.pos_start.split("-")
                    color = RED if note.button == "A" else YELLOW if note.button == "B" else BLUE
                    pygame.draw.circle(main_screen, color, [int(note_pos[0]), 500 - int(note_pos[1])], 30)
                    note.status = time.time()
                    text = font.render(note.button, True, BLACK)
                    main_screen.blit(text, [int(note_pos[0])-8,500-int(note_pos[1])-8])
        note_counter = note_counter + 1
        last_note = time.time()
    pygame.display.flip() ##refresh the display each time through the main loop?

while not done:
    for event in pygame.event.get(): #Pygame events are only used for handling window close
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
