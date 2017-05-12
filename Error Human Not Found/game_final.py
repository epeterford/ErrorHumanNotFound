import pygame, sys, random, time
from pygame.locals import *

from pygame import display

#LIST OF ANCHORS TO USE
my_list = list()
my_list = ((600 + 100,350), (750+ 100,350),(900+ 100,350),(450+ 100,350),(450+ 100,500),(900+ 100,500),(750+ 100,500),(600+ 100,500))
x = list(my_list)
random.shuffle(x)



#dimensions
TILESIZE = 100
MAPWIDTH = 1
MAPHEIGHT = 1
WINDOWWIDTH = 1520
WINDOWHEIGHT = 930

BLANK = ('tileBack.png')
ONE = ('tileFront0.png')
ONEB = ('tileFront00.png')
TWO = ('tileFront1.png')
TWOB = ('tileFront01.png')
THREE = ('tileFront2.png')
THREEB = ('tileFront10.png')
FOUR = ('tileFront3.png')
FOURB = ('tileFront11.png')
BACKGROUND = ('tilEBackground.png')
LIGHTWRONG =('LightOff.png')
LIGHTON = ('LightOn.png')
LIGHTOFF =('Light.png')

def main():
    #set up display
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    myfont = pygame.font.SysFont("None", 30)
    #DISPLAYSURF = pygame.image.load(BACKGROUND)
    attempts = 10
    score = 0
    
    background = pygame.image.load(BACKGROUND).convert_alpha()
    blank =pygame.image.load(BLANK).convert_alpha()
    onenum =pygame.image.load(ONE).convert_alpha()
    onebin =pygame.image.load(ONEB).convert_alpha()
    twonum =pygame.image.load(TWO).convert_alpha()
    twobin=pygame.image.load(TWOB).convert_alpha()
    threenum=pygame.image.load(THREE).convert_alpha()
    threebin=pygame.image.load(THREEB).convert_alpha()
    fournum=pygame.image.load(FOUR).convert_alpha()
    fourbin=pygame.image.load(FOURB).convert_alpha()
    lightOn=pygame.image.load(LIGHTON).convert_alpha()
    lightOff=pygame.image.load(LIGHTOFF).convert_alpha()
    lightWrong =pygame.image.load(LIGHTWRONG).convert_alpha()
         
    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Binary Memory Game')
    screen.blit(background,(0,0))
    screen.blit(lightOn,(30,400))
    screen.blit(lightWrong,(30,400))
    screen.blit(lightOff,(30,400))
    screen.blit(onenum,x[0]) 
    screen.blit(onebin,x[1])
    screen.blit(twonum,x[2])  
    screen.blit(twobin,x[3])  
    screen.blit(threenum,x[4])  
    screen.blit(threebin,x[5])  
    screen.blit(fournum,x[6])  
    screen.blit(fourbin,x[7])
    screen.blit(blank,x[0])  
    screen.blit(blank,x[1])
    screen.blit(blank,x[2])  
    screen.blit(blank,x[3])  
    screen.blit(blank,x[4])  
    screen.blit(blank,x[5])  
    screen.blit(blank,x[6])  
    screen.blit(blank,x[7])    
    y = x
    posa, posb = zip(*y)
    onenpos = Rect(posa[0], posb[0], 100, 100)
    onebpos = Rect(posa[1], posb[1], 100, 100)     
    twonpos = Rect(posa[2], posb[2], 100, 100)     
    twobpos = Rect(posa[3], posb[3], 100, 100)     
    threenpos = Rect(posa[4], posb[4], 100, 100)     
    threebpos = Rect(posa[5], posb[5], 100, 100)     
    fournpos = Rect(posa[6], posb[6], 100, 100)     
    fourbpos = Rect(posa[7], posb[7], 100, 100)    
    oneClick = True
    onebClick = True
    twoClick = True
    twobClick = True
    threeClick = True
    threebClick = True
    fourClick = True
    fourbClick = True
    
    tally_list = list() 

    score = 0
    attempts = 12
    click_counter = 0   
    miss = False
    lightactive = False
    
    instructions = myfont.render('match the binary numbers', True, (255,255,255))
    instruct2 = myfont.render( 'with their numerical counter part',True,(255,255,255))
    screen.blit(instructions, (200,370))
    screen.blit(instruct2,(200,400))
    score_board = myfont.render('score = ' + str(score), True,(255,255,255))
    screen.blit(score_board,(1150,400))
    attempt_counter = myfont.render('attempts left = ' + str(attempts), True,(255,255,255))
    screen.blit(attempt_counter,(1150,550))
    
    clickL= list()
    
    while True:
        if (lightactive == True):
            time.sleep(.5)
            screen.blit(lightOff,(30,400))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif attempts == 0 :
                sys.exit()                
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
            elif event.type == MOUSEBUTTONUP:
                mouse_pos = event.pos
                mousex, mousey = event.pos
                mouseClicked = True
                if onenpos.collidepoint(mouse_pos):
                    if (oneClick == True):
                        clickL.append(1)
                        click_counter +=1                       
                        print ('1')
                        oneClick = False
                        screen.blit(onenum,x[0]) 
                if onebpos.collidepoint(mouse_pos):
                    if (onebClick == True):
                        clickL.append(1)
                        click_counter +=1
                        print ('1')
                        onebClick = False
                        screen.blit(onebin,x[1])
                if twonpos.collidepoint(mouse_pos):
                    if (twoClick == True):
                        clickL.append(2)
                        click_counter +=1
                        print ('2')
                        twoClick = False
                        screen.blit(twonum,x[2]) 
                if twobpos.collidepoint(mouse_pos):
                    if (twobClick == True):
                        clickL.append(2)
                        click_counter +=1
                        print ('2')
                        twobClick = False
                        screen.blit(twobin,x[3])
                if threenpos.collidepoint(mouse_pos):
                    if (threeClick == True):
                        clickL.append(3)
                        click_counter +=1
                        print ('3')
                        threeClick = False
                        screen.blit(threenum,x[4]) 
                if threebpos.collidepoint(mouse_pos):
                    if (threebClick == True):
                        clickL.append(3)
                        click_counter +=1
                        print ('3')
                        threebClick = False
                        screen.blit(threebin,x[5])
                if fournpos.collidepoint(mouse_pos):
                    if (fourClick == True):
                        clickL.append(4)
                        click_counter +=1
                        print ('4')
                        fourClick = False
                        screen.blit(fournum,x[6]) 
                if fourbpos.collidepoint(mouse_pos):
                    if (fourbClick == True):
                        clickL.append(4)
                        click_counter +=1
                        print ('4')
                        fourbClick = False
                        screen.blit(fourbin,x[7])

      
                pygame.display.update()    
               
                
            if (click_counter == 2) :  
                if (clickL[0] == clickL[1]):
                    if (clickL[0] == 1):
                        oneClick = False
                        onebClick = False
                    if (clickL[0]  == 2):
                        twoClick = False
                        twobClick = False
                    if (clickL[0]  == 3):
                        threeClick = False
                        threebClick = False
                    if (clickL[0]  == 4):
                        fourClick = False
                        fourbClick = False
                    score += 1
                    attempts -= 1
                    click_counter = 0
                    print('score = ',score)
                    del clickL[1]
                    del clickL[0]
                    screen.blit(lightOn,(30,400))
                    time.sleep(.5)
                    lightactive = True
                elif (clickL[0] is not clickL[1]):
                    attempts -= 1
                    miss = True
                    screen.blit(lightWrong,(30,400))
                    if (miss == True):
                        time.sleep(.5)
                        if (clickL[0] == 1 and clickL[1] == 2):
                            oneClick = True
                            onebClick = True
                            twoClick = True
                            twobClick = True
                            screen.blit(blank,x[0])  
                            screen.blit(blank,x[1])
                            screen.blit(blank,x[2])  
                            screen.blit(blank,x[3])
                        elif (clickL[0]  == 2 and clickL[1] == 1):
                            oneClick = True
                            onebClick = True
                            twoClick = True
                            twobClick = True
                            screen.blit(blank,x[0])  
                            screen.blit(blank,x[1])
                            screen.blit(blank,x[2])  
                            screen.blit(blank,x[3])
                        elif (clickL[0]  == 1 and clickL[1] == 3):
                            screen.blit(blank,x[0])  
                            screen.blit(blank,x[1])
                            screen.blit(blank,x[4])  
                            screen.blit(blank,x[5])
                            oneClick = True
                            onebClick = True
                            threeClick = True
                            threebClick = True
                        elif (clickL[0]  == 3 and clickL[1] == 1):
                            screen.blit(blank,x[0])
                            screen.blit(blank,x[1])
                            screen.blit(blank,x[4])  
                            screen.blit(blank,x[5])
                            oneClick = True
                            onebClick = True
                            threeClick = True
                            threebClick = True
                        elif (clickL[0]  == 1 and clickL[1] == 4):
                            oneClick = True
                            onebClick = True
                            fourClick = True
                            fourbClick = True
                            screen.blit(blank,x[0])
                            screen.blit(blank,x[1])
                            screen.blit(blank,x[6])
                            screen.blit(blank,x[7])
                        elif (clickL[0]  == 4 and clickL[1] == 1):
                            oneClick = True
                            onebClick = True
                            fourClick = True
                            fourbClick = True
                            screen.blit(blank,x[0])
                            screen.blit(blank,x[1])
                            screen.blit(blank,x[6])
                            screen.blit(blank,x[7])
                        elif (clickL[0]  == 2 and clickL[1] == 3):
                            twoClick = True
                            twobClick = True
                            threeClick = True
                            threebClick = True
                            screen.blit(blank,x[2])
                            screen.blit(blank,x[3])
                            screen.blit(blank,x[4])
                            screen.blit(blank,x[5])
                        elif (clickL[0]  == 3 and clickL[1] == 2):
                            twoClick = True
                            twobClick = True
                            threeClick = True
                            threebClick = True
                            screen.blit(blank,x[2])
                            screen.blit(blank,x[3])
                            screen.blit(blank,x[4])
                            screen.blit(blank,x[5])
                        elif (clickL[0]  == 2 and clickL[1] == 4):
                            fourClick = True
                            fourbClick = True
                            twoClick = True
                            twobClick = True
                            screen.blit(blank,x[2])
                            screen.blit(blank,x[3])
                            screen.blit(blank,x[6])
                            screen.blit(blank,x[7])
                        elif (clickL[0]  == 4 and clickL[1] == 2):
                            fourClick = True
                            fourbClick = True
                            twoClick = True
                            twobClick = True
                            screen.blit(blank,x[2])
                            screen.blit(blank,x[3])
                            screen.blit(blank,x[6])
                            screen.blit(blank,x[7])
                            print('inside')
                        elif (clickL[0]  == 3 and clickL[1] == 4):
                            fourClick = True
                            fourbClick = True
                            threeClick = True
                            threebClick = True
                            screen.blit(blank,x[4])
                            screen.blit(blank,x[5])
                            screen.blit(blank,x[6])
                            screen.blit(blank,x[7])
                        elif (clickL[0]  == 4 and clickL[1] == 3):
                            fourClick = True
                            fourbClick = True
                            threeClick = True
                            threebClick = True
                            screen.blit(blank,x[4])
                            screen.blit(blank,x[5])
                            screen.blit(blank,x[6])
                            screen.blit(blank,x[7])
                        else:
                            print ('god what have you done')
                        click_counter = 0
                        miss =False
                        del clickL[1]
                        del clickL[0]
                        lightactive = True 

        #update
        pygame.display.update() 


#game starter
main()