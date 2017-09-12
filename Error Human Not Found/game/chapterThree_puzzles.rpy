
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
#    play channel00 wwAmb0 fadeout 1.0 fadein 1.0
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
#    play channel00 wwAmb0 fadeout 1.0 fadein 1.0
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
