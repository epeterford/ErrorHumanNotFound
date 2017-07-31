#init python:
#    #Create an empty list
#    $ my_list = []
#    #gives a number of tiles to use for loop
#    $ number_of_tiles = 8
#    #first tile x value to use for incrementing 
#    $ p = 900
#    #number that determines number of tiles in a row (see inner if statement)
#    $ n=0
#    #first tile y value for tiles 
#    $ o = 350
#    #puts x and y value into set for the list appending
#    m = (p,o)
#    #adds set to list
#    my_list.append(m)
#    #loop value for generating tile space
#    q=0
#    while (number_of_tiles - 1 > q):
#        #increment value for x increase for wider gap decrease for narrower
#        p +=150
#        #increments the column value
#        n += 1
#        # the value you set n equal to will determine the ammount of columns
#        if (n==4):
#            #set as new y value for second row can be entered to give more rows
#            o += 150
#            #resets x value for tile placement in new row change to same value above of the x firts tile
#            p = 900
#            #resets n so that new  rows will be able to be made
#            n= 0
#            #adds iteration to loop
#            q +=1
#            #takes new values and puts them in list
#            m = (p,o)
#            my_list.append(m)
#        #puts starting list in new format
#        x = list(my_list)
#        #shuffles values to randomize values
#        renpy.random.shuffle(x)
    
#    class BinaryMatch:


#screen binaryMatching_scr: 
#    image button:
#        xpos
#        ypos
#        idle
        
#label binaryMatchEasy:
#    $renpy.block_rollback()
#    $quick_menu = False

#    #loads background
#    scene bg binary
#    #loads tiles to value tags to be utilized
#    image BLANK = ('tileBack.png')
#    image ONE = ('tileFront0.png')
#    image ONEB = ('tileFront00.png')
#    image TWO = ('tileFront1.png')
#    image TWOB = ('tileFront01.png')
#    image THREE = ('tileFront2.png')
#    image THREEB = ('tileFront10.png')
#    image FOUR = ('tileFront3.png')
#    image FOURB = ('tileFront11.png')
#    image LIGHTOFF =('LightOff.png')
#    image LIGHTON = ('LightOn.png')
    
#    $ winner = True
#    show BLANK at 
#    show BLANK as BLANK1 at
#    show BLANK as BLANK2 at
#    show BLANK as BLANK3 at
#    show BLANK as BLANK4 at
#    show BLANK as BLANK5 at
#    show BLANK as BLANK6 at
#    show BLANK as BLANK7 at
#    #loads in images and assigns them to new image vairiables to be used
##    blank =pygame.image.load(BLANK).convert_alpha()
##    onenum =pygame.image.load(ONE).convert_alpha()
##    onebin =pygame.image.load(ONEB).convert_alpha()
##    twonum =pygame.image.load(TWO).convert_alpha()
##    twobin=pygame.image.load(TWOB).convert_alpha()
##    threenum=pygame.image.load(THREE).convert_alpha()
##    threebin=pygame.image.load(THREEB).convert_alpha()
##    fournum=pygame.image.load(FOUR).convert_alpha()
##    fourbin=pygame.image.load(FOURB).convert_alpha()
##    lightOn=pygame.image.load(LIGHTON).convert_alpha()
##    lightOff=pygame.image.load(LIGHT).convert_alpha()
##    lightWrong =pygame.image.load(LIGHTOFF).convert_alpha()
##    lightOff2=pygame.image.load(LIGHTRED).convert_alpha()
    
##    #gets mouse values
##    mousex = 0 # used to store x coordinate of mouse event
##    mousey = 0 # used to store y coordinate of mouse event
    
##    #each screen.blit adds an image to the screen for the user to see
##    screen.blit(background,(0,0))
##    screen.blit(lightOn,(130, 900))
##    screen.blit(lightWrong,(300,900))
##    screen.blit(lightOff,(130, 900))
##    screen.blit(lightOff2, (300, 900))
##    screen.blit(onenum,x[0]) 
##    screen.blit(onebin,x[1])
##    screen.blit(twonum,x[2])  
##    screen.blit(twobin,x[3])  
##    screen.blit(threenum,x[4])  
##    screen.blit(threebin,x[5])  
##    screen.blit(fournum,x[6])  
##    screen.blit(fourbin,x[7])
        
##    #adds the blank tiles on top of the numbers
##    screen.blit(blank,x[0])  
##    screen.blit(blank,x[1])
##    screen.blit(blank,x[2])  
##    screen.blit(blank,x[3])  
##    screen.blit(blank,x[4])  
##    screen.blit(blank,x[5])  
##    screen.blit(blank,x[6])  
##    screen.blit(blank,x[7])


#    #gives a list of unzipped values for the x and y to be used for individual placement
#    $ y = x
#    $ posa, posb = renpy.zip(*y)
    
##    #takes unzipped values to make clickable rectangles on the images the 100's are pixel size
##    onenpos = Rect(posa[0], posb[0], 100, 100)
##    onebpos = Rect(posa[1], posb[1], 100, 100)     
##    twonpos = Rect(posa[2], posb[2], 100, 100)     
##    twobpos = Rect(posa[3], posb[3], 100, 100)     
##    threenpos = Rect(posa[4], posb[4], 100, 100)     
##    threebpos = Rect(posa[5], posb[5], 100, 100)     
##    fournpos = Rect(posa[6], posb[6], 100, 100)     
##    fourbpos = Rect(posa[7], posb[7], 100, 100)
    
#    #adds boolean for each tile if they have been clicked or not 
#    oneClick = True
#    onebClick = True
#    twoClick = True
#    twobClick = True
#    threeClick = True
#    threebClick = True
#    fourClick = True
#    fourbClick = True
    
#    #sets the light to off
#    lightactive = False
#    #counter for the tiles to determine if two have been clicked
#    click_counter = 0
#    #sets the miss bool 
#    miss = False
#    #user events list to hold clicked values
#    clickL= list()
        
#    #The current place for instructions. This will be replaced with a png later
#    instructions = myfont.render('Match the binary numbers', True, (235,255,255))
#    instruct2 = myfont.render( 'with their corresponding', True, (235, 255, 255))
#    instruct3 = myfont.render ('integer value.',True,(235,255,255))
#    screen.blit(instructions, (200,370))
#    screen.blit(instruct2,(200,400))
#    screen.blit(instruct3,(200, 430))

#    #loop to run game while the player hasnt expended all attempts
#    while (ATTEMPTS>=0):
#        # clear/erase the last drawn sprites
#        all.clear(screen, background)

#        #update all the sprites
#        all.update()

#        #draw the scene
#        dirty = all.draw(screen)
#        pygame.display.update(dirty) 
#        if (lightactive == True):
#            time.sleep(.2)
#            screen.blit(lightOff,(130, 900))
#            screen.blit(lightOff2, (300, 900))
#        #checks to see if an event has happened
#        for event in pygame.event.get():
#            if event.type == QUIT:
#                pygame.quit()
#                sys.exit()
#            elif ATTEMPTS == 0 :
#                sys.exit()                
#            elif event.type == MOUSEMOTION:
#                mousex, mousey = event.pos
#            elif event.type == MOUSEBUTTONUP:
#                mouse_pos = event.pos
#                mousex, mousey = event.pos
#                mouseClicked = True
#                #after a mouse event has happened checks to see if a image was clicked
#                if onenpos.collidepoint(mouse_pos):
#                    if (oneClick == True):
#                        clickL.append(1)
#                        click_counter +=1
#                        oneClick = False
#                        screen.blit(onenum,x[0]) 
#                if onebpos.collidepoint(mouse_pos):
#                    if (onebClick == True):
#                        clickL.append(1)
#                        click_counter +=1
#                        onebClick = False
#                        screen.blit(onebin,x[1])
#                if twonpos.collidepoint(mouse_pos):
#                    if (twoClick == True):
#                        clickL.append(2)
#                        click_counter +=1
#                        twoClick = False
#                        screen.blit(twonum,x[2]) 
#                if twobpos.collidepoint(mouse_pos):
#                    if (twobClick == True):
#                        clickL.append(2)
#                        click_counter +=1
#                        twobClick = False
#                        screen.blit(twobin,x[3])
#                if threenpos.collidepoint(mouse_pos):
#                    if (threeClick == True):
#                        clickL.append(3)
#                        click_counter +=1
#                        threeClick = False
#                        screen.blit(threenum,x[4]) 
#                if threebpos.collidepoint(mouse_pos):
#                    if (threebClick == True):
#                        clickL.append(3)
#                        click_counter +=1
#                        threebClick = False
#                        screen.blit(threebin,x[5])
#                if fournpos.collidepoint(mouse_pos):
#                    if (fourClick == True):
#                        clickL.append(4)
#                        click_counter +=1
#                        fourClick = False
#                        screen.blit(fournum,x[6]) 
#                if fourbpos.collidepoint(mouse_pos):
#                    if (fourbClick == True):
#                        clickL.append(4)
#                        click_counter +=1
#                        fourbClick = False
#                        screen.blit(fourbin,x[7])

#                pygame.display.update()
#            # after two images has been clicked enters   
#            if (click_counter == 2) :  
#                #if they matched then proceds to make the tiles unclickable for the remainder of the game
#                if (clickL[0] == clickL[1]):
#                    if (clickL[0] == 1):
#                        oneClick = False
#                        onebClick = False
#                    if (clickL[0]  == 2):
#                        twoClick = False
#                        twobClick = False
#                    if (clickL[0]  == 3):
#                        threeClick = False
#                        threebClick = False
#                    if (clickL[0]  == 4):
#                        fourClick = False
#                        fourbClick = False
#                    #adds score and removes attempt as well as flashes the green light and resets the list of player clicks
#                    SCORE += 1
#                    ATTEMPTS -= 1
#                    click_counter = 0
#                    del clickL[1]
#                    del clickL[0]
#                    screen.blit(lightOn,(130,900))
#                    time.sleep(.5)
#                    lightactive = True
#                #if the player clicked two wron tiles removes attempt and flashes red light
#                elif (clickL[0]  is not clickL[1] ):
#                    ATTEMPTS -= 1
#                    lightactive = True
#                    screen.blit(lightWrong,(300,900))
#                    time.sleep(.5)
#                    miss = True
#                    #after miss will reset the clickability of the tile and flips it back over
#                    if (miss == True):
#                        if (clickL[0] == 1 or clickL[1] == 1):
#                            oneClick = True
#                            onebClick = True
#                            screen.blit(blank,x[0])  
#                            screen.blit(blank,x[1])
#                        if (clickL[0]  == 2 or clickL[1] == 2):
#                            twoClick = True
#                            twobClick = True
#                            screen.blit(blank,x[2])  
#                            screen.blit(blank,x[3])
#                        if (clickL[0]  == 3 or clickL[1] == 3):
#                            screen.blit(blank,x[4])  
#                            screen.blit(blank,x[5])
#                            threeClick = True
#                            threebClick = True
#                        if (clickL[0]  == 4 or clickL[1] == 4):
#                            fourClick = True
#                            fourbClick = True
#                            screen.blit(blank,x[6])
#                            screen.blit(blank,x[7])
#                        #resets values after the player misses something
#                        click_counter = 0
#                        miss =False
#                        del clickL[1]
#                        del clickL[0]
#            #alerts the player that they won the game           
#            if (SCORE == 4):
#                if (winner):
#                    score_board = myfont.render('You Win ', True,(255,255,255))
#                    screen.blit(score_board,(400,500))
#                    WIN = True
#                    winner = False
                                     

#        #update
#        pygame.display.update()
#        if (not(winner)):
#            pygame.time.wait(2000)
#            pygame.quit()
#            sys.exit()
#        elif(ATTEMPTS==0):
#            pygame.time.wait(2000)
#            pygame.quit()
#            sys.exit()
#        #return WIN

##game starter
#main()
