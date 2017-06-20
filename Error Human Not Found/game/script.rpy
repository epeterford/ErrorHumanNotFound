# The script of the game goes in this file.

#Character Declarations
define g = Character("Grace", color ="#006d0d")
define a = Character("Ada", color="#3a416c")
define secretary = Character("Virtual Secretary", color ="#383838") 
define h = Character("Director Hirose", color="8b00bf")
define knuth = Character("Director Knuth", color="#5a0167")
define neva = Character("Director Nevalinna", color="#5a0167")
define cray = Character("Director Cray", color="#5a0167")
define godel = Character("Director Gödel", color="#5a0167")
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

#Opening Crawl
image openingCrawl = "openCrawlText.png"
image bg splashScreen = "Error_TitleSplash.png"
image bg openCrawlBG = "openCrawlBG.png"
##Grace's Lab BG
image bg G_main = "GraceLab_Main.png"
image bg G_deskArea = "GraceDesk_Main.png"
#image bg G_left1 "GraceDesk_Left1.png"
#image bg G_left2 "GraceDesk_Left2.png"
#image bg G_right "GraceDesk_Right.png"

##The Conclave
#image bg conclaveWaitingRoom = "ConclaveReception_Main.png"
#image bg conclaveDoor = "ConclaveReception_Close.png"
#image bg conclave = "Conclave_Proper.png"

#Hirose's Space

#The Balcony

#Hallway Shots

#Lab 2


image bg bed = "bg bed layout.png"
image bg computer = "bg computer terminal.png"
image bg view = "bg window and lamp.png"
image bg conclaveWaitingRoom = "2_theconclave_A_1.png"
image bg conclaveDoor = "2_theconclave_A1_1.png"
image bg conclave = "2_theconclave_B_2.png"
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
    with fade(5.0)
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
    with fade(5.0)
    jump prologue
