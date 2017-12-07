# The script of the game goes in this file.
image splash = "errorSplashscreen.png"
image mm_base = "mm_idle.png"
#Character Declarations
define g = Character("Grace", color ="#006d0d")
define a = Character("Ada", color="#3a416c")
define secretary = Character("Virtual Secretary", color ="#383838") 
define h = Character("Director Hirose", color="8b00bf")
define knuth = Character("Chief Knuth", color="#5a0167")
define neva = Character("Chief Nevanlinna", color="#5a0167")
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
define investigator1 = Character("Detective", color="#000000")
define investigator2 = Character("Officer 1", color="#000000")
define investigator3= Character("Officer 2", color="#000000")
define unknown=Character("???", color="#000000")

#Sprites for the Conclave
image Nevalinna speaking = "sprites/Nevalinna.png"
image Cray speaking = "sprites/Cray.png"
image Knuth speaking = "sprites/Knuth.png"
image Godel speaking = "sprites/Godel.png"
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
image Mopr = "sprites/MOPR.png"
image Lynn = "sprites/Lynn_Sprite.png"
image Lynn empty = "phone_0.png"
image Blue happy = "sprites/blueHappy.png"
image Blue smug = "sprites/blueSmug.png"
image Blue threaten = "sprites/blueThreaten.png"
image Blue pout = "sprites/bluePout.png"
image Blue flirty = "sprites/blueFlirty.png"
image Blue confused = "sprites/blueConfused.png"
image Blue neutral = "sprites/blueNormal.png"
image Blue angry = "sprites/blueAngry.png"
image Hirose neutral = "sprites/hirose_neutral.png"
image Hirose thoughtful = "sprites/hirose_thoughtful.png"
image Hirose pleased = "sprites/hirose_pleased.png"
image Hirose angry = "sprites/hirose_angry.png"
image Hirose annoyed = "sprites/hirose_annoyed.png"
image Hirose concerned = "sprites/hirose_concerned.png"
image Colossus = "sprites/Colossus.png"
image EG_main angry = "sprites/EG_Main_Angry.png"
image EG_main inquisitive = "sprites/EG_Main_Inquisitive.png"
image EG_main neutral = "sprites/EG_Main_Neutral.png"
image EG_main unamused = "sprites/EG_Main_Unamused.png"
image EG_ov angry = "sprites/EG_Overview_Angry.png"
image EG_ov inquisitive = "sprites/EG_Overview_Inquisitive.png"
image EG_ov neutral = "sprites/EG_Overview_Neutral.png"
image EG_ov unamused = "sprites/EG_Overview_Unamused.png"
image EG angry = "sprites/EG_angry.png"
image EG unamused = "sprites/EG_unamused.png"
image EG neutral = "sprites/EG_neutral.png"
image EG inquisitive = "sprites/EG_inquisitive.png"

image Ivan dour = "sprites/ivan_dour.png"
image Ivan phony = "sprites/ivan_phonySmile.png"
image Ivan disgusted  = "sprites/ivan_disgusted.png"
image Ivan defensive = "sprites/ivan_defensive.png"
image Alan worried = "sprites/alan_worried.png"
image Alan happy = "sprites/alan_happy.png"
image Alan neutral = "sprites/alan_neutral.png"
image Alan confused = "sprites/alan_confused.png"

image inv1 = "sprites/koman.png"
image inv2 = "sprites/brodowsky.png"
image Detective = "sprites/Laslo.png"

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
image bg lgEasy1 = "tutorials_lgEasy_1.png"
image bg lgEasy2 = "tutorials_lgEasy_2.png"
image bg lgEasy2b = "tutorials_lgEasy_3.png"
image bg lgEasy3 = "truthTable_instructions.png"
image bg lgEasy4 = "NOT_instructions.png"
image bg lgEasy5 = "AND_OR_instructions.png"
image bg tutorial_inv_1 = "inv_instruction1.png"
image bg tutorial_inv_2 = "inv_instruction2.png"
image bg gramEasy1 = "easyGrammar_Tut1.png"
image bg gramEasy2 = "easyGrammar_Tut2.png"
image bg gramEasy3 = "easyGrammar_Tut3.png"
image bg gramEasy3b = "easyGrammar_Tut3b.png"
image bg gramEasy4 = "easyGrammar_Tut4.png"
image bg gramEasy5 = "easyGrammar_Tut5.png"
image bg gramEasy6 = "easyGrammar_Tut6.png"
image bg gramEasy7 = "easyGrammar_Tut7.png"
image bg tutorial_binary2Bit_1 = "binary_tutorial1.png"
image bg tutorial_binary2Bit_2 = "binary_tutorial2.png"
image bg tutorial_binary2Bit_3 = "binary_tutorial3.png"
image bg tutorial_binary2Bit_4 = "binary_tutorial4.png"
image bg tutorial_binary2Bit_5 = "binary_tutorial5.png"
image bg tutorial_LL1 = "ll_easy_Tutorial.png"
image bg tutorial_LL1b = "ll_easy_Tutorial1b.png"
image bg tutorial_LL2 = "ll_easy_Tutorial2.png"
image bg tutorial_LL3 = "ll_easy_Tutorial3.png"
image bg tutorial_lgMed = "tutorials_lgMed.png"
image bg tutorial_lgHard = "tutorials_lgHard.png"
image bg tutorial_binaryMed = "tutorials_binaryMed.png"
image bg tutorial_binaryHard_1 = "tutorials_binaryHard1.png"
image bg tutorial_binaryHard_2 = "tutorials_binaryHard2.png"
image bg tutorial_llMed = "tutorials_llMed.png"
image bg tutorial_llHard_1 = "tutorials_llHard_1.png"
image bg tutorial_llHard_2 = "tutorials_llHard_2.png"
image bg tutorial_gramMed = "tutorials_gramMed.png"
image bg tutorial_gramHard = "tutorials_gramHard.png"


##The Conclave
image bg conclaveWaitingRoom = "bg/ConclaveReception_Main.png"
image bg conclaveDoor = "bg/ConclaveReception_Close.png"
image bg conclave = "bg/Conclave_Proper.png"
image bg conclaveOccupied = "bg/Conclave_Occupied.png"
image other darken = "blackout.png"
                       
#Hirose's Space
image bg hiroseDoor= "bg/Hirose_Door.png"
image bg hiroseOfficeDesk = "bg/Hirose_OfficeDesk.png"
image bg hiroseOfficeDesk2 = "bg/Hirose_OfficeDeskLoggedIn.png"
image bg hiroseOfficeMain = "bg/Hirose_OfficeMain.png"
image bg hiroseOfficeTransition = "bg/Hirose_OfficeTransition.png"
image bg hirosePersonalBed = "bg/Hirose_PersonalBed.png"
image bg hirosePersonalComputer = "bg/Hirose_PersonalComputer.png"
image bg hirosePersonalComputer_logged = "bg/Hirose_PersonalComputerLoggedIn.png"
image bg hirosePersonalArea = "bg/Hirose_PersonalMain.png"
image bg hirosePersonalArea_logged = "bg/Hirose_PersonalMain_Login.png"
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

#Transition shots
image bg prologue = "images/bg/PrologueTransition.png"
image bg chapterOne = "images/bg/ChapterOneTransition.png"
image bg chapterTwo = "images/bg/ChapterTwoTransition.png"
image bg chapterThree = "images/bg/ChapterThreeTransition.png"
image bg chapterFour = "images/bg/ChapterFourTransition.png"
image bg chapterFiveS= "images/bg/ChapterFiveSTransition.png"
image bg chapterFiveSbE = "images/bg/ChapterFiveSbETransition.png"
image bg chapterFiveE = "images/bg/ChapterFiveETransition.png"
image bg endDemo = "images/bg/endOfDemo.png"

#Hallway Shots
image bg hallwayBalcony = "images/bg/Hallway_Balcony1.png"
image bg hallwayGrace2 = "images/bg/Hallway_Grace2.png"
image bg hallwayLab2 = "images/bg/Hallway_Lab2.png"
image bg hallwayLab2Door = "images/bg/Hallway_Lab2Door.png"
image bg door2 = "bg/WW_Door.png"

#Lab 2
image bg lab2Main_locked = "images/bg/Lab2_Overview_Locked.png"
image bg lab2Main_unlocked = "images/bg/Lab2_Overview_Unlocked.png"
image bg lab2Main_Ivan = "images/bg/Lab2_Overview_NightshiftLocked.png"
image bg lab2WS_locked = "images/bg/Lab2_Workstation_Locked.png"
image bg lab2WS_unlocked = "images/bg/Lab2_Workstation_Unlocked.png"
image bg lab2Ivan_locked = "images/bg/Lab2_Ivan_Locked.png"
image bg lab2_cord = "images/bg/Lab2_Main_Locked_Cable.png"
image bg lab2_noCord = "images/bg/Lab2_Main_Locked_Table.png"
image bg lab2Ivan_unlocked = "images/bg/Lab2_Ivan_Unlocked.png"
image bg lab2Table_locked = "images/bg/Lab2_Main.png"
image bg lab2Table_unlocked = "images/bg/Lab2_Main_Unlocked.png"

image bg PG = "images/bg/puzzleBG.png"
#AI Core
image bg AICoreDoor = "images/bg/AICore_Door.png"
image bg AICoreHallway = "images/bg/AICore_Hallway.png"
image bg AICoreLong = "images/bg/AICore_HallwayLong.png"
image bg AICoreMain = "images/bg/AICore_Main.png"
image bg AICoreOverview = "images/bg/AICore_Overview.png"
image bg AICoreStairs = "images/bg/AICore_Stairs.png"

#Blue's Workspace
image bg creepyHallwayLong = "images/bg/Blue_CreepyHallwayLong.png"
image bg creepyHallwayMed = "images/bg/Blue_CreepyHallwayMed.png"
image bg creepyHallwayDoor = "images/bg/Blue_CreepyHallwayDoor.png"
image bg blueCore = "images/bg/Blue_BlueCore.png"
image bg blueStairs = "images/bg/Blue_BlueStairs.png"
image bg blueLeft = "images/bg/Blue_HumanSpaceLeft.png"
image bg blueRight = "images/bg/Blue_HumanSpaceRight.png"
image bg blueMain = "images/bg/Blue_HumanSpaceMain.png"

#Watson's Server
image bg wsDesk = "images/bg/WS_Desk.png"
image bg wsMain = "images/bg/WS_DeskArea.png"
image bg wsOverview = "images/bg/WS_Overview.png"
image bg wsSafe = "images/bg/WS_Safe.png"
image bg wsDesk_drive = "images/bg/WS_Desk_Drive.png"
image bg wsMain_drive = "images/bg/WS_DeskArea_Drive.png"

#Watson's Workspace
image bg wwLongCrit = "images/bg/WW_Overview_CRITICAL.png"
image bg wwLongNom = "images/bg/WW_Overview_NOMINAL.png"
image bg wwMedCrit = "images/bg/WW_Walkway_CRITICAL.png"
image bg wwMedNom = "images/bg/WW_Walkway_NOMINAL.png"
image bg wwStairs = "images/bg/WW_StairsDown.png"
image bg wwWorkArea = "images/bg/WW_WorkArea.png"
image bg wwNominal = "images/bg/WW_BigScreen_NOMINAL.png"
image bg wwCritical = "images/bg/WW_BigScreen_CRITICAL.png"

#Oxygen Garden
image bg ogOverview = "images/bg/OG_Overview.png"
image bg ogStairs = "images/bg/OG_Stairs.png"
image bg ogLong = "images/bg/OG_LongView.png"
image bg ogClose = "images/bg/OG_CloseView.png"

#Miscellaneous
image bg Logic_Gate = "LOGIC_GATE_BG.png"
image bg black = "blackScreen.png"
image bg binary = "tileBackground.png"
        

define dissolve = Dissolve (1.0)

image Tosh neutral = "sprites/Tosh_Happy.png"

#Audio names
#main theme
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

#logic gate puzzle sounds
define audio.pipeFlowR = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_01.ogg"
define audio.pipeFlowG = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_02.ogg"
define audio.pipeFlowN = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_03.ogg"
define audio.lgWin = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_RightOutput.ogg"
define audio.lgLose = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_WrongOutput.ogg"

#grammar puzzle sounds
define audio.gramWin = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_RightSolution.ogg"
define audio.gramLose = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_WrongSolution.ogg"
define audio.gramText1 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TextEnterNoise_01.ogg"
define audio.gramText2 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TextEnterNoise_02.ogg"
define audio.gramText3 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TextEnterNoise_03.ogg"
define audio.gramTree1 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_02.ogg"
define audio.gramTree2 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_01.ogg"
define audio.gramTree3 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_03.ogg"
define audio.gramTree4 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_04.ogg"
define audio.gramTree5 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_05.ogg"

define audio.llLose = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_LoseSound.ogg"
define audio.llCharge = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_BatteryChargeUp.ogg"
define audio.llLightOff1 = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_LightsOff_01.ogg"
define audio.llLightOff2 = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_LightsOff_02.ogg"
define audio.llLightOff3 = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_LightsOff_03.ogg"
define audio.llLightOn1 = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_LightsOn_01.ogg"
define audio.llLightOn2 = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_LightsOn_02.ogg"
define audio.llLightOn3 = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_LightsOn_03.ogg"
define audio.llPipe1 = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_PipeFlow_01.ogg"
define audio.llPipe2 = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_PipeFlow_02.ogg"
define audio.llPipe3 = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_PipeFlow_03.ogg"
define audio.llWin = "music/UI/loopLogicPuzzle/EHNF_UI_LoopLogicPuzzle_WinSound.ogg"

#door sounds
define audio.doorOpen1 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_OPEN_1.ogg"
define audio.doorOpen2 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_OPEN_2.ogg"
define audio.doorClose1 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_CLOSE_1.ogg"
define audio.doorClose2 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_CLOSE_2.ogg"
define audio.doorDenied = "music/Object/Door_Audio/ENHF_Object_Door_AccessDenied.ogg"
define audio.doorAccess= "music/Object/Door_Audio/ENHF_Object_Door_AccessGranted.ogg"
define audio.doorScan = "music/Object/Door_Audio/EHNF_OBJECT_Door_Scan.ogg"

#balcony ambience sounds
define audio.balconyAmb = "music/Amb/Balcony/EHNF_BAL_AMB.ogg"
define audio.balconyBGM = "music/BGM/EHNF_BAL_BGM.ogg"

#Watson's Workspace Ambience
define audio.wwAmb0 = "music/Amb/watsonWorkspace/EHNF_WW_L0.ogg"
define audio.wwAmb1 = "music/Amb/watsonWorkspace/EHNF_WW_L1.ogg"
define audio.wwAmb2 = "music/Amb/watsonWorkspace/EHNF_WW_L2.ogg"
define audio.wwAmb3 = "music/Amb/watsonWorkspace/EHNF_WW_L3.ogg"
define audio.wwAmb4 = "music/Amb/watsonWorkspace/EHNF_WW_L4.ogg"
define audio.wwAmb5 = "music/Amb/watsonWorkspace/EHNF_WW_L5.ogg"
define audio.wwAmb6 = "music/Amb/watsonWorkspace/EHNF_WW_L6.ogg"

#Watson Server Ambiance
define audio.wsAmb0 = "music/Amb/WS/EHNF_WS_L0.ogg"
define audio.wsAmb1 = "music/Amb/WS/EHNF_WS_L1.ogg"
define audio.wsAmb2 = "music/Amb/WS/EHNF_WS_L2.ogg"
define audio.wsAmb3 = "music/Amb/WS/EHNF_WS_L3.ogg"
define audio.wsAmb4 = "music/Amb/WS/EHNF_WS_L4.ogg"
define audio.wsAmb5 = "music/Amb/WS/EHNF_WS_L5.ogg"
define audio.wsAmb6 = "music/Amb/WS/EHNF_WS_L6.ogg"
define audio.wsAmb7 = "music/Amb/WS/EHNF_WS_L7.ogg"

#Conclave audio
define audio.conclaveReceptionAmb = "music/amb/Conclave/Ambiance_Conclave_Reception_Area.ogg"
define audio.conclaveProperAmb = "music/amb/Conclave/EHNF_CC_Amb.mp3"
#define audio.conclaveProperAmb = "music/amb/Conclave/Ambiance_Conclave_Proper.ogg"

#Grace lab audio
define audio.typing = "music/Amb/Grace_Lab/Typing/EHNF_AMB_Grace_Lab_TYP_L_0.ogg"
define audio.graceLabAmb = "music/Amb/Grace_Lab/Normal/EHNF_Grace_Lab_Norm.ogg"

define audio.hallwayAmb = "music/Amb/Hallway/EHNF_Hall_AMB.ogg"

#hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"

#hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
#                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"

define audio.ch5BGM = "music/EHNF_CH5.mp3"
#Hirose audio 1
define audio.hiroseOffice1_00 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L0.ogg"
define audio.hiroseOffice1_01 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L1.ogg"
define audio.hiroseOffice1_02 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L2.ogg"
define audio.hiroseOffice1_03 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L3.ogg"
define audio.hiroseOffice1_04 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L4.ogg"
define audio.hiroseOffice1_05 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L5.ogg"
define audio.hiroseOffice1_06 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L6.ogg"
define audio.hiroseOffice1_07 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L7.ogg"
define audio.hiroseOffice1_08 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L8.ogg"
define audio.hiroseOffice1_09 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L9.ogg"
define audio.hiroseOffice1_10 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L10.ogg"
define audio.hiroseOffice1_11 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L11.ogg"
define audio.hiroseOffice1_12 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L12.ogg"
define audio.hiroseOffice1_13 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L13.ogg"
define audio.hiroseOffice1_14 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L14.ogg"
define audio.hiroseOffice1_15 = "music/Amb/Hirose_Office/L1/EHNF_Hirose1_AMB_L15.ogg"
#hirose audio 2
define audio.hiroseOffice2_00 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L0.ogg"
define audio.hiroseOffice2_01 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L1.ogg"
define audio.hiroseOffice2_02 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L2.ogg"
define audio.hiroseOffice2_03 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L3.ogg"
define audio.hiroseOffice2_04 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L4.ogg"
define audio.hiroseOffice2_05 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L5.ogg"
define audio.hiroseOffice2_06 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L6.ogg"
define audio.hiroseOffice2_07 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L7.ogg"
define audio.hiroseOffice2_08 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L8.ogg"
define audio.hiroseOffice2_09 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L9.ogg"
define audio.hiroseOffice2_10 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L10.ogg"
define audio.hiroseOffice2_11 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L11.ogg"
define audio.hiroseOffice2_12 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L12.ogg"
define audio.hiroseOffice2_13 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L13.ogg"
define audio.hiroseOffice2_14 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L14.ogg"
define audio.hiroseOffice2_15 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L15.ogg"
define audio.hiroseOffice2_16 = "music/Amb/Hirose_Office/L2/EHNF_Hirose2_AMB_L16.ogg"
#hirose audio 3
define audio.hiroseOffice3_00 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L0.ogg"
define audio.hiroseOffice3_01 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L1.ogg"
define audio.hiroseOffice3_02 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L2.ogg"
define audio.hiroseOffice3_03 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L3.ogg"
define audio.hiroseOffice3_04 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L4.ogg"
define audio.hiroseOffice3_05 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L5.ogg"
define audio.hiroseOffice3_06 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L6.ogg"
define audio.hiroseOffice3_07 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L7.ogg"
define audio.hiroseOffice3_08 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L8.ogg"
define audio.hiroseOffice3_09 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L9.ogg"
define audio.hiroseOffice3_10 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L10.ogg"
define audio.hiroseOffice3_11 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L11.ogg"
define audio.hiroseOffice3_12 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L12.ogg"
define audio.hiroseOffice3_13 = "music/Amb/Hirose_Office/L3/EHNF_Hirose3_AMB_L13.ogg"

#Lab 2
define audio.lab2Amb_0 = "music/Amb/Lab2/EHNF_LAB2_L0.ogg"
define audio.lab2Amb_1 = "music/Amb/Lab2/EHNF_LAB2_L1.ogg"
define audio.lab2Amb_2 = "music/Amb/Lab2/EHNF_LAB2_L2.ogg"
define audio.lab2Amb_3 = "music/Amb/Lab2/EHNF_LAB2_L3.ogg"
define audio.lab2Amb_4 = "music/Amb/Lab2/EHNF_LAB2_L4.ogg"
define audio.lab2Amb_5 = "music/Amb/Lab2/EHNF_LAB2_L5.ogg"
define audio.lab2Amb_6 = "music/Amb/Lab2/EHNF_LAB2_L6.ogg"
define audio.lab2Amb_7 = "music/Amb/Lab2/EHNF_LAB2_L7.ogg"
define audio.lab2Amb_8 = "music/Amb/Lab2/EHNF_LAB2_L8.ogg"
define audio.lab2Amb_9 = "music/Amb/Lab2/EHNF_LAB2_L9.ogg"
define audio.lab2Amb_10 = "music/Amb/Lab2/EHNF_LAB2_L10.ogg"
define audio.lab2Amb_11 = "music/Amb/Lab2/EHNF_LAB2_L11.ogg"

#Oxygen Garden
define audio.ogAmb_0 = "music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L0.ogg"
define audio.ogAmb_1 = "music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L1.ogg"
define audio.ogAmb_2 = "music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L2.ogg"
define audio.ogAmb_3 = "music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L3.ogg"
define audio.ogAmb_4 = "music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L4.ogg"
define audio.ogAmb_5 = "music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L5.ogg"
define audio.ogAmb_6 = "music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L6.ogg"
define audio.ogAmb_7 = "music/Amb/Oxygen_Garden/EHNF_Oxygen_Garden_L7.ogg"

#BGM
#AI core
define audio.AICoreMusic_0 = "music/BGM/AI_Core/EHNF_L0_BGM_AI_Ref.ogg"
define audio.AICoreMusic_1 = "music/BGM/AI_Core/EHNF_L1_BGM_AI_Piano.ogg"
define audio.AICoreMusic_2 = "music/BGM/AI_Core/EHNF_L2_BGM_AI_Bass.ogg"
define audio.AICoreMusic_3 = "music/BGM/AI_Core/EHNF_L3_BGM_AI_String.ogg"
define audio.AICoreMusic_4 = "music/BGM/AI_Core/EHNF_L4_BGM_AI_Synth.ogg"
define audio.AICoreMusic_5 = "music/BGM/AI_Core/EHNF_L5_BGM_AI_Synth_Key.ogg"
define audio.AICoreMusic_6 = "music/BGM/AI_Core/EHNF_L6_BGM_AI_String2.ogg"
define audio.AICoreMusic_7 = "music/BGM/AI_Core/EHNF_L7_BGM_AI_Arp_Synth.ogg"
define audio.AICoreMusic_8 = "music/BGM/AI_Core/EHNF_L8_BGM_AI_Elec_Guit.ogg"
define audio.AICoreMusic_9 = "music/BGM/AI_Core/EHNF_L9_BGM_AI_Thunder.ogg"
define audio.AICoreMusic_10 = "music/BGM/AI_Core/EHNF_L10_BGM_AI_String_Bus.ogg"
define audio.AICoreMusic_11 = "music/BGM/AI_Core/EHNF_L11_BGM_AI_Kick.ogg"
#define audio.AICoreMusic_12 = "music/BGM/AI_Core/EHNF_L12_BGM_AI_Ref.ogg"
define audio.AICoreMusic_13 = "music/BGM/AI_Core/EHNF_L13_BGM_AI_Snare.ogg"
define audio.AIAmb_00 = "music/Amb/AI_Core/EHNF_AC_L0.ogg"
define audio.AIAmb_01 = "music/Amb/AI_Core/EHNF_AC_L1.ogg"
define audio.AIAmb_02 = "music/Amb/AI_Core/EHNF_AC_L2.ogg"
define audio.AIAmb_03 = "music/Amb/AI_Core/EHNF_AC_L3.ogg"
define audio.AIAmb_04 = "music/Amb/AI_Core/EHNF_AC_L4.ogg"
define audio.AIAmb_05 = "music/Amb/AI_Core/EHNF_AC_L5.ogg"

#Blue
define audio.BlueBGM_0 = "music/BGM/Blue/EHNF_L0_BGM_Blue_Kick.ogg"
define audio.BlueBGM_1 = "music/BGM/Blue/EHNF_L1_BGM_Blue_Ghost_Kick.ogg"
define audio.BlueBGM_2 = "music/BGM/Blue/EHNF_L2_BGM_Blue_3p_Horn_Bus.ogg"
define audio.BlueBGM_3 = "music/BGM/Blue/EHNF_L3_BGM_Blue_Snare.ogg"
define audio.BlueBGM_4 = "music/BGM/Blue/EHNF_L4_BGM_Blue_Percussion.ogg"
define audio.BlueBGM_5 = "music/BGM/Blue/EHNF_L5_BGM_Blue_Cymbals_Large.ogg"
define audio.BlueBGM_6 = "music/BGM/Blue/EHNF_L6_BGM_Blue_Cymbals_Small.ogg"
define audio.BlueBGM_7 = "music/BGM/Blue/EHNF_L7_BGM_Blue_Cymbals_Swells.ogg"
define audio.BlueBGM_8 = "music/BGM/Blue/EHNF_L8_BGM_Blue_Glass_Mallet.ogg"
define audio.BlueBGM_9 = "music/BGM/Blue/EHNF_L9_BGM_Blue_Liquid_Mallet.ogg"
define audio.BlueBGM_10 = "music/BGM/Blue/EHNF_L10_BGM_Blue_Reflective_Mallet.ogg"
define audio.BlueBGM_11 = "music/BGM/Blue/EHNF_L11_BGM_Blue_Grime_Bass.ogg"
define audio.BlueBGM_12 = "music/BGM/Blue/EHNF_L12_BGM_Blue_Sub_Bass.ogg"
define audio.BlueBGM_13 = "music/BGM/Blue/EHNF_L13_BGM_Blue_Sparkling_Water_Drops.ogg"
define audio.BlueBGM_14 = "music/BGM/Blue/EHNF_L14_BGM_Blue_Ambient_Room_Pad.ogg"
define audio.BlueBGM_15 = "music/BGM/Blue/EHNF_L15_BGM_Blue_Strings_Legatto.ogg"
define audio.BlueBGM_16 = "music/BGM/Blue/EHNF_L16_BGM_Blue_Strings_Staccato.ogg"
define audio.BlueBGM_17 = "music/BGM/Blue/EHNF_L17_BGM_Blue_Strings_Tremelo.ogg"
define audio.BlueBGM_18 = "music/BGM/Blue/EHNF_L18_BGM_Blue_Wire_Pluck.ogg"
define audio.BlueBGM_19 = "music/BGM/Blue/EHNF_L19_BGM_Blue_Flutes_Disonant.ogg"
define audio.BlueBGM_20 = "music/BGM/Blue/EHNF_L20_BGM_Blue_French_Horn_Legatto.ogg"
define audio.BlueBGM_21 = "music/BGM/Blue/EHNF_L21_BGM_Blue_French_Horn_Staccato.ogg"
define audio.BlueAmb_00 = "music/Amb/Blue/EHNF_BW_L0.ogg"
define audio.BlueAmb_01 = "music/Amb/Blue/EHNF_BW_L1.ogg"
define audio.BlueAmb_02 = "music/Amb/Blue/EHNF_BW_L2.ogg"
define audio.BlueAmb_03 = "music/Amb/Blue/EHNF_BW_L3.ogg"

#Lab 2/Grace Lab music?
define audio.labBGM_0 = "music/BGM/Lab2/EHNF_LAB2_BGM.ogg"
define audio.labBGM_1 = "music/AMB/Lab2/EHNF_LAB2_AMB.ogg"

#Oxygen Garden
define audio.ogBGM_0 = "music/BGM/Oxygen_Garden/EHNF_L0_BGM_Oxy_Piano_Harm_Mid.ogg"
define audio.ogBGM_1 = "music/BGM/Oxygen_Garden/EHNF_L1_BGM_Oxy_Piano_Harm_Low.ogg"
define audio.ogBGM_2 = "music/BGM/Oxygen_Garden/EHNF_L2_BGM_Oxy_Double_Bass.ogg"
define audio.ogBGM_3 = "music/BGM/Oxygen_Garden/EHNF_L3_BGM_Oxy_Pad.ogg"
define audio.ogBGM_4 = "music/BGM/Oxygen_Garden/EHNF_L4_BGM_Oxy_Bells.ogg"
define audio.ogBGM_5 = "music/BGM/Oxygen_Garden/EHNF_L5_BGM_Oxy_BG_CounterMelody_Synth.ogg"
define audio.ogBGM_6 = "music/BGM/Oxygen_Garden/EHNF_L6_BGM_Oxy_BG_CounterMelody_Verb.ogg"
define audio.ogBGM_7 = "music/BGM/Oxygen_Garden/EHNF_L7_BGM_Oxy_Piano_Melody.ogg"
define audio.ogBGM_8 = "music/BGM/Oxygen_Garden/EHNF_L8_BGM_Oxy_Room_Short_Verb.ogg"

#Character SFX
#Ada
define audio.adaClumsy = "music/Character/ADA/EHNF_ADA_Movement_Clumsy.ogg"
define audio.adaDoor = "music/Character/ADA/EHNF_ADA_Movement_Clumsy_Door.ogg"
define audio.adaWalk = "music/Character/ADA/EHNF_ADA_Movement_Normal.ogg"
define audio.adaGraceful = "music/Character/ADA/EHNF_ADA_Movement_Graceful.ogg"

#Alpha
define audio.alphaFailure = "music/Character/ALPHA/EHNF_Character_Alpha_Failure.ogg"
define audio.alphaStartup = "music/Character/ALPHA/EHNF_Character_Alpha_Startup.ogg"
define audio.facePlate = "music/Character/ALPHA/ENHF_Character_Alpha_FacePlateRemoval.ogg"

#Blue
define audio.blueClaws = "music/Character/Blue/EHNF_Blue_Claws.ogg"
define audio.blueLaugh = "music/Character/Blue/EHNF_Blue_Laughter.ogg"

#Grace
define audio.graceWalk = "music/Character/Grace/EHNF_Grace_Footsteps_Normal.ogg"
define audio.graceHurry = "music/Character/Grace/EHNF_Grace_Footsteps_Hurried.ogg"
define audio.graceTea = "music/Character/Grace/ENHF_Grace_SippingTea_001.ogg"
define audio.graceTea2 = "music/Character/Grace/ENHF_Grace_SippingTea_002.ogg"

#MOPR
define audio.moprAlarmed = "music/Character/MOPR/ENHF_MOPR_AlarmedShrill.ogg"
define audio.moprAlarmed2 = "music/Character/MOPR/ENHF_MOPR_AlarmedShrill2.ogg"
define audio.moprConfused = "music/Character/MOPR/ENHF_MOPR_Confused.ogg"
define audio.moprConfused2 = "music/Character/MOPR/ENHF_MOPR_Confused2.ogg"
define audio.moprCurious = "music/Character/MOPR/ENHF_MOPR_Curious.ogg"
define audio.moprCurious2 = "music/Character/MOPR/ENHF_MOPR_Curious2.ogg"
define audio.moprHappy = "music/Character/MOPR/ENHF_MOPR_Happy.ogg"
define audio.moprHappy2 = "music/Character/MOPR/ENHF_MOPR_Happy2.ogg"
define audio.moprInquisitive = "music/Character/MOPR/ENHF_MOPR_Inquistive.ogg"
define audio.moprInquisitive2 = "music/Character/MOPR/ENHF_MOPR_Inquistive2.ogg"
define audio.moprSad = "music/Character/MOPR/ENHF_MOPR_Sad.ogg"
define audio.moprSad2 = "music/Character/MOPR/ENHF_MOPR_Sad2.ogg"
define audio.moprSuspicious = "music/Character/MOPR/ENHF_MOPR_Suspicous.ogg"
define audio.moprSuspicious2 = "music/Character/MOPR/ENHF_MOPR_Suspicous2.ogg"
define audio.moprAffirmative = "music/Character/MOPR/MOPR_Affirmative_1.mp3"
define audio.moprAffirmative2 = "music/Character/MOPR/MOPR_Affirmative_2.mp3"
define audio.moprWorried = "music/Character/MOPR/MOPR_Worried_1.mp3"
define audio.moprWorried2 = "music/Character/MOPR/MOPR_Worried_2.mp3"

#Tosh
define audio.toshStartup = "music/Character/Tosh/EHNF_CH_Tosh_Startup.ogg"

#Objects
#Bracelet audio
define audio.beepLoud = "music/Object/Bracelet_Audio/EHNF_OBJECT_BRACELET_BEEP_LOUD.ogg"
define audio.beepMedium = "music/Object/Bracelet_Audio/EHNF_OBJECT_BRACELET_BEEP_MED.ogg"
define audio.beepSoft = "music/Object/Bracelet_Audio/EHNF_OBJECT_BRACELET_BEEP_SOFT.ogg"
define audio.dialtone = "music/Object/Bracelet_Audio/EHNF_OBJECT_BRACELET_PHONEDIALTONE.ogg"
define audio.answertone = "music/Object/Bracelet_Audio/EHNF_OBJECT_BRACELET_RING_ANSWERTONE.ogg"

#Computer audio
define audio.computer1 = "music/Object/Computer_Audio/EHNF_Computer_Start_01.ogg"
define audio.computer2 = "music/Object/Computer_Audio/EHNF_Computer_Start_02.ogg"
define audio.computer3 = "music/Object/Computer_Audio/EHNF_Computer_Start_03.ogg"
define audio.computer4 = "music/Object/Computer_Audio/EHNF_Computer_Start_04.ogg"

#Misc
define audio.marching = "music/Object/Misc_Audio/EHNF_InvestigatorsMarching.ogg"
define audio.clue = "music/Object/Misc_Audio/EHNF_Item_Clue.ogg"
define audio.pickup = "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
define audio.speakerCrackle = "music/Object/Misc_Audio/EHNF_Speaker_Crackle1.ogg"
define audio.shortWhiteNoise = "music/Object/Misc_Audio/EHNF_White_Noise_1Sec.ogg"
define audio.longWhiteNoise = "music/Object/Misc_Audio/EHNF_White_Noise_20Sec.ogg"
define audio.paperCrumple = "music/Object/Misc_Audio/EHNF_Paper_Crumple_OB.ogg"


#Raptor
define audio.raptor1 = "music/Object/Raptor_Audio/Robot_Velociraptor1.ogg"
define audio.raptor2 = "music/Object/Raptor_Audio/Robot_Velociraptor2.ogg"

#UI
#Bracelet UI
define audio.braceletHighlight = "music/UI/Bracelet_Phone/EHNF_UI_BRACELET_PHONE_HIGHLIGHT.ogg"
define audio.braceletSelect = "music/UI/Bracelet_Phone/EHNF_UI_BRACELET_PHONE_SELECTED.ogg"

#Dialogue select
define audio.dialogueSelect = "music/UI/Dialogue_Select/EHNF_UI_DialogueSelect_Click.ogg"
define audio.dialogueHighlight = "music/UI/Dialogue_Select/EHNF_UI_DialogueSelect_Highlight.ogg"

#Investigate
define audio.investigateHighlight = "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
define audio.investigateSelect = "music/UI/Investigate/ENHF_Investigate_Selected.ogg"

#logicGatePuzzle
define audio.lgFlow1 = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_01.ogg"
define audio.lgFlow2 = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_02.ogg"
define audio.lgFlow3 = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_03.ogg"
define audio.lgWin = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_RightOutput.ogg"
define audio.lgLose = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_WrongOutput.ogg"

#Main Menu
define audio.mmHighlight = "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
define audio.mmClick = "music/UI/mainMenu/ENHF_UI_MM_Click.ogg"

#Binary Puzzle
define audio.binaryRight = "music/UI/Puzzle/EHNF_UI_Puzzle_BinaryCorrectLight.ogg"
define audio.binaryWrong = "music/UI/Puzzle/EHNF_UI_Puzzle_BinaryWrongLight.ogg"
define audio.binaryLose = "music/UI/Puzzle/EHNF_UI_Puzzle_Lose.ogg"
define audio.binaryLose2 = "music/UI/Puzzle/EHNF_UI_Puzzle_Lose2.ogg"
define audio.binaryWin = "music/UI/Puzzle/EHNF_UI_Puzzle_Win.ogg"
define audio.tileFlip1 = "music/UI/Puzzle/ENHF_Tile_Flip_V2_001.ogg"
define audio.tileFlip2 = "music/UI/Puzzle/ENHF_Tile_Flip_V2_002.ogg"
define audio.tileFlip3 = "music/UI/Puzzle/ENHF_Tile_Flip_V2_003.ogg"

define audio.ui1 = "music/UI/ENHF_UI_Button_v1.ogg"
define audio.ui2 = "music/UI/ENHF_UI_Button_v2.ogg"
define audio.menuEnter = "music/UI/ENHF_UI_Menu_Enter.ogg"
define audio.menuExit = "music/UI/ENHF_UI_Menu_Exit.ogg"
init -100 python:
    databasePage = 1
    puzzleGallery = False
#    config.image_cache_size = 50
init: 
    $ config.keymap['hide_windows'].remove('mouseup_2')
init python:
    renpy.music.register_channel("channel00", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel01", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel02", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel03", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel04", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel05", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel06", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel07", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel08", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel09", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel10", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel11", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel12", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel13", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel14", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel15", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel16", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel17", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel18", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel19", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel20", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel21", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel22", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel23", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel24", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel25", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel26", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("channel27", mixer="music", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    
    
    renpy.music.register_channel("sound01", mixer="sfx", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("sound02", mixer="sfx", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("sound03", mixer="sfx", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("sound04", mixer="sfx", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("sound05", mixer="sfx", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("sound06", mixer="sfx", loop=True, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)

    renpy.music.register_channel("soundP01", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("soundP02", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("soundP03", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("soundP04", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("soundP05", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("soundP06", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("soundP07", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("soundP08", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("soundP09", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("soundP10", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)
    renpy.music.register_channel("soundP11", mixer="sfx", loop=False, stop_on_mute=True, tight=True, file_prefix="", file_suffix="", buffer_queue=True)


    config.rollback_side_size = 0.0
    rollback_side = None
    config.main_menu_music = "music/EHNF_Main_Theme.ogg"
    #atl_transform ::= "transform" scrolling_vertical "("parameters")" ":"
init python:
    centerScreen = Position(xpos=0.5, xanchor =0.5, ypos =0.2, yanchor = 0.2)
    centerScreen2 = Position(xpos=0.5, xanchor =0.5, ypos =0.35, yanchor = 0.2)
    currentPage_journal = 0
    currentPage_notes = 0
    pageUnlocked_journal=6
    pageUnlocked_notes = 0
    journal1 = False
    journal2 = ""
    journal3 = ""
    journal4 = ""
    journal5 = ""
    journal6 = ""
    notes_hard1 = "none"
    notes_hard2 = "none"
    notes_hard3 = "none"
    nearLeft = Position(xpos=0.27, xanchor=0.1, ypos=0.1, yanchor = 0.1)
    invLeft = Position(xpos=0.2, xanchor=0.1, ypos=0.1, yanchor = 0.1)
    invRight = Position(xpos=0.33, xanchor=0.1, ypos=0.1, yanchor = 0.1)
    nearRight = Position(xpos=0.55, xanchor=0.1, ypos=0.1, yanchor = 0.1)
    near_left = Position(xpos=0.25, ypos = 0.5)
    tutorial_lgMed = True
    tutorial_lgHard = True
    tutorial_gramMed = True
    tutorial_gramHard = True
    tutorial_binaryMed = True
    tutorial_binaryHard = True
    tutorial_llMed = True
    tutorial_llHard = True
    repeat_number = 0
# The game starts here.
label start:
    $Preference("rollback side", "disable")
    $ slot_name = ""
    $ gate_name = ""
    $ points_SbE = 0
    $ points_E = 0
    $ points_S = 0
    $ quick_menu = False
    $ gate_name = ""
    #hirose variables
    $ hiroseTea_inv = False
    $ hiroseOfficeComputer = False
    $ hiroseTree_inv = False
    $ hiroseTransitionItems = 0
    $ hiroseRecorder_inv = False
    $ hiroseOfficeItems = 0
    $ hiroseBed_inv = False
    $ hirosePC = False
    $ hirosePhoto_inv = False
    $ hiroseWindow_inv = False
    $ hirosePersonalItems = 0
    $ talkAdaHirosePersonal_value = 0
    $ hirosePersonalItems_value = 0
    #Grace office variables
    $ talkAdaGraceLab_times = 0
    $ graceRightDesk_value = 0
    $ graceLeft1Desk_value = 0
    $ graceLeft2Desk_value = 0
    $ graceNeuralNetwork_look = False
    $ graceHardDrive_look = False
    $ graceCandD_look = False
    $ graceCoffee_look = False
    $ graceBust_look = False
    $ gracePhoto_look = False
    $ gracePens_look = False
    $ graceStickynotes_look = False
    
    $ Logic_A_solved = False
    $ Logic_B_solved = False
    $ solved_LG_easy = False
    $ lgEasy_tries = 0
    $ tutorial_LGEasy = True
    $ tutorial_gramEasy = True
    $ resume = ""
    $ LGEasyHints = 0
    $ gramEasyHints = 0
    $ attemptsLogicGate1 = 0
    $ attemptsGramEasy = 0
    
    #Balcony variables
    $ callAttempts = 0
    $ balconyItems = 0
    $ moprScene = False
    $ balconyView_look = False
    $ alphaBody_look = False
    $ balconyJumpdrive_look = False
    $ balconyScratches_look = False
    
    #Variables for chapter two puzzles
    $ alphaBodyItems = 0
    $ binaryEasyDone = False
    $ loopLogicEasyDone = False
    $ binaryEasy_tries = 0
    $ loopLogicEasy_tries = 0
    $ tutorial_binaryEasy = False
    $ tutorial_loopLogicEasy = False
    
    #Variables for chapter three
    $ talkIvan_count = 0
    $ burntCord_inv = False
    $ ivanComp_lock = True
    $ nightShift_lock = True
    $ catPhoto_inv = False
    $ lab2Items = 0
    $ ivanNotes_inv = False
    $ llMed_attempts = 0
    $ lgMed_attempts = 0
    $ binaryMed_attempts = 0
    $ gramMed_attempts = 0
    $ llMed_solved = False
    $ lgMedA_solved = False
    $ lgMedB_solved = False
    $ lgMedC_solved = False
    $ binaryMed_solved = False
    $ gramMed_solved = False
    $ lab2Items_table = 0
    
    #Variables for chapter four
    #Blues
    $ blueItems_main = 0
    $ blueItems_left = 0
    $ blueItems_right = 0
    $ soilSamples_inv = False
    $ scanner_inv = False
    $ atmosphereReading_inv = False
    $ bluesCore_inv = False
    $ foodPrinter_inv = False
    $ medKit_inv = False
    $ bluesDemands_inv = False
    $ convenienceTable_inv = False
    $ bluesFloor_inv = False
    $ talkBlue_count = False
    $ transitionBlue = False
    #Puzzle
    $ llHard_solved = False
    $ llHard_attempts = 0
    $ lgHardA_solved = False
    $ lgHardB_solved = False
    $ lgHardC_solved = False
    $ lgHard_attempts = 0
    $ binaryHard_solved = False
    $ binaryHard_attempts = 0
    $ gramHard_solved = False
    $ gramHard_attempts = 0
    
    #Watson's Server
    $ drive2_inv = False
    $ safe_inv = False
    $ watsonDesk_inv = False
    $ watsonScreens_inv = False
    $ watsonItems_left = 0
    $ watsonItems_right = 0
    $ watsonItems_main = 0 
    $ llHard_attempts = 0
    $ lgHard_attempts = 0
    $ binaryHard_attempts = 0
    $ gramHard_attempts = 0
    $ llHard_solved = False
    $ lgHardA_solved = False
    $ lgHardB_solved = False
    $ lgHardC_solved = False
    $ binaryHard_solved = False
    $ gramHard_solved = False
    $ talkAdaWatson_count = 0
    
    #Oxygen Garden
    $raptor_inv = False
    $fern_inv = False
    $camcorder_inv = False
    $ogItems = 0
    $talkAlan_count = 0
    
    transform crawlScroll:
        yalign 0.0 xalign 0.5
        linear 50.0 yalign 1.0
        
    transform basicfade:
        on show:
            alpha 0.0
            linear 0.3 alpha 1.0
        on hide:
            linear 0.1 alpha 0.0   
    if (puzzleGallery):
        jump pg_mainMenu
    window hide
    scene bg openCrawlBG at basicfade
    show openingCrawl at crawlScroll
    $ renpy.pause(51.0)
    scene bg splashScreen
    #with fade(5.0)
    $ renpy.pause(5.0)
    stop music fadeout 1.0
#    menu:
#        "Chapter 3 SbE":
#            jump chapterThree_SbE
#        "Chapter 3 E":
#            jump chapterThree_E
#        "Chapter 3 S":
#            jump chapterThree_S
#        "Chapter 4 S.":
#            jump chapterFour_S
#        "Chapter 4 E.":
#            jump chapterFour_E
#        "Test MOPR slide.":
#            jump enterthemopr_E
    show bg black with fade
    scene bg prologue with fade
    $renpy.pause(3.0)
    show bg black with fade
    scene bg G_deskArea with fade #at basicfade
    with None 
    $ quick_menu = True
    #with fade(5.0)
    jump prologue
    
label splashscreen:
    scene bg black
    $renpy.movie_cutscene('images/ErrorOpening.mpg')
    show splash with fade
    play sound moprInquisitive
    $renpy.pause(4.0)
    scene bg black with fade
    show mm_base with fade
    return