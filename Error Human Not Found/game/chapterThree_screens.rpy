label chapterThree_screens:
# screen llMedLose_scr:
#     imagebutton:
#            idle "yes.png" 
#            hover "yes_hover.png" 
#            xpos 705
#            ypos 610 
#            focus_mask True
#            action Jump("loopLogicEasyChoose") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"
#        imagebutton:
#            idle "no.png" 
#            hover "no_hover.png" 
#            xpos 925
#            ypos 610 
#            focus_mask True
#            action Jump("balcony_alpha") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"
#    screen llMedWin_scr:
#        imagebutton:
#            idle "finish.png" 
#            hover "finish_hover.png" 
#            xpos 815
#            ypos 610
#            focus_mask True
#            action Jump("llDoneTalk") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"  

#    screen lgMedWin_scr:
#        imagebutton:
#            idle "yes.png" 
#            hover "yes_hover.png" 
#            xpos 705
#            ypos 610 
#            focus_mask True
#            action Jump("pickNextPuzzleLGEasy") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"
#        imagebutton:
#            idle "no.png" 
#            hover "no_hover.png" 
#            xpos 925
#            ypos 610
#            focus_mask True
#            action Jump("exploreHiroseOffice") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"

#    screen lgMedLose_scr:
#        imagebutton:
#            idle "yes.png" 
#            hover "yes_hover.png" 
#            xpos 705
#            ypos 610 
#            focus_mask True
#            action Jump("pickNextPuzzleLGEasy") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"
#        imagebutton:
#            idle "no.png" 
#            hover "no_hover.png" 
#            xpos 925
#            ypos 610 
#            focus_mask True
#            action Jump("exploreHiroseOffice") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"

#    screen lgMedDone_scr:
#        imagebutton:
#            idle "finish.png" 
#            hover "finish_hover.png" 
#            xpos 815
#            ypos 610
#            focus_mask True
#            action Jump("lgEasyDone_talk") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"

#    screen gramMedLose_scr:
#        imagebutton:
#            idle "yes.png" 
#            hover "yes_hover.png" 
#            xpos 705
#            ypos 610 
#            focus_mask True
#            action Jump("chooseEasyGram") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"
#        imagebutton:
#            idle "no.png" 
#            hover "no_hover.png" 
#            xpos 925
#            ypos 610 
#            focus_mask True
#            action Jump("doorPuzzle") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"

#    screen gramMedDone_scr:
#        imagebutton:
#            idle "finish.png" 
#            hover "finish_hover.png" 
#            xpos 815
#            ypos 610
#            focus_mask True
#            action Jump("hiroseDoorPassed") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"

#    screen binaryMedLose_scr:
#        imagebutton:
#            idle "yes.png" 
#            hover "yes_hover.png" 
#            xpos 705
#            ypos 610 
#            focus_mask True
#            action Jump("binaryEasy") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"
#        imagebutton:
#            idle "no.png" 
#            hover "no_hover.png" 
#            xpos 925
#            ypos 610 
#            focus_mask True
#            action Jump("balcony_alpha") #CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg"

#    screen binaryMedWin_scr:
#        imagebutton:
#            idle "finish.png" 
#            hover "finish_hover.png" 
#            xpos 815
#            ypos 610
#            focus_mask True
#            action Jump("binaryDoneTalk")#CHANGE
#            hover_sound "audio/ENHF_UI_Button_v2.ogg"
#            activate_sound "audio/ENHF_UI_Button_v1.ogg" 

###INSERT TUTORIAL SCREENS HERE!!!!

#OBJECT SCREENS
    screen nightShift_scr:
        if(llMed_solved==False):
            imagebutton:
                idle "objects/nightShift_idle.png"
                hover "objects/nightShift_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("investigateNightShift")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
    screen lab2_inv_scr:
        imagebutton:
            idle "ivanTalk.png"
            hover "ivanTalk_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("talkIvan")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("investigateIvan")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen lab2Table_scr:
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[lab2Items_table]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "1" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        imagebutton:
            idle "objects/wire_idle.png"
            hover "objects/wire_hover.png"
            xpos 0
            ypos 0 
            focus_mask True
            action Jump("lab2Table_resume")
            hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
            activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
            
    screen ivanComp_scr:
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("lab2_inv")
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
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[lab2Items]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "2" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if(catPhoto_inv==False):
            imagebutton:
                idle "objects/catPhoto_idle.png"
                hover "objects/catPhoto_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("investigateCatPhoto")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(ivanNotes_inv==False):
            imagebutton:
                idle "objects/ivanNotes_idle.png"
                hover "objects/ivanNotes_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("investigateIvanNotes")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        
#label investigateCord:
#    $burntCord_inv = True
#    $lab2Items +=1
#    show other darken
#    show "objects/cord_closeup.png" at centerscreen
#    "{i}A small section of burnt-out cord. It looks similar to the cords used in the body of the androids for Alpha and Ada.{/i}"
#    hide other darken
#    hide "objects/cord_closeup.png"
#    show Grace surprised at left
#    #show Ivan dour at right
#    g "Aha!"
#    g "What do we have here?"
#    #show Ivan dour
#    ivan "A defective power cord. Do I really have to remind you what that is?"
#    show Grace snarky
#    g "But why was it tucked away behind a desk like this?"
#    #show Ivan defensive
#    ivan "It must have fallen out of the disposal bin. MOPRs are efficient, but they're clumsy sometimes."
#    jump ???

label lab2_inv:
    $quick_menu = False
    if(ivanComp_lock==True):
        scene bg lab2Ivan_locked with fade
    else:
        scene bg lab2Ivan_unlocked with fade
    call screen lab2_inv_scr
    
label investigateIvan:
    $quick_menu = False
    if(ivanComp_lock==True):
        scene bg lab2Ivan_locked with fade
    else:
        scene bg lab2Ivan_unlocked with fade
    call screen ivanComp_scr
    
label investigateIvanNotes:
    $ivanNotes_inv = True
    $lab2Items +=1
    show other darken
    show image "objects/ivanNotes_closeup.png" at centerScreen
    $quick_menu = True
    "{i}A stack of tablets with Ivan's research notes about the Markov Project. There is a stark contrast between the neatly stacked tablets which Ivan keeps his notes on and the sprawl of post-it notes and papers on Grace's desk."
    hide other darken
    hide image "objects/ivanNotes_closeup.png"
    show Grace snarky at left
    #show Ivan dour at right
    g "Well, what do we have--"
    "{i}Ivan snatches his notes away."
    #show Ivan defensive
    ivan "And just what are you doing?"
    show Grace annoyed
    g "I wanted to look at your notes. You know, compare them to mine and all that."
    ivan "And what, you think you can just peer into somone else's notes like that?"
    g "Ivan, we're working on the {i}same project{/i}. There's literally no reason for you to act like this."
    #show Ivan dour
    ivan "Here's a reason: I don't want you looking at my notes."
    $quick_menu = False
    jump investigateIvan
    
label investigateCatPhoto:
    $catPhoto_inv = True
    $lab2Items +=1
    show other darken
    show image "objects/catPhoto_closeup.png" at centerScreen
    $quick_menu = True
    "{i}A framed picture of Ivan's overweight black cat, Mr. Frillywhiskers.  A large, yellow bowtie lies around his neck, and his expression shows that he is not amused."
    hide other darken
    hide image "objects/catPhoto_closeup.png"
    show Grace happy at left
    #show Ivan dour at right
    g "Your cat's adorable, Ivan. Too bad it has to live with {i}you{/i}"
    #show Ivan disgusted
    ivan "I'll have you know that Mr. Frillywiskers and I were fated to be together."
    ivan "I absolutely disdain anything that isn't him, and he reciprocates the feeling."
    show Grace snarky
    g "Just marry your cat while you're at it, Ivan. Who needs people?"
    ivan "For once, we're in agreement on something."
#    hide Ivan
    hide Grace
    window hide
    $quick_menu = False
    jump investigateIvan
    
label talkIvan:
    $quick_menu=True
    if(talkIvan_count==0):
        if(resume=="S"):
            jump talkIvanLab2_S
        if(resume=="E"):
            jump talkIvanLab2_E
        if(resume=="SbE"):
            jump talkIvanLab2_SbE
    if(lab2Items==2 and talkIvan_count>0):
        if(resume="S"):
            jump finishLab2Inv_S
        if(resume="E"):
            jump finishLab2Inv_E
        if(resume="SbE"):
            jump finishLab2Inv_SbE
        #PLAY SFX here
            
    if(talkIvan_count==1):
        $talkIvan_count +=1
        show Grace neutral at left
        #show Ivan dour at center
        g "Hey, Ivan, about what we talked about..."
        #show Ivan dour
        ivan "Not again, Fortran. There's only so much of you I can take."
        g "I was just going to say--"
        ivan "What part of 'there's only so much of you I can take' do you not understand?"
        Ivan "Stop harassing me."
        show Grace annoyed
        g "Fine. So grumpy..."
        $quick_menu = False
        jump lab2_inv
        
    if(talkIvan_count==2):
        $talkIvan_count +=1
        show Grace neutral at left
        #show Ivan dour at center
        g "Ivan, there was another thing I wanted to talk about."
        #show Ivan disgusted
        ivan "Enough, Fortran! You are wasting my time."
        ivan "Every passing second is insufferable with you here."
        ivan "Why don't you spend less time making me miserable and more time completing your little fool's errand so you can leave me in peace?"
        show Grace snarky
        g "..."
        g "So you {i}don't{/i} want to talk?"
        #show Ivan dour
        ivan "{i}No{/i}."
        $quick_menu=False
        jump lab2_inv

    if(talkIvan_count>2):
        $talkIvan_count +=1
        show Grace snarky at left
        #show Ivan dour at center
        g "Hey, Ivan?"
        #show Ivan dour
        ivan "..."
        g "You're not gonna talk?"
        ivan "..."
        show Grace neutral
        g "I think he's ignoring me."
        $quick_menu = False
        jump lab2_inv
    
label nightShift_comp:
    $quick_menu = False
    hide Grace
    #hide Ivan
    if(gramMed_solved==False):
        show bg lab2WS_locked with fade
        call screen nightShift_scr
    else:
        show bg lab2WS_unlocked with fade
        "Temporary placeholder for end of Puzzle 2."
        if (resume=="E"):
            jump endCh3_E
        if (resume=="SbE"):
            jump endCh3_SbE
        if(resume=="S"):
            jump endCh3_S
            
label lab2Table:
    hide Grace
    #hide Ivan
    $quick_menu = False
    window hide
    call screen lab2Table_scr
    
label lab2Table_resume:
    if(resume = "S"):
        jump postCord_S
    if(resume="E"):
        jump postCord_E
    if(resume="SbE"):
        jump postCord_SbE
    
label investigateNightShift:
    if(llMed_attempts==0):
        show other darken
        show image "objects/nightShift_closeup.png" at centerScreen
        "{i}The main computer used by the night crew. Ivan has a habit of leaving aggressive notes on here when disatisfied with the state that the lab is left in."
        hide other darken
        hide image "objects/nightShift_closeup.png"
        #dialogue displayed before the puzzle starts
        show Grace neutral at left
        g "This one's Ellen's, right?"
        #show Ivan dour at right
        ivan "Of course, Doctor Fortran. Do you have any other obvious questions."
        show Grace annoyed
        g "Right. Because asking something about a lab I don't work in is an obvious question." 
        $llMed_solved = True #REMOVE THIS, PUT IN PUZZLE
        show bg lab2WS_unlocked with fade
        "Temporary placeholder for end of Puzzle 2."
        if (resume=="E"):
            jump endCh3_E
        if (resume=="SbE"):
            jump endCh3_SbE
        if(resume=="S"):
            jump endCh3_S
        #jump nightShift_comp
#        jump tutorial_gramMed1
    else:
        jump choose_gramMed