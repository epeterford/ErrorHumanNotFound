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
image Tosh alarmed = "sprites/Tosh_alarmed.png" 
image Ada afraid = "sprites/ada_afraid.png"
image Ada surprised = "sprites/ada_afraid.png"
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


#tutorial backgrounds
image bg lgEasy1 = "dragNDrop_instructions.png"
image bg lgEasy2 = "LG_instructions.png"
image bg lgEasy3 = "truthTable_instructions.png"
image bg lgEasy4 = "NOT_instructions.png"
image bg lgEasy5 = "AND_OR_instructions.png"
image bg tutorial_inv_1 = "inv_instruction1.png"
image bg tutorial_inv_2 = "inv_instruction2.png"
image bg gramEasy1 = "easyGrammar_Tut1.png"
image bg gramEasy2 = "easyGrammar_Tut2.png"
image bg gramEasy3 = "easyGrammar_Tut3.png"
image bg gramEasy4 = "easyGrammar_Tut4.png"
image bg gramEasy5 = "easyGrammar_Tut5.png"
image bg gramEasy6 = "easyGrammar_Tut6.png"
image bg gramEasy7 = "easyGrammar_Tut7.png"

##The Conclave
image bg conclaveWaitingRoom = "bg/ConclaveReception_Main.png"
image bg conclaveDoor = "bg/ConclaveReception_Close.png"
image bg conclave = "bg/Conclave_Proper.png"
image other darken = "blackout.png"
                       
#Hirose's Space
image bg hiroseDoor= "bg/Hirose_Door.png"
image bg hiroseOfficeDesk = "bg/Hirose_OfficeDesk.png"
image bg hiroseOfficeDesk2 = "bg/Hirose_OfficeDeskLoggedIn.png"
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
image special emptyButton = "button_empty.png"
#The Balcony
image bg black = "bg/blackScreen.png"
image bg balconyMain = "bg/Balcony_Main.png"
image bg balconyCorner = "bg/Balcony_Corner.png"
image bg balconyTop = "bg/Balcony_RailingTopDown.png"
image bg balconyClose = "bg/Balcony_RailingClose.png"
image bg balconyLong = "bg/Balcony_RailingLong.png"
image bg balconyRamp = "bg/Balcony_Ramp.png"
image bg bbalconyTransition = "bg/Balcony_Transition.png"

#Hallway Shots
image bg Logic_Gate = "LOGIC_GATE_BG.png"
image bg black = "blackScreen.png"

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

#define audio.lab2_00 = "music/Creep_Wav.ogg"
#define audio.lab2_01 = "music/Digi_Sprites.ogg"
#define audio.lab2_02 = "music/robotScanner.ogg"
#define audio.lab2_03 = "music/srafTexture.ogg"
#define audio.lab2_04 = "music/stabTapeEcho.ogg"
#define audio.lab2_05 = "music/stabTapeEcho.ogg"
#define audio.lab2_06 = "music/stabTapeEcho.ogg"
#define audio.lab2_07 = "music/stabTapeEcho.ogg"
#define audio.lab2_08 = "music/stabTapeEcho.ogg"
#define audio.lab2_09 = "music/stabTapeEcho.ogg"
define audio.mt_bellsL = "music/MainTheme/EHNF_L1_Bells_L_Bounced.ogg"
define audio.mt_bellsR = "music/MainTheme/EHNF_L2_Bells_R_Bounced.ogg"
define audio.mt_piano = "music/MainTheme/EHNF_L3_Brians_Piano.ogg"
define audio.mt_ghostBus = "music/MainTheme/EHNF_L4_Ghost_Bus.ogg"
define audio.mt_ghostL = "music/MainTheme/EHNF_L5_Ghosts_L.ogg"
define audio.mt_ghostR = "music/MainTheme/EHNF_L6_Ghosts_R.ogg"
define audio.mt_orchestra = "music/MainTheme/EHNF_L7_Orchestra_Percussion.ogg"
define audio.mt_sciFi = "music/MainTheme/EHNF_L8_SciFi_Pad.ogg"
define audio.mt_touchOrchestra = "music/MainTheme/EHNF_L9_Touch_Orchestra_Bounced.ogg"
define audio.mt_tornado = "music/MainTheme/EHNF_L10_Tornado_CMKD_Bounced.ogg"
define audio.mt_ultrasweeper = "music/MainTheme/EHNF_L11_Ultrasweeper_FP_Bounced.ogg"
define audio.mt_violins = "music/MainTheme/EHNF_L12_Violins.ogg"
define audio.mt_wistful = "music/MainTheme/EHNF_L13_WistfulLead_SP_Bounced.ogg"
define audio.pipeFlowR = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_01.ogg"
define audio.pipeFlowG = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_02.ogg"
define audio.pipeFlowN = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_03.ogg"
define audio.lgWin = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_RightOutput.ogg"
define audio.lgLose = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_WrongOutput.ogg"

define audio.gramWin = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_RightSolution.ogg"
define audio.gramLose = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_WrongSolution.ogg"
define audio.gramText1 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TextEnterNoise_01.ogg"
define audio.gramText2 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TextEnterNoise_02.ogg"
define audio.gramText3 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TextEnterNoise_03.ogg"
define audio.gramTree1 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_01.ogg"
define audio.gramTree2 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_02.ogg"
define audio.gramTree3 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_03.ogg"
define audio.gramTree4 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_04.ogg"
define audio.gramTree5 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_05.ogg"

define audio.doorOpen1 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_OPEN_1.ogg"
define audio.doorOpen2 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_OPEN_2.ogg"
define audio.doorClose1 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_CLOSE_1.ogg"
define audio.doorClose2 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_CLOSE_2.ogg"
define audio.doorDenied = "music/Object/Door_Audio/ENHF_Object_Door_AccessDenied.ogg"
define audio.doorAccess= "music/Object/Door_Audio/ENHF_Object_Door_AccessGranted.ogg"



init: 
    $ config.keymap['hide_windows'].remove('mouseup_2')
init python:
    renpy.music.register_channel("channel00", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel01", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel02", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel03", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel04", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel05", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel06", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel07", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel08", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel09", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel10", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel11", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel12", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel13", mixer=None, loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    config.main_menu_music = "music/EHNF_Main_Theme.ogg"
#    config.main_menu_music = ("music/MainTheme/EHNF_L1_Bells_L_Bounced.ogg" and "music/MainTheme/EHNF_L2_Bells_R_Bounced.ogg" and "music/MainTheme/EHNF_L3_Brians_Piano.ogg" and "music/MainTheme/EHNF_L4_Ghost_Bus.ogg" and "music/MainTheme/EHNF_L5_Ghosts_L.ogg"and "music/MainTheme/EHNF_L6_Ghosts_R.ogg"and "music/MainTheme/EHNF_L7_Orchestra_Percussion.ogg"and "music/MainTheme/EHNF_L8_SciFi_Pad.ogg"and "music/MainTheme/EHNF_L9_Touch_Orchestra_Bounced.ogg"and "music/MainTheme/EHNF_L10_Tornado_CMKD_Bounced.ogg"and "music/MainTheme/EHNF_L11_Ultrasweeper_FP_Bounced.ogg"and "music/MainTheme/EHNF_L12_Violins.ogg"and "music/MainTheme/EHNF_L13_WistfulLead_SP_Bounced.ogg")
#        play channel00 mt_bellsL,
#        play channel01 mt_bellsR,
#        play channel02 mt_piano,
#        play channel03 mt_ghostBus,
#        play channel04 mt_ghostL,
#        play channel05 mt_ghostR,
#        play channel06 mt_orchestra,
#        play channel07 mt_sciFi,
#        play channel08 mt_touchOrchestra,
#        play channel09 mt_tornado,
#        play channel10 mt_ultrasweeper,
#        play channel11 mt_violins,
#        play channel12 mt_wistful]
    #atl_transform ::= "transform" scrolling_vertical "("parameters")" ":"

    
    
#Creep_Wav.ogg, #Digi_Sprites.ogg, robotScanner.ogg, sraftexture.ogg, stabTapeEcho.ogg 

# The game starts here.
label start:
    stop music
    $ points_SbE = 0
    $ points_E = 0
    $ points_S = 0
    $ quick_menu = False
    $ gate_name = ""
    $ centerScreen = Position(xpos=0.5, xanchor =0.5, ypos =0.2, yanchor = 0.2)
    $ centerScreen2 = Position(xpos=0.5, xanchor =0.5, ypos =0.35, yanchor = 0.2)
    $ near_left = Position(xpos=0.25, ypos = 0.5)
    $ hiroseTea_inv = False
    $ hiroseOfficeComputer = False
    $ hiroseTree_inv = False
    $ hiroseTransitionItems = 0
    $ hiroseRecorder_inv = False
    $ hiroseOfficeItems = 0
    $ hiroseBed_inv = False
    $ hirosePhoto_inv = False
    $ hiroseWindow_inv = False
    $ hirosePersonalItems = 0
    $ talkAdaHirosePersonal_value = 0
    $ hirosePersonalItems_value = 0
    $ graceRightDesk_value = 0
    $ graceLeft1Desk_value = 0
    $ graceLeft2Desk_value = 0
    $ Logic_A_solved = False
    $ Logic_B_solved = False
    $ solved_LG_easy = False
    $ lgEasy_tries = 0
    $ tutorial_LGEasy = True
    $ tutorial_gramEasy = True
    $ resume = ""
    $ callAttempts = 0
    $ balconyItems = 0
    $ moprScene = False
    $ LGEasyHints = 0
    $ gramEasyHints = 0
    $ attemptsLogicGate1 = 0
    transform crawlScroll:
        yalign 0.0 xalign 0.5
        linear 50.0 yalign 1.0
        
    transform basicfade:
        on show:
            alpha 0.0
            linear 0.3 alpha 1.0
        on hide:
            linear 0.1 alpha 0.0   

    #play music "audio/Main_Title_BGM.wav"
    play channel00 mt_bellsL
    play channel01 mt_bellsR
    play channel02 mt_piano
    play channel03 mt_ghostBus
    play channel04 mt_ghostL
    play channel05 mt_ghostR
    play channel06 mt_orchestra
    play channel07 mt_sciFi
    play channel08 mt_touchOrchestra
    play channel09 mt_tornado
    play channel10 mt_ultrasweeper
    play channel11 mt_violins
    play channel12 mt_wistful

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
    
    scene bg G_deskArea with fade #at basicfade
    with None 
    $ quick_menu = True
    #with fade(5.0)
    jump prologue
