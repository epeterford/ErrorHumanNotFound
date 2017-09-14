#LOOP LOGIC PUZZLE
screen llMedLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("choose_llMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("lab2_inv")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen llMedWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("llMedDone")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen tutorial_scrLLMed_1:
    imagebutton:
        idle "next.png" 
        hover "next_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("tutorial_LLMed_2")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
              
screen tutorial_scrLLMed_2:
    imagebutton:
        idle "back.png" 
        hover "back_hover.png" 
        xpos 0
        ypos 940 
        focus_mask True
        action Jump("tutorial_LLMed_1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
    imagebutton:
        idle "next.png" 
        hover "next_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("tutorial_LLMed_3")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
    
screen tutorial_scrLLMed_3:
    imagebutton:
        idle "back.png" 
        hover "back_hover.png" 
        xpos 0
        ypos 940 
        focus_mask True
        action Jump("tutorial_LLMed_2")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("choose_llMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label llMedLose:
    show other darken
    image systemStartFail ="binaryEasyLose.png" #CHANGE ME
    show systemStartFail at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen llMedLose_scr
    
label llMedWin:
    show other darken
    image systemStartup= "loopLogicEasyWin.png" #CHANGE ME
    show systemStartup at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen llMedWin_scr
    
label llMedDone:
    $quick_menu = True
    $lab2Items +=1
    scene bg lab2Ivan_unlocked
    stop music fadeout 1.0
    $llMed_solved = True
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L4.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L5.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L6.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L7.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L8.ogg", channel='channel08', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L9.ogg", channel='channel09', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L10.ogg", channel='channel10', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L11.ogg", channel='channel11', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    if(llMed_attempts ==0):
        #show Ivan dour at right
        show Grace happy at left
    if(llMed_attempts ==1):
        #show Ivan dour at right
        show Grace neutral at left
    if(llMed_attempts>1):
        show Grace annoyed at left
        #show Ivan dour at right
    hide Grace
    #hide Ivan
    $quick_menu = False
    if(resume=="SbE"):
        jump finishGPuzzle1_SbE
    if(resume=="E"):
        jump finishGPuzzle1_E
    if(resume=="S"):
        jump finishGPuzzle1_S

label choose_llMed:
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    stop channel06 fadeout 1.0
    stop channel07 fadeout 1.0
    stop channel08 fadeout 1.0
    stop channel09 fadeout 1.0
    stop channel10 fadeout 1.0
    stop channel11 fadeout 1.0
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    $LLMedHints=0
#    if (llMed_attempts == 0):
#        jump tutorial_LLMed_1
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $light1Sound =0
    $light2Sound = 0
    $light3Sound = 0
    $light4Sound = 0
    jump loopLogic_med1
    $randomNumberEasyLL = renpy.random.randint(0,4)
    if randomNumberEasyLL==0:
        jump loopLogic_med1
    if randomNumberEasyLL==1:
        jump loopLogic_med2
    if randomNumberEasyLL==2:
        jump loopLogic_med3
    if randomNumberEasyLL==3:
        jump loopLogic_med4
    if randomNumberEasyLL==4:
        jump loopLogic_med5
    "If you see this, an error has occured. Please contact Blue or some other capable individual to resolve."
    
label tutorial_LLMed_1:
    window hide
    $quick_menu = False
    scene bg tutorial_llMed_1
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrLLMed_1
    
label tutorial_LLMed_2:
    window hide
    $quick_menu = False
    scene bg tutorial_llMed_1
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrLLMed_2
    
label tutorial_LLMed_3:
    window hide
    $quick_menu = False
    scene bg tutorial_llMed_1
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrLLMed_3
    
label hints_llMed_1:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLMedHints%3 
    show LLM_1_tile64 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLM_1_tile65 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
    show LLM_1_tile66 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_1_tile67 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        $LLMedHints +=1
        a "Since there are no blue IFs, the ELSE must be used to get the blue."
        hide other darken onlayer screens
        hide LLM_1_tile64 onlayer screens
        hide LLM_1_tile65 onlayer screens
        hide LLE_1_tile66 onlayer screens
        hide LLE_1_tile67 onlayer screens
        jump gamefile_llm1
    if (remainder==1):
        $LLMedHints +=1
        a "We have two green IFs and two green lights. I would try placing a green IF where I wanted a green light on."
        hide other darken onlayer screens
        hide LLM_1_tile64 onlayer screens
        hide LLM_1_tile65 onlayer screens
        hide LLE_1_tile66 onlayer screens
        hide LLE_1_tile67 onlayer screens
        jump gamefile_llm1
    if (remainder==2):
        $LLMedHints +=1
        a "Remember that an ELSE can only be placed after an IF, so make sure you have an IF gate in before you try to use the ELSE."
        hide other darken onlayer screens
        hide LLM_1_tile64 onlayer screens
        hide LLM_1_tile65 onlayer screens
        hide LLE_1_tile66 onlayer screens
        hide LLE_1_tile67 onlayer screens
        jump gamefile_llm1
    jump gamefile_llm1
    
label hints_llMed_2:
    
label hints_llMed_3:
    
label hints_llMed_4:
    
label hints_llMed_5:

#BINARY PUZZLE
#ADD SCREENS FOR TUTORIAL AND LABELS TO CALL

screen binaryMedLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("binaryMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("wwPuzzleScreen") #CHANGE
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen binaryMedWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("binaryMedDoneTalk") #CHANGE
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
#TUTORIAL FOR MEDIUM ARE NOT DONE. SCREENS ARE PLACEHOLDERS ONLY.        
screen tutorial_scrBinary3Bit_1:
    imagebutton:
        idle "next.png" 
        hover "next_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("tutorial_Binary3Bit_2")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        
screen tutorial_scrBinary3Bit_2:
    imagebutton:
        idle "back.png" 
        hover "back_hover.png" 
        xpos 0
        ypos 940 
        focus_mask True
        action Jump("tutorial_Binary3Bit_1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
    imagebutton:
        idle "next.png" 
        hover "next_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("tutorial_Binary3Bit_3")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
screen tutorial_scrBinary3Bit_5:
    imagebutton:
        idle "back.png" 
        hover "back_hover.png" 
        xpos 0
        ypos 940 
        focus_mask True
        action Jump("tutorial_Binary3Bit_4")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("binaryMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen wwPuzzleScreen_scr:
    imagebutton:
        idle "objects/wwScreen_idle.png"
        hover "objects/wwScreen_hover.png"
        xpos 0
        ypos 0
        focus_mask True
        action Jump("binaryMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label wwPuzzleScreen:
    $config.skipping=None
    $renpy.block_rollback()
    stop music fadeout 1.0
    play channel00 wwAmb0 fadeout 1.0 fadein 1.0
    play channel01 wwAmb1 fadeout 1.0 fadein 1.0
    play channel02 wwAmb2 fadeout 1.0 fadein 1.0
    play channel03 wwAmb3 fadeout 1.0 fadein 1.0
    play channel04 wwAmb4 fadeout 1.0 fadein 1.0
    play channel05 wwAmb5 fadeout 1.0 fadein 1.0
    play channel06 wwAmb6 fadeout 1.0 fadein 1.0
    scene bg wwCritical
    show Ada seething at right
    a "If I don't get the habitat back to Nominal, Colossus will not allow me to continue my investigation."
    hide Ada
    call screen wwPuzzleScreen_scr

label binaryMed:
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    stop channel06 fadeout 1.0
    #Add more stops here if needed when the BGM is added
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
#    if (binaryMed_attempts==0): Uncomment when have tutorial
#        jump tutorial_Binary3Bit_1
    $binaryMedHints = 0
    call binaryMatchMed
    
label tutorial_Binary3Bit_1:
    $renpy.block_rollback()
    $config.skipping=None
    window hide
    $ quick_menu = False
    scene bg tutorial_binary3Bit_1
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary3Bit_1
    
label tutorial_Binary3Bit_2:
    window hide
    $ quick_menu = False
    scene bg tutorial_binary3Bit_2
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary3Bit_2
    
label tutorial_Binary3Bit_5:
    window hide
    $ quick_menu = False
    scene bg tutorial_binary3Bit_5
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary3Bit_5
        
label binaryMediumHints:
    show screen disable_hide
    $config.skipping=None
    $remainder = binaryMedHints%3 
    show other darken onlayer screens
    if (remainder==0):
        $binaryMedHints +=1
        a "Okay Ada, you can do this. 0 and 1 are the same as integers, just with extra zeros to the left."
        hide other darken onlayer screens
        window hide
        jump turns_loopMed
    if (remainder==1):
        $binaryMedHints +=1
        a "The third bit place is worth 4 if there is a one there. The second is worth 2 if there is a one there, and the rightmost bit is worth 1."
        hide other darken onlayer screens
        window hide
        jump turns_loopMed
    if (remainder==2):
        $binaryMedHints +=1
        a "The highest number with three bits is 0111, or 7. Working backwards, I just remove the rightmost bit to get 6, so 0110."
        hide other darken onlayer screens
        window hide
        jump turns_loopMed
    jump turns_loopMed

label binaryMedWin:
    hide screen binaryMatch_med
    show other darken
    image discStartup= "binaryEasyWin.png" #CHANGE ME
    show discStartup at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen binaryMedWin_scr
    
label binaryMedLose:
    hide screen binaryMatch_med
    show other darken
    $ binaryMed_attempts +=1
    image bootFail ="loopLogicEasyLose.png" #CHANGE ME
    show bootFail at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen binaryMedLose_scr
    
label binaryMedDoneTalk:
    scene bg wwNominal with fade
    $quick_menu = True
    stop music fadeout 1.0
    play channel00 wwAmb0 fadeout 1.0 fadein 1.0
    play channel01 wwAmb1 fadeout 1.0 fadein 1.0
    play channel02 wwAmb2 fadeout 1.0 fadein 1.0
    play channel03 wwAmb3 fadeout 1.0 fadein 1.0
    play channel04 wwAmb4 fadeout 1.0 fadein 1.0
    play channel05 wwAmb5 fadeout 1.0 fadein 1.0
    play channel06 wwAmb6 fadeout 1.0 fadein 1.0
    if(binaryMed_attempts==0):
        show Ada annoyed at right
        a "Watson has the same computational abilities as I do. To skip out on such an elementary task is just lazy."
    if (binaryMed_attempts>=1) and (binaryMed_attempts<3):
        show Ada neutral at right
        a "Perhaps I have been dedicating too much of my background processes to comprehending the nuances of human interaction. I seemed to have some difficulty with this task."
    if (binaryMed_attempts>=3):
        show Ada frustrated at right
        a "I should not have had to utilize as much RAM as I did to return the habitat to nominal conditions. Perhaps Watson does have a point."
    if (resume=="S"):
        jump postBinaryMed_S
    if (resume=="SbE"):
        jump postBinaryMed_SbE
    if (resume=="E"):
        jump postBinaryMed_E
