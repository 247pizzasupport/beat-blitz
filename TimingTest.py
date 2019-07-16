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

main_screen = pygame.display.set_mode(screen_size)
font = pygame.font.SysFont('Calibri', 18, True, False)
done = False
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

def songSelectWindow():
    song_list = os.listdir('./Resources/Songs/')

def songWindow():
    mychart = Chart("./Resources/Songs/Bad Apple/SampleChart.txt", 276, 11)
    mysong = Song("Test Song", "./Resources/Songs/Bad Apple/Bad Apple.mp3", 10, 276, mychart)
    
    note_period = 1.0/(float(mychart.bpm)/60.0)
    note_counter = -1
    my_score = 0

    z_pressed = False
    x_pressed = False
    n_pressed = False
    m_pressed = False
    input_period = 0.001
    
    main_screen.fill(WHITE)
    score_text = font.render(str(my_score), True, BLACK)
    main_screen.blit(score_text, [0,0])
    pygame.display.flip()
    
    drawList = []

    pygame.mixer.music.load(mysong.filepath)
    pygame.mixer.music.play()
    start_time = time.time()
    last_note = time.time()
    last_input = time.time()
    while(time.time() - start_time <= mysong.song_length):
        if(time.time() - last_input > input_period):
            #POLL FOR Z
            if(not z_pressed and keyboard.is_pressed('z')):
                z_pressed = True
                for note in drawList:
                    if(note.button == 'A' and note.status != 0 and time.time() - note.status < note_period*2):
                        print('A note hit!')
                        my_score = my_score + int(200 * abs(round(time.time() - (note.status + note_period), 2)) * (1.0/note_period))
                        note.status = 0
                        break
            elif(z_pressed and not keyboard.is_pressed('z')):
                z_pressed = False
                
            #POLL FOR X
            if(not x_pressed and keyboard.is_pressed('x')):
                x_pressed = True
                for note in drawList:
                    if(note.button == 'B' and note.status != 0 and time.time() - note.status < note_period*2):
                        print('B note hit!')
                        my_score = my_score + int(200 * abs(round(time.time() - (note.status + note_period), 2)) * (1.0/note_period))
                        note.status = 0
                        break
            elif(x_pressed and not keyboard.is_pressed('x')):
                x_pressed = False
    
            #POLL FOR N
            if(not n_pressed and keyboard.is_pressed('n')):
                n_pressed = True
                for note in drawList:
                    if(note.button == 'C' and note.status != 0 and time.time() - note.status < note_period*2):
                        print('C note hit!')
                        my_score = my_score + int(200 * abs(round(time.time() - (note.status + note_period), 2)) * (1.0/note_period))
                        note.status = 0
                        break
            elif(n_pressed and not keyboard.is_pressed('n')):
                n_pressed = False

            #POLL FOR M
            if(not m_pressed and keyboard.is_pressed('m')):
                m_pressed = True
                for note in drawList:
                    if(note.button == 'D' and note.status != 0 and time.time() - note.status < note_period*2):
                        print('D note hit!')
                        my_score = my_score + int(200 * abs(round(time.time() - (note.status + note_period), 2)) * (1.0/note_period))
                        note.status = 0
                        break
            elif(m_pressed and not keyboard.is_pressed('m')):
                m_pressed = False
            last_input = time.time()
    
        #Check for new notes to place
        if(time.time() - last_note > note_period):
            if(note_counter < mychart.chart_len):
                upcoming_notes = mychart.get_notes(note_counter+1)
                if(upcoming_notes != "-"):
                    for note in upcoming_notes:
                        drawList.append(note)
                        note.status = time.time()
            note_counter = note_counter + 1
            last_note = time.time()
    
        #Clean up the screen
        main_screen.fill(WHITE)
        score_text = font.render(str(my_score), True, BLACK)
        main_screen.blit(score_text, [0,0])
        for note in drawList:
            #Remove expired notes
            if(time.time() - note.status < note_period):
                #Animate active notes
                time_since_start = time.time() - note.status
                time_since_start = round(time_since_start, 2)*(1.0/note_period)
                note.radius = int(30*time_since_start)
            if(time.time() - note.status < note_period*2):
                note_pos = note.pos_start.split("-")
                color = RED if note.button == "A" else YELLOW if note.button == "B" else GREEN if note.button == "C" else BLUE
                pygame.draw.circle(main_screen, BLACK, [int(note_pos[0]), 500 - int(note_pos[1])], 32)
                pygame.draw.circle(main_screen, WHITE, [int(note_pos[0]), 500 - int(note_pos[1])], 30)
                pygame.draw.circle(main_screen, color, [int(note_pos[0]), 500 - int(note_pos[1])], note.radius)
                text = font.render(note.button, True, BLACK)
                main_screen.blit(text, [int(note_pos[0])-8,500-int(note_pos[1])-8])
            else:
                note.status = 0
                drawList.remove(note)
        pygame.display.flip() ##refresh the display each time through the main loop?

def resultsScreen():
    #pass song, score, etc to this func

while not done:
    for event in pygame.event.get(): #Pygame events are only used for handling window close
        if event.type == pygame.QUIT:
            done = True

    if(windowSwitch == 1):
        windowSwitch = 0
        mainWindow()
        windowSwitch = 2
    if(windowSwitch == 2):
        windowSwitch = 0
        songWindow()
        windowSwitch = 1

pygame.quit()
