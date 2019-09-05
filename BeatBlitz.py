import time, keyboard, pygame, os
from rhythm import *

screen_size = (600,600)
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GRAY     = ( 186, 186, 186)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
YELLOW   = ( 255, 255,   0)
LIGHT_BLUE = ( 0, 255, 255)
ORANGE   = ( 255, 100,   0)

a_key = 'z'
b_key = 'x'
c_key = 'n'
d_key = 'm'

song_delay = 0

pygame.init()
pygame.mixer.init()

main_screen = pygame.display.set_mode(screen_size)
font = pygame.font.SysFont('Calibri', 18, True, False)
done = False
windowSwitch = 1

def mainWindow(contextDict):
    print("main window called")
    time.sleep(0.2)
    done = False
    retDict = {}
    main_screen.fill(WHITE)
    titleScreen = pygame.image.load('./Resources/TitleScreen.png')
    main_screen.blit(titleScreen, [0,0])
    pygame.draw.rect(main_screen, BLUE, [100,420,150,40])
    play_text = font.render("Play", True, BLACK)
    main_screen.blit(play_text, [175-int(play_text.get_rect().width/2),430])
    pygame.draw.rect(main_screen, BLUE, [350,420,150,40])
    option_text = font.render("Options", True, BLACK)
    main_screen.blit(option_text, [425-int(option_text.get_rect().width/2),430])
    pygame.display.flip()
    
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

        if(pygame.mouse.get_pos()[0] > 100 and pygame.mouse.get_pos()[0] < 250 and pygame.mouse.get_pos()[1] > 420 and pygame.mouse.get_pos()[1] < 460):
            pygame.draw.rect(main_screen, RED, [100,420,150,40])
            if(pygame.mouse.get_pressed()[0]):
                retDict['next'] = 5
                done = True
        else:
            pygame.draw.rect(main_screen, BLUE, [100,420,150,40])

        if(pygame.mouse.get_pos()[0] > 350 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 420 and pygame.mouse.get_pos()[1] < 460):
            pygame.draw.rect(main_screen, RED, [350,420,150,40])
            if(pygame.mouse.get_pressed()[0]):
                retDict['next'] = 4
                done = True
        else:
            pygame.draw.rect(main_screen, BLUE, [350,420,150,40])

        main_screen.blit(play_text, [175-int(play_text.get_rect().width/2),430])
        main_screen.blit(option_text, [425-int(option_text.get_rect().width/2),430])
        pygame.display.flip()

    return retDict

def optionsWindow(contextDict):
    print("options window called")
    time.sleep(0.2)
    done = False

    click_pressed = False

    a_selected = False
    b_selected = False
    c_selected = False
    d_selected = False

    global song_delay
    global a_key
    global b_key
    global c_key
    global d_key

    main_screen.fill(WHITE)
    options_text = font.render("Options", True, BLACK)
    A_text = font.render("A", True, BLACK)
    B_text = font.render("B", True, BLACK)
    C_text = font.render("C", True, BLACK)
    D_text = font.render("D", True, BLACK)
    akey_text = font.render(str(a_key), True, BLACK)
    bkey_text = font.render(str(b_key), True, BLACK)
    ckey_text = font.render(str(c_key), True, BLACK)
    dkey_text = font.render(str(d_key), True, BLACK)
    delay_text = font.render("Song delay", True, BLACK)
    delay_value_text = font.render(str(song_delay) + "ms", True, BLACK)
    minus_text = font.render("-", True, BLACK)
    plus_text = font.render("+", True, BLACK)
    ok_text = font.render("OK", True, BLACK)
    main_screen.blit(options_text, [300-int(options_text.get_rect().width/2), 20])
    main_screen.blit(A_text, [75-int(A_text.get_rect().width/2), 100])
    main_screen.blit(B_text, [225-int(B_text.get_rect().width/2), 100])
    main_screen.blit(C_text, [375-int(C_text.get_rect().width/2), 100])
    main_screen.blit(D_text, [525-int(D_text.get_rect().width/2), 100])
    pygame.draw.rect(main_screen, BLUE, [50,120,50,50])
    pygame.draw.rect(main_screen, BLUE, [200,120,50,50])
    pygame.draw.rect(main_screen, BLUE, [350,120,50,50])
    pygame.draw.rect(main_screen, BLUE, [500,120,50,50])
    main_screen.blit(akey_text, [75-int(akey_text.get_rect().width/2), 145-int(akey_text.get_rect().height/2)])
    main_screen.blit(bkey_text, [225-int(bkey_text.get_rect().width/2), 145-int(bkey_text.get_rect().height/2)])
    main_screen.blit(ckey_text, [375-int(ckey_text.get_rect().width/2), 145-int(ckey_text.get_rect().height/2)])
    main_screen.blit(dkey_text, [525-int(dkey_text.get_rect().width/2), 145-int(dkey_text.get_rect().height/2)])
    main_screen.blit(delay_text, [300-int(delay_text.get_rect().width/2), 300])
    pygame.draw.rect(main_screen, BLUE, [275,350,50,50])
    main_screen.blit(delay_value_text, [300-int(delay_value_text.get_rect().width/2), 375-int(delay_value_text.get_rect().height/2)])
    pygame.draw.rect(main_screen, BLUE, [240,360,30,30])
    main_screen.blit(minus_text, [255-int(minus_text.get_rect().width/2), 375-int(minus_text.get_rect().height/2)])
    pygame.draw.rect(main_screen, BLUE, [330,360,30,30])
    main_screen.blit(plus_text, [345-int(plus_text.get_rect().width/2), 375-int(plus_text.get_rect().height/2)])
    pygame.draw.rect(main_screen, BLUE, [225,500,150,50])
    main_screen.blit(ok_text, [300-int(ok_text.get_rect().width/2),525-int(ok_text.get_rect().height/2)])
    pygame.display.flip()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

            if(pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 100 and pygame.mouse.get_pos()[1] > 120 and pygame.mouse.get_pos()[1] < 170):
                if(not a_selected and not click_pressed and pygame.mouse.get_pressed()[0]):
                    click_pressed = True
                    a_selected = True
                    b_selected = False
                    c_selected = False
                    d_selected = False
                else:
                    click_pressed = False

            if(a_selected):
                pygame.draw.rect(main_screen, RED, [50,120,50,50])
                
            else:
                pygame.draw.rect(main_screen, BLUE, [50,120,50,50])

            if(pygame.mouse.get_pos()[0] > 200 and pygame.mouse.get_pos()[0] < 250 and pygame.mouse.get_pos()[1] > 120 and pygame.mouse.get_pos()[1] < 170):
                if(not b_selected and not click_pressed and pygame.mouse.get_pressed()[0]):
                    click_pressed = True
                    b_selected = True
                    a_selected = False
                    c_selected = False
                    d_selected = False
                else:
                    click_pressed = False

            if(b_selected):
                pygame.draw.rect(main_screen, RED, [200,120,50,50])
            else:
                pygame.draw.rect(main_screen, BLUE, [200,120,50,50])

            if(pygame.mouse.get_pos()[0] > 350 and pygame.mouse.get_pos()[0] < 400 and pygame.mouse.get_pos()[1] > 120 and pygame.mouse.get_pos()[1] < 170):
                if(not c_selected and not click_pressed and pygame.mouse.get_pressed()[0]):
                    click_pressed = True
                    c_selected = True
                    a_selected = False
                    b_selected = False
                    d_selected = False
                else:
                    click_pressed = False

            if(c_selected):
                pygame.draw.rect(main_screen, RED, [350,120,50,50])
            else:
                pygame.draw.rect(main_screen, BLUE, [350,120,50,50])

            if(pygame.mouse.get_pos()[0] > 500 and pygame.mouse.get_pos()[0] < 550 and pygame.mouse.get_pos()[1] > 120 and pygame.mouse.get_pos()[1] < 170):
                if(not d_selected and not click_pressed and pygame.mouse.get_pressed()[0]):
                    click_pressed = True
                    d_selected = True
                    a_selected = False
                    b_selected = False
                    c_selected = False
                else:
                    click_pressed = False

            if(d_selected):
                pygame.draw.rect(main_screen, RED, [500,120,50,50])
            else:
                pygame.draw.rect(main_screen, BLUE, [500,120,50,50])
                

            if(pygame.mouse.get_pos()[0] > 240 and pygame.mouse.get_pos()[0] < 270 and pygame.mouse.get_pos()[1] > 360 and pygame.mouse.get_pos()[1] < 390):
                pygame.draw.rect(main_screen, RED, [240,360,30,30])
                if(not click_pressed and pygame.mouse.get_pressed()[0]):
                    click_pressed = True
                    song_delay = song_delay - 1
                else:
                    click_pressed = False
            else:
                pygame.draw.rect(main_screen, BLUE, [240,360,30,30])

            if(pygame.mouse.get_pos()[0] > 330 and pygame.mouse.get_pos()[0] < 360 and pygame.mouse.get_pos()[1] > 360 and pygame.mouse.get_pos()[1] < 390):
                pygame.draw.rect(main_screen, RED, [330,360,30,30])
                if(not click_pressed and pygame.mouse.get_pressed()[0]):
                    click_pressed = True
                    song_delay = song_delay + 1
                else:
                    click_pressed = False
            else:
                pygame.draw.rect(main_screen, BLUE, [330,360,30,30])

            if(pygame.mouse.get_pos()[0] > 225 and pygame.mouse.get_pos()[0] < 375 and pygame.mouse.get_pos()[1] > 500 and pygame.mouse.get_pos()[1] < 550):
                pygame.draw.rect(main_screen, RED, [225,500,150,50])
                if(pygame.mouse.get_pressed()[0]):
                    done = True
            else:
                pygame.draw.rect(main_screen, BLUE, [225,500,150,50])

            main_screen.blit(options_text, [300-int(options_text.get_rect().width/2), 20])
            main_screen.blit(A_text, [75-int(A_text.get_rect().width/2), 100])
            main_screen.blit(B_text, [225-int(B_text.get_rect().width/2), 100])
            main_screen.blit(C_text, [375-int(C_text.get_rect().width/2), 100])
            main_screen.blit(D_text, [525-int(D_text.get_rect().width/2), 100])
            main_screen.blit(akey_text, [75-int(akey_text.get_rect().width/2), 145-int(akey_text.get_rect().height/2)])
            main_screen.blit(bkey_text, [225-int(bkey_text.get_rect().width/2), 145-int(bkey_text.get_rect().height/2)])
            main_screen.blit(ckey_text, [375-int(ckey_text.get_rect().width/2), 145-int(ckey_text.get_rect().height/2)])
            main_screen.blit(dkey_text, [525-int(dkey_text.get_rect().width/2), 145-int(dkey_text.get_rect().height/2)])
            main_screen.blit(delay_text, [300-int(delay_text.get_rect().width/2), 300])
            pygame.draw.rect(main_screen, BLUE, [275,350,50,50])
            delay_value_text = font.render(str(song_delay) + "ms", True, BLACK)
            main_screen.blit(delay_value_text, [300-int(delay_value_text.get_rect().width/2), 375-int(delay_value_text.get_rect().height/2)])
            main_screen.blit(minus_text, [255-int(minus_text.get_rect().width/2), 375-int(minus_text.get_rect().height/2)])
            main_screen.blit(plus_text, [345-int(plus_text.get_rect().width/2), 375-int(plus_text.get_rect().height/2)])
            main_screen.blit(ok_text, [300-int(ok_text.get_rect().width/2),525-int(ok_text.get_rect().height/2)])
            pygame.display.flip()        

    return {}

def songSelectWindow(contextDict):
    song_list = []
    for d in os.listdir('./Resources/Songs/'):
        song_dict = {}
        song_dict['title'] = d
        with open('./Resources/Songs/'+d+'/conf.txt', 'r') as f:
            length = int(f.readline().rstrip('\n'))
            song_dict['seconds'] = length
            song_dict['length'] = str(int(length/60)) + ":" + str("{:02d}".format(length%60))
            song_dict['bpm'] = f.readline().rstrip('\n')
        song_list.append(song_dict)
        
    done = False
    current = 0
    prev = current - 1 if current >= 0 else len(song_list) - 1
    post = current + 1 if current < len(song_list) - 1 else 0
    up_pressed = 0
    down_pressed = 0
    enter_pressed = 0

    main_screen.fill(WHITE)
    select_text = font.render("Song Select", True, BLACK)
    current_text = font.render(str(song_list[current]['title']) + " - " + str(song_list[current]['length']) + " - " + str(song_list[current]['bpm']) + "BPM", True, BLACK)
    prev_text = font.render(str(song_list[prev]['title']) + " - " + str(song_list[prev]['length']) + " - " + str(song_list[prev]['bpm']) + "BPM", True, BLACK)
    post_text = font.render(str(song_list[post]['title']) + " - " + str(song_list[post]['length']) + " - " + str(song_list[post]['bpm']) + "BPM", True, BLACK)
    cont_text = font.render("Press [Enter] to select", True, BLACK)
    main_screen.blit(select_text, [300-int(select_text.get_rect().width/2),20])
    pygame.draw.rect(main_screen, GRAY, [50,260,500,80])
    main_screen.blit(current_text, [300-int(current_text.get_rect().width/2),300-int(current_text.get_rect().height/2)])
    pygame.draw.rect(main_screen, GRAY, [100,110,400,50])
    main_screen.blit(prev_text, [300-int(prev_text.get_rect().width/2),135-int(current_text.get_rect().height/2)])
    pygame.draw.rect(main_screen, GRAY, [100,460,400,50])
    main_screen.blit(post_text, [300-int(post_text.get_rect().width/2), 485-int(current_text.get_rect().height/2)])
    main_screen.blit(cont_text, [300-int(cont_text.get_rect().width/2),580])
    pygame.draw.polygon(main_screen, BLACK, [(290,70),(310,70),(300,50)])
    pygame.draw.polygon(main_screen, BLACK, [(290,550),(310,550),(300,570)])
    pygame.display.flip()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

        if(not up_pressed and keyboard.is_pressed('up')):
            current = current - 1 if current >= 0 else len(song_list) - 1
            prev = current - 1 if current >= 0 else len(song_list) - 1
            post = current + 1 if current < len(song_list) - 1 else 0
            up_pressed = True
        elif(up_pressed and not keyboard.is_pressed('up')):
            up_pressed = False

        if(not down_pressed and keyboard.is_pressed('down')):
            current = current +1 if current < len(song_list) - 1 else 0
            prev = current - 1 if current >= 0 else len(song_list) - 1
            post = current + 1 if current < len(song_list) - 1 else 0
            down_pressed = True
        elif(down_pressed and not keyboard.is_pressed('down')):
            down_pressed = False

        if(not enter_pressed and keyboard.is_pressed('enter')):
            done = True

        main_screen.fill(WHITE)
        select_text = font.render("Song Select", True, BLACK)
        current_text = font.render(str(song_list[current]['title']) + " - " + str(song_list[current]['length']) + " - " + str(song_list[current]['bpm']) + "BPM", True, BLACK)
        prev_text = font.render(str(song_list[prev]['title']) + " - " + str(song_list[prev]['length']) + " - " + str(song_list[prev]['bpm']) + "BPM", True, BLACK)
        post_text = font.render(str(song_list[post]['title']) + " - " + str(song_list[post]['length']) + " - " + str(song_list[post]['bpm']) + "BPM", True, BLACK)
        cont_text = font.render("Press [Enter] to select", True, BLACK)
        main_screen.blit(select_text, [300-int(select_text.get_rect().width/2),20])
        pygame.draw.rect(main_screen, GRAY, [50,260,500,80])
        main_screen.blit(current_text, [300-int(current_text.get_rect().width/2),300-int(current_text.get_rect().height/2)])
        pygame.draw.rect(main_screen, GRAY, [100,110,400,50])
        main_screen.blit(prev_text, [300-int(prev_text.get_rect().width/2),135-int(current_text.get_rect().height/2)])
        pygame.draw.rect(main_screen, GRAY, [100,460,400,50])
        main_screen.blit(post_text, [300-int(post_text.get_rect().width/2), 485-int(current_text.get_rect().height/2)])
        main_screen.blit(cont_text, [300-int(cont_text.get_rect().width/2),580])
        pygame.draw.polygon(main_screen, BLACK, [(290,70),(310,70),(300,50)])
        pygame.draw.polygon(main_screen, BLACK, [(290,550),(310,550),(300,570)])
        pygame.display.flip()

    return {'song':song_list[current]}

def songWindow(contextDict):
    print("song window called")
    mychart = Chart("./Resources/Songs/"+str(contextDict['song']['title'])+"/"+str(contextDict['song']['title'])+".txt", contextDict['song']['bpm'])
    mysong = Song(str(contextDict['song']['title']), "./Resources/Songs/"+str(contextDict['song']['title'])+"/"+str(contextDict['song']['title'])+".mp3", contextDict['song']['seconds'], contextDict['song']['bpm'], mychart)

    global song_delay
    
    note_period = (1.0/(float(mychart.bpm)/60.0)/4.0)
    note_counter = -1
    my_score = 0
    total_notes_hit = 0
    current_combo = 0
    max_combo = 0

    a_pressed = False
    b_pressed = False
    c_pressed = False
    d_pressed = False
    input_period = 0.001
    
    main_screen.fill(WHITE)
    score_text = font.render(str(my_score), True, BLACK)
    main_screen.blit(score_text, [0,0])
    combo_text = font.render(str(current_combo)+" Combo", True, BLACK)
    main_screen.blit(combo_text, [500,0])
    pygame.display.flip()
    
    drawList = []
    resultDrawList = []

    song_started = False
    pygame.mixer.music.load(mysong.filepath)
    if(song_delay <= 0):
        pygame.mixer.music.play()
        song_started = True
    time.sleep(0.01*song_delay)
    start_time = time.time()
    last_note = time.time()
    last_input = time.time()
    while(time.time() - start_time <= mysong.song_length):
        for event in pygame.event.get(): #Pygame events are only used for handling window close, but without this code here the pygame window will crash
            if event.type == pygame.QUIT:
                pygame.quit()

        if(not song_started and round(time.time() - start_time,2) == 0.01*song_delay):
            pygame.mixer.music.play()
            song_started = True
                
        if(len(drawList) > 0 and time.time() - last_input > input_period):
            print("Input poll: " + str(time.time() - start_time))
            #POLL FOR Z
            if(len(drawList) > 0 and not a_pressed and keyboard.is_pressed(a_key)):
                print("A pressed!")
                a_pressed = True
                note = drawList[0]
                front_time = note.status
                for n in drawList:
                    if(round(n.status,2) == round(note.status, 2) and n.button == 'A'):
                        note = n
                        break
                if(note.button == 'A' and note.status != 0 and note.radius > 0 and time.time() - note.status < note_period*5 and time.time() - note.status > note_period*2):
                    print("A note hit!")
                    total_notes_hit = total_notes_hit + 1
                    current_combo = current_combo + 1
                    max_combo = current_combo if current_combo > max_combo else max_combo
                    my_score = my_score + int(200 * abs(round(time.time() - (note.status + note_period), 2)) * (1.0/note_period))
                    drawList.remove(note)
                    note.status = 0
                    note.radius = 0
                    resultDrawList.append(Result('H',time.time(),note.pos_x,note.pos_y))
                elif(note.button != 'A' and note.status != 0 and time.time() - note.status < note_period*5 and time.time() - note.status > note_period*2):
                    resultDrawList.append(Result('M',time.time(),note.pos_x,note.pos_y))
                    current_combo = 0
                    note.status = 0
                    note.radius = 0
                    drawList.remove(note)
            elif(a_pressed and not keyboard.is_pressed(a_key)): #debounce input
                a_pressed = False
                
            #POLL FOR X
            if(len(drawList) > 0 and not b_pressed and keyboard.is_pressed(b_key)):
                print("B pressed!")
                b_pressed = True
                note = drawList[0]
                front_time = note.status
                for n in drawList:
                    if(round(n.status,2) == round(note.status, 2) and n.button == 'B'):
                        note = n
                        break
                if(note.button == 'B' and note.status != 0 and note.radius > 0 and time.time() - note.status < note_period*5 and time.time() - note.status > note_period*2):
                    print("B note hit!")
                    total_notes_hit = total_notes_hit + 1
                    current_combo = current_combo + 1
                    max_combo = current_combo if current_combo > max_combo else max_combo
                    my_score = my_score + int(200 * abs(round(time.time() - (note.status + note_period), 2)) * (1.0/note_period))
                    drawList.remove(note)
                    note.status = 0
                    note.radius = 0
                    resultDrawList.append(Result('H',time.time(),note.pos_x,note.pos_y))
                elif(note.button != 'B' and note.status != 0 and time.time() - note.status < note_period*5 and time.time() - note.status > note_period*2):
                    resultDrawList.append(Result('M',time.time(),note.pos_x,note.pos_y))
                    current_combo = 0
                    note.status = 0
                    note.radius = 0
                    drawList.remove(note)
            elif(b_pressed and not keyboard.is_pressed(b_key)):
                b_pressed = False
    
            #POLL FOR N
            if(len(drawList) > 0 and not c_pressed and keyboard.is_pressed(c_key)):
                print("C pressed!")
                c_pressed = True
                note = drawList[0]
                front_time = note.status
                for n in drawList:
                    if(round(n.status,2) == round(note.status, 2) and n.button == 'C'):
                        note = n
                        break
                if(note.button == 'C' and note.status != 0 and note.radius > 0 and time.time() - note.status < note_period*5 and time.time() - note.status > note_period*2):
                    print("C note hit!")
                    total_notes_hit = total_notes_hit + 1
                    current_combo = current_combo + 1
                    max_combo = current_combo if current_combo > max_combo else max_combo
                    my_score = my_score + int(200 * abs(round(time.time() - (note.status + note_period), 2)) * (1.0/note_period))
                    drawList.remove(note)
                    note.status = 0
                    note.radius = 0
                    resultDrawList.append(Result('H',time.time(),note.pos_x,note.pos_y))
                elif(note.button != 'C' and note.status != 0 and time.time() - note.status < note_period*5 and time.time() - note.status > note_period*2):
                    resultDrawList.append(Result('M',time.time(),note.pos_x,note.pos_y))
                    current_combo = 0
                    note.status = 0
                    note.radius = 0
                    drawList.remove(note)
            elif(c_pressed and not keyboard.is_pressed(c_key)):
                c_pressed = False

            #POLL FOR M
            if(len(drawList) > 0 and not d_pressed and keyboard.is_pressed(d_key)):
                print("D pressed!")
                d_pressed = True
                note = drawList[0]
                front_time = note.status
                for n in drawList:
                    if(round(n.status,2) == round(note.status, 2) and n.button == 'D'):
                        note = n
                        break
                if(note.button == 'D' and note.status != 0 and note.radius > 0 and time.time() - note.status < note_period*5 and time.time() - note.status > note_period*2):
                    print("D note hit!")
                    total_notes_hit = total_notes_hit + 1
                    current_combo = current_combo + 1
                    max_combo = current_combo if current_combo > max_combo else max_combo
                    my_score = my_score + int(200 * abs(round(time.time() - (note.status + note_period), 2)) * (1.0/note_period))
                    drawList.remove(note)
                    note.status = 0
                    note.radius = 0
                    resultDrawList.append(Result('H',time.time(),note.pos_x,note.pos_y))
                elif(note.button != 'D' and note.status != 0 and time.time() - note.status < note_period*5 and time.time() - note.status > note_period*2):
                    resultDrawList.append(Result('M',time.time(),note.pos_x,note.pos_y))
                    current_combo = 0
                    note.status = 0
                    note.radius = 0
                    drawList.remove(note)
            elif(d_pressed and not keyboard.is_pressed(d_key)):
                d_pressed = False
            last_input = time.time()
    
        #Check for new notes to place
        if(time.time() - last_note > note_period):
            print("Note update: " + str(time.time() - start_time))
            if(note_counter+2 < mychart.chart_len):
                upcoming_notes = mychart.get_notes(note_counter+3)
                if(upcoming_notes != "-"):
                    for note in upcoming_notes:
                        drawList.append(note)
                        note.status = time.time()
            note_counter = note_counter + 1
            last_note = time.time()
    
        #Clean up the screen
        print("Screen update: " + str(time.time() - start_time))
        main_screen.fill(WHITE)
        score_text = font.render(str(my_score), True, BLACK)
        main_screen.blit(score_text, [0,0])
        combo_text = font.render(str(current_combo)+" Combo", True, BLACK)
        main_screen.blit(combo_text, [500,0])
        pygame.draw.rect(main_screen, BLACK, [0,580,600,20])
        pygame.draw.rect(main_screen, GREEN, [0,580,int(600*((time.time()-start_time)/mysong.song_length)),20])
        for note in drawList:
            if(time.time() - note.status < note_period*4):
                #Animate active notes
                time_since_start = time.time() - note.status
                time_since_start = round(time_since_start, 2)/(4.0*note_period)
                note.radius = int(30*time_since_start)
            if(time.time() - note.status < note_period*5):
                color = RED if note.button == "A" else YELLOW if note.button == "B" else GREEN if note.button == "C" else BLUE
                pygame.draw.circle(main_screen, BLACK, [note.pos_x, 600 - note.pos_y], 32)
                pygame.draw.circle(main_screen, WHITE, [note.pos_x, 600 - note.pos_y], 30)
                pygame.draw.circle(main_screen, color, [note.pos_x, 600 - note.pos_y], note.radius)
                text = font.render(note.button, True, BLACK)
                main_screen.blit(text, [note.pos_x-8,600-note.pos_y-8])
            #Remove expired notes
            else:
                resultDrawList.append(Result('M',time.time(),note.pos_x,note.pos_y))
                current_combo = 0
                note.status = 0
                note.radius = 0
                drawList.remove(note)
        for result in resultDrawList:
            if(time.time() - result.status <= 0.2): #arbitrary timeout, maybe adjust?
                color = LIGHT_BLUE if result.result == 'H' else ORANGE
                pygame.draw.circle(main_screen, color, [result.pos_x, 600 - result.pos_y], 32)
            else:
                result.status = 0
                resultDrawList.remove(result)
        pygame.display.flip() ##refresh the display each time through the main loop?
    pygame.mixer.music.stop()
    return {'song':mysong,'score':my_score,'notes_hit':total_notes_hit,'max_combo':max_combo}

def resultsWindow(contextDict):
    print("results window called")
    done = False
    main_screen.fill(WHITE)
    title_text = font.render(str(contextDict['song'].title), True, BLACK)
    main_screen.blit(title_text, [300-int(title_text.get_rect().width/2),50])
    banner = pygame.image.load('./Resources/Songs/'+str(contextDict['song'].title)+'/'+str(contextDict['song'].title)+'.jpg')
    main_screen.blit(banner, [300 - int(banner.get_rect().width/2),100])
    score_text = font.render("Total score: " + str(contextDict['score']), True, BLACK)
    main_screen.blit(score_text, [300-int(score_text.get_rect().width/2),300])
    notes_text = font.render("Notes hit: " + str(contextDict['notes_hit']) +"/" + str(contextDict['song'].chart.notes), True, BLACK)
    main_screen.blit(notes_text, [300-int(notes_text.get_rect().width/2),350])
    combo_text = font.render("Max combo: " + str(contextDict['max_combo']), True, BLACK)
    main_screen.blit(combo_text, [300-int(combo_text.get_rect().width/2),400])
    continue_text = font.render("Click anywhere to continue", True, BLACK)
    main_screen.blit(continue_text, [300-int(continue_text.get_rect().width/2),500])
    pygame.display.flip()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()

        if(pygame.mouse.get_pressed()[0]):
            done = True
                
    return {}

#main while loop, context switching
while not done:
    for event in pygame.event.get(): #Pygame events are only used for handling window close
        if event.type == pygame.QUIT:
            done = True

    contextDict = {}

    if(windowSwitch == 1):
        windowSwitch = 0
        contextDict = mainWindow(contextDict)
        print(str(contextDict))
        windowSwitch = contextDict['next']
    if(windowSwitch == 5):
        windowSwitch = 0
        contextDict = songSelectWindow(contextDict)
        print(str(contextDict))
        windowSwitch = 2
    if(windowSwitch == 2):
        windowSwitch = 0
        contextDict = songWindow(contextDict)
        print(str(contextDict))
        windowSwitch = 3
    if(windowSwitch == 3):
        windowSwitch = 0
        contextDict = resultsWindow(contextDict)
        print(str(contextDict))
        windowSwitch = 1
    if(windowSwitch == 4):
        windowSwitch = 0
        contextDict = optionsWindow(contextDict)
        print(str(contextDict))
        windowSwitch = 1

pygame.quit()
