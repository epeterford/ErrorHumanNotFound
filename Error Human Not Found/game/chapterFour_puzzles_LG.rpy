#LOGIC GATE PUZZLE
screen lgHardLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("choose_lgHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("watsonLeft_pre")
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
        
screen lgHardDone_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("lgHard_doneTalk")
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
        
screen lgHardWin_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("choose_lgHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610
        focus_mask True
        action Jump("watsonLeft_pre")
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
        
screen lgHardWin_scr2:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("choose_lgHard")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610
        focus_mask True
        action Jump("watsonLeft_pre")
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
    
screen tutorial_scrLGHard_1:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("choose_lgHard")
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
    
label choose_lgHard:
    $LGHardHints =0
    stop channel00 fadeout 1.0
    $slot_name=""
    $gate_name = ""
    $temp_gate = ""
    $ temp_slot = ""
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    window hide
    hide Ada
    hide Grace
    $quick_menu = False
    if(tutorial_lgHard):
        $tutorial_lgHard = False
        $pageUnlocked_notes +=1
        if notes_hard1 =="LL":
            if notes_hard2 =="B":
                $notes_hard3 = "LG"
            else:
                $notes_hard2 = "LG"
        else:
            $notes_hard1 = "LG"
        jump tutorial_lgHard_1
    $randomLGHard = renpy.random.randint(0,2)
    if(lgHardA_solved==False):
        if(randomLGHard==0):
            jump logicGate_hardA1
        if(randomLGHard==1):
            jump logicGate_hardA2
        if(randomLGHard==2):
            jump logicGate_hardA3
    if(lgHardB_solved==False):
        if(randomLGHard==0):
            jump logicGate_hardB1
        if(randomLGHard==1):
            jump logicGate_hardB2
        if(randomLGHard==2):
            jump logicGate_hardB3
    if(lgHardC_solved==False):
        if(randomLGHard==0):
            jump logicGate_hardC1
        if(randomLGHard==1):
            jump logicGate_hardC2
        if(randomLGHard==2):
            jump logicGate_hardC3
            
label tutorial_lgHard_1:
    window hide
    $quick_menu = False
    scene bg tutorial_lgHard
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrLGHard_1
    
label lgHard_lose:
    $config.skipping=None
    $renpy.block_rollback()
    show other darken
    image lgHardA_loseImage = "lgHardA_lose.png"
    show lgHardA_loseImage at centerScreen2
    call screen lgHardLose_scr
    
label lgHard_lose2:
    $config.skipping=None
    $renpy.block_rollback()
    show other darken
    image lgHardB_loseImage = "lgHardB_lose.png"
    show lgHardB_loseImage at centerScreen2
    call screen lgHardLose_scr
    
label lgHard_lose3:
    $config.skipping=None
    $renpy.block_rollback()
    show other darken
    image lgHardC_loseImage = "lgHardC_lose.png"
    show lgHardC_loseImage  at centerScreen2
    call screen lgHardLose_scr
    
label lgHard_done:
    $config.skipping=None
    $renpy.block_rollback()
    show other darken
    image lgHardC_winImage = "lgHardC_win.png"
    show lgHardC_winImage at centerScreen2
    call screen lgHardDone_scr
    
label lgHard_win:
    $config.skipping=None
    $renpy.block_rollback()
    show other darken
    image lgHardA_winImage = "lgHardA_win.png"
    show lgHardA_winImage at centerScreen2
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $stackDepth -=1
    call screen lgHardWin_scr
    
label lgHard_win2:
    $config.skipping=None
    $renpy.block_rollback()
    show other darken
    image lgHardB_winImage = "lgHardB_win.png"
    show lgHardB_winImage at centerScreen2
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $stackDepth -=1
    call screen lgHardWin_scr2
    
    
label watsonLeft_pre:
    if not(binaryHard_solved ):
        scene bg wsDesk_drive with fade
    else:
        scene bg wsDesk with fade
    $quick_menu = True
    if lgHard_attempts==0:
        show Grace neutral at left
        show Ada neutral at right
        g "Still need to check a few areas for Watson."
        a "I will do it momentarily, Grace. Perhaps there is something else you can do while I free some more RAM?"
    else:
        show Grace neutral at left
        show Ada annoyed at right
        a "I need a moment before I finish searching for Watson."
        g "Do try not to take too long--we don't have much time left."
        show Ada neutral
        a "I am aware of the time limit imposed of us. I will finish the search within the allotted time."
    $quick_menu = False
    hide Grace
    hide Ada
    window hide
    jump watsonLeft
    
#######################################NEED TO FINISH THE FAILS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
label lgHard_doneTalk:
    $quick_menu = True
    $config.skipping = None
    $renpy.block_rollback()
    stop music fadeout 1.0
    $watsonItems_left +=1
    $renpy.music.play("music/Amb/WS/EHNF_WS_AMB.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    if not(binaryHard_solved ):
        scene bg wsDesk_drive with fade
    else:
        scene bg wsDesk with fade
    show Grace neutral at left
    if(lgHard_attempts==0):
        show Ada happy at right
        a "I have yet to discover anything in the physical realm that matches the joy experienced when code executes flawlessly."
        if (lgMed_attempts==0) and (lgEasy_tries==0):
            $achievement.Sync()
            $achievement.sync()
            $achievement.grant("ACH_LOGIC")
            $achievement.sync()
            $achievement.Sync()
    if(lgHard_attempts==1):
        show Ada neutral at right
        a "The amount of firewalls Watson utilizes to try and conceal his location is absurd. He spends more time working to not be found than if he just did his work in the first place."
        show Grace snarky
        g "Had a few problems breaking them, I take it?"
        show Ada annoyed
        a "They are down now."
    if(lgHard_attempts==2):
        show Ada annoyed at right
        a "When Watson does surface, I am going to show his firewalls to Colossus. He is excellent at security protocols when it benefits him."
        show Grace snarky
        g "I think someone may be rusty. That, or you are focusing more on other areas like walking and not crashing into doors."
        show Ada seething
        a "I was able to conduct the search despite his countermeasures."
    if(lgHard_attempts>2):
        show Ada seething at right
        a "I am tempted to find Watson and stick him in a harddrive and jettison it into space."
        show Grace surprised
        g "That seems a bit extreme."
        show Ada amused
        a "Perhaps. I did get around his firewalls and finish my search. However, I experienced far more difficulty than anticipated."
        show Grace snarky
        g "Welcome to the normal state of us mere mortals."
    show Ada annoyed
    a "I could not locate Watson on any of the devices connected to the network. It seems he is offline somewhere."
    show Grace annoyed
    g "He couldn't do that by himself. Guess we won't be talking to him right now."
    show Ada seething
    a "It would seem so."
    show Grace sad
    g "Well, I suppose we can't do anything about it now. What are we on, plan Z?"
    hide Ada
    hide Grace
    window hide
    $quick_menu = False
    jump watsonLeft
        
label hints_lgHardA1:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGHardHints%3 
    $LGHardHints +=1
    show HA199tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show HA199tile07_09 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show HA199tile07_08 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "Remember, the crescent moon with the curved line to the left of it is the XOR gate, or the {i}exclusive{/i} OR gate. It only turns green when one input is zero, or red, and one input is one, or green."
    if (remainder==1):
        g "The end light is green with a NOT gate before it, meaning we need a red line to come out of the last slot where we can put a gate."
    if (remainder==2):
        g "There are multiple correct answers, though I would suggest placing the XOR at either the beginning or the end."
    hide other darken onlayer screens
    hide HA199tile07_02
    hide HA199tile07_09
    hide HA199tile07_08
    jump gamefileHA1
    
label hints_lgHardA2:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGHardHints%3 
    $LGHardHints +=1
    show HA216tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show HA216tile07_09 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show HA216tile07_08 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "With the last gate before the light being a NOR gate, to get a green light we need both inputs in to be red. The only way to get a red output from the top slot is to use the AND gate there."
    if (remainder==1):
        g "With the NOT gate on the bottom input going into the NOR gate, we need the last slot that we can fill to output green."
    if (remainder==2):
        g "With the XOR gate, or the exclusive OR, it only outputs green when one input is red and one is green. Otherwise the output will be red. That's the crescent moon with the curved line to the left of it."
    hide other darken onlayer screens
    hide HA216tile07_02
    hide HA216tile07_08
    hide HA216tile07_09
    jump gamefileHA2
    
label hints_lgHardA3:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGHardHints%3 
    $LGHardHints +=1
    show HA399tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show HA399tile07_09 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show HA399tile07_08 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "There are a handful of correct solutions to this puzzle. Just remember, the crescent moon with the curved line to the left of it is the XOR gate, which outputs green if and only if one input is green and one input is red."
    if (remainder==1):
        g "Personally, I would put the XOR in a position where it would output green, like the bottom."
    if (remainder==2):
        g "As long as one input is green into the final gate, if I use the OR gate there it will output green."
    hide other darken onlayer screens
    hide HA399tile07_02 
    hide HA399tile07_09
    hide HA399tile07_08
    jump gamefileHA3
    
label hints_lgHardB1:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGHardHints%3 
    $LGHardHints +=1
    show HB1250tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
    show HB1250tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
    show HB1250tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show HB1250tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "We need two green lines going into the NAND gate so that the output is red and is then flipped by the NOT gate to get the light to turn green."
    if (remainder==1):
        g "The bottom middle gate looks like we might want to put an XOR there. To get the XOR to output green, we need a red line to come in. To get that, we could use either an AND or an XOR gate in the bottom left."
    if (remainder==2):
        g "With the NOR, it will output red if put it in the upper left slot. That would mean we have to use an XOR gate to the right of that to get two green lines for the NAND gate."
    hide other darken onlayer screens
    hide HB1250tile02_09
    hide HB1250tile02_10
    hide HB1250tile07_02
    hide HB1250tile07_08
    jump gamefileHB1
    
label hints_lgHardB2:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGHardHints%3 
    $LGHardHints +=1
    show HB1260tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
    show HB1260tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
    show HB1260tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show HB1260tile07_08 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "With the NOR gate at the end, we need two red inputs to get a green output. The bottom row is a good place to start, as the OR needs two red inputs to output red, which requires a green input into the NOT gate, and only one of our gates will output green with a double red input."
    if (remainder==1):
        g "Since we have two XOR's, I might try one in the first slot on the top, as that will give the middle slot a double green input, which with the other XOR produces a red output."
    if (remainder==2):
        g "The AND gate is going to turn red unless there are two green inputs, but we want red lines going into the final gate so you might want to place it where it will output red."
    hide other darken onlayer screens
    hide HB1260tile02_09
    hide HB1260tile02_10
    hide HB1260tile07_02
    hide HB1260tile07_08
    jump gamefileHB2
    
label hints_lgHardB3:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGHardHints%3 
    $LGHardHints +=1
    show HB12tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
    show HB12tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
    show HB12tile07_02 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show HB12tile07_08 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "Since our end goal is red, we need both inputs into the final OR gate to be red. For the bottom, we need green going into the NOT gate which means both inputs for the AND gate need to be green."
    if (remainder==1):
        g "The NOR gate is especially useful as it will output red unless both inputs are red. I would put it towards the end, posssibly in the last gate, to get a red output."
    if (remainder==2):
        g "I would go ahead and try putting the NAND gate in the top slot, if you're stuck. It will output green, but if you get the bottom to output red for the last top gate, you should be good."
    hide other darken onlayer screens
    hide HB12tile02_09
    hide HB12tile02_10
    hide HB12tile07_02
    hide HB12tile07_08
    jump gamefileHB3
    
label hints_lgHardC1:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGHardHints%3 
    $LGHardHints +=1
    show HB1295tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
    show HB1295tile02_10 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
    show HB1195tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show HB1195tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "To get the light to turn green, we need two red lines into the NOR gate. To do that, we first have to get two red lines into the OR gate, which means we cannot use the XOR or the NAND gate in the top slot."
    if (remainder==1):
        g "The NAND gate will turn anything with at least one red input green, and since the right two gates in the bottom portion need the outputs to be red, I would put it in the leftmost slot on the bottom row."
    if (remainder==2):
        g "To get the correct solution, I wouldn't fuss two much about where the AND and XOR go. Both will output red when both inputs are red."
    hide other darken onlayer screens
    hide HB1295tile02_09
    hide HB1295tile02_10
    hide HB1195tile07_02
    hide HB1195tile07_08
    jump gamefileHC1
    
label hints_lgHardC2:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGHardHints%3 
    $LGHardHints +=1
    show HC1290tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
    show HC1290tile02_10 at Position(xpos = xor2x, xanchor = 0, ypos = xor2y, yanchor = 0)
    show HC1190tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show HC1190tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "With the AND gate at the end, we need both inputs to be green. Only the AND gate will output green when both inputs are green."
    if (remainder==1):
        g "There is no spot where the NOR gate will output green, as it requires both inputs to be red and that doesn't occur anywhere. So for this puzzle, it will always output red."
    if (remainder==2):
        g "The bottom gate on the right has to be an XOR gate to output green, given that the NOR gate cannot and the AND gate is required elsewhere. It needs one red input and one green input to output green, remember."
    hide other darken onlayer screens
    hide HC1290tile02_09
    hide HC1290tile02_10
    hide HC1190tile07_02
    hide HC1190tile07_08
    jump gamefileHC2
    
label hints_lgHardC3:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGHardHints%3 
    $LGHardHints +=1
    show HC1270tile02_09 at Position(xpos = xor1x, xanchor = 0, ypos = xor1y, yanchor = 0)
    show HC1170tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show HC1270tile02_10 at Position(xpos = nor2x, xanchor = 0, ypos = nor2y, yanchor = 0)
    show HC1170tile07_02 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "With the final gate being an AND gate, we need both inputs to be green. For the top slot, that means we need a gate that will output green with two red inputs, and only one of our three types of available gates will do that."
    if (remainder==1):
        g "To get the bottom green, there are a couple of different options. Personally, I would start with the NOR gate as the OR gate is the easiest gate we have to get to output green."
    if (remainder==2):
        g "Since the XOR gate only works if exactly one input is green, I would not use it anyplace where that condition does not exist. I would place that before I tried to insert the OR gate."
    hide other darken onlayer screens
    hide HC1270tile02_09
    hide HC1270tile02_10
    hide HC1170tile07_08
    hide HC1170tile07_02
    jump gamefileHC3
    