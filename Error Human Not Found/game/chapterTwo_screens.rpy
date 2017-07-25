label chapterTwo_screens:
    $ gracePoster_look = False
    screen graceLab_actionsScr:
        imagebutton:
            idle "adaTalk.png" 
            hover "adaTalk_hover.png" 
            xpos 0
            ypos 0 
            focus_mask True
            action Jump("talkAdaGraceLab")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("graceLab_inv")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen graceLab_invScr:
        imagebutton:
            idle "arrowL.png"
            hover "arrowL_hover.png"
            xpos 450
            ypos 170
            focus_mask True
            action Jump("graceLab_left1")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrowR.png"
            hover "arrowR_hover.png"
            xpos 1190
            ypos 480
            focus_mask True
            action Jump("graceLab_right")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("graceLab_actions")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
            
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
                hover_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrowD.png"
            hover "arrowD_hover.png"
            xpos 1190
            ypos 890
            focus_mask True
            action Jump("graceLab_inv")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrowL.png"
            hover "arrowL_hover.png"
            xpos 0
            ypos 710
            focus_mask True
            action Jump("graceLab_left2")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen graceLab_left2Scr:
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[graceLeft2Desk_value]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "3" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        imagebutton:
            idle "arrowR.png"
            hover "arrowR_hover.png"
            xpos 1730
            ypos 710
            focus_mask True
            action Jump("graceLab_left1")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
            
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
        imagebutton:
            idle "arrowD.png"
            hover "arrowD_hover.png"
            xpos 865
            ypos 890
            focus_mask True
            action Jump("graceLab_inv")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen balcony_actionsScr:
        imagebutton:
            idle "callLynn.png" #Comment SWAP THIS WITH WRISTBAND
            hover "callLynn_hover.png" #SWAP THIS WITH WRISTBAND/CELL
            xpos 0
            ypos 0 
            focus_mask True
            action Jump("talkLynn")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("balcony_inv")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen balcony_invScr:
        imagebutton:
            idle "arrowD.png"
            hover "arrowD_hover.png"
            xpos 860
            ypos 200
            focus_mask True
            action Jump("balcony_alpha")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("balcony_actions")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen balcony_alphaScr:
        #Add explorable objects here
        imagebutton:
            idle "arrow.png"
            hover "arrow_hover.png"
            xpos 860
            ypos 0
            focus_mask True
            action Jump("balcony_inv")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"

            
            
label graceLab_actions:
    scene bg G_deskArea
    $ quick_menu = False
    window hide
    call screen graceLab_actionsScr
    
label talkAdaGraceLab:
    scene bg G_deskArea
    "Next click will jump."
    if(resume =="E"):
        jump resumeChapterTwo_E
    if(resume == "SbE"):
         jump resumeChapterTwo_SbE
    if(resume == "S"):
         jump resumeChapterTwo_S
    
label graceLab_inv:
    scene bg G_deskArea with fade
    $ quick_menu = False
    window hide
    call screen graceLab_invScr
    
label graceLab_left1:
    scene bg G_left1 with fade
    $ quick_menu = False
    window hide    
    call screen graceLab_left1Scr
    
label graceLab_left2:
    scene bg G_left2 with fade
    $ quick_menu = False
    window hide    
    call screen graceLab_left2Scr
    
label graceLab_right:
    scene bg G_right with fade
    $ quick_menu = False
    window hide
    call screen graceLab_right
    
label balcony_actions:
    scene bg balconyClose
    $ quick_menu = False
    window hide
    call screen balcony_actionsScr
    
label gracePoster_inv:
    $ quick_menu = True
    $ gracePoster_look = True
    $ graceLeft1Desk_value +=1
    show other darken
    show image "objects/gracePoster_closeup.png" at centerScreen
    window show
    "An official Noah Sphere poster designed for employee motivation. The image is based on the old Earth  'Rosie the Riveter'  cultural icon."
    hide image "objects/gracePoster_closeup.png"
    hide other darken
    #show Grace neutral
    g "This poster is so cheesy."
    #show Ada neutral
    a "I detect no traces of curd."
    #show Grace annoyed
    g "No, Ada, what I meant was that I don't like how, er... to the point this poster is."
    a "Is that not the point? To clearly indicate the poster's purpose while imparting the significance upon the viewer?"
    g "I want to keep defending my point, but that was solid."
    a "Solid logic is just another day on the job for me."
    jump graceLab_left1
    
    #Comment need all the image buttons for objects
    #Also need all the labels for the items
    
label talkLynn:
    scene bg balconyClose
    if (balconyItems == 3) and (moprScene==False):
        if(resume =="E"):
            jump enterthemopr_E
        if(resume == "SbE"):
            jump enterthemopr_SbE
        if(resume == "S"):
            jump enterthemopr_S
    if(balconyItems==3) and (moprScene==True):
        if(resume =="E"):
            jump lynnfinallyfrickinanswers_E
        if(resume == "SbE"):
            jump lynnfinallyfrickinanswers_SbE
        if(resume == "S"):
            jump lynnfinallyfrickinanswers_S
    if callAttempts <1:
        "The dial tone plays for several seconds."
        lynn "Hi!"
        #show Grace happy
        g "Lynn, hello. How are you--"
        lynn "You've reached my voicemail! Leave me a message after the beep."
        "BEEP!"
        "Grace hangs up."
        g "I feel deceived."
        $ callAttempts +=1
        jump balcony_actions
    if (callAttempts>0) and (callAttempts<4):
        "The dial tone plays for several seconds."
        lynn "Hi!"
        #show Grace frustrated
        g "..."
        lynn "You've reached my--"
        "Grace hangs up."
        g "Typical."
        $ callAttempts +=1
        jump balcony_actions
    if callAttempts>3:
        "The dial tone plays for several seconds."
        #show Grace frustrated
        g "Come on."
        lynn "Hi!"
        lynn "You've--"
        "Grace hangs up."
        $ balconyItems = 3 #CHANGE THIS. THIS IS JUST WHILE THE OTHER OBJECTS DO NOT EXIST
    jump balcony_actions
        
label balcony_inv:
    window hide
    $ quick_menu = False
    scene bg balconyClose with fade
    call screen balcony_invScr
    
label balcony_alpha:
    window hide
    $ quick_menu = False
    scene bg balconyTop with fade
    call screen balcony_alphaScr
    

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