import pygame, sys, random, time
from pygame.locals import *
from pygame import display

#LIST OF ANCHORS TO USE
my_list = list()
my_list = ((600 + 100,350), (750+ 100,350),(900+ 100,350),(450+ 100,350),(450+ 100,500),(900+ 100,500),(750+ 100,500),(600+ 100,500))
x = list(my_list)
random.shuffle(x)

#colors
BLUE = (0,70,200)

LIGHTOFF =('LightOff.png')
LIGHTON = ('LightOn.png')
LIGHT =('Light.png')

WIN = False
ATTEMPTS = 12
SCORE = 0
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
##
class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #self.font = pygame.font.SysFont("None", 40)
        self.font = pygame.font.Font("TemploGordo.ttf", 40)

        self.font.set_italic(0)
        self.color = (255, 255, 255, 255)
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(1200, 450)
        
    def update(self):
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            self.image = self.font.render(msg, 0, self.color)

class Attempts(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        #self.font = pygame.font.SysFont("None", 40)
        pygame.font.init()
        #Font= pygame.font.Font("TemploGordo.ttf", 40)
        self.font = pygame.font.Font("TemploGordo.ttf", 40)

        self.font.set_italic(0)
        self.color = (255, 255, 255, 255)
        self.lastattempts = -1
        self.update()
        self.rect = self.image.get_rect().move(1200, 500)
        
    def update(self):
        if ATTEMPTS != self.lastattempts:
            self.lastattempts = ATTEMPTS
            msg = "Attempts: %d" % ATTEMPTS
            self.image = self.font.render(msg, 0, self.color)

def main(winstyle=0):
    #set up display
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    winstyle = 0
    pygame.font.init()
    myfont = pygame.font.Font("TemploGordo.ttf", 30)
    #myfont = pygame.font.SysFont("None", 30)
    #DISPLAYSURF = pygame.image.load(BACKGROUND)
    winner = True
    
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
    lightOff=pygame.image.load(LIGHT).convert_alpha()
    lightWrong =pygame.image.load(LIGHTOFF).convert_alpha()
    lightOff2=pygame.image.load(LIGHT).convert_alpha()
         
    mousex = 0 # used to store x coordinate of mouse event
    mousey = 0 # used to store y coordinate of mouse event
    pygame.display.set_caption('Binary Memory Game')
    
    screen.blit(background,(0,0))
    screen.blit(lightOn,(30,280))
    screen.blit(lightWrong,(30,520))
    screen.blit(lightOff,(30,280))
    screen.blit(lightOff2, (30, 520))
    screen.blit(onenum,x[0]) 
    screen.blit(onebin,x[1])
    screen.blit(twonum,x[2])  
    screen.blit(twobin,x[3])  
    screen.blit(threenum,x[4])  
    screen.blit(threebin,x[5])  
    screen.blit(fournum,x[6])  
    screen.blit(fourbin,x[7])

    #Test new score draw method
    all = pygame.sprite.RenderUpdates()
    Score.containers = all
    Attempts.containers = all
    global attempts
    global score
    global SCORE
    global ATTEMPTS
    global WIN
    if pygame.font:
        all.add(Score())
        all.add(Attempts())


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
    
    screen.blit(blank,x[0])  
    screen.blit(blank,x[1])
    screen.blit(blank,x[2])  
    screen.blit(blank,x[3])  
    screen.blit(blank,x[4])  
    screen.blit(blank,x[5])  
    screen.blit(blank,x[6])  
    screen.blit(blank,x[7])
    
    oneClick = True
    onebClick = True
    twoClick = True
    twobClick = True
    threeClick = True
    threebClick = True
    fourClick = True
    fourbClick = True
    
    tally_list = list() 
    totalcounter = 0
    first_click = 5000
    second_click = 6000
    click_counter = 0
    miss = False
    lightactive = False
    
    #The current place for instructions. This will be replaced with a png later
    instructions = myfont.render('Match the binary numbers', True, (235,255,255))
    instruct2 = myfont.render( 'with their corresponding', True, (235, 255, 255))
    instruct3 = myfont.render ('integer value.',True,(235,255,255))
    screen.blit(instructions, (200,370))
    screen.blit(instruct2,(200,400))
    screen.blit(instruct3,(200, 430))

    #user events
    clickL= list()
    
    while (ATTEMPTS>=0):
        # clear/erase the last drawn sprites
        all.clear(screen, background)

        #update all the sprites
        all.update()

        #draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty) 
        if (lightactive == True):
            time.sleep(1)
            screen.blit(lightOff,(30,520))
            screen.blit(lightOff,(30,280))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif ATTEMPTS == 0 :
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
                        totalcounter += 1
                        print ('1')
                        oneClick = False
                        screen.blit(onenum,x[0]) 
                if onebpos.collidepoint(mouse_pos):
                    if (onebClick == True):
                        clickL.append(1)
                        click_counter +=1
                        totalcounter += 1
                        print ('1')
                        onebClick = False
                        screen.blit(onebin,x[1])
                if twonpos.collidepoint(mouse_pos):
                    if (twoClick == True):
                        clickL.append(2)
                        click_counter +=1
                        totalcounter += 1
                        print ('2')
                        twoClick = False
                        screen.blit(twonum,x[2]) 
                if twobpos.collidepoint(mouse_pos):
                    if (twobClick == True):
                        clickL.append(2)
                        click_counter +=1
                        totalcounter += 1
                        print ('2')
                        twobClick = False
                        screen.blit(twobin,x[3])
                if threenpos.collidepoint(mouse_pos):
                    if (threeClick == True):
                        clickL.append(3)
                        click_counter +=1
                        totalcounter += 1
                        print ('3')
                        threeClick = False
                        screen.blit(threenum,x[4]) 
                if threebpos.collidepoint(mouse_pos):
                    if (threebClick == True):
                        clickL.append(3)
                        click_counter +=1
                        totalcounter += 1
                        print ('3')
                        threebClick = False
                        screen.blit(threebin,x[5])
                if fournpos.collidepoint(mouse_pos):
                    if (fourClick == True):
                        clickL.append(4)
                        click_counter +=1
                        totalcounter += 1
                        print ('4')
                        fourClick = False
                        screen.blit(fournum,x[6]) 
                if fourbpos.collidepoint(mouse_pos):
                    if (fourbClick == True):
                        clickL.append(4)
                        click_counter +=1
                        totalcounter += 1
                        print ('4')
                        fourbClick = False
                        screen.blit(fourbin,x[7])

      
                pygame.display.update()
                
            if (click_counter == 2) :  
                time.sleep(.5)
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
                    SCORE += 1
                    ATTEMPTS -= 1
                    click_counter = 0
                    print('attempts = ', ATTEMPTS)
                    print('score = ',SCORE)
                    del clickL[1]
                    del clickL[0]
                    screen.blit(lightOn,(30,520))
                    time.sleep(.5)
                    lightactive = True
                elif (first_click is not second_click):
                    ATTEMPTS -= 1
                    print('miss')
                    time.sleep(.5)
                    lightactive = True
                    screen.blit(lightWrong,(30,280))
                    miss = True
                    if (miss == True):
                        print('miss is true')
                        print('click list 1 = ',clickL[0])
                        print('click list 2 = ', clickL[1])
                        print('score = ',SCORE)
                        print('attempts = ', ATTEMPTS)
                        print('total counter = ', totalcounter)
                        if (clickL[0] == 1 and clickL[1] == 2):
                            oneClick = True
                            onebClick = True
                            twoClick = True
                            twobClick = True
                            screen.blit(blank,x[0])  
                            screen.blit(blank,x[1])
                            screen.blit(blank,x[2])  
                            screen.blit(blank,x[3])
                            print('inside')
                        elif (clickL[0]  == 2 and clickL[1] == 1):
                            oneClick = True
                            onebClick = True
                            twoClick = True
                            twobClick = True
                            screen.blit(blank,x[0])  
                            screen.blit(blank,x[1])
                            screen.blit(blank,x[2])  
                            screen.blit(blank,x[3])
                            print('inside')
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
                            print('inside')
                        elif (clickL[0]  == 1 and clickL[1] == 4):
                            oneClick = True
                            onebClick = True
                            fourClick = True
                            fourbClick = True
                            screen.blit(blank,x[0])
                            screen.blit(blank,x[1])
                            screen.blit(blank,x[6])
                            screen.blit(blank,x[7])
                            print('inside')
                        elif (clickL[0]  == 4 and clickL[1] == 1):
                            oneClick = True
                            onebClick = True
                            fourClick = True
                            fourbClick = True
                            screen.blit(blank,x[0])
                            screen.blit(blank,x[1])
                            screen.blit(blank,x[6])
                            screen.blit(blank,x[7])
                            print('inside')
                        elif (clickL[0]  == 2 and clickL[1] == 3):
                            twoClick = True
                            twobClick = True
                            threeClick = True
                            threebClick = True
                            screen.blit(blank,x[2])
                            screen.blit(blank,x[3])
                            screen.blit(blank,x[4])
                            screen.blit(blank,x[5])
                            print('inside')
                        elif (clickL[0]  == 3 and clickL[1] == 2):
                            twoClick = True
                            twobClick = True
                            threeClick = True
                            threebClick = True
                            screen.blit(blank,x[2])
                            screen.blit(blank,x[3])
                            screen.blit(blank,x[4])
                            screen.blit(blank,x[5])
                            print('inside')
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
                        print('post miss')
                        del clickL[1]
                        del clickL[0]
                        
            if (SCORE == 4):
                if (winner):
                    #pygame.draw.rect(screen,BLUE,(400,1000,100,25))
                    score_board = myfont.render('You Win ', True,(255,255,255))
                    screen.blit(score_board,(400,500))
                    print ('you win')
                    WIN = True
                    winner = False
                                     

        #update
        pygame.display.update()
        if (not(winner)):
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()
        elif(ATTEMPTS==0):
            pygame.time.wait(2000)
            pygame.quit()
            sys.exit()
        #return WIN

#game starter
main()
