# The script of the game goes in this file.

#Character Declarations
define g = Character("Grace", color ="#006d0d")
define a = Character("Ada", color="#3a416c")
define secretary = Character("Virtual Secretary", color ="#383838") 
define h = Character("Director Hirose", color="8b00bf")
define knuth = Character("Chief Knuth", color="#5a0167")
define neva = Character("Chief Nevalinna", color="#5a0167")
define cray = Character("Chief Cray", color="#5a0167")
define godel = Character("Chief Godel", color="#5a0167")
define b = Character("Blue", color="#0016bb")
define c = Character("Colossus", color="#765e00")
define e = Character("Eastern Goddess", color="#e6e03d")
define w = Character("Watson", color="#000000")
define ivan = Character("Ivan", color="#556b1f")
define lynn = Character("Lynn", color="#ce00a0")
define alan = Character("Alan", color="#005aaf")
define tosh = Character("Tosh", color="#383838")
define mopr = Character("M.O.P.R", color="#ad0000")
#Investigators
#define  = Character("", color="#000000")
#define = Character("", color="#000000")
#define = Character("", color="#000000")

#Sprites for the Conclave
image Nevalinna speaking = "sprites/nevalinna_speaking.png"
image Grace snarky = "sprites/grace_snarky.png"
image Grace happy = "sprites/grace_happy.png"
image Grace angry = "sprites/grace_angry.png"
image Grace annoyed = "sprites/grace_annoyed.png"
image Grace neutral = "sprites/grace_neutral.png"
image Grace sad = "sprites/grace_sad.png"
image Grace surprised = "sprites/grace_surprised.png"
image Grace frustrated = "sprites/grace_annoyed.png"
image Tosh pleasant = "sprites/Tosh_Happy.png"
image Ada afraid = "sprites/ada_afraid.png"
image Ada amused = "sprites/ada_amused.png"
image Ada annoyed = "sprites/ada_annoyed.png"
image Ada frustrated = "sprites/ada_annoyed.png"
image Ada happy = "sprites/ada_happy.png"
image Ada neutral = "sprites/ada_neutral.png"
image Ada seething = "sprites/ada_seething.png"
image Ada concerned = "sprites/ada_afraid.png"
image Ada nervous = "sprites/ada_afraid.png"

#Opening Crawl
image openingCrawl = "openCrawlText.png"
image bg splashScreen = "Error_TitleSplash.png"
image bg openCrawlBG = "openCrawlBG.png"
##Grace's Lab BG
image bg G_main = "bg/GraceLab_Main.png"
image bg G_deskArea = "bg/GraceDesk_Main.png"
image bg G_left1 = "bg/GraceDesk_Left1.png"
image bg G_left2 = "bg/GraceDesk_Left2.png"
image bg G_right = "bg/GraceDesk_Right.png"
image bg hallwayGrace = "bg/Hallway_Grace.png"
##The Conclave
image bg conclaveWaitingRoom = "bg/ConclaveReception_Main.png"
image bg conclaveDoor = "bg/ConclaveReception_Close.png"
image bg conclave = "bg/Conclave_Proper.png"

#Hirose's Space
image bg hiroseDoor= "bg/Hirose_Door.png"
image bg hiroseOfficeDesk = "bg/Hirose_OfficeDesk.png"
image bg hiroseOfficeMain = "bg/Hirose_OfficeMain.png"
image bg hiroseOfficeTransition = "bg/Hirose_OfficeTransition.png"
image bg hirosePersonalBed = "bg/Hirose_PersonalBed.png"
image bg hirosePersonalComputer = "bg/Hirose_PersonalComputer.png"
image bg hirosePersonalArea = "bg/Hirose_PersonalMain.png"
image bg hiroseReception = "bg/Hirose_Reception.png"
#$ hiroseTea_inv = False
#$ hiroseSafe_inv = False
#$ solvedBinary1 = False
#$ hiroseOfficeItems = 0

#

#The Balcony

#Hallway Shots

#Lab 2

#Screens
#    imagemap: 
#        ground "hiroseOffice1.png"
#        hover "hiroseOffice1_hover.png"
        
#        hotspot (1340, 419, 188, 185) clicked Jump("hiroseOffice2")
        

image bg bed = "bg bed layout.png"
image bg computer = "bg computer terminal.png"
image bg view = "bg window and lamp.png"
#image bg ".png"
#image bg ".png"
#image bg ".png"
define dissolve = Dissolve (1.0)

image Tosh neutral = "Tosh_Happy1.png"

define audio.creep = "music/Creep_Wav.ogg"
define audio.digi = "music/Digi_Sprites.ogg"
define audio.robot = "music/robotScanner.ogg"
define audio.sraf = "music/srafTexture.ogg"
define audio.stab = "music/stabTapeEcho.ogg"


init python:
    renpy.music.register_channel("channel00", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel01", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel02", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel03", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel04", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    #atl_transform ::= "transform" scrolling_vertical "("parameters")" ":"
    
    
    
#Creep_Wav.ogg, #Digi_Sprites.ogg, robotScanner.ogg, sraftexture.ogg, stabTapeEcho.ogg 

# The game starts here.
label start:
    $ quick_menu = False
    $ centerScreen = Position(xpos=0.5, xanchor =0.5, ypos =0.2, yanchor = 0.2)
    $ hiroseTea_inv = False
    $ hiroseSafe_inv = False
    $ solvedBinary1 = False
    $ hiroseOfficeItems = 0
    $ hiroseBed_inv = False
    $ hirosePhoto_inv = False
    $ hiroseWindow_inv = False
    $ hirosePersonalItems = 0
    $ talkAdaHirosePersonal_value = 0
    $ hirosePersonalItems_value = 0
    transform crawlScroll:
        yalign 0.0 xalign 0.5
        linear 50.0 yalign 1.0
        
    transform basicfade:
        on scene:
            alpha 0.0
            linear 3.0 alpha 1.0
        on hide:
            linear 3.0 alpha 0.0   


    play music "audio/Main_Title_BGM.wav"

    window hide
    scene bg openCrawlBG at basicfade
    show openingCrawl at crawlScroll
    $ renpy.pause(51.0)
    scene bg splashScreen
    #with fade(5.0)
    $ renpy.pause(5.0)

    stop music
#    play channel00 creep
#    play channel01 digi
#    play channel02 robot
#    play channel03 sraf
#    play channel04 stab


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    scene bg G_deskArea at basicfade
    $ quick_menu = True
    #with fade(5.0)
    jump prologue
