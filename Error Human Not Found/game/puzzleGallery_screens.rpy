screen pg_binaryHardLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("binaryMatchHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_binaryMain")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_binaryHardWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_binaryMain") 
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"

label pg_binaryHardWin:
    hide screen binaryMatch_hard
    show other darken
    image pg_binaryHard_winImage = "pg_win.png"
    show pg_binaryHard_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_binaryHardWin_scr
    
label pg_binaryHardLose:
    hide screen binaryMatch_hard
    show other darken
    image pg_binaryHard_loseImage ="pg_lose.png"
    show pg_binaryHard_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_binaryHardLose_scr
    
screen pg_binaryEasyLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("binaryMatchEasy")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_binaryMain")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_binaryEasyWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_binaryMain")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    
label pg_binaryEasyWin:
    hide screen binaryMatch 
    show other darken
    image pg_winImage= "pg_win.png"
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_binaryEasyWin_scr
    
label pg_binaryEasyLose:
    hide screen binaryMatch
    show other darken
    image pg_loseImage ="pg_lose.png"
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_binaryEasyLose_scr
    
label pg_binaryMedWin:
    hide screen binaryMatch_med
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_binaryMedWin_scr
    
label pg_binaryMedLose:
    hide screen binaryMatch_med
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_binaryMedLose_scr
    
screen pg_binaryMedLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("binaryMatchMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_binaryMain")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_binaryMedWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_binaryMain")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    
    
    
########################################### END BINARY SCREENS #######################################################
    
screen pg_llHardLose_scr1:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action (SetVariable("repeat_number", 1), Jump("repeat_llHard"))
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_llHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen pg_llHardLose_scr2:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action (SetVariable("repeat_number", 2), Jump("repeat_llHard"))
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_llHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen pg_llHardLose_scr3:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action (SetVariable("repeat_number", 3), Jump("repeat_llHard"))
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_llHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen pg_llHardLose_scr4:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action (SetVariable("repeat_number", 4), Jump("repeat_llHard"))
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_llHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen pg_llHardLose_scr5:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action (SetVariable("repeat_number", 5), Jump("repeat_llHard"))
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_llHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_llHardWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_llHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label pg_llHardLose1:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_llHardLose_scr1
    
label pg_llHardLose2:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_llHardLose_scr2
    
label pg_llHardLose3:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_llHardLose_scr3
    
label pg_llHardLose4:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_llHardLose_scr4

label pg_llHardLose5:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_llHardLose_scr5
    
label pg_llHardWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_llHardWin_scr
        
label repeat_llHard:
    $LLHardHints=0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $light1Sound =0
    $light2Sound = 0
    $light3Sound = 0
    $light4Sound = 0
    $light5Sound = 0
    $light6Sound = 0
    $light7Sound = 0
    $charge1_sound1 = 0
    $charge1_sound2 = 0
    $charge2_sound1 = 0
    $charge2_sound2 = 0
    $charge3_sound1 = 0
    $charge3_sound2 = 0
    if repeat_number ==1:
        jump loopLogic_hard1
    if repeat_number ==2:
        jump loopLogic_hard2
    if repeat_number ==3:
        jump loopLogic_hard3
    if repeat_number ==4:
        jump loopLogic_hard4
    if repeat_number ==5:
        jump loopLogic_hard5
        
############################################### END Loop logic hard ###############################
screen pg_llMedLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_llMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_llMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_llMedWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_llMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label pg_llMedLose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_llMedLose_scr
    
label pg_llMedWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_llMedWin_scr
        
label repeat_llMed:
    $LLMedHints=0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $light1Sound =0
    $light2Sound = 0
    $light3Sound = 0
    $light4Sound = 0
    $light5Sound = 0
    $light6Sound = 0
    $light7Sound = 0
    $charge1_sound1 = 0
    $charge1_sound2 = 0
    $charge2_sound1 = 0
    $charge2_sound2 = 0
    $charge3_sound1 = 0
    $charge3_sound2 = 0
    if repeat_number ==1:
        jump loopLogic_med1
    if repeat_number ==2:
        jump loopLogic_med2
    if repeat_number ==3:
        jump loopLogic_med3
    if repeat_number ==4:
        jump loopLogic_med4
    if repeat_number ==5:
        jump loopLogic_med5
        
################################## END LL MED #########################################

screen pg_llEasyLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_llEasy")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_llEasy")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_llEasyWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_llEasy")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label pg_llEasyLose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_llEasyLose_scr
    
label pg_llEasyWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_llEasyWin_scr
        
label repeat_llEasy:
    $LLEasyHints=0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $light1Sound =0
    $light2Sound = 0
    $light3Sound = 0
    if repeat_number ==1:
        jump loopLogic_easy1
    if repeat_number ==2:
        jump loopLogic_easy2
    if repeat_number ==3:
        jump loopLogic_easy3
    if repeat_number ==4:
        jump loopLogic_easy4
    if repeat_number ==5:
        jump loopLogic_easy5
        
##############################################################################END LL ##########################
screen pg_lgEasyAWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_lgEasyA")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"

screen pg_lgEasyBLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_lgEasyB")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_lgEasyB")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_lgEasyBWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_lgEasyB")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen pg_lgEasyCLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_lgEasyC")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_lgEasyC")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_lgEasyCWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_lgEasyC")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label pg_lgEasyBLose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgEasyBLose_scr
    
label pg_lgEasyCLose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgEasyCLose_scr
    
label pg_lgEasyAWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgEasyAWin_scr

label pg_lgEasyBWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgEasyBWin_scr
    
label pg_lgEasyCWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgEasyCWin_scr
        
label repeat_lgEasyB:
    $LGEasyHints=0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    if repeat_number ==1:
        jump logicGate_easyB1
    if repeat_number ==2:
        jump logicGate_easyB2
    if repeat_number ==3:
        jump logicGate_easyB3
        
label repeat_lgEasyC:
    $LGEasyHints=0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    if repeat_number ==1:
        jump logicGate_easyC1
    if repeat_number ==2:
        jump logicGate_easyC2
    if repeat_number ==3:
        jump logicGate_easyC3
        
################################################################ LG MED ###########################

screen pg_lgMedALose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_lgMedA")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_lgMedA")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen pg_lgMedAWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_lgMedA")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"

screen pg_lgMedBLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_lgMedB")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_lgMedB")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_lgMedBWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_lgMedB")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen pg_lgMedCLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_lgMedC")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_lgMedC")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_lgMedCWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_lgMedC")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label pg_lgMedALose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgMedALose_scr
    
label pg_lgMedBLose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgMedBLose_scr
    
label pg_lgMedCLose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgMedCLose_scr
    
label pg_lgMedAWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgMedAWin_scr

label pg_lgMedBWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgMedBWin_scr
    
label pg_lgMedCWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgMedCWin_scr
        
label repeat_lgMedA:
    $LGMedHints = 0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    if repeat_number ==1:
        jump logicGate_mediumA1
    if repeat_number ==2:
        jump logicGate_mediumA2
    if repeat_number ==3:
        jump logicGate_mediumA3
        
label repeat_lgMedB:
    $LGMedHints = 0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    if repeat_number ==1:
        jump logicGate_mediumB1
    if repeat_number ==2:
        jump logicGate_mediumB2
    if repeat_number ==3:
        jump logicGate_mediumB3
        
label repeat_lgMedC:
    $LGMedHints = 0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    if repeat_number ==1:
        jump logicGate_mediumC1
    if repeat_number ==2:
        jump logicGate_mediumC2
    if repeat_number ==3:
        jump logicGate_mediumC3
        
################################################################ END LG MED ################################
screen pg_lgHardALose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_lgHardA")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_lgHardA")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen pg_lgHardAWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_lgHardA")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"

screen pg_lgHardBLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_lgHardB")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_lgHardB")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_lgHardBWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_lgHardB")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen pg_lgHardCLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_lgHardC")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_lgHardC")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_lgHardCWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_lgHardC")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label pg_lgHardALose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgHardALose_scr
    
label pg_lgHardBLose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgHardBLose_scr
    
label pg_lgHardCLose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgHardCLose_scr
    
label pg_lgHardAWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgHardAWin_scr

label pg_lgHardBWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgHardBWin_scr
    
label pg_lgHardCWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_lgHardCWin_scr
        
label repeat_lgHardA:
    $LGHardHints = 0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    if repeat_number ==1:
        jump logicGate_hardA1
    if repeat_number ==2:
        jump logicGate_hardA2
    if repeat_number ==3:
        jump logicGate_hardA3
        
label repeat_lgHardB:
    $LGHardHints = 0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    if repeat_number ==1:
        jump logicGate_hardB1
    if repeat_number ==2:
        jump logicGate_hardB2
    if repeat_number ==3:
        jump logicGate_hardB3
        
label repeat_lgHardC:
    $LGHardHints = 0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    if repeat_number ==1:
        jump logicGate_hardC1
    if repeat_number ==2:
        jump logicGate_hardC2
    if repeat_number ==3:
        jump logicGate_hardC3

####################################################### END LG HARD ######################################
####################################################### START GRAM #######################################

screen pg_gramMedLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_gramMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_gramMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_gramMedWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_gramMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label pg_gramMedLose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_gramMedLose_scr
    
label pg_gramMedWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_gramMedWin_scr
        
label repeat_gramMed:
    $gramMedHints =0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $gramRow1_L_sound =0
    $gramRow1_R_sound = 0
    
    $gramRow1_C_sound = 0
    $gramRow1_C_sound_wrong1 = 0
    $gramRow1_C_sound_wrong2 = 0
    $gramRow1_C_sound_right1 = 0
    $gramRow1_C_sound_right2 = 0
    
    $gramRow2_L_sound = 0
    $gramRow2_L_sound_wrong1 = 0
    $gramRow2_L_sound_right1 = 0
    $gramRow2_L_sound_wrong2 = 0
    $gramRow2_L_sound_right2 = 0
    
    $gramRow2_R_sound = 0
    $gramRow2_R_sound_right1 = 0
    $gramRow2_R_sound_right2 = 0
    $gramRow2_R_sound_wrong1 = 0
    $gramRow2_R_sound_wrong2 = 0
    
    $gramRow2_C_sound = 0
    $gramRow2_C_sound_wrong1 = 0
    $gramRow2_C_sound_right1 = 0
    $gramRow2_C_sound_wrong2 = 0
    $gramRow2_C_sound_right2 = 0
    
    $gramRow3_L_sound = 0
    $gramRow3_L_sound_wrong1 = 0
    $gramRow3_L_sound_wrong2 = 0
    $gramRow3_L_sound_right1 = 0
    $gramRow3_L_sound_right2 = 0
    
    $gramRow3_R_sound = 0
    $gramRow3_R_sound_right1 = 0
    $gramRow3_R_sound_wrong1 = 0
    $gramRow3_R_sound_right2 = 0
    $gramRow3_R_sound_wrong2 = 0
    
    $gramRow3_C_sound = 0
    $gramRow3_C_sound_right1 = 0
    $gramRow3_C_sound_wrong1 = 0
    $gramRow3_C_sound_right2 = 0
    $gramRow3_C_sound_wrong2 = 0
    if repeat_number ==1:
        jump gram_m1
    if repeat_number ==2:
        jump gram_m2
    if repeat_number ==3:
        jump gram_m3
    if repeat_number ==4:
        jump gram_m4
    if repeat_number ==5:
        jump gram_m5
        
############################################################# END MED GRAM ######################
screen pg_gramEasyLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_gramEasy")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_gramEasy")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_gramEasyWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_gramEasy")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label pg_gramEasyLose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_gramEasyLose_scr
    
label pg_gramEasyWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_gramEasyWin_scr
        
label repeat_gramEasy:
    $LGEasyHints =0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $gramRow1_L_sound =0
    $gramRow1_R_sound = 0
    
    $gramRow1_C_sound = 0
    $gramRow1_C_sound_wrong1 = 0
    $gramRow1_C_sound_wrong2 = 0
    $gramRow1_C_sound_right1 = 0
    $gramRow1_C_sound_right2 = 0
    
    $gramRow2_L_sound = 0
    $gramRow2_L_sound_wrong1 = 0
    $gramRow2_L_sound_right1 = 0
    $gramRow2_L_sound_wrong2 = 0
    $gramRow2_L_sound_right2 = 0
    
    $gramRow2_R_sound = 0
    $gramRow2_R_sound_right1 = 0
    $gramRow2_R_sound_right2 = 0
    $gramRow2_R_sound_wrong1 = 0
    $gramRow2_R_sound_wrong2 = 0
    
    $gramRow2_C_sound = 0
    $gramRow2_C_sound_wrong1 = 0
    $gramRow2_C_sound_right1 = 0
    $gramRow2_C_sound_wrong2 = 0
    $gramRow2_C_sound_right2 = 0
    
    $gramRow3_L_sound = 0
    $gramRow3_L_sound_wrong1 = 0
    $gramRow3_L_sound_wrong2 = 0
    $gramRow3_L_sound_right1 = 0
    $gramRow3_L_sound_right2 = 0
    
    $gramRow3_R_sound = 0
    $gramRow3_R_sound_right1 = 0
    $gramRow3_R_sound_wrong1 = 0
    $gramRow3_R_sound_right2 = 0
    $gramRow3_R_sound_wrong2 = 0
    
    $gramRow3_C_sound = 0
    $gramRow3_C_sound_right1 = 0
    $gramRow3_C_sound_wrong1 = 0
    $gramRow3_C_sound_right2 = 0
    $gramRow3_C_sound_wrong2 = 0
    if repeat_number ==1:
        jump eng_gram_e1
    if repeat_number ==2:
        jump eng_gram_e2
    if repeat_number ==3:
        jump eng_gram_e3
    if repeat_number ==4:
        jump eng_gram_e4
    if repeat_number ==5:
        jump eng_gram_e5
        
################################################### END GRAM EASY ###################################
screen pg_gramHardLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("repeat_gramHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("pg_gramHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen pg_gramHardWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("pg_gramHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label pg_gramHardLose:
    show other darken
    show pg_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_gramHardLose_scr
    
label pg_gramHardWin:
    show other darken
    show pg_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen pg_gramHardWin_scr
        
label repeat_gramHard:
    $gramHardHints=0
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $gramRow1_L_sound =0
    $gramRow1_R_sound = 0
    
    $gramRow1_C_sound = 0
    $gramRow1_C_sound_wrong1 = 0
    $gramRow1_C_sound_wrong2 = 0
    $gramRow1_C_sound_right1 = 0
    $gramRow1_C_sound_right2 = 0
    
    $gramRow2_L_sound = 0
    $gramRow2_L_sound_wrong1 = 0
    $gramRow2_L_sound_right1 = 0
    $gramRow2_L_sound_wrong2 = 0
    $gramRow2_L_sound_right2 = 0
    
    $gramRow2_R_sound = 0
    $gramRow2_R_sound_right1 = 0
    $gramRow2_R_sound_right2 = 0
    $gramRow2_R_sound_wrong1 = 0
    $gramRow2_R_sound_wrong2 = 0
    
    $gramRow2_C_sound = 0
    $gramRow2_C_sound_wrong1 = 0
    $gramRow2_C_sound_right1 = 0
    $gramRow2_C_sound_wrong2 = 0
    $gramRow2_C_sound_right2 = 0
    
    $gramRow3_L_sound = 0
    $gramRow3_L_sound_wrong1 = 0
    $gramRow3_L_sound_wrong2 = 0
    $gramRow3_L_sound_right1 = 0
    $gramRow3_L_sound_right2 = 0
    
    $gramRow3_R_sound = 0
    $gramRow3_R_sound_right1 = 0
    $gramRow3_R_sound_wrong1 = 0
    $gramRow3_R_sound_right2 = 0
    $gramRow3_R_sound_wrong2 = 0
    
    $gramRow3_C_sound = 0
    $gramRow3_C_sound_right1 = 0
    $gramRow3_C_sound_wrong1 = 0
    $gramRow3_C_sound_right2 = 0
    $gramRow3_C_sound_wrong2 = 0
    if repeat_number ==1:
        jump eng_gram_h1
    if repeat_number ==2:
        jump eng_gram_h2
    if repeat_number ==3:
        jump eng_gram_h3
    if repeat_number ==4:
        jump eng_gram_h4
    if repeat_number ==5:
        jump eng_gram_h5