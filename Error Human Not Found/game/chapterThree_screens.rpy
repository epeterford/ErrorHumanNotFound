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
#    screen nightShift_scr:
#        if(llMed_solved==False):
#            imagebutton:
#                idle
#                hover
#                xpos 0
#                ypos 0
#                focus_mask True
#                action Jump("")
#                hover_sound "audio/ENHF_UI_Button_v2.ogg"
#                activate_sound "audio/ENHF_UI_Button_v1.ogg"            

    screen ivanComp_scr:
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
    
label talkIvan:
    if(talkIvan_count==0):
        if(resume="S"):
            jump 
        if(resume="E"):
            jump
        if(resume="SbE"):
            jump
    if(talkIvan_count>0) and (talkIvan_count<3):
        if(resume="S"):
            jump 
        if(resume="E"):
            jump
        if(resume="SbE"):
            jump
    else:
        if(resume="S"):
            jump 
        if(resume="E"):
            jump
        if(resume="SbE"):
            jump
            
label investigateNightShift:
    if(llMed_attempts==0):
        show other darken
        show "objects/nightShift_closeup.png" at centerscreen
        "{i}The main computer used by the night crew. Ivan has a habit of leaving aggressive notes on here when disatisfied with the state that the lab is left in."
        hide other darken
        hide "objects/nightShift_closeup.png"
        #dialogue displayed before the puzzle starts
        show Grace neutral at left
        g "This one's Ellen's, right?"
        #show Ivan dour at right
        ivan "Of course, Doctor Fortran. Do you have any other obvious questions."
        show Grace annoyed
        g "Right. Because asking something about a lab I don't work in is an obvious question." 
    else