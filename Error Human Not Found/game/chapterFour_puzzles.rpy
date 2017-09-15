label llHard_done:
    ##INSERT GRACE'S PUZZLE
    ##syddoyourcomscithing
    #if (attempts == 1)
    #g "Wow, that was {i}surprisingly{/i} easy."
    #if (attempts >1) and (attempts<4)
    #g "Okay, Watson, you little trickster. You almost got me, but I succeeded!"
    #if (attempts>3)
    #g "Hmmm. This is trickier than I thought. What was Watson thinking?"
    ##show Ada neutral
    #show other darken
    #show image "objects/jumpdrive_closeup.png" at centerScreen
    #"{i}Description of the encryption key here."
    #hide other darken
    #hide image "objects/jumpdrive_closeup.png" at centerScreen
    #show Grace happy at left
    #show Ada neutral at right
    #a "This is the decryption key for all the data drives we have found. All four are rather large and complex in their encryption, so even with the key this will take some time." 
    #a "Unfortunately, my neural network is not quite as capable as a quantum computer."
    #g "As long as it decodes soon, I'm okay with that."
    #a "Assuming there are no surprises, it will be soon."
    #g "Great. In the meantime, I'm going to get ahold of my friend Alan. I need a break from today."
    #a "Go on, take your break."
    "Grace cracks the safe here."
    jump watsonRight
    
label lgHard_done:
    "Ada cannot find Watson here (Watson's computer)."
    jump watsonRight
    
label gramHard_done:
    "Post Blue puzzle here."
    jump blueActions #NO IDEA IF THIS IS RIGHT. CHECK. IT'S BLUE'S SOMETHING. 


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
        action Jump("watsonActions")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
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
        

#TUTORIAL FOR HARD ARE NOT DONE. SCREENS ARE PLACEHOLDERS ONLY.        
screen tutorial_scrBinary4Bit_1:
    imagebutton:
        idle "next.png" 
        hover "next_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("tutorial_Binary4Bit_2")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        
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
        idle "next.png" 
        hover "next_hover.png" 
        xpos 1650
        ypos 940 
        focus_mask True
        action Jump("tutorial_Binary4Bit_3")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
screen tutorial_scrBinary4Bit_5:
    imagebutton:
        idle "back.png" 
        hover "back_hover.png" 
        xpos 0
        ypos 940 
        focus_mask True
        action Jump("tutorial_Binary4Bit_4")
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

label binaryHard:
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    stop channel06 fadeout 1.0
    stop channel07 fadeout 1.0
    #Add more stops here if needed when the BGM is added
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
#    if (binaryHard_attempts==0): Uncomment when have tutorial
#        jump tutorial_Binary4Bit_1
    $binaryHardHints = 0
    call binaryMatchHard from _call_binaryMatchHard
    
label tutorial_Binary4Bit_1:
    $renpy.block_rollback()
    $config.skipping=None
    window hide
    $ quick_menu = False
    scene bg tutorial_binary4Bit_1
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary4Bit_1
    
label tutorial_Binary4Bit_2:
    window hide
    $ quick_menu = False
    scene bg tutorial_binary4Bit_2
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary4Bit_2
    
label tutorial_Binary4Bit_5:
    window hide
    $ quick_menu = False
    scene bg tutorial_binary4Bit_5
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary4Bit_5
        
label binaryHardHints:
    show screen disable_hide
    $config.skipping=None
    $remainder = binaryHardHints%3 
    show other darken onlayer screens
    if (remainder==0):
        $binaryHardHints +=1
        g "Four bits is a little more challenging. The left-most bit is worth 8, the next one 4, the next 2, and then 1."
        hide other darken onlayer screens
        window hide
        jump turns_loopHard
    if (remainder==1):
        $binaryHardHints +=1
        g "The highest bit is 1111, which is fifteen. 1000 is just 8, then we had 0100 which is 4, and 0010, which is 2, and 0001, which is just one."
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
    image discStartup= "binaryEasyWin.png" #CHANGE ME
    show discStartup at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen binaryHardWin_scr
    
label binaryHardLose:
    hide screen binaryMatch_hard
    show other darken
    $ binaryHard_attempts +=1
    image bootFail ="loopLogicEasyLose.png" #CHANGE ME
    show bootFail at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen binaryHardLose_scr
    
label binaryHardDoneTalk:
    scene bg wsMain with fade
    $quick_menu = True
    stop music fadeout 1.0
    $renpy.music.play("music/Amb/WS/EHNF_WS_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L4.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L5.ogg", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L6.ogg", channel='channel06', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/WS/EHNF_WS_L7.ogg", channel='channel07', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    if(binaryHard_attempts==0):
        show Grace neutral at left
        show Ada amused at right
        a "With the correct encryption key, this was easy enough to crack. Now we just have to wait for the rest to finish decrypting."
    if (binaryHard_attempts>=1) and (binaryHard_attempts<3):
        show Ada seething at right
        show Grace neutral at left
        a "Trust Watson to have additional security measures in place. The encryption key certainly helped, but I still had to bypass several other surprises he left behind."
    if (binaryHard_attempts>=3):
        show Ada annoyed at right
        show Grace snarky at left
        g "You know Ada, an encryption key is supposed to make decryption pretty simple. Add that you're basically a walking computer, and I would have thought--"
        a "If you are going to be that way, next time you can try to crack it."
        show Grace surprised
        g "Oh, no, please. I wouldn't want to take that from you."
    $quick_menu=False
    window hide
    hide Grace
    hide Ada
    jump watsonActions