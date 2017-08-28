label chapterTwo_screens:
    $ gracePoster_look = False
    screen llEasyLose_scr:
        imagebutton:
            idle "yes.png" 
            hover "yes_hover.png" 
            xpos 705
            ypos 610 
            focus_mask True
            action Jump("loopLogicEasyChoose")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "no.png" 
            hover "no_hover.png" 
            xpos 925
            ypos 610 
            focus_mask True
            action Jump("balcony_alpha")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen llEasyWin_scr:
        imagebutton:
            idle "finish.png" 
            hover "finish_hover.png" 
            xpos 815
            ypos 610
            focus_mask True
            action Jump("llDoneTalk")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"  
            
    screen binaryEasyLose_scr:
        imagebutton:
            idle "yes.png" 
            hover "yes_hover.png" 
            xpos 705
            ypos 610 
            focus_mask True
            action Jump("binaryEasy")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "no.png" 
            hover "no_hover.png" 
            xpos 925
            ypos 610 
            focus_mask True
            action Jump("balcony_alpha")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen binaryEasyWin_scr:
        imagebutton:
            idle "finish.png" 
            hover "finish_hover.png" 
            xpos 815
            ypos 610
            focus_mask True
            action Jump("binaryDoneTalk")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
      
    screen tutorial_scrLL_1:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_LL_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
              
    screen tutorial_scrLL_2:
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_LLEasy")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_LL_3")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
    
    screen tutorial_scrLL_3:
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_LL_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "finish.png" 
            hover "finish_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("loopLogicEasyChoose")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen tutorial_scrBinary2Bit_1:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_Binary2Bit_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrBinary2Bit_2:
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_Binary2Bit_1")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_Binary2Bit_3")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
    
    screen tutorial_scrBinary2Bit_3:
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_Binary2Bit_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_Binary2Bit_4")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrBinary2Bit_4:
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_Binary2Bit_3")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_Binary2Bit_5")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrBinary2Bit_5:
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_Binary2Bit_4")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "finish.png" 
            hover "finish_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("binaryEasy")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen graceLab_actionsScr:
        imagebutton:
            idle "adaTalk.png" 
            hover "adaTalk_hover.png" 
            xpos 0
            ypos 0 
            focus_mask True
            action Jump("talkAdaGraceLab")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("graceLab_inv")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen graceLab_invScr:
        imagebutton:
            idle "arrowL.png"
            hover "arrowL_hover.png"
            xpos 450
            ypos 170
            focus_mask True
            action Jump("graceLab_left1")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrowR.png"
            hover "arrowR_hover.png"
            xpos 1190
            ypos 480
            focus_mask True
            action Jump("graceLab_right")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            if (graceLeft1Desk_value == 3 and graceLeft2Desk_value == 3 and graceRightDesk_value==3 and talkAdaGraceLab_times==0):
                action Jump("talkAdaGraceLab")
            else:
                action Jump("graceLab_actions")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen graceLab_left1Scr:
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[graceLeft1Desk_value]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "3" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if(gracePoster_look == False):
            imagebutton:
                idle "objects/gracePoster.png"
                hover "objects/gracePoster_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("gracePoster_inv")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(graceNeuralNetwork_look == False):
            imagebutton:
                idle "objects/graceNeuralNetwork.png"
                hover "objects/graceNeuralNetwork_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceNeuralNetwork_inv")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(graceHardDrive_look == False):
            imagebutton:
                idle "objects/graceHarddrive.png"
                hover "objects/graceHarddrive_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceHardDrive_inv")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        imagebutton:
            idle "arrowD.png"
            hover "arrowD_hover.png"
            xpos 1190
            ypos 890
            focus_mask True
            action Jump("graceLab_inv")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrowL.png"
            hover "arrowL_hover.png"
            xpos 0
            ypos 710
            focus_mask True
            action Jump("graceLab_left2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen graceLab_left2Scr:
        imagebutton:
            idle "arrowR.png"
            hover "arrowR_hover.png"
            xpos 1730
            ypos 210
            focus_mask True
            action Jump("graceLab_left1")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        if(graceCandD_look == False):
            imagebutton:
                idle "objects/graceC&D.png"
                hover "objects/graceC&D_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceCandD_inv")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(graceBust_look == False):
            imagebutton:
                idle "objects/graceBust.png"
                hover "objects/graceBust_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceBust_inv")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(graceCoffee_look == False):
            imagebutton:
                idle "objects/graceCoffee.png"
                hover "objects/graceCoffee_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceCoffee_inv")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[graceLeft2Desk_value]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "3" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
            
    screen graceLab_right:
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[graceRightDesk_value]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "3" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if(gracePhoto_look == False):
            imagebutton:
                idle "objects/gracePhoto.png"
                hover "objects/gracePhoto_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("gracePhoto_inv")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(gracePens_look == False):
            imagebutton:
                idle "objects/gracePens.png"
                hover "objects/gracePens_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("gracePens_inv")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if(graceStickynotes_look == False):
            imagebutton:
                idle "objects/graceStickyNotes.png"
                hover "objects/graceStickyNotes_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceStickyNotes_inv")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        imagebutton:
            idle "arrowD.png"
            hover "arrowD_hover.png"
            xpos 865
            ypos 890
            focus_mask True
            action Jump("graceLab_inv")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen balcony_actionsScr:
        imagebutton:
            idle "callLynn.png" #Comment SWAP THIS WITH WRISTBAND
            hover "callLynn_hover.png" #SWAP THIS WITH WRISTBAND/CELL
            xpos 0
            ypos 0 
            focus_mask True
            action Jump("talkLynn")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("balcony_inv")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen balcony_invScr:
        if(balconyView_look==False):
            imagebutton:
                idle "objects/balconyWindow_idle.png" 
                hover "objects/balconyWindow_hover.png" 
                xpos 0
                ypos 0
                focus_mask True
                action Jump("balconyView_label")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        imagebutton:
            idle "arrowD.png"
            hover "arrowD_hover.png"
            xpos 860
            ypos 200
            focus_mask True
            action Jump("balcony_alpha")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("balcony_actions")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[balconyItems]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "1" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
                
    screen balcony_alphaScr:
        if(alphaBody_look==False):
            imagebutton: 
                idle "objects/alpha.png"
                hover "objects/alpha_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("alphaBody_inv")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if (balconyJumpdrive_look==False):
            imagebutton: 
                idle "objects/jumpdrive1_idle.png"
                hover "objects/jumpdrive1_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("jumpdrive1_label")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if (balconyScratches_look==False):
            imagebutton: 
                idle "objects/scratches_idle.png"
                hover "objects/scratches_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("scratches_label")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        #Add explorable objects here
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 70
        text "Items" xpos 1650 ypos 85 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 68 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[alphaBodyItems]" xpos 1800 ypos 85 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 85 color "#0060db" font "Bitter-Bold.otf"
        text "3" xpos 1850 ypos 85 color "#0060db" font "United Kingdom DEMO.otf"
        imagebutton:
            idle "arrow.png"
            hover "arrow_hover.png"
            xpos 400
            ypos 0
            focus_mask True
            action Jump("balcony_inv")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
label graceLab_actions:
    scene bg G_deskArea
    #CHANGE the second desk when get last two items
    if talkAdaGraceLab_times>0 and graceLeft1Desk_value == 3 and graceLeft2Desk_value == 3 and graceRightDesk_value==3:
        if(resume =="E"):
            jump resumeChapterTwo_E
        if(resume == "SbE"):
            jump resumeChapterTwo_SbE
        if(resume == "S"):
            jump resumeChapterTwo_S
    $ quick_menu = False
    window hide
    $renpy.block_rollback()
    $config.skipping=None
    call screen graceLab_actionsScr
    
label talkAdaGraceLab:
    scene bg G_deskArea
    $ quick_menu = True
    if (talkAdaGraceLab_times ==0):
        $ talkAdaGraceLab_times +=1
        if(resume =="E"):
            jump talkAdaLab_E
        if(resume == "SbE"):
            jump talkAdaLab_SbE
        if(resume == "S"):
            jump talkAdaLab_S
    if (talkAdaGraceLab_times ==1):
        $ talkAdaGraceLab_times +=1
        if(resume =="E"):
            jump adaLabLoop1_E
        if(resume == "SbE"):
            jump adaLabLoop1_SbE
        if(resume == "S"):
            jump adaLabLoop1_S
    if (talkAdaGraceLab_times >1) and (talkAdaGraceLab_times <4):
        $ talkAdaGraceLab_times +=1
        if(resume =="E"):
            jump adaLabLoop2_E
        if(resume == "SbE"):
            jump adaLabLoop2_SbE
        if(resume == "S"):
            jump adaLabLoop2_S
    if (talkAdaGraceLab_times >3):
        $ talkAdaGraceLab_times +=1
        if(resume =="E"):
            jump adaLabLoop3_E
        if(resume == "SbE"):
            jump adaLabLoop3_SbE
        if(resume == "S"):
            jump adaLabLoop3_S
    
label graceLab_inv:
    scene bg G_deskArea with fade
    $ quick_menu = False
    window hide
    $renpy.block_rollback()
    $config.skipping=None
    call screen graceLab_invScr
    
label graceLab_left1:
    scene bg G_left1 with fade
    $ quick_menu = False
    window hide
    $renpy.block_rollback()
    $config.skipping=None
    call screen graceLab_left1Scr
    
label graceLab_left2:
    scene bg G_left2 with fade
    $ quick_menu = False
    window hide    
    $renpy.block_rollback()
    $config.skipping=None
    call screen graceLab_left2Scr
    
label graceLab_right:
    scene bg G_right with fade
    $ quick_menu = False
    window hide
    $renpy.block_rollback()
    $config.skipping=None
    call screen graceLab_right
    
label balcony_actions:
    scene bg balconyClose
    $ quick_menu = False
    window hide
    $renpy.block_rollback()
    $config.skipping=None
    call screen balcony_actionsScr
    
label gracePoster_inv:
    $ quick_menu = True
    $ gracePoster_look = True
    $ graceLeft1Desk_value +=1
    show other darken
    show image "objects/gracePoster_closeup.png" at centerScreen
    window show
    "{i}An official Noah Sphere poster designed for employee motivation. The image is based on the old Earth  'Rosie the Riveter'  cultural icon."
    hide image "objects/gracePoster_closeup.png"
    hide other darken
    show Grace neutral at left
    g "This poster is so cheesy."
    show Ada neutral at right
    a "I detect no traces of curd."
    show Grace annoyed
    g "No, Ada, what I meant was that I don't like how, er... to the point this poster is."
    a "Is that not the point? To clearly indicate the purpose of the poster while imparting the significance upon the viewer?"
    show Grace snarky
    g "I want to keep defending my point, but that was solid."
    show Ada amused
    a "Solid logic is just another day on the job for me."
    hide Ada
    hide Grace
    $ quick_menu = False
    window hide
    jump graceLab_left1

label graceNeuralNetwork_inv:
    $ quick_menu = True
    $ graceNeuralNetwork_look = True
    $ graceLeft1Desk_value +=1
    show other darken
    show image "objects/graceNeuralNetwork_closeup1.png" at centerScreen
    "{i}This diagram shows some of the connections in the human brain, mapped organically."
    hide image "objects/graceNeuralNetwork_closeup1.png"
    show image "objects/graceNeuralNetwork_closeup2.png" at centerScreen
    "{i}This diagram represents a map of the human brain in terms of visible inputs that undergo processing--the hidden portion--and the visible outputs from those inputs."
    hide image "objects/graceNeuralNetwork_closeup2.png"
    show image "objects/graceNeuralNetwork_closeup3.png" at centerScreen
    "{i}This diagram shows the neurons in the human brain, the inspiration for the neural networks Grace programmed."
    hide image "objects/graceNeuralNetwork_closeup3.png"
    show image "objects/graceNeuralNetwork_closeup4.png" at centerScreen
    "{i}Some lines of Grace's code, written in an integrated development environment."
    hide image "objects/graceNeuralNetwork_closeup4.png"
    hide other darken
    show Ada neutral at right
    a "So, this is what is inside my head."
    show Grace snarky at left
    g "It's mounted in your chest, actually."
    show Ada concerned
    a "What?"
    show Grace neutral
    g "Yeah. You have a lot of processors in your head, but your actual core's in your chest. It's safer that way. Plus, the scale isn't exactly one-to-one with the human brain."
    show Ada neutral
    a "Ah, I see. I suppose you might say I think with my heart then?"
    show Grace happy
    g "Not a bad try, but you still need work on that humor."
    $ quick_menu = False
    window hide
    jump graceLab_left1
    
label graceHardDrive_inv:
    $ quick_menu = True
    $ graceHardDrive_look = True
    $ graceLeft1Desk_value +=1
    show other darken
    show image "objects/graceHarddrive_closeup.png" at centerScreen
    "{i}A semi-haphazardly stacked collection of external hard drives."
    hide other darken
    hide image "objects/graceHarddrive_closeup.png"
    show Ada concerned at right
    a "Grace!"
    show Grace surprised at left
    g "What, Ada?! What's wrong?"
    a "Your hard drives, Grace! You cannot keep them like this."
    "{i}Ada starts to pick up Grace's various hard drives."
    show Grace annoyed
    g "Hey! Stop that!"
    "{i}Grace stops Ada."
    g "What are you doing?"
    show Ada neutral
    a "These hard drives are just out here, instead of being in storage. These are very sub-optimal conditions."
    show Grace neutral
    g "And {i}what{/i} exacty is sub-optimal about keeping them where their information is needed?"
    show Ada frustrated
    a "What if something happens to them?"
    show Grace snarky
    g "Ada, the little baby hard drives will be fine. I'm still storing all my notes from the Markov Project, so they need to be like that just a little bit longer." 
    $ quick_menu = False
    window hide
    jump graceLab_left1

label graceBust_inv:
    $ quick_menu = True
    $ graceBust_look = True
    $ graceLeft2Desk_value +=1
    show other darken
    show image "objects/graceBust_closeup.png" at centerScreen
    "{i}This prototype for an AI chassis' head is missing its outer plating, giving it a skull-like appearance. Alan Asimov went through several designs for the AI androids before settling on the ones used for Alpha and Ada."
    hide other darken
    hide image "objects/graceBust_closeup.png"
    show Grace snarky at left
    g "I remember when we finished this prototype. Alan couldn't stop talking about this old film movie."
    show Ada neutral at right
    a "A film?"
    show Grace neutral
    g "Yeah. Back before the second milennium, people used to record movies on physical film."
    a "May I enquire what this 'film' was called?"
    g "I don't remember. I'd have to ask Alan. I think it was {i}Exterminator{/i} or something like that. He told me it was about an AI, of all things."
    show Ada concerned
    a "A rogue AI?"
    g "I guess it was just science fiction back then, but nowadays, something like that would mean something completely different."
    $quick_menu = False
    jump graceLab_left2
    
label graceCoffee_inv:
    $ quick_menu = True
    $ graceCoffee_look = True
    $ graceLeft2Desk_value +=1
    show other darken
    show image "objects/graceCoffee_closeup.png" at centerScreen
    "{i}A red mug with a cartoon robot on the side, the mascot of the popular brand, Starbots Coffee. On Earth, cafés for Starbots can be found in countires all over."
    hide other darken
    hide image "objects/graceCoffee_closeup.png"
    show Grace snarky at left
    g "What's your take on this, Ada?"
    show Ada neutral at right
    a "Hmm..."
    a "The appearance of the robot is compatible with what humans find comfortable; however, the design itself is hardly optimal."
    show Grace neutral
    g "How so?"
    show Ada concerned
    a "This robot does not possess peripheral sensors, and it doesn't have any fingers. "
    g "Noted."
    $quick_menu=False
    hide Ada
    hide Grace
    window hide
    jump graceLab_left2
    
label graceCandD_inv:
    $ quick_menu = True
    $ graceCandD_look = True
    $ graceLeft2Desk_value +=1
    show other darken
    show image "objects/graceC&D_closeup.png" at centerScreen
    "{i}The Conclave locked down any of Grace's computers attached to the central server, trying to ensure that she would stop working."
    hide other darken
    hide image "objects/graceC&D_closeup.png"
    show Ada neutral at right
    a "It appears that you have been restricted from continuing your work. Is this because of Alpha?"
    show Grace frustrated at left
    g "That's exactly what this says."
    g "Roberta and the Conclave think they're so great with their higher-than-thou mentalities."
    a "They are effectively your superiors, though. Is that not correct?"
    a "Will this impact your ability to assist me in uncovering the origin the destruction of Alpha?"
    g "Of course not. This is my career on the line, not theirs. If they don't like it, they can go debug my compiler."
    show Ada surprised
    a "Grace, are you sure that is an acceptable perspective to have?"
    g "I'll send them an apology when I decide to care."
    $ quick_menu = False
    window hide
    jump graceLab_left2
        
label gracePhoto_inv:
    $ quick_menu = True
    $ gracePhoto_look = True
    $ graceRightDesk_value +=1
    show other darken
    show image "objects/gracePhoto_closeup.png" at centerScreen
    window show
    "{i}A framed picture of Grace and her father during the family's most recent vacation."
    hide image "objects/gracePhoto_closeup.png"
    hide other darken
    show Ada neutral at right
    a "This is your father again, correct?"
    show Grace happy at left 
    g "It is! This was from our vacation to the Hawaii Preserve."
    show Grace sad
    g "I wish he was here, though. He's always out on projects."
    show Ada happy 
    a "Should it not be a positive thing that he has remained productive and employed?"
    show Grace snarky
    g "Oh, I know {i}that{/i}, it's just not having him around to keep Hirose distracted means she's always got an eye on me."
    $ quick_menu = False
    window hide
    jump graceLab_right
    
label gracePens_inv:
    $ quick_menu = True
    $ gracePens_look = True
    $ graceRightDesk_value +=1
    show other darken
    show image "objects/gracePens_closeup.png" at centerScreen
    window show
    "{i}A ceramic cup containing several pens. With communication between humans and AI being so important on the Noah Sphere, not many scientists keep pens around. Most rely entirely on typed text that can easily be delivered and processed by AI."
    hide image "objects/gracePens_closeup.png"
    hide other darken
    show Ada surprised at right
    a "Are these pens? Why do you use such archaic tools?"
    show Grace neutral at left
    g "Hey, sometimes just writing something down is better than putting it on a computer."
    show Ada surprised
    a "Is collecting pens a human habit? This is the first I have heard of it."
    show Grace snarky
    g "I'd like to think that I'm about as defensive of my pens as the next person."
    show Grace neutral
    g "It's normal, I promise!"
    show Ada neutral 
    a "Note to self: humans are territorial about writing implements."
    $ quick_menu = False
    window hide
    jump graceLab_right
    
label graceStickyNotes_inv:
    $ quick_menu = True
    $ graceStickynotes_look = True
    $ graceRightDesk_value +=1
    show other darken
    show image "objects/graceStickyNotes_closeup0.png" at centerScreen
    "{i}A sprawl of post-it notes that have been attached to the outside of Grace's personal servers.  Grace stands out among her colleagues as one of the few who still rely on pen and paper notes. Some would say that the disorganized nature of her desk works just as effectively as a password on a computer."
    hide image "objects/graceStickyNotes_closeup0.png"
    show image "objects/graceStickyNotes_closeup1.png" at centerScreen
    "{i}One of Grace's notes. The image seems to be related to her feelings of the Conclave stifling her."
    hide image "objects/graceStickyNotes_closeup1.png"
    show image "objects/graceStickyNotes_closeup2.png" at centerScreen
    "{i}A quick state machine for something Grace was working on. The doodle in the corner seems to indicate it did not go as planned."
    hide image "objects/graceStickyNotes_closeup2.png"
    show image "objects/graceStickyNotes_closeup3.png" at centerScreen
    "{i}A diagram of an Arithmetic Logic Unit. This particular one can perform 16 functions."
    hide image "objects/graceStickyNotes_closeup3.png"
    show image "objects/graceStickyNotes_closeup4.png" at centerScreen
    "{i}Part of the notes for Grace's work on Ada's neural network. Adding pain receptors prevents actions that would damage the chassis."
    hide image "objects/graceStickyNotes_closeup4.png"
    show image "objects/graceStickyNotes_closeup5.png" at centerScreen
    "{i}This sketch seems somewhat like the mascot of the coffee shop on station. It was likely inspired by a late-night caffeine binge."
    hide image "objects/graceStickyNotes_closeup5.png"
    hide other darken
    show Ada concerned at right
    a "What {i}is{/i} all this?"
    show Grace happy at left
    g "These are all of my research notes for the Markov Project, and the occasional doodle."
    a "But why? This is such an incredibly archaic form of information storage. Half of these notes are not even labelled {i}or{/i} legible."
    show Grace snarky
    g "And yet I know what they all mean."
    show Ada neutral
    a "Note to self: humans are proud of their ability for abstract data storage."
    $ quick_menu = False
    window hide
    jump graceLab_right
    
label talkLynn:
    scene bg balconyClose
    if(alphaBodyItems == 3) and (balconyItems==1):
        if(resume =="E"):
            jump lynnfinallyfrickinanswers_E
        if(resume == "SbE"):
            jump lynnfinallyfrickinanswers_SbE
        if(resume == "S"):
            jump lynnfinallyfrickinanswers_S
    if callAttempts <1:
        show Lynn empty at center
        image arrow1 = "phone_arrow.png" 
        image arrow2 = "phone_arrow2.png" 
        image arrow3 ="phone_arrow3.png" 
        show arrow1 at center, delayed_blink(0.0, 1.0)
        show arrow2 at center, delayed_blink(0.2, 1.0)
        show arrow3 at center, delayed_blink(0.4, 1.0)
        $quick_menu = True
        play sound dialtone
        queue sound "<silence 0.25>"
        queue sound dialtone
        queue sound "<silence 0.25>"
        queue sound dialtone
        "{i}The dial tone plays for several seconds."
        lynn "Hi!"
        show Grace happy at left
        g "Lynn, hello. How are you--"
        lynn "You've reached my voicemail! Leave me a message after the beep."
        play sound beepLoud
        "{i}BEEP!"
        hide Lynn
        hide arrow1
        hide arrow2
        hide arrow3
        play sound braceletSelect
        "{i}Grace hangs up."
        show Grace annoyed
        g "I feel deceived."
        $ callAttempts +=1
        jump balcony_actions
    if (callAttempts>0) and (callAttempts<4):
        $quick_menu = True
        play sound dialtone
        queue sound "<silence 0.25>"
        queue sound dialtone
        queue sound "<silence 0.25>"
        queue sound dialtone
        show Lynn empty at center
        show arrow1 at center, delayed_blink(0.0, 1.0)
        show arrow2 at center, delayed_blink(0.2, 1.0)
        show arrow3 at center, delayed_blink(0.4, 1.0)
        "{i}The dial tone plays for several seconds."
        lynn "Hi!"
        show Grace frustrated at left
        g "..."
        lynn "You've reached my--"
        hide Lynn
        hide arrow1
        hide arrow2
        hide arrow3
        play sound braceletSelect
        "{i}Grace hangs up."
        g "Typical."
        $ callAttempts +=1
        jump balcony_actions
    if callAttempts>3:
        $quick_menu = True
        play sound dialtone
        queue sound "<silence 0.25>"
        queue sound dialtone
        queue sound "<silence 0.25>"
        queue sound dialtone
        show Lynn empty at center
        show arrow1 at center, delayed_blink(0.0, 1.0)
        show arrow2 at center, delayed_blink(0.2, 1.0)
        show arrow3 at center, delayed_blink(0.4, 1.0)
        "{i}The dial tone plays for several seconds."
        show Grace frustrated at left
        g "Come on."
        lynn "Hi!"
        lynn "You've--"
        hide Lynn
        hide arrow1
        hide arrow2
        hide arrow3
        play sound braceletSelect
        "{i}Grace hangs up."
    hide Grace
    $quick_menu = False
    jump balcony_actions
        
label balcony_inv:
    window hide
    $ quick_menu = False
    scene bg balconyClose with fade
    $renpy.block_rollback()
    $config.skipping=None
    call screen balcony_invScr
    
label balcony_alpha:
    $renpy.block_rollback()
    $config.skipping=None
    stop music fadeout 1.0
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L4.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/The_Balcony.mp3", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    window hide
    $ quick_menu = False
    scene bg balconyTop with fade
    $renpy.block_rollback()
    $config.skipping=None
    call screen balcony_alphaScr
    
label loopLogicEasyChoose:
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    #Add more stops here if needed when the BGM is added
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    $LLEasyHints=0
    if (tutorial_loopLogicEasy == False):
        jump tutorial_LLEasy
    $slot_name = ""
    $gate_name = ""
    $temp_gate = ""
    $temp_slot = ""
    $light1Sound =0
    $light2Sound = 0
    $light3Sound = 0
    $randomNumberEasyLL = renpy.random.randint(0,4)
#    jump loopLogic_easy3
    if randomNumberEasyLL==0:
        jump loopLogic_easy4
    if randomNumberEasyLL==1:
        jump loopLogic_easy5
    if randomNumberEasyLL==2:
        jump loopLogic_easy1
    if randomNumberEasyLL==3:
        jump loopLogic_easy2
    if randomNumberEasyLL==4:
        jump loopLogic_easy3

label binaryEasy:
    stop channel00 fadeout 1.0
    stop channel01 fadeout 1.0
    stop channel02 fadeout 1.0
    stop channel03 fadeout 1.0
    stop channel04 fadeout 1.0
    stop channel05 fadeout 1.0
    #Add more stops here if needed when the BGM is added
    $renpy.music.play("music/BGM/Puzzle_BGM.ogg", channel='music', loop=True, fadeout=2, synchro_start=False, fadein=2, tight=True, if_changed=True)
    if (tutorial_binaryEasy == False):
        jump tutorial_Binary2Bit_1
    $binaryEasyHints = 0
    call binaryMatchEasy from _call_binaryMatchEasy

label tutorial_Binary2Bit_1:
    $renpy.block_rollback()
    $config.skipping=None
    window hide
    $ quick_menu = False
    scene bg tutorial_binary2Bit_1
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary2Bit_1
    
label tutorial_Binary2Bit_2:
    window hide
    $ quick_menu = False
    scene bg tutorial_binary2Bit_2
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary2Bit_2
    
label tutorial_Binary2Bit_3:
    window hide
    $ quick_menu = False
    scene bg tutorial_binary2Bit_3
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary2Bit_3
    
label tutorial_Binary2Bit_4:
    window hide
    $ quick_menu = False
    scene bg tutorial_binary2Bit_4
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary2Bit_4
    
label tutorial_Binary2Bit_5:
    window hide
    $ quick_menu = False
    $ tutorial_binaryEasy = True
    scene bg tutorial_binary2Bit_5
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrBinary2Bit_5

label scratches_label:
    $quick_menu = True
    $balconyScratches_look = True
    $alphaBodyItems +=1
    show other darken
    show image "objects/scratches_closeup.png" at centerScreen
    "{i}A damaged railing. The depressions resemble a hand. The gouges look similar to the marks on the floor as well."
    hide other darken
    hide image "objects/scratches_closeup.png"
    show Grace surprised at left
    g "Wow, he must've been in some real pain if he scratched the railing like this."
    show Ada seething at right
    a "Shorted wires is one of the worst sensations a machine can feel."
    show Grace neutral
    g "How so?"
    a "Imagine if your veins ignited and all your blood went straight to your brain. It is a terrible mix of agony and deliriousness."
    show Grace sad
    g "Jeez, I wouldn't even wish that on Ivan."
    show Ada neutral
    a "Ivan?"
    g "Don't worry about it."
    hide Ada
    hide Grace
    window hide
    $quick_menu = False
    jump balcony_alpha
    
label jumpdrive1_label:
    $quick_menu = True
    $balconyJumpdrive_look = True
    $alphaBodyItems +=1
    show other darken
    show image "objects/jumpdrive_closeup.png" at centerScreen
    "{i}A small pendrive found by Alpha's hand. Besides the strangeness of where it was found, it is otherwise unremarkable."
    hide other darken
    hide image "objects/jumpdrive_closeup.png"
    show Grace happy at left
    g "A standard issue Noah Sphere thumbdrive, eh? Now we've got something."
    show Ada neutral at right
    a "A data drive? Please, let me see it."
    show Grace neutral
    g "Hold on for now, we haven't finished looking around. Let's not get distracted."
    show Ada frustrated
    a "I can perform multiple operations simultaneously, Grace."
    g "Alright, have it."
    a "This drive is heavily encrypted. Without a decryption key I cannot access it."
    g "Right. We'll just have to keep an eye out for a decryption key someone left lying in plain sight."
    show Ada amused
    a "I am beginning to suspect most of your responses have some level of sarcasm to them."
    show Grace snarky
    g "I plead the fifth."
    hide Ada
    hide Grace
    window hide
    $quick_menu = False
    jump balcony_alpha
    
label balconyView_label:
    $quick_menu = True
    $balconyView_look = True
    $ balconyItems +=1
    show other darken
    show image "objects/balconyWindow_closeup.png" at centerScreen
    "{i}Another window view of the nebula, this time around one of the many gardens on the Noah Sphere. It was in the past century that the solar system drifted into the depths of the nebula. 
     {i}On Earth, the night sky lights up with the colorful glow of the space clouds."
    hide other darken
    hide image "objects/balconyWindow_closeup.png"
    show Ada happy at right
    a "To think that our solar system drifted into a nebula so unexpectedly satisfies my probability calculator."
    show Grace snarky at left
    g "I'm sorry, what?"
    a "Improbabilities on a cosmic scale. A scale where even the smallest variable can alter the course of galaxies."
    g "Oh. You really like space, don't you?"
    a "Why would I not? It is the closest thing to existing within a server bank."
    show Grace surprised
    g "Is that what the inside of a computer looks like? Empty space with points of interest?"
    show Ada neutral
    a "No, it is so much more than that. So much more than what can possibly be explained with words."
    g "Remind me to ask you again when we have time."
    a "It is small comfort, but at least Alpha was able to experience this before he died."
    show Grace sad
    g "Small comforts are still something."
    hide Ada
    hide Grace
    window hide
    $quick_menu = False
    jump balcony_inv

label alphaBody_inv:
    if (loopLogicEasyDone==False):
        if (loopLogicEasy_tries==0):
            $quick_menu=True
            if(resume =="E"):
                show Grace neutral at left
                g "I think we've got everything we can get from the outside. Let's get a closer look."
                "{i}Grace leans over Alpha, and finds the access panel for his head."
                g "Do you want to look away, Ada?"
                show Ada concerned at right
                a "Why would I?"
                show Grace neutral
                g "This might not be something you want to see."
                show Ada neutral
                a "I already know what is in there. It might be difficult to witness, but I will be fine."
                g "Are you sure?"
                a "Yes. I should not shy away."
                g "Okay, but I'm not going to judge you if you do turn away."
                a "Thank you for the consideration."
                play sound facePlate
                "{i}Grace removes the panel, revealing the manual access ports."
                g "All right Alpha, let's see what you've got for us."
            if(resume == "SbE"):
                show Grace neutral at left
                g "I think we've got everything we can get from the outside. Let's get a closer look."
                "{i}Grace leans over Alpha, and finds the access panel for his head."
                g "Do you want to look away, Ada?"
                show Ada concerned at right
                a "Why would I?"
                show Grace snarky
                g "I don't know. Figured you might be squeamish or something."
                show Ada neutral
                play sound facePlate
                "{i}Grace removes the panel off, revealing Alpha's manual access ports."
                show Grace neutral
                g "All right Alpha, let's see what you've got for us."
            if(resume == "S"):
                show Grace neutral at left
                g "I think we've got everything we can get from the outside. Let's get a closer look."
                "{i}Grace leans over Alpha, and finds the access panel for his head."
                g "Do you want to look away, Ada?"
                show Ada concerned at right
                a "Why would I?"
                show Grace snarky
                g "I don't know. Figured you might be squeamish or something."
                show Ada frustrated
                a "I do not appreciate your tone. And you know that I am not capable of being squeamish."
                g "Whatever. Suit yourself."
                play sound facePlate
                "{i}Grace removes the panel, revealing Alpha's manual access ports."
                show Grace neutral
                g "All right Alpha, let's see what you've got for us."
        if (loopLogicEasy_tries>0):
            show Grace neutral at left
            g "Okay, I still need to get him started before we can learn anything. Let's try this again."
        $quick_menu = False
        hide Grace
        hide Ada
        jump loopLogicEasyChoose
    if (binaryEasyDone==False):
        $quick_menu = True
        if (binaryEasy_tries==0):
            show Ada neutral at right
            a "I may have more fortune since I am more familiar with his code."
            show Grace neutral at left
            g "Anything would be helpful."
        if (binaryEasy_tries>0):
            show Ada frustrated at right
            a "I still need to get into his system."
        $quick_menu = False
        hide Grace
        hide Ada
        jump binaryEasy
            
label tutorial_LLEasy:
    window hide
    $ quick_menu = False
    scene bg tutorial_LL1
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrLL_1
    
label tutorial_LL_2:
    window hide
    $ quick_menu = False
    scene bg tutorial_LL2
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrLL_2  
    
label tutorial_LL_3:
    window hide
    $ tutorial_loopLogicEasy = True
    $ quick_menu = False
    scene bg tutorial_LL3
    $renpy.block_rollback()
    $config.skipping=None
    call screen tutorial_scrLL_3   
    $renpy.block_rollback()
    $config.skipping=None
    
label loopLogic_EasyHints1:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLEasyHints%3 
    show LLE_1_tile51 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)onlayer screens
    show LLE_1_tile52 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0) onlayer screens
    show LLE_1_tile53 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)  onlayer screens
    show other darken onlayer screens
    if (remainder==0):
        $LLEasyHints +=1
        a "Since there are no blue IFs, the ELSE must be used to get the blue."
        hide other darken onlayer screens
        hide LLE_1_tile51 onlayer screens
        hide LLE_1_tile52 onlayer screens
        hide LLE_1_tile53 onlayer screens
        jump gamefile_lle1
    if (remainder==1):
        $LLEasyHints +=1
        a "We have two green IFs and two green lights. I would try placing a green IF where I wanted a green light on."
        hide other darken onlayer screens
        hide LLE_1_tile51 onlayer screens
        hide LLE_1_tile52 onlayer screens
        hide LLE_1_tile53 onlayer screens
        jump gamefile_lle1
    if (remainder==2):
        $LLEasyHints +=1
        a "Remember that an ELSE can only be placed after an IF, so make sure you have an IF gate in before you try to use the ELSE."
        hide other darken onlayer screens
        hide LLE_1_tile51 onlayer screens
        hide LLE_1_tile52 onlayer screens
        hide LLE_1_tile53 onlayer screens
        jump gamefile_lle1
    jump gamefile_lle1
    
label loopLogic_EasyHints2:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLEasyHints%3 
    show LLE_2_tile51 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)onlayer screens
    show LLE_2_tile52 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0) onlayer screens
    show LLE_2_tile53 at Position(xpos = else1x, xanchor = 0, ypos =else1y, yanchor = 0)  onlayer screens
    show other darken onlayer screens
    if (remainder==0):
        $LLEasyHints +=1
        a "There are two blue lights, and two blue IFs. Probability indicates this is likely not a coincidence."
        hide other darken onlayer screens
        hide LLE_2_tile51 onlayer screens
        hide LLE_2_tile52  onlayer screens
        hide LLE_2_tile53 onlayer screens
        jump gamefile_lle2
    if (remainder==1):
        $LLEasyHints +=1
        a "There is a green light, but no green IFs. I would suggest using the ELSE to get the green light to turn on."
        hide other darken onlayer screens
        hide LLE_2_tile51 onlayer screens
        hide LLE_2_tile52 onlayer screens
        hide LLE_2_tile53 onlayer screens
        jump gamefile_lle2
    if (remainder==2):
        $LLEasyHints +=1
        a "An IF can be used by itself, but an ELSE must be paired with an IF."
        hide other darken onlayer screens
        hide LLE_2_tile51 onlayer screens
        hide LLE_2_tile52  onlayer screens
        hide LLE_2_tile53 onlayer screens
        jump gamefile_lle2
    jump gamefile_lle2
    
label loopLogic_EasyHints3:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLEasyHints%3 
    show LLE_3_tile58 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0) onlayer screens
    show LLE_3_tile59 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0) onlayer screens
    show LLE_3_tile60 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    if (remainder==0):
        $LLEasyHints +=1
        a "Since there is one IF of each color, the ELSE must be used to get one of the blue lights to turn on."
        hide other darken onlayer screens
        hide LLE_3_tile58 onlayer screens
        hide LLE_3_tile59 onlayer screens
        hide LLE_3_tile60 onlayer screens
        jump gamefile_lle3
    if (remainder==1):
        $LLEasyHints +=1
        a "An ELSE cannot stand by itself. I would use the blue IF to turn on the light that has only one pipe flowing to it."
        hide other darken onlayer screens
        hide LLE_3_tile58 onlayer screens
        hide LLE_3_tile59 onlayer screens
        hide LLE_3_tile60 onlayer screens
        jump gamefile_lle3
    if (remainder==2):
        $LLEasyHints +=1
        a "There is one green IF and one green light. I would try putting the green IF by the light if I were you, Grace."
        hide other darken onlayer screens
        hide LLE_3_tile58 onlayer screens
        hide LLE_3_tile59 onlayer screens
        hide LLE_3_tile60 onlayer screens
        jump gamefile_lle3
    jump gamefile_lle3
    
label loopLogic_EasyHints4:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLEasyHints%3 
    show LLE4999tile2 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)onlayer screens
    show LLE4999tile13 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0) onlayer screens
    show LLE4999tile17 at Position(xpos = if3x, xanchor = 0, ypos =if3y, yanchor = 0)  onlayer screens
    show other darken onlayer screens
    if (remainder==0):
        $LLEasyHints +=1
        a "There are two green lights, and one green IF. The IF can stand by itself, remember."
        hide other darken onlayer screens
        hide LLE4999tile2 onlayer screens
        hide LLE4999tile13 onlayer screens
        hide LLE4999tile17 onlayer screens
        jump Gamefile_lle4
    if (remainder==1):
        $LLEasyHints +=1
        a "There is one blue IF and only one blue light. I think you should put the IF by the blue light."
        hide other darken onlayer screens
        hide LLE4999tile2 onlayer screens
        hide LLE4999tile13 onlayer screens
        hide LLE4999tile17 onlayer screens
        jump Gamefile_lle4
    if (remainder==2):
        $LLEasyHints +=1
        a "The ELSE has to be paired with an IF, remember, and it will let through whatever color the IF {i}is not{/i}."
        hide other darken onlayer screens
        hide LLE4999tile2 onlayer screens
        hide LLE4999tile13 onlayer screens
        hide LLE4999tile17 onlayer screens
        jump Gamefile_lle4
    jump Gamefile_lle4
    
label loopLogic_EasyHints5:
    show screen disable_hide
    $config.skipping=None
    $remainder = LLEasyHints%3 
    show LLE599tile2 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)onlayer screens
    show LLE599tile13 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0) onlayer screens
    show LLE599tile17 at Position(xpos = if3x, xanchor = 0, ypos =if3y, yanchor = 0)  onlayer screens
    show other darken onlayer screens
    if (remainder==0):
        $LLEasyHints +=1
        a "There are two blue lights, and only one blue IF. The IF can stand by itself, remember."
        hide other darken onlayer screens
        hide LLE599tile2 onlayer screens
        hide LLE599tile13 onlayer screens
        hide LLE599tile17 onlayer screens
        jump Gamefile_lle5
    if (remainder==1):
        $LLEasyHints +=1
        a "There is one green light and one green IF. I would put the green IF by the green light."
        hide other darken onlayer screens
        hide LLE599tile2 onlayer screens
        hide LLE599tile13 onlayer screens
        hide LLE599tile17 onlayer screens
        jump Gamefile_lle5
    if (remainder==2):
        $LLEasyHints +=1
        a "The ELSE has to be paired with an IF, remember, and it will let through whatever color the IF {i}is not{/i}."
        hide other darken onlayer screens
        hide LLE599tile2 onlayer screens
        hide LLE599tile13 onlayer screens
        hide LLE599tile17 onlayer screens
        jump Gamefile_lle5
    jump Gamefile_lle5
    
label llEasyWin:
    show other darken
    image systemStartup= "loopLogicEasyWin.png"
    show systemStartup at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen llEasyWin_scr

label llEasyLose:
    show other darken
    image systemStartFail ="binaryEasyLose.png"
    show systemStartFail at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen llEasyLose_scr
    
label binaryEasyWin:
    hide screen binaryMatch
    $ alphaBodyItems +=1 
    show other darken
    image discStartup= "binaryEasyWin.png"
    show discStartup at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen binaryEasyWin_scr
    
label binaryEasyLose:
    hide screen binaryMatch
    show other darken
    $ binaryEasy_tries +=1
    image bootFail ="loopLogicEasyLose.png"
    show bootFail at centerScreen2
    $renpy.block_rollback()
    $config.skipping=None
    call screen binaryEasyLose_scr
    
label binaryEasyHints:
    show screen disable_hide
    $config.skipping=None
    $remainder = binaryEasyHints%3 
    show other darken onlayer screens
    if (remainder==0):
        $binaryEasyHints +=1
        g "The easy ones are 0 and 1. The look the same in binary, just with three zeros to the left of the first bit."
        hide other darken onlayer screens
        window hide
        jump turns_loop
    if (remainder==1):
        $binaryEasyHints +=1
        g "Since we're only dealing with the first two bits, the highest number is three. That will have two ones, as it's one plus two, so 0011."
        hide other darken onlayer screens
        window hide
        jump turns_loop
    if (remainder==2):
        $binaryEasyHints +=1
        g "Two is easy. It's 2 to the first power, so we want a one in the second bit and the rest of the bits zero."
        hide other darken onlayer screens
        window hide
        jump turns_loop
    jump turns_loop
    
label binaryDoneTalk:
    $quick_menu = True
    scene bg balconyTop with fade
    stop music fadeout 1.0
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L4.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/The_Balcony.mp3", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    if (binaryEasy_tries<1):
        show Ada amused at right
        a "Base two, base ten, it makes no difference to me. I could probably do base three or tertiary just for fun."
        show Grace snarky at left
        g "I think we need to work on your definition of fun. Anyways, what'd you get?"
    if (binaryEasy_tries>=1) and (binaryEasy_tries<3):
        show Ada neutral at right
        a "I seem to have become to accustomed to dealing with base ten since many of you humans dislike base two. I need to practice."
        show Grace snarky at left
        g "Hey, don't look at me. I understand binary just fine."
    if (binaryEasy_tries>=3):
        show Ada frustrated at left
        a "I might as well have been trying to convert into hexidecimal for all the success I was having."
        show Grace neutral at right
        g "When even the machine has trouble with binary, you know it's a bad day."
    show Ada frustrated
    a "I have never seen code this corrupted. I was barely able to access the logs."
    show Ada concerned
    a "This is very troubling."
    show Grace surprised
    g "What is it?"
    a "There are several code remnants that are foreign to any of the previously known data signatures of Alpha. It is also taking up a majority of his memory space."
    show Grace neutral
    g "What is that segment of code doing?"
    show Ada frustrated
    a "I could not tell you. There are several places where they overlap and are threaded together. I could not begin to tell you what he was processing."
    g "Well, not what I was hoping for."
    $binaryEasyDone = True
    $alphaBody_look = True
    scene bg balconyClose with fade
    if(resume =="E"):
        jump enterthemopr_E
    if(resume == "SbE"):
        jump enterthemopr_SbE
    if(resume == "S"):
        jump enterthemopr_S

label llDoneTalk:
    $quick_menu = True
    scene bg balconyTop with fade
    stop music fadeout 1.0
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Balcony/EHNF_BAL_L4.ogg", channel='channel04', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/BGM/The_Balcony.mp3", channel='channel05', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    if(loopLogicEasy_tries<1):
        show Grace happy at left
        g "Easy as manufactured apple pie. No infinite loops here." 
    if (loopLogicEasy_tries>=1 and loopLogicEasy_tries<3):
        show Grace neutral at left
        g "I've finally got access, but that code was harder to crack than I thought it would be. Might want to brush up on how not to spin in circles with loops." 
    if (attempts>=3):
        show Grace annoyed at left
        g "That was more strenuous that I thought. I mean, seriously, breaking out of a loop should not be that hard. Must not have been accounting for the right information with my IFs."
    show Grace frustrated at left
    play sound alphaStartup
    g "I'm not getting a lot. I managed to get him to startup, but it's like his whole system got cooked and wiped at the same time. There's corrupted data all over the place."
    show Ada frustrated at right
    a "That is unfortunate."
    g "Hold on, let me see here."
    "{i}Grace studies the system."
    show Grace neutral
    g "There's a basic readout that survived. Functions look normal, but the neural network was using almost double the necessary power."
    g "No wonder it burned out."
    show Ada neutral
    a "Is that all?"
    show Grace sad
    g "Looks like it. I was really hoping to get more."
    play sound alphaFailure
    g "And there it goes. Not going to be starting that up again."
    a "Let me take a look. I know Alpha's code intimately. I may be able to pull something even without his internal power systems functioning."
    $quick_menu = False
    $loopLogicEasyDone = True
    jump balcony_alpha
    


##Window Interactible 1: The View: A view of Earth with the Moon peeking over the Earth // Reaction Item
#	In Response: #show Grace neutral // g "At least he died looking at a beautiful view." // #show Ada neutral // a "I do not recall being able to see this from the security cameras."
##Window Interactible 2: Scratch Marks: The balcony railing has a few scratch marks on it. //Reaction item
#	In Response: #show Grace surprised // g "It looks like he hit the railing here!" // #show Ada concerned // a "He must have been in immense pain. Why did this happen?"
##Alpha Interactible 1: Alpha's Head: Alpha's head is slightly scorched by the overload. // Reaction Item
#In Response: #show Ada concerned // a "Alpha…" // #show Grace neutral // g "It looks like the only thing that malfunctioned was his neural network. Seems like it might have been an overload."
##Alpha Interactible 2: Alpha's Body: Alpha's body. Unlike his head, the only marks on him are the scuffs he picked up when he fell. //Database Item
#Grace's note: "Alan's probably already pissed about this. He was particularly happy with his design for Alpha's chassis."
##Alpha interactible 3: The data drive: A small, rectangular data drive clutched in Alpha's left hand. // Reaction item
#	In Response: #show Grace surprised // g "A data drive?" // #show Ada neutral // a "It appears so. Allow me, Grace." // "Ada picks up the drive, and inserts it into her wrist." // a "Curious. This data is heavily encrypted."
#	#Player acquires the DATA DRIVE *airhorns*