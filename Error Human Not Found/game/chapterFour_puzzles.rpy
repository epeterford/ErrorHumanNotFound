
#BINARY PUZZLE
#ADD SCREENS FOR TUTORIAL AND LABELS TO CALL

screen binaryHardLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("binaryHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("watsonLeft")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    key 'h' action NullAction() #action Hide("")
    key 'K_PAGEUP' action NullAction() #action Hide("")
    key 'repeat_K_PAGEUP' action NullAction() #action Hide("")
    key 'K_AC_BACK' action NullAction() #action Hide("")
    key 'mousedown_4' action NullAction() #action Hide("")
    key 'K_LCTRL' action NullAction() #action Skip("")
    key 'K_RCTRL' action NullAction() #action Skip("")
    key 'K_TAB' action NullAction() #action Hide("")
    key '>' action NullAction() #action Skip("")
    $renpy.block_rollback()
    $config.skipping=None
            
screen binaryHardWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("binaryHardDoneTalk") 
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    key 'h' action NullAction() #action Hide("")
    key 'K_PAGEUP' action NullAction() #action Hide("")
    key 'repeat_K_PAGEUP' action NullAction() #action Hide("")
    key 'K_AC_BACK' action NullAction() #action Hide("")
    key 'mousedown_4' action NullAction() #action Hide("")
    key 'K_LCTRL' action NullAction() #action Skip("")
    key 'K_RCTRL' action NullAction() #action Skip("")
    key 'K_TAB' action NullAction() #action Hide("")
    key '>' action NullAction() #action Skip("")
    $renpy.block_rollback()
    $config.skipping=None
              
screen tutorial_scrBinary4Bit_1:
    imagebutton:
        idle "next.png" 
        hover "next_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("tutorial_Binary4Bit_2")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
    key 'h' action NullAction() #action Hide("")
    key 'K_PAGEUP' action NullAction() #action Hide("")
    key 'repeat_K_PAGEUP' action NullAction() #action Hide("")
    key 'K_AC_BACK' action NullAction() #action Hide("")
    key 'mousedown_4' action NullAction() #action Hide("")
    key 'K_LCTRL' action NullAction() #action Skip("")
    key 'K_RCTRL' action NullAction() #action Skip("")
    key 'K_TAB' action NullAction() #action Hide("")
    key '>' action NullAction() #action Skip("")
    $renpy.block_rollback()
    $config.skipping=None
        
screen tutorial_scrBinary4Bit_2:
    imagebutton:
        idle "back.png" 
        hover "back_hover.png" 
        xpos 0
        ypos 940 
        focus_mask True
        action Jump("tutorial_Binary4Bit_1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("binaryHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    key 'h' action NullAction() #action Hide("")
    key 'K_PAGEUP' action NullAction() #action Hide("")
    key 'repeat_K_PAGEUP' action NullAction() #action Hide("")
    key 'K_AC_BACK' action NullAction() #action Hide("")
    key 'mousedown_4' action NullAction() #action Hide("")
    key 'K_LCTRL' action NullAction() #action Skip("")
    key 'K_RCTRL' action NullAction() #action Skip("")
    key 'K_TAB' action NullAction() #action Hide("")
    key '>' action NullAction() #action Skip("")
    $renpy.block_rollback()
    $config.skipping=None

label binaryHard:
    stop channel00 fadeout 1.0
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    if (tutorial_binaryHard):
        $tutorial_binaryHard = False
        $pageUnlocked_notes +=3
        if (notes_hard2 =="LG") or (notes_hard2 =="LL"):
            $notes_hard3 = "B"
        else:
            $notes_hard2 = "B"
        jump tutorial_Binary4Bit_1
    $binaryHardHints = 0
    call binaryMatchHard from _call_binaryMatchHard
    
label tutorial_Binary4Bit_1:
    $renpy.block_rollback()
    $config.skipping=None
    window hide
    $ quick_menu = False
    scene bg tutorial_binaryHard_1
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary4Bit_1
    
label tutorial_Binary4Bit_2:
    window hide
    $ quick_menu = False
    scene bg tutorial_binaryHard_2
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary4Bit_2
        
label binaryHardHints:
    show screen disable_hide
    $config.skipping=None
    $remainder = binaryHardHints%3 
    $can_clickHard = False
    show other darken onlayer screens
    if (remainder==0):
        $binaryHardHints +=1
        g "Four bits is a little more challenging. The left-most bit is worth 8, the next one 4, the next 2, and then 1."
        hide other darken onlayer screens
        window hide
        jump turns_loopHard
    if (remainder==1):
        $binaryHardHints +=1
        g "The highest bit is 1111, which is fifteen. 1000 is just 8, then we have 0100 which is 4, and 0010, which is 2, and 0001, which is just one."
        hide other darken onlayer screens
        window hide
        jump turns_loopHard
    if (remainder==2):
        $binaryHardHints +=1
        g "There are a lot of tiles, but 0000 and 0001 are still easy. Integers run 0 to 15. Just try to take it slow if you're having problems. The investigators aren't here yet."
        hide other darken onlayer screens
        window hide
        jump turns_loopHard
    jump turns_loopHard

label binaryHardWin:
    hide screen binaryMatch_hard
    show other darken
    $binaryHard_solved = True
    image binaryHard_winImage = "binaryHard_win.png" #CHANGE ME
    show binaryHard_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen binaryHardWin_scr
    
label binaryHardLose:
    hide screen binaryMatch_hard
    show other darken
    $ binaryHard_attempts +=1
    image binaryHard_loseImage ="binaryHard_lose.png" #CHANGE ME
    show binaryHard_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen binaryHardLose_scr
    
label binaryHardDoneTalk:
    scene bg wsDesk with fade
    $quick_menu = True
    stop music fadeout 1.0
    $watsonItems_left +=1
    $renpy.music.play("music/Amb/WS/EHNF_WS_AMB.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $binaryHard_solved = True
    $renpy.block_rollback()
    $config.skipping=None
    $config.rollback_enabled = True
    $config.allow_skipping = True
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $stackDepth -=1
    hide screen disable_hide
    if(binaryHard_attempts==0):
        show Grace neutral at left
        show Ada amused at right
        a "With the correct encryption key, this was easy enough to crack. Now we just have to wait for the rest to finish decrypting."
        if (binaryMed_attempts==0) and (binaryEasy_tries ==0):
            $achievement.Sync()
            $achievement.sync()
            $achievement.grant("ACH_BINARY")
            $achievement.sync()
            $achievement.Sync()
    if (binaryHard_attempts>=1) and (binaryHard_attempts<3):
        show Ada seething at right
        show Grace neutral at left
        a "Trust Watson to have additional security measures in place. The encryption key certainly helped, but I still had to bypass several other surprises he left behind."
        g "So what did we get?"
        show Ada neutral
        a "It will still take some time to decrypt all of the data. I will let you know when the process is complete."
    if (binaryHard_attempts>=3):
        show Ada annoyed at right
        show Grace snarky at left
        g "You know Ada, an encryption key is supposed to make decryption pretty simple. Add that you're basically a walking computer, and I would have thought--"
        a "If you are going to be that way, next time you can try to crack it."
        show Grace surprised
        g "Oh, no, please. I wouldn't want to take that from you."
        show Grace neutral
        g "So what did we get?"
        show Ada neutral
        a "It will still take some time to decrypt all of the data. I will let you know when the process is complete."
    $quick_menu=False
    window hide
    hide Grace
    hide Ada
    jump watsonLeft
    
###########################################GRAMMAR PUZZLE HERE#####################################
screen gramHard_lose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("choose_gramHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("blueSpace_puzzle") #CHANGE ME
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
screen gramHard_win_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("gramHard_done")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"

screen gramHard_puzzleItem_scr:
    imagebutton:
        idle "blueButton_idle.png"
        hover "blueButton_hover.png"
        xpos 0
        ypos 0
        focus_mask True
        action Jump("choose_gramHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen tutorial_gramHard_1_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("choose_gramHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
    key 'h' action NullAction() #action Hide("")
    key 'K_PAGEUP' action NullAction() #action Hide("")
    key 'repeat_K_PAGEUP' action NullAction() #action Hide("")
    key 'K_AC_BACK' action NullAction() #action Hide("")
    key 'mousedown_4' action NullAction() #action Hide("")
    key 'K_LCTRL' action NullAction() #action Skip("")
    key 'K_RCTRL' action NullAction() #action Skip("")
    key 'K_TAB' action NullAction() #action Hide("")
    key '>' action NullAction() #action Skip("")
    $renpy.block_rollback()
    $config.skipping=None
#######LABELS##############

label tutorial_gramHard_1:
    window hide
    $ quick_menu = False
    scene bg tutorial_gramHard
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_gramHard_1_scr
    
label gramHard_lose:
    $config.skipping=None
    $renpy.block_rollback()
    show other darken
    image gramHard_loseImage = "gramHard_lose.png" #CHANGE THIS
    show gramHard_loseImage at centerScreen2 #CHANGE
    call screen gramHard_lose_scr
    
label gramHard_win:
    $config.skipping=None
    $renpy.block_rollback()
    show other darken
    image gramHard_winImage = "gramHard_win.png" #CHANGE THIS
    show gramHard_winImage at centerScreen2 #CHANGE
    call screen gramHard_win_scr
    
label gramHard_done:
    $quick_menu = True
    scene bg blueMain with fade
    stop music fadeout 1.0
    $renpy.music.play("music/BGM/Blue/EHNF_L0_BGM_Blue_Kick.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L1_BGM_Blue_Ghost_Kick.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L2_BGM_Blue_3p_Horn_Bus.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L3_BGM_Blue_Snare.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L4_BGM_Blue_Percussion.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L5_BGM_Blue_Cymbals_Large.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L6_BGM_Blue_Cymbals_Small.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L7_BGM_Blue_Cymbals_Swells.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L8_BGM_Blue_Glass_Mallet.ogg", channel='channel08', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L9_BGM_Blue_Liquid_Mallet.ogg", channel='channel09', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L10_BGM_Blue_Reflective_Mallet.ogg", channel='channel10', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L11_BGM_Blue_Grime_Bass.ogg", channel='channel11', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L12_BGM_Blue_Sub_Bass.ogg", channel='channel12', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L13_BGM_Blue_Sparkling_Water_Drops.ogg", channel='channel13', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L14_BGM_Blue_Ambient_Room_Pad.ogg", channel='channel14', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L15_BGM_Blue_Strings_Legatto.ogg", channel='channel15', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L16_BGM_Blue_Strings_Staccato.ogg", channel='channel16', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L17_BGM_Blue_Strings_Tremelo.ogg", channel='channel17', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L18_BGM_Blue_Wire_Pluck.ogg", channel='channel18', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L19_BGM_Blue_Flutes_Disonant.ogg", channel='channel19', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L20_BGM_Blue_French_Horn_Legatto.ogg", channel='channel20', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L21_BGM_Blue_French_Horn_Staccato.ogg", channel='channel21', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L0.ogg", channel='channel22', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L1.ogg", channel='channel23', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L2.ogg", channel='channel24', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L3.ogg", channel='channel25', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)

    ##Attempt comments
    $config.rollback_enabled = True
    $config.allow_skipping = True
    hide screen disable_hide
    hide screen grammar_h4
    hide screen grammar_hard3
    hide screen grammar_h2
    hide screen grammar_hard5
    hide screen grammar_h1
    if (gramHard_attempts == 0):
        show Ada amused at right
        show Blue neutral at center
        show Grace snarky at left
        g "Ha, ha, Blue! Got it on the first try."
        show Blue pout
        b "Meh."  
        if (gramMed_attempts==0) and (attemptsGramEasy==0):
            $achievement.Sync()
            $achievement.sync()
            $achievement.grant("ACH_GRAMMAR")
            $achievement.sync()
            $achievement.Sync()
    if (gramHard_attempts==1):
        show Ada neutral at right
        show Blue smug at center
        show Grace neutral at left
        b "This demonstrates why humans are inferior."
        show Grace annoyed
        g "It was one mistake. One."
        show Blue flirty
        b "One more than I would have made!"
    if (gramHard_attempts>1):
        show Grace annoyed at left
        show Ada neutral at right
        show Blue neutral at center
        g "That was harder than I anticipated, but I still got it."
        show Blue pout
        b "Who would have thought? Fortunately for you human, the condition was if you could solve it."
        show Blue smug
        b "Next time I'll impose a number of tries before I consider you having lost the game."
    if (resume=="E"):
        jump ch4postPuzzle1_E
    if (resume=="SbE"):
        jump ch4postPuzzle1_SbE
    if(resume=="S"):
        jump ch4postPuzzle1_S
        
label choose_gramHard:
    $quick_menu=False
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
    stop channel12 fadeout 1.0
    stop channel13 fadeout 1.0
    stop channel14 fadeout 1.0
    stop channel15 fadeout 1.0
    stop channel16 fadeout 1.0
    stop channel17 fadeout 1.0
    stop channel18 fadeout 1.0
    stop channel19 fadeout 1.0
    stop channel20 fadeout 1.0
    stop channel21 fadeout 1.0
    stop channel22 fadeout 1.0
    stop channel23 fadeout 1.0
    stop channel24 fadeout 1.0
    stop channel25 fadeout 1.0
    
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    $gramHardHints=0
    if (tutorial_gramHard): #UNCOMMENT ME WHEN TUTORIAL IS IN
        $pageUnlocked_notes +=1
        $tutorial_gramHard = False
        jump tutorial_gramHard_1
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

    $randomNumberHardGram = renpy.random.randint(0,4)
    if randomNumberHardGram==0:
        jump eng_gram_h1
    if randomNumberHardGram==1:
        jump eng_gram_h2
    if randomNumberHardGram==2:
        jump eng_gram_h3
    if randomNumberHardGram==3:
        jump eng_gram_h4
    if randomNumberHardGram==4:
        jump eng_gram_h5
    "If you see this, an error has occured. Please contact Blue or some other capable individual to resolve."

label blueSpace_puzzle:
    $config.rollback_enabled = True
    $config.allow_skipping = True
    hide screen disable_hide
    hide screen grammar_h4
    hide screen grammar_hard3
    hide screen grammar_h2
    hide screen grammar_hard5
    hide screen grammar_h1
    $quick_menu = True
    scene bg blueMain with fade
    stop music fadeout 1.0
    $renpy.music.play("music/BGM/Blue/EHNF_L0_BGM_Blue_Kick.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L1_BGM_Blue_Ghost_Kick.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L2_BGM_Blue_3p_Horn_Bus.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L3_BGM_Blue_Snare.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L4_BGM_Blue_Percussion.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L5_BGM_Blue_Cymbals_Large.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L6_BGM_Blue_Cymbals_Small.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L7_BGM_Blue_Cymbals_Swells.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L8_BGM_Blue_Glass_Mallet.ogg", channel='channel08', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L9_BGM_Blue_Liquid_Mallet.ogg", channel='channel09', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L10_BGM_Blue_Reflective_Mallet.ogg", channel='channel10', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L11_BGM_Blue_Grime_Bass.ogg", channel='channel11', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L12_BGM_Blue_Sub_Bass.ogg", channel='channel12', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L13_BGM_Blue_Sparkling_Water_Drops.ogg", channel='channel13', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L14_BGM_Blue_Ambient_Room_Pad.ogg", channel='channel14', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L15_BGM_Blue_Strings_Legatto.ogg", channel='channel15', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L16_BGM_Blue_Strings_Staccato.ogg", channel='channel16', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L17_BGM_Blue_Strings_Tremelo.ogg", channel='channel17', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L18_BGM_Blue_Wire_Pluck.ogg", channel='channel18', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L19_BGM_Blue_Flutes_Disonant.ogg", channel='channel19', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L20_BGM_Blue_French_Horn_Legatto.ogg", channel='channel20', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/Blue/EHNF_L21_BGM_Blue_French_Horn_Staccato.ogg", channel='channel21', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L0.ogg", channel='channel22', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L1.ogg", channel='channel23', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L2.ogg", channel='channel24', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Blue/EHNF_BW_L3.ogg", channel='channel25', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)

    show Ada neutral at right
    show Grace neutral at left
    show Blue neutral at center
    g "It's okay, I've got this."
    show Blue smug
    b "Keep telling yourself that."
    show Blue pout
    b "But do let me know when you're done wasting my time. Just tap on me when you want to try again."
    show Blue smug
    b "I know how difficult this can be for a mere human."
    window hide
    hide Grace
    hide Ada
    $quick_menu = False
    hide Blue
    call screen gramHard_puzzleItem_scr
    
#####HINTS
label hints_gramHard_1:
    show screen disable_hide
    $config.skipping=None
    $remainder = gramHardHints%3 
    show gram_h1_tile202 at Position(xpos = letterK1x, xanchor = 0, ypos = letterK1y, yanchor = 0)
    show gram_h1_tile206 at Position(xpos = letterK2x, xanchor = 0, ypos = letterK2y, yanchor = 0)
    show gram_h1_tile203 at Position(xpos = letterT3x, xanchor = 0, ypos = letterT3y, yanchor = 0)
    show gram_h1_tile205 at Position(xpos = letterA4x, xanchor = 0, ypos = letterA4y, yanchor = 0)
    show gram_h1_tile201 at Position(xpos = lettertT5x, xanchor = 0, ypos = lettertT5y, yanchor = 0)
    show gram_h1_tile204 at Position(xpos = letterA6x, xanchor = 0, ypos = letterA6y, yanchor = 0)
    show gram_h1_tile208 at Position(xpos = letterF7x, xanchor = 0, ypos = letterF7y, yanchor = 0)
    show other darken onlayer screens
    $gramHardHints +=1
    if (remainder==0):
        a "T can produce both an expansion and a one-to-one substitution. Fortunately, as we have the framework, determining which substitution should be used for which T is as simple as counting the number of child slots available."
    if (remainder==1):
        a "K is both terminal and intermediary, so it will be on the bottom of the tree once and in a middle position once."
    if (remainder==2):
        a "A has two potential string substitutions, but both are terminal, and I have the feeling that as long as the A's are in the correct position the strings will follow suit."
    hide other darken onlayer screens
    hide gram_h1_tile202
    hide gram_h1_tile206 
    hide gram_h1_tile203
    hide gram_h1_tile205
    hide gram_h1_tile201
    hide gram_h1_tile204
    hide gram_h1_tile208
    jump gamefile_h1
    
label hints_gramHard_2:
    show screen disable_hide
    $config.skipping=None
    $remainder = gramHardHints%3 
    show gram_h2_tile202 at Position(xpos = letterT1x, xanchor = 0, ypos = letterT1y, yanchor = 0)
    show gram_h2_tile206 at Position(xpos = letterT2x, xanchor = 0, ypos = letterT2y, yanchor = 0)
    show gram_h2_tile203 at Position(xpos = letterT3x, xanchor = 0, ypos = letterT3y, yanchor = 0)
    show gram_h2_tile205 at Position(xpos = letterQ4x, xanchor = 0, ypos = letterQ4y, yanchor = 0)
    show gram_h2_tile201 at Position(xpos = letterQ5x, xanchor = 0, ypos = letterQ5y, yanchor = 0)
    show gram_h2_tile204 at Position(xpos = letterK6x, xanchor = 0, ypos = letterK6y, yanchor = 0)
    show gram_h2_tile208 at Position(xpos = letterJ7x, xanchor = 0, ypos = letterJ7y, yanchor = 0)
    show gram_h2_tile209 at Position(xpos = letterM8x, xanchor = 0, ypos = letterM8y, yanchor = 0)
    show gram_h2_tile210 at Position(xpos = letterS9x, xanchor = 0, ypos = letterS9y, yanchor = 0)
    show gram_h2_tile211 at Position(xpos = letterS10x, xanchor = 0, ypos = letterS10y, yanchor = 0)
    show other darken onlayer screens
    $gramHardHints +=1
    if (remainder==0):
        a "There are two two-letter substitutions for T; I would advise looking at their substitutions in turn to determine if you should use QQ or JM. JM has two terminal substitutions and QQ only one."
    if (remainder==1):
        a "The substitutions for S indicate that it will be used only at the top of the tree and at the very bottom of the tree."
    if (remainder==2):
        a "K,J, and M are all terminal letters that will be used only once in the puzzle. As they are terminal, they must all be used in the bottom of the tree."
    hide other darken onlayer screens
    hide gram_h2_tile202
    hide gram_h2_tile206 
    hide gram_h2_tile203
    hide gram_h2_tile205
    hide gram_h2_tile201
    hide gram_h2_tile204
    hide gram_h2_tile208
    hide gram_h2_tile209
    hide gram_h2_tile210
    hide gram_h2_tile211
    jump gamefile_h2
    
label hints_gramHard_3:
    show screen disable_hide
    $config.skipping=None
    $remainder = gramHardHints%3 
    show gram_h3_letterS1 at Position(xpos = letterS1x, xanchor = 0, ypos = letterS1y, yanchor = 0)
    show gram_h3_letterS2 at Position(xpos = letterS2x, xanchor = 0, ypos = letterS2y, yanchor = 0)
    show gram_h3_letterS3 at Position(xpos = letterS3x, xanchor = 0, ypos = letterS3y, yanchor = 0)
    show gram_h3_letterS4 at Position(xpos = letterS4x, xanchor = 0, ypos = letterS4y, yanchor = 0)
    show gram_h3_letterS5 at Position(xpos = letterS5x, xanchor = 0, ypos = letterS5y, yanchor = 0)
    show gram_h3_letterT1 at Position(xpos = letterT1x, xanchor = 0, ypos = letterT1y, yanchor = 0)
    show gram_h3_letterT2 at Position(xpos = letterT2x, xanchor = 0, ypos = letterT2y, yanchor = 0)
    show gram_h3_letterT3 at Position(xpos = letterT3x, xanchor = 0, ypos = letterT3y, yanchor = 0)
    show gram_h3_letterJ at Position(xpos = letterJx, xanchor = 0, ypos = letterJy, yanchor = 0)
    show gram_h3_letterK at Position(xpos = letterKx, xanchor = 0, ypos = letterKy, yanchor = 0)
    show gram_h3_letterH at Position(xpos = letterHx, xanchor = 0, ypos = letterHy, yanchor = 0)
    show other darken onlayer screens
    $gramHardHints +=1
    if (remainder==0):
        a "S has three possible substitutions, but they vary in the amount of letters. I would suggest looking at the number of children an S tile has to determine which rule applies. S can be terminal, but it just goes to an empty string."
    if (remainder==1):
        a "T has three valid substitution as well, Grace, but like S, the two intermediary ones produce different amounts of letters and the third substitution is terminal."
    if (remainder==2):
        a "J, K, and H are only used once each and all three are terminal, so they all belong in the bottom of the tree."
    hide other darken onlayer screens
    hide gram_h3_letterS1
    hide gram_h3_letterS2
    hide gram_h3_letterS3
    hide gram_h3_letterS4
    hide gram_h3_letterS5
    hide gram_h3_letterT1
    hide gram_h3_letterT2
    hide gram_h3_letterT3
    hide gram_h3_letterJ
    hide gram_h3_letterK
    hide gram_h3_letterH
    jump gamefile_h3
    
label hints_gramHard_4:
    show screen disable_hide
    $config.skipping=None
    $remainder = gramHardHints%3 
    show gram_h4_tile202 at Position(xpos = letterK1x, xanchor = 0, ypos = letterK1y, yanchor = 0)
    show gram_h4_tile206 at Position(xpos = letterK2x, xanchor = 0, ypos = letterK2y, yanchor = 0)
    show gram_h4_tile203 at Position(xpos = letterM3x, xanchor = 0, ypos = letterM3y, yanchor = 0)
    show gram_h4_tile205 at Position(xpos = letterA4x, xanchor = 0, ypos = letterA4y, yanchor = 0)
    show gram_h4_tile201 at Position(xpos = lettertT5x, xanchor = 0, ypos = lettertT5y, yanchor = 0)
    show gram_h4_tile204 at Position(xpos = letterA6x, xanchor = 0, ypos = letterA6y, yanchor = 0)
    show gram_h4_tile208 at Position(xpos = letterH7x, xanchor = 0, ypos = letterH7y, yanchor = 0)
    show gram_h4_tile408 at Position(xpos = letterA8x, xanchor = 0, ypos = letterA8y, yanchor = 0)
    show gram_h4_tile409 at Position(xpos = letterT9x, xanchor = 0, ypos = letterT9y, yanchor = 0)
    show gram_h4_tile410 at Position(xpos = letterA10x, xanchor = 0, ypos = letterA10y, yanchor = 0)
    show gram_h4_tile411 at Position(xpos = letterT11x, xanchor = 0, ypos = letterT11y, yanchor = 0)
    show other darken onlayer screens
    $gramHardHints +=1
    if (remainder==0):
        a "If you look at the substitutions, all the ones that require three letters have T in the middle. Therefore, it may be prudent to look at placing T's in the middle of the tree."
    if (remainder==1):
        a "It appears that there may be two correct solutions, as the empty strings can be moved around--the order of the words in relation to each other will dictate the answer."
    if (remainder==2):
        a "The outside branches of the tree are fairly straightforward. K and A both have two substitutions, but for each of them, one is terminal, and one is not, making it easy to determine which case can be applied where."
    hide other darken onlayer screens
    hide gram_h4_tile202
    hide gram_h4_tile206 
    hide gram_h4_tile203
    hide gram_h4_tile205
    hide gram_h4_tile201
    hide gram_h4_tile204
    hide gram_h4_tile208
    hide gram_h4_tile408
    hide gram_h4_tile409
    hide gram_h4_tile410
    hide gram_h4_tile411
    jump gamefile_h4
    
label hints_gramHard_5:
    show screen disable_hide
    $config.skipping=None
    $remainder = gramHardHints%3 
    show gram_h5_letterK1 at Position(xpos = letterK1x, xanchor = 0, ypos = letterK1y, yanchor = 0)
    show gram_h5_letterK2 at Position(xpos = letterK2x, xanchor = 0, ypos = letterK2y, yanchor = 0)
    show gram_h5_letterK3 at Position(xpos = letterK3x, xanchor = 0, ypos = letterK3y, yanchor = 0)
    show gram_h5_letterK4 at Position(xpos = letterK4x, xanchor = 0, ypos = letterK4y, yanchor = 0)
    show gram_h5_letterR at Position(xpos = letterRx, xanchor = 0, ypos = letterRy, yanchor = 0)
    show gram_h5_letterA at Position(xpos = letterAx, xanchor = 0, ypos = letterAy, yanchor = 0)
    show gram_h5_letterM at Position(xpos = letterMx, xanchor = 0, ypos = letterMy, yanchor = 0)
    show gram_h5_letterJ at Position(xpos = letterJx, xanchor = 0, ypos = letterJy, yanchor = 0)
    show gram_h5_letterT at Position(xpos = letterTx, xanchor = 0, ypos = letterTy, yanchor = 0)
    show other darken onlayer screens
    $gramHardHints +=1
    if (remainder==0):
        a "K has multiple potential substitutions, but they all have different lengths. If you look at the amount of children the slot has, it should be easy to determine which substitution is correct."
    if (remainder==1):
        a "The tree is fairly shallow but the deepest branch includes a substitution where one letter is terminal and one is not."
    if (remainder==2):
        a "There are six terminal nodes, but it appears two of them will include epsilon as there are only four unique words. That means that two of the terminal slots will be K."
    hide other darken onlayer screens
    hide gram_h5_letterK1
    hide gram_h5_letterK2 
    hide gram_h5_letterK3
    hide gram_h5_letterK4
    hide gram_h5_letterR
    hide gram_h5_letterA
    hide gram_h5_letterM
    hide gram_h5_letterJ
    hide gram_h5_letterT
    jump gamefile_h5