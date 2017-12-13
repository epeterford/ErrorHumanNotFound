
##############################################################################
#LOOP LOGIC PUZZLE
############SCREENS####################################
screen llHardLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("chooseLLHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("watsonRight_llH")
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
        
screen llHardWin_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("llHardDone")
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
        
screen tutorial_scrLLHard_1:
    imagebutton:
        idle "next.png" 
        hover "next_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("tutorial_LLHard_2")
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
    
screen tutorial_scrLLHard_2:
    imagebutton:
        idle "back.png" 
        hover "back_hover.png" 
        xpos 0
        ypos 940 
        focus_mask True
        action Jump("tutorial_LLHard_1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("chooseLLHard")
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

################################LABELS########################################################
        
label llHardLose:
    show other darken
    image llHard_loseImage ="llHard_lose.png" 
    show llHard_loseImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen llHardLose_scr
    
label llHardWin:
    show other darken
    image llHard_winImage = "llHard_win.png" 
    show llHard_winImage at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen llHardWin_scr
    
label llHardDone:
    $ llHard_solved = True 
    $watsonItems_right +=1 
    $quick_menu = True
    $safe_inv = True
    scene bg wsSafe with fade
    $renpy.block_rollback()
    $config.skipping=None
    $config.rollback_enabled = True
    $config.allow_skipping = True
    hide screen disable_hide
    hide screen loopLogicHard_5Scr
    hide screen loopLogicHard_4Scr
    hide screen loopLogicHard_3Scr
    hide screen loopLogicHard_2Scr
    hide screen loopLogicHard_1Scr
    $renpy.music.play("music/Amb/WS/EHNF_WS_AMB.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    stop music fadeout 1.0
    if(llHard_attempts ==0):
        show Grace surprised at left
        show Ada neutral at right
        g "Wow, that was {i}surprisingly{/i} easy."
        show Ada seething
        a "I fear that this was only part of the work needed to determine where he is, however."
        show Grace sad
        g "Couldn't even let me have this victory for a moment?"
        show Ada neutral
        a "I apologize, but we are running out of time."
        if (llMed_attempts==0) and (loopLogicEasy_tries==0):
            $achievement.Sync()
            $achievement.sync()
            $achievement.grant("ACH_LOOP")
            $achievement.sync()
            $achievement.Sync()
    if(llHard_attempts ==1):
        show Grace neutral at left
        show Ada neutral at right
        g "Alright, safe-cracking, even electronically, may not be my speciality. Why does an AI even need a physical safe?"
        show Ada amused
        a "You are asking as if Watson ever does anything by what might be considered normal logic rules."
        show Grace snarky
        g "Can't argue with you there."
    if(llHard_attempts>1):
        show Grace angry at left
        show Ada neutral at right
        g "If Watson ever gets an android body, I'm going to strangle him!"
        show Ada surprised
        a "I do not think attempting to strangle a metal alloy body will succeed."
        show Grace annoyed
        g "Don't give me your logic sass! That little trickster had a ridiculous level of encryption for the
           lock on this safe. I managed to circumvent it eventually, but seriously, why Watson?"
        show Ada amused
        a "Perhaps you can ask him when we find him."
    show Grace neutral
    show Ada neutral
    g "Let's see what was so important..."
    hide Grace
    hide Ada
    show other darken
    show image "objects/jumpdrive_closeup.png" at centerScreen
    "{i}It appears to be another drive like that discovered on Alpha's body.{/i}"
    hide other darken
    hide image "objects/jumpdrive_closeup.png" at centerScreen
    show Grace happy at left
    show Ada neutral at right
    a "This is the decryption key for all the data drives we have found."
    if(drive2_inv):
        show Ada seething
        a "All four are rather large and complex in their encryption, so even with the key this will take some time." 
    else:
        show Ada seething
        a "The drives are rather large and complex with their encryption, so even with the key this will take some time. I also appear to still be missing a piece of the puzzle. Perhaps there is another drive around here?"
        show Grace neutral
        g "We'll take a look."
    show Ada neutral
    a "Unfortunately, my neural network is not quite as capable as a quantum computer."
    show Grace happy
    g "As long as it decodes soon, I'm okay with that."
    show Ada annoyed
    a "Assuming there are no surprises, it will be soon."
    show Grace sad
    g "Great. Let's finish up here, and then I'm going to get ahold of my friend Alan. I need a break from today."
    hide Grace
    hide Ada
    $quick_menu = False
    window hide
    jump watsonRight

label chooseLLHard:
    $quick_menu=False
    stop channel00 fadeout 1.0
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    $LLHardHints=0
    if (tutorial_llHard):
        $tutorial_llHard = False
        $pageUnlocked_notes +=1
        if notes_hard1=="LG":
            $notes_hard2 ="LL"
        else:
            $notes_hard1 = "LL"
        jump tutorial_LLHard_1
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
    $randomNumberHardLL = renpy.random.randint(0,4)
    if randomNumberHardLL==0:
        jump loopLogic_hard1
    if randomNumberHardLL==1:
        jump loopLogic_hard2
    if randomNumberHardLL==2:
        jump loopLogic_hard3
    if randomNumberHardLL==3:
        jump loopLogic_hard4
    if randomNumberHardLL==4:
        jump loopLogic_hard5
    "If you see this, an error has occured. Please contact Blue or some other capable individual to resolve."
    
label tutorial_LLHard_1:
    window hide
    $quick_menu = False
    scene bg tutorial_llHard_1
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrLLHard_1

label tutorial_LLHard_2:
    window hide
    $quick_menu = False
    scene bg tutorial_llHard_2
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrLLHard_2
##########HINTS##################################
label hints_llHard_1:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLHardHints%3 
    show LLH_1_ifR at Position(xpos = ifRx, xanchor = 0, ypos = ifRy, yanchor = 0)
    show LLH_1_ifG at Position(xpos = ifGx, xanchor = 0, ypos = ifGy, yanchor = 0)
    show LLH_1_ifB at Position(xpos = ifBx, xanchor = 0, ypos = ifBy, yanchor = 0)
    show LLH_1_ifRG at Position(xpos = ifRGx, xanchor = 0, ypos = ifRGy, yanchor = 0)
    show LLH_1_ifBG at Position(xpos = ifBGx, xanchor = 0, ypos = ifBGy, yanchor = 0)
    show LLH_1_else1 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLH_1_else2 at Position(xpos = else2x, xanchor = 0, ypos = else2y, yanchor = 0)
    show LLH_1_whileRB at Position(xpos = whileRBx, xanchor = 0, ypos = whileRBy, yanchor = 0)
    show other darken onlayer screens
    $LLHardHints +=1
    if (remainder==0):
        a "There are two split-colored IFs. Given that they pull two color, I would try them in the slots directly to the left and right of the start tiles. I would also put the WHILE tile in the one slot with a charge off of it too."
    if (remainder==1):
        a "Remember that ELSEs only work when they are off of a pipe connector, and there is an IF in the other slot."
    if (remainder==2):
        a "The easy part is pairing the colored IFs with their corresponding lights."
    hide other darken onlayer screens
    hide LLH_1_ifR
    hide LLH_1_ifG 
    hide LLH_1_ifB
    hide LLH_1_ifRG
    hide LLH_1_ifBG
    hide LLH_1_else1
    hide LLH_1_else2
    hide LLH_1_whileRB
    jump gamefile_llh1
    
label hints_llHard_2:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLHardHints%3 
    $LLHardHints +=1
    show LLH_2_ifR at Position(xpos = ifRx, xanchor = 0, ypos = ifRy, yanchor = 0)
    show LLH_2_ifG at Position(xpos = ifGx, xanchor = 0, ypos = ifGy, yanchor = 0)
    show LLH_2_ifB at Position(xpos = ifBx, xanchor = 0, ypos = ifBy, yanchor = 0)
    show LLH_2_ifGR at Position(xpos = ifGRx, xanchor = 0, ypos = ifGRy, yanchor = 0)
    show LLH_2_ifBR at Position(xpos = ifBRx, xanchor = 0, ypos = ifBRy, yanchor = 0)
    show LLH_2_else1 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLH_2_else2 at Position(xpos = else2x, xanchor = 0, ypos = else2y, yanchor = 0)
    show LLH_2_whileR at Position(xpos = whileRx, xanchor = 0, ypos = whileRy, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "Looking at the overall puzzle, I would start with thw two-color IFs. They will narrow the three pipes to two on either side of the start tile."
    if (remainder==1):
        a "Remember that while an IF can go in the same spot as an ELSE, an ELSE can only go in a slot with the connectors on the pipes."
    if (remainder==2):
        a "Fill in the IFs with their matching lights, and the one WHILE with the charge slot, and I believe you will beat this."
    hide other darken onlayer screens
    hide LLH_2_ifR
    hide LLH_2_ifG
    hide LLH_2_ifB 
    hide LLH_2_ifGR
    hide LLH_2_ifBR
    hide LLH_2_else1
    hide LLH_2_else2
    hide LLH_2_whileR
    jump gamefile_llh2
    
label hints_llHard_3:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLHardHints%3 
    $LLHardHints +=1
    show LLH_3_ifR at Position(xpos = ifRx, xanchor = 0, ypos = ifRy, yanchor = 0)
    show LLH_3_ifG at Position(xpos = ifGx, xanchor = 0, ypos = ifGy, yanchor = 0)
    show LLH_3_ifR2 at Position(xpos = ifR2x, xanchor = 0, ypos = ifR2y, yanchor = 0)
    show LLH_3_whileBG at Position(xpos = whileBGx, xanchor = 0, ypos = whileBGy, yanchor = 0)
    show LLH_3_ifBG at Position(xpos = ifBGx, xanchor = 0, ypos = ifBGy, yanchor = 0)
    show LLH_3_whileRG at Position(xpos = whileRGx, xanchor = 0, ypos = whileRGy, yanchor = 0)
    show LLH_3_ifRB at Position(xpos = ifRBx, xanchor = 0, ypos = ifRBy, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "Either WHILE will charge the green charge nodes, but the charge nodes on the right need a color that only one of the WHILEs has. I would start there."
    if (remainder==1):
        a "The nodes with two lights coming off of them will require an IF with two colors, otherwise at best only one light will be powered."
    if (remainder==2):
        a "The remaining nodes just simply require the IFs that match the colors of the light."
    hide other darken onlayer screens
    hide LLH_3_ifR 
    hide LLH_3_ifG
    hide LLH_3_ifR2
    hide LLH_3_whileBG
    hide LLH_3_ifBG
    hide LLH_3_whileRG
    hide LLH_3_ifRB
    jump gamefile_llh3
    
label hints_llHard_4:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLHardHints%3 
    $LLHardHints +=1
    show LLH_4_ifR at Position(xpos = ifRx, xanchor = 0, ypos = ifRy, yanchor = 0)
    show LLH_4_ifG at Position(xpos = ifGx, xanchor = 0, ypos = ifGy, yanchor = 0)
    show LLH_4_ifB1 at Position(xpos = ifB1x, xanchor = 0, ypos = ifB1y, yanchor = 0)
    show LLH_4_ifB2 at Position(xpos = ifB2x, xanchor = 0, ypos = ifB2y, yanchor = 0)
    show LLH_4_ifGR at Position(xpos = ifGRx, xanchor = 0, ypos = ifGRy, yanchor = 0)
    show LLH_4_ifBG at Position(xpos = ifBGx, xanchor = 0, ypos = ifBGy, yanchor = 0)
    show LLH_4_else at Position(xpos = elsex, xanchor = 0, ypos = elsey, yanchor = 0)
    show LLH_4_whileG at Position(xpos = whileGx, xanchor = 0, ypos = whileGy, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "To start with, there is only one WHILE and one charge node. The WHILE is green, but the node feeding it power also needs to feed a blue light."
    if (remainder==1):
        a "Remember that instead of an IF/ELSE, you can also utilize two IFs. Especially if you have an extra color coming into a block compared to what you need out of it."
    if (remainder==2):
        a "The split IFs will let those two colors through and both of those colors will then need an outlet--I recommend putting them in spots with two output pipes."
    hide other darken onlayer screens
    hide LLH_4_ifR
    hide LLH_4_ifG
    hide LLH_4_ifB1
    hide LLH_4_ifB2
    hide LLH_4_ifGR
    hide LLH_4_ifBG
    hide LLH_4_else
    hide LLH_4_whileG
    jump gamefile_llh4
    
label hints_llHard_5:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLHardHints%3 
    $LLHardHints +=1
    show LLH_5_ifR at Position(xpos = ifRx, xanchor = 0, ypos = ifRy, yanchor = 0)
    show LLH_5_ifG at Position(xpos = ifGx, xanchor = 0, ypos = ifGy, yanchor = 0)
    show LLH_5_ifB at Position(xpos = ifBx, xanchor = 0, ypos = ifBy, yanchor = 0)
    show LLH_5_ifRB at Position(xpos = ifRBx, xanchor = 0, ypos = ifRBy, yanchor = 0)
    show LLH_5_whileBG at Position(xpos = whileBGx, xanchor = 0, ypos = whileBGy, yanchor = 0)
    show LLH_5_else at Position(xpos = elsex, xanchor = 0, ypos = elsey, yanchor = 0)
    show LLH_5_whileGR at Position(xpos = whileGRx, xanchor = 0, ypos = whileGRy, yanchor = 0)
    show LLH_5_whileBR at Position(xpos = whileBRx, xanchor = 0, ypos = whileBRy, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "I would recommend starting with the WHILE tiles. Some lights will not be available until the correct WHILE tile has lit up both of the corresponding charge nodes."
    if (remainder==1):
        a "Since there is only a single green light branching off the larger IF block, that IF requires two colors since there are three lines leading in."
    if (remainder==2):
        a "The most complex part of the IFs is determining where to use the else and where to use the green IF since there are two green lights. There is only one red IF and one red light, and the same for blue, so those should be easy enough."
    hide other darken onlayer screens
    hide LLH_5_ifR
    hide LLH_5_ifG 
    hide LLH_5_ifB
    hide LLH_5_ifRB
    hide LLH_5_whileBG
    hide LLH_5_else
    hide LLH_5_whileGR
    hide LLH_5_whileBR
    jump gamefile_llh5