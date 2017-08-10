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
image bg binary = "tileBackground.png"
        

define dissolve = Dissolve (1.0)

image Tosh neutral = "Tosh_Happy1.png"

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
define audio.gramTree1 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_01.ogg"
define audio.gramTree2 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_02.ogg"
define audio.gramTree3 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_03.ogg"
define audio.gramTree4 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_04.ogg"
define audio.gramTree5 = "music/UI/grammarPuzzle/EHNF_UI_GrammarPuzzle_TreeDrawingNoise_05.ogg"

#door sounds
define audio.doorOpen1 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_OPEN_1.ogg"
define audio.doorOpen2 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_OPEN_2.ogg"
define audio.doorClose1 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_CLOSE_1.ogg"
define audio.doorClose2 = "music/Object/Door_Audio/EHNF_OBJECT_DOOR_CLOSE_2.ogg"
define audio.doorDenied = "music/Object/Door_Audio/ENHF_Object_Door_AccessDenied.ogg"
define audio.doorAccess= "music/Object/Door_Audio/ENHF_Object_Door_AccessGranted.ogg"

#balcony ambience sounds
define audio.balconyAmb0 = "music/Amb/Balcony/EHNF_BAL_L0.ogg"
define audio.balconyAmb1 = "music/Amb/Balcony/EHNF_BAL_L1.ogg"
define audio.balconyAmb2 = "music/Amb/Balcony/EHNF_BAL_L2.ogg"
define audio.balconyAmb3 = "music/Amb/Balcony/EHNF_BAL_L3.ogg"
define audio.balconyAmb4 = "music/Amb/Balcony/EHNF_BAL_L4.ogg"

#Grace lab audio
define audio.typing = "music/Amb/Grace_Lab/Typing/EHNF_AMB_Grace_Lab_TYP_L_0.ogg"
define audio.graceLabAmb = "music/Amb/Grace_Lab/Normal/EHNF_Grace_Lab_Norm.ogg"

define audio.hallwayAmb = "music/Amb/Hallway/EHNF_Amb_Scene_Hallway_Norm.ogg"

#hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"

#hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
#                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
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

#Lab 2/Grace Lab music?
define audio.labBGM_0 = "music/BGM/Lab2/EHNF_L0_BGM_Lab2_Pad.ogg"
define audio.labBGM_1 = "music/BGM/Lab2/EHNF_L1_BGM_Lab2_Bass.ogg"
define audio.labBGM_2 = "music/BGM/Lab2/EHNF_L2_BGM_Lab2_Pad2.ogg"
define audio.labBGM_3 = "music/BGM/Lab2/EHNF_L3_BGM_Lab2_Pad_Melodic_Stinger.ogg"
define audio.labBGM_4 = "music/BGM/Lab2/EHNF_L4_BGM_Lab2_Melody.ogg"
define audio.labBGM_5 = "music/BGM/Lab2/EHNF_L5_BGM_Lab2_Sweep.ogg"

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
define aduio.speakerCrackle = "music/Object/Misc_Audio/EHNF_Speaker_Crackle1.ogg"

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

#Investigate. Currently empty folder.

#logicGatePuzzle
define audio.lgFlow1 = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_01.ogg"
define audio.lgFlow2 = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_02.ogg"
define audio.lgFlow3 = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_PipeFlow_03.ogg"
define audio.lgWin = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_RightOutput.ogg"
define audio.lgLose = "music/UI/logicGatePuzzle/EHNF_UI_LogicGatePuzzle_WrongOutput.ogg"

#Main Menu
define audio.mmHighlight = "music/UI/mainMenu/ENHF_UI_Highlight.ogg"

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

    config.main_menu_music = "music/EHNF_Main_Theme.ogg"
    #atl_transform ::= "transform" scrolling_vertical "("parameters")" ":"

# The game starts here.
label start:
    $ slot_name = ""
    $ gate_name = ""
    stop music
    $ points_SbE = 0
    $ points_E = 0
    $ points_S = 0
    $ quick_menu = False
    $ gate_name = ""
    $ centerScreen = Position(xpos=0.5, xanchor =0.5, ypos =0.2, yanchor = 0.2)
    $ centerScreen2 = Position(xpos=0.5, xanchor =0.5, ypos =0.35, yanchor = 0.2)
    $ near_left = Position(xpos=0.25, ypos = 0.5)
    #hirose variables
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
    $ callAttempts = 0
    $ balconyItems = 0
    $ moprScene = False
    $ LGEasyHints = 0
    $ gramEasyHints = 0
    $ attemptsLogicGate1 = 0
    
    #Variables for chapter two puzzles
    $ alphaBodyItems = 0
    $ binaryEasyDone = False
    $ loopLogicEasyDone = False
    $ binaryEasy_tries = 0
    $ loopLogicEasy_tries = 0
    $ tutorial_binaryEasy = False
    $ tutorial_loopLogicEasy = False
    
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
    play channel00 mt_bellsL fadein 1.0
    play channel01 mt_bellsR fadein 1.0
    play channel02 mt_piano fadein 1.0
    play channel03 mt_ghostBus fadein 1.0
    play channel04 mt_ghostL fadein 1.0
    play channel05 mt_ghostR fadein 1.0
    play channel06 mt_orchestra fadein 1.0
    play channel07 mt_sciFi fadein 1.0
    play channel08 mt_touchOrchestra fadein 1.0
    play channel09 mt_tornado fadein 1.0
    play channel10 mt_ultrasweeper fadein 1.0
    play channel11 mt_violins fadein 1.0
    play channel12 mt_wistful fadein 1.0

    window hide
    scene bg openCrawlBG at basicfade
    show openingCrawl at crawlScroll
    $ renpy.pause(51.0)
    scene bg splashScreen
    #with fade(5.0)
    $ renpy.pause(5.0)

#    stop music

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
