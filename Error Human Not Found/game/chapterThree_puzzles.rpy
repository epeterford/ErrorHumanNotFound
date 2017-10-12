#LOGIC GATE PUZZLE
screen lgMedLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("choose_lgMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("wwDoor")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen lgMedDone_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("lgMed_doneTalk")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen lgMedWin_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("choose_lgMed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610
        focus_mask True
        action Jump("wwDoor")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
screen wwDoor_scr:
    imagebutton:
        idle "objects/wwDoor_idle.png"
        hover "objects/wwDoor_hover.png"
        xpos 0
        ypos 0
        focus_mask True
        action Jump("choose_lgMed")
        hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
        activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        
label choose_lgMed:
    $LGMedHints =0
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    stop channel06 fadeout 1.0
    $slot_name=""
    $gate_name = ""
    $temp_gate = ""
    $ temp_slot = ""
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    window hide
    hide Ada
    $quick_menu = False
    $randomLGMed = renpy.random.randint(0,2)
    #if(lgMedA_solved==False)and(lgMed_attempts==0):
        #jump tutorial_lgMed_1
    if(lgMedA_solved==False):
        if(randomLGMed==0):
            jump logicGate_mediumA1
        if(randomLGMed==1):
            jump logicGate_mediumA2
        if(randomLGMed==2):
            jump logicGate_mediumA3
    if(lgMedB_solved==False):
        if(randomLGMed==0):
            jump logicGate_mediumB1
        if(randomLGMed==1):
            jump logicGate_mediumB2
        if(randomLGMed==2):
            jump logicGate_mediumB3
    if(lgMedC_solved==False):
        if(randomLGMed==0):
            jump logicGate_mediumC1
        if(randomLGMed==1):
            jump logicGate_mediumC2
        if(randomLGMed==2):
            jump logicGate_mediumC3

label wwDoor:
    $quick_menu = True
    $config.skipping = None
    $renpy.block_rollback()
    stop music fadeout 1.0
    play channel00 wwAmb0 fadeout 1.0 fadein 1.0
    play channel01 wwAmb1 fadeout 1.0 fadein 1.0
    play channel02 wwAmb2 fadeout 1.0 fadein 1.0
    play channel03 wwAmb3 fadeout 1.0 fadein 1.0
    play channel04 wwAmb4 fadeout 1.0 fadein 1.0
    play channel05 wwAmb5 fadeout 1.0 fadein 1.0
    play channel06 wwAmb6 fadeout 1.0 fadein 1.0
    scene bg door2 with fade
    show Ada seething at right
    a "Alright Ada. If Grace could do it, then you can too. It just might take a little more practice."
    hide Ada
    $quick_menu = False
    window hide
    call screen wwDoor_scr
    
label lgMed_lose:
    $config.skipping=None
    $renpy.block_rollback()
    show other darken
    image segmentFailed = "segmentFailed.png"
    show segmentFailed at centerScreen2
    call screen lgMedLose_scr
    
label lgMed_done:
    $config.skipping=None
    $renpy.block_rollback()
    show other darken
    image passwordAccepted = "passwordAccepted.png" #CHANGE ME
    show passwordAccepted at centerScreen2
    call screen lgMedDone_scr
    
label lgMed_win:
    $config.skipping=None
    $renpy.block_rollback()
    show other darken
    image segmentComplete = "segmentComplete.png"
    show segmentComplete at centerScreen2
    $ stackDepth =renpy.call_stack_depth()
    while stackDepth>0:
        $renpy.pop_call()
        $stackDepth -=1
    call screen lgMedWin_scr
    
label lgMed_doneTalk:
    $quick_menu = True
    $config.skipping = None
    $renpy.block_rollback()
    stop music fadeout 1.0
    play channel00 wwAmb0 fadeout 1.0 fadein 1.0
    play channel01 wwAmb1 fadeout 1.0 fadein 1.0
    play channel02 wwAmb2 fadeout 1.0 fadein 1.0
    play channel03 wwAmb3 fadeout 1.0 fadein 1.0
    play channel04 wwAmb4 fadeout 1.0 fadein 1.0
    play channel05 wwAmb5 fadeout 1.0 fadein 1.0
    play channel06 wwAmb6 fadeout 1.0 fadein 1.0
    scene bg door2 with fade
    if(lgMed_attempts==0):
        show Ada happy at right
        a "Ah! It seems Grace is not the only capable of a simple manual override. I think I like interfacing with hardware."
    if(lgMed_attempts==1):
        show Ada neutral at right
        a "It was not perfect, but the margin of error was small enough that with the data I gathered, I shall be even more proficient the next time. Machine learning is, after all, based on some trial and error."
    if(lgMed_attempts==2):
        show Ada annoyed at right
        a "Grace made this look so easy! Her processing speeds are no where near mine, and yet she seemed to grasp the concept far quicker. I shall have to run some simulations in my downtime."
    if(lgMed_attempts==3):
        show Ada seething at right
        a "Manual overrides are inefficient. If everything were interfaced, it would be much simpler to get this silly door open. At least no was witness to my inability to manipulate hardware."
    show Ada neutral
    if(resume=="S"):
        jump resume_lgMed_S
    if(resume=="SbE"):
        jump resume_lgMed_SbE
    if(resume=="E"):
        jump resume_lgMed_E
        
label hints_lgMedA1:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGMedHints%3 
    $LGMedHints +=1
    show MA111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show MA111tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "The half-moon AND gate will only turn green if both inputs are green. That cannot happen here, so it will always output red."
    if (remainder==1):
        a "The crescent-moon with the circle is the NOR gate, which reverses the outputs of an OR gate. That means it only outputs green when both inputs are red."
    if (remainder==2):
        a "If I get stuck, I can access notes from the journal."
    hide other darken onlayer screens
    hide MA111tile07_02 
    hide MA111tile07_08
    jump gamefileMA1
    
label hints_lgMedA2:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGMedHints%3 
    $LGMedHints +=1
    show MA297tile07_02 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show MA296tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "The crescent-moon OR gate is true as long as one input is, so as long as one input is green, it will output green."
    if (remainder==1):
        a "The crescent-moon with the circle is the NOR gate, which reverses the outputs of an OR gate. That means it only outputs green with both inputs are red.."
    if (remainder==2):
        a "If I get stuck, I can access notes from the journal."
    hide other darken onlayer screens
    hide MA297tile07_02 
    hide MA296tile07_08
    jump gamefileMA2
    
label hints_lgMedA3:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGMedHints%3 
    $LGMedHints +=1
    show MA36tile07_02 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
    show MA36tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "The crescent-moon OR gate is true as long as one input is, so as long as one input is green, it will output green."
    if (remainder==1):
        a "The half-moon with the circle at the right is the NAND gate. It reverses the output of the AND gate, so it will output true, or green, unless both inputs are green."
    if (remainder==2):
        a "If I get stuck, I can access notes from the journal."
    hide other darken onlayer screens
    hide MA36tile07_02 
    hide MA36tile07_08
    jump gamefileMA3
    
label hints_lgMedB1:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGMedHints%3 
    $LGMedHints +=1
    show MB12tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
    show MB12tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show MB12tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "Since the last gate is the NAND gate, I need to ensure both the inputs going into it are true, or green, so the output will be false, or red."
    if (remainder==1):
        a "The NAND gate will output green more often than the NOR gate--the opposite of the AND and OR gate."
    if (remainder==2):
        a "I might want to try the NOR gate in the bottom middle slot. It will output red with both input green, but then I could use the NAND gate."
    hide other darken onlayer screens
    hide MB12tile02_09
    hide MB12tile07_02
    hide MB12tile07_08
    jump gamefileMB1
    
label hints_lgMedB2:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGMedHints%3 
    $LGMedHints +=1
    show lLGMB2tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
    show lLGMB2tile07_02 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
    show lLGMB2tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "The NOT gate is always an easy one. Since it is the only unary operation, or an operation that functions on one input, I just need to place it where there is only one pipe."
    if (remainder==1):
        a "The final gate is an OR gate, and since I want the output to be false, or red, I need both inputs to be false, or red."
    if (remainder==2):
        a "Since the NAND gate, or the half-moon with the circle on the right, reverses the output of the AND gate, it will output true, or green, as long as both inputs are {i}not{/i} true, or green."
    hide other darken onlayer screens
    hide lLGMB2tile02_09
    hide lLGMB2tile07_02
    hide lLGMB2tile07_08
    jump gamefileMB2
    
label hints_lgMedB3:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGMedHints%3 
    $LGMedHints +=1
    show fLGMB3tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
    show fLGMB3tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show fLGMB3tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "The NOR gate will output red, or false, as long as one input is green, or true."
    if (remainder==1):
        a "The final gate is an AND gate, and since I want the output to be false, or red, I just need one input to be false, or red."
    if (remainder==2):
        a "Since the NAND gate, or the half-moon with the circle on the right, reverses the output of the AND gate, it will output true, or green, as long as both inputs are {i}not{/i} true, or green."
    hide other darken onlayer screens
    hide fLGMB3tile02_09
    hide fLGMB3tile07_02
    hide fLGMB3tile07_08
    jump gamefileMB3
    
label hints_lgMedC1:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGMedHints%3 
    $LGMedHints +=1
    show MC111tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
    show MC111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show MC111tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "The NOR gate will output red, or false, as long as one input is green, or true."
    if (remainder==1):
        a "The final gate is an AND gate, and since I want the output to be true, or green, I need both inputs to be true, or green."
    if (remainder==2):
        a "Since the NAND gate, or the half-moon with the circle on the right, reverses the output of the AND gate, it will output true, or green, as long as both inputs are {i}not{/i} true, or green."
    hide other darken onlayer screens
    hide MC111tile02_09
    hide MC111tile07_02 
    hide MC111tile07_08
    jump gamefileMC1
    
label hints_lgMedC2:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGMedHints%3 
    $LGMedHints +=1
    show MC2111tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
    show MC2111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show MC2111tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "Both the NAND and NOR gate will output true, or green, when both inputs are false, or red, like in the bottom left slot. I should consider which one has to be used elsewhere then."
    if (remainder==1):
        a "The final gate is a NAND gate, and since I want the output to be false, or red, I need both inputs to be true, or green."
    if (remainder==2):
        a "The NOR will output green if and only if both inputs are red. NAND will output green as long as one input is false, or red."
    hide other darken onlayer screens
    hide MC2111tile02_09
    hide MC2111tile07_02
    hide MC2111tile07_08
    jump gamefileMC2
    
label hints_lgMedC3:
    show screen disable_hide
    $config.skipping=None
    $remainder = LGMedHints%3 
    $LGMedHints +=1
    show MC3111tile02_09 at Position(xpos = nand1x, xanchor = 0, ypos = nand1y, yanchor = 0)
    show MC3111tile07_02 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show MC3111tile07_08 at Position(xpos = nor1x, xanchor = 0, ypos = nor1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        a "The OR can potentially go in two places for a winning solution, since as long as one input is true, or green, the output will be green."
    if (remainder==1):
        a "The final gate is an AND gate, and since I want the output to be true, or green, I need both inputs to be true, or green. The top slot needs to produce green since the penultimate gate on the top is an AND gate as well."
    if (remainder==2):
        a "Either the NAND or the NOR gate will output green, or true, when both inputs are red, or false."
    hide other darken onlayer screens
    hide MC3111tile02_09
    hide MC3111tile07_02
    hide MC3111tile07_08
    jump gamefileMC3
    
##############################################################################
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
    
    $renpy.music.play("music/Creep_Wav.ogg", channel='channel12', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Digi_Sprites.ogg", channel='channel13', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/robotScanner.ogg", channel='channel14', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/srafTexture.ogg", channel='channel15', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/stabTapeEcho.ogg", channel='channel16', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    if(llMed_attempts ==0):
        #show Ivan dour at right
        show Grace happy at left
        g "Look Ivan! A sort algorithm saves time and sanity. Oh, wait, you don't have any sanity to begin with."
        ivan "It's a pity you have to demean others in an attempt to make yourself feel worthwile. Doesn't make a difference, however."
        show Grace annoyed
        g "You know, let's just see what it turned up."
    if(llMed_attempts ==1):
        #show Ivan dour at right
        show Grace neutral at left
        g "Okay, you really need to trim the fat on your data here. Ever heard of defragging either? I swear, if your files are stored anything like this data, your poor computer..."
        ivan "Blaming me for your inability to cleanly write a sort algorithm is very transparent, Fortran. Now, do you see what you want? Because I want you gone."
    if(llMed_attempts>1):
        show Grace annoyed at left
        #show Ivan dour at right
        g "Bubble sort, priority queues... I need a real refresher on all on this. I mean, I could have constructed an entire binary search tree in the time--"
        ivan "Fortran, no one cares about your innane babbling. Please, do get on with it. Some of use have lives we would like to return to."
    if(resume=="SbE"):
        jump finishGPuzzle1_SbE
    if(resume=="E"):
        jump finishGPuzzle1_E
    if(resume=="S"):
        jump finishGPuzzle1_S

label choose_llMed:
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
    $light5Sound = 0
    $randomNumberMedLL = renpy.random.randint(0,4)
    if randomNumberMedLL==0:
        jump loopLogic_med1
    if randomNumberMedLL==1:
        jump loopLogic_med2
    if randomNumberMedLL==2:
        jump loopLogic_med3
    if randomNumberMedLL==3:
        jump loopLogic_med4
    if randomNumberMedLL==4:
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
    $LLMedHints +=1
    if (remainder==0):
        g "I've got one node that needs power, which a WHILE will provide. It's a blue bolt, so it needs a blue WHILE."
    if (remainder==1):
        g "I've got one green IF and only one green light that takes a tile. I should probably put that there."
    if (remainder==2):
        g "The blue light by itself needs a blue tile. The blue IF looks like it would be perfect there."
    hide other darken onlayer screens
    hide LLM_1_tile64 
    hide LLM_1_tile65 
    hide LLE_1_tile66 
    hide LLE_1_tile67
    jump gamefile_llm1
    
label hints_llMed_2:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLMedHints%3 
    $LLMedHints +=1
    show LLM_2_tile64 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLM_2_tile65 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
    show LLM_2_tile66 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_2_tile67 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "Okay, I've got a green charge node, which means I need a green WHILE to power it."
    if (remainder==1):
        g "I've got one green IF and only one green light that takes a tile. I should probably put that there."
    if (remainder==2):
        g "The blue light by itself needs a blue tile. The blue IF looks like it would be perfect there."
    hide other darken onlayer screens
    hide LLM_2_tile64 
    hide LLM_2_tile65 
    hide LLE_2_tile66 
    hide LLE_2_tile67 
    jump gamefile_llm2
    
label hints_llMed_3:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLMedHints%3 
    $LLMedHints +=1
    show LLM_3_tile64 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLM_3_tile65 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
    show LLM_3_tile66 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_3_tile67 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "Okay, I've got a blue charge node, which means I need a blue WHILE."
    if (remainder==1):
        g "The WHILE will only fire when blue is being fed to it, which means I probably need the blue IF before the WHILE."
    if (remainder==2):
        g "One green IF, on green light. I think that one is pretty straightforward."
    hide other darken onlayer screens
    hide LLM_3_tile64 
    hide LLM_3_tile65 
    hide LLE_3_tile66 
    hide LLE_3_tile67 
    jump gamefile_llm3
    
label hints_llMed_4:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLMedHints%3 
    $LLMedHints +=1
    show LLM_4_tile64 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLM_4_tile65 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
    show LLM_4_tile66 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_4_tile67 at Position(xpos = while2x, xanchor = 0, ypos = while2y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "Two powered nodes and two green WHILEs. Seems self-explanatory"
    if (remainder==1):
        g "Only one blue light, and one blue IF. I should probably try the IF in that slot."
    if (remainder==2):
        g "The ELSE has to go with the one IF."
    hide other darken onlayer screens
    hide LLM_4_tile64
    hide LLM_4_tile65 
    hide LLE_4_tile66
    hide LLE_4_tile67 
    jump gamefile_llm4
    
label hints_llMed_5:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLMedHints%3 
    $LLMedHints +=1
    show LLM_5_tile74 at Position(xpos = while2x, xanchor = 0, ypos = while2y, yanchor = 0)
    show LLM_5_tile75 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
    show LLM_5_tile76 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_5_tile77 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "Okay, I've got two WHILEs. Color goes with the charge light, not the color of the pipe."
    if (remainder==1):
        g "There's only one green light, and one green IF, so the IF probably goes there. Won't be able to tell unless the charge node is lit up first, though."
    if (remainder==2):
        g "The ELSE has to go to the blue light. Now where else would make sense."
    hide other darken onlayer screens
    hide LLM_5_tile74
    hide LLM_5_tile75
    hide LLE_5_tile76
    hide LLE_5_tile77 
    jump gamefile_llm5
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
    call binaryMatchMed from _call_binaryMatchMed
    
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

####GRAMMAR PUZZLE
screen gramEasyLose_scr:
    imagebutton:
        idle "yes.png" 
        hover "yes_hover.png" 
        xpos 705
        ypos 610 
        focus_mask True
        action Jump("chooseEasyGram")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "no.png" 
        hover "no_hover.png" 
        xpos 925
        ypos 610 
        focus_mask True
        action Jump("doorPuzzle")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
            
screen gramEasyDone_scr:
    imagebutton:
        idle "finish.png" 
        hover "finish_hover.png" 
        xpos 815
        ypos 610
        focus_mask True
        action Jump("hiroseDoorPassed")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
        
label hints_llMed_1:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLMedHints%3 
    show LLM_1_tile64 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLM_1_tile65 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
    show LLM_1_tile66 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_1_tile67 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
    show other darken onlayer screens
    $LLMedHints +=1
    if (remainder==0):
        g "I've got one node that needs power, which a WHILE will provide. It's a blue bolt, so it needs a blue WHILE."
    if (remainder==1):
        g "I've got one green IF and only one green light that takes a tile. I should probably put that there."
    if (remainder==2):
        g "The blue light by itself needs a blue tile. The blue IF looks like it would be perfect there."
    hide other darken onlayer screens
    hide LLM_1_tile64 
    hide LLM_1_tile65 
    hide LLE_1_tile66 
    hide LLE_1_tile67
    jump gamefile_llm1
    
label hints_llMed_2:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLMedHints%3 
    $LLMedHints +=1
    show LLM_2_tile64 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLM_2_tile65 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
    show LLM_2_tile66 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_2_tile67 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "Okay, I've got a green charge node, which means I need a green WHILE to power it."
    if (remainder==1):
        g "I've got one green IF and only one green light that takes a tile. I should probably put that there."
    if (remainder==2):
        g "The blue light by itself needs a blue tile. The blue IF looks like it would be perfect there."
    hide other darken onlayer screens
    hide LLM_2_tile64 
    hide LLM_2_tile65 
    hide LLE_2_tile66 
    hide LLE_2_tile67 
    jump gamefile_llm2
    
label hints_llMed_3:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLMedHints%3 
    $LLMedHints +=1
    show LLM_3_tile64 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLM_3_tile65 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
    show LLM_3_tile66 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_3_tile67 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "Okay, I've got a blue charge node, which means I need a blue WHILE."
    if (remainder==1):
        g "The WHILE will only fire when blue is being fed to it, which means I probably need the blue IF before the WHILE."
    if (remainder==2):
        g "One green IF, on green light. I think that one is pretty straightforward."
    hide other darken onlayer screens
    hide LLM_3_tile64 
    hide LLM_3_tile65 
    hide LLE_3_tile66 
    hide LLE_3_tile67 
    jump gamefile_llm3
    
label hints_llMed_4:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLMedHints%3 
    $LLMedHints +=1
    show LLM_4_tile64 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLM_4_tile65 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
    show LLM_4_tile66 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_4_tile67 at Position(xpos = while2x, xanchor = 0, ypos = while2y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "Two powered nodes and two green WHILEs. Seems self-explanatory"
    if (remainder==1):
        g "Only one blue light, and one blue IF. I should probably try the IF in that slot."
    if (remainder==2):
        g "The ELSE has to go with the one IF."
    hide other darken onlayer screens
    hide LLM_4_tile64
    hide LLM_4_tile65 
    hide LLE_4_tile66
    hide LLE_4_tile67 
    jump gamefile_llm4
    
label hints_llMed_5:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLMedHints%3 
    $LLMedHints +=1
    show LLM_5_tile74 at Position(xpos = while2x, xanchor = 0, ypos = while2y, yanchor = 0)
    show LLM_5_tile75 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
    show LLM_5_tile76 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_5_tile77 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
    show other darken onlayer screens
    if (remainder==0):
        g "Okay, I've got two WHILEs. Color goes with the charge light, not the color of the pipe."
    if (remainder==1):
        g "There's only one green light, and one green IF, so the IF probably goes there. Won't be able to tell unless the charge node is lit up first, though."
    if (remainder==2):
        g "The ELSE has to go to the blue light. Now where else would make sense."
    hide other darken onlayer screens
    hide LLM_5_tile74
    hide LLM_5_tile75
    hide LLE_5_tile76
    hide LLE_5_tile77 
    jump gamefile_llm