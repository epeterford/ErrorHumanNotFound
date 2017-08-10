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
        if(graceNeuralNetwork_look == False):
            imagebutton:
                idle "objects/graceNeuralNetwork.png"
                hover "objects/graceNeuralNetwork_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceNeuralNetwork_inv")
                hover_sound "audio/ENHF_UI_Button_v1.ogg"
        if(graceHardDrive_look == False):
            imagebutton:
                idle "objects/graceHarddrive.png"
                hover "objects/graceHarddrive_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceHardDrive_inv")
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
            idle "arrowR.png"
            hover "arrowR_hover.png"
            xpos 1730
            ypos 710
            focus_mask True
            action Jump("graceLab_left1")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        if(graceCandD_look == False):
            imagebutton:
                idle "objects/graceC&D.png"
                hover "objects/graceC&D_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceCandD_inv")
                hover_sound "audio/ENHF_UI_Button_v1.ogg"
        if(graceBust_look == False):
            imagebutton:
                idle "objects/graceBust.png"
                hover "objects/graceBust_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceBust_inv")
                hover_sound "audio/ENHF_UI_Button_v1.ogg"
        if(graceCoffee_look == False):
            imagebutton:
                idle "objects/graceCoffee.png"
                hover "objects/graceCoffee_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceCoffee_inv")
                hover_sound "audio/ENHF_UI_Button_v1.ogg"
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
                hover_sound "audio/ENHF_UI_Button_v1.ogg"
        if(gracePens_look == False):
            imagebutton:
                idle "objects/gracePens.png"
                hover "objects/gracePens_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("gracePens_inv")
                hover_sound "audio/ENHF_UI_Button_v1.ogg"
        if(graceStickynotes_look == False):
            imagebutton:
                idle "objects/graceStickyNotes.png"
                hover "objects/graceStickyNotes_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("graceStickyNotes_inv")
                hover_sound "audio/ENHF_UI_Button_v1.ogg"
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
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[alphaBodyItems]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "3" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if (binaryEasyDone == False) and (loopLogicEasyDone==False):
            imagebutton: 
                idle "objects/alpha.png"
                hover "objects/alpha_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("loopLogicEasyChoose")
                hover_sound "audio/ENHF_UI_Button_v1.ogg"
        if (binaryEasyDone == False) and (loopLogicEasyDone==True):
            imagebutton: 
                idle "objects/alpha.png"
                hover "objects/alpha_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("binaryEasy")
                hover_sound "audio/ENHF_UI_Button_v1.ogg"
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
    "{i}An official Noah Sphere poster designed for employee motivation. The image is based on the old Earth  'Rosie the Riveter'  cultural icon."
    hide image "objects/gracePoster_closeup.png"
    hide other darken
    #show Grace neutral
    g "This poster is so cheesy."
    #show Ada neutral
    a "I detect no traces of curd."
    #show Grace annoyed
    g "No, Ada, what I meant was that I don't like how, er... to the point this poster is."
    a "Is that not the point? To clearly indicate the purpose of the poster while imparting the significance upon the viewer?"
    g "I want to keep defending my point, but that was solid."
    a "Solid logic is just another day on the job for me."
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
    a "Your hard drives, Grace! You can't keep them like this."
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
    g "Ada, the little baby hard drives will be fine. I'm still storing all my notes from the Markov project, so they need to be like that just a little bit longer." 
    $ quick_menu = False
    window hide
    jump graceLab_left1

label graceBust_inv:
    $ quick_menu = True
    $ graceBust_look = True
    $ graceLeft2Desk_value +=1
    show other darken
    show image "objects/graceBust_closeup.png" at centerScreen
    "{i}The Conclave locked down any of Grace's computers attached to the central server, trying to ensure that she would stop working."
    hide other darken
    hide image "objects/graceBust_closeup.png"
    show Grace snarky at left
    g "What's your take on this, Ada?"
    show Ada neutral at right
    a "Hmm..."
    a "The appearance of this robot is compatible with what humans find comfortable; however, the design itself is hardly optimal."
    show Grace neutral
    g "How so?"
    show Ada concerned
    a "This robot does not possess peripheral sensors, and it doesn't have any fingers. "
    g "Noted."
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
    a "The robot's appearance is compatible with what humans find comfortable; however, the design itself is hardly optimal."
    show Grace neutral
    g "How so?"
    show Ada concerned
    a "This robot does not possess peripheral sensors, and it doesn't have any fingers. "
    g "Noted."
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
    a "Is this your father?"
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
    a "Note to self: Humans are territorial about writing implements."
    $ quick_menu = False
    window hide
    jump graceLab_right
    
label graceStickyNotes_inv:
    $ quick_menu = True
    $ graceStickynotes_look = True
    $ graceRightDesk_value +=1
    show other darken
    show image "objects/graceStickyNotes_closeup1.png" at centerScreen
    "{i}A sprawl of binders, folders, and post-it notes scattered across the desk.  Grace stands out among her colleagues as one of the few who still rely on pen and paper notes. Some would say that the disorganized nature of her desk works just as effectively as a password on a computer."
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
    a "Note to self: Humans are proud of their ability for abstract data storage."
    $ quick_menu = False
    window hide
    jump graceLab_right
    
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
        "{i}The dial tone plays for several seconds."
        lynn "Hi!"
        #show Grace happy
        g "Lynn, hello. How are you--"
        lynn "You've reached my voicemail! Leave me a message after the beep."
        "{i}BEEP!"
        "{i}Grace hangs up."
        g "I feel deceived."
        $ callAttempts +=1
        jump balcony_actions
    if (callAttempts>0) and (callAttempts<4):
        "{i}The dial tone plays for several seconds."
        lynn "Hi!"
        #show Grace frustrated
        g "..."
        lynn "You've reached my--"
        "{i}Grace hangs up."
        g "Typical."
        $ callAttempts +=1
        jump balcony_actions
    if callAttempts>3:
        "{i}The dial tone plays for several seconds."
        #show Grace frustrated
        g "Come on."
        lynn "Hi!"
        lynn "You've--"
        "{i}Grace hangs up."
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
    
label loopLogicEasyChoose:
    #if (tutorial_loopLogicEasy == False):
        #jump tutorial_LLEasy
    $randomNumberEasyLL = renpy.random.randint(0,1)
    if randomNumberEasyLL==0:
        jump loopLogic_easy4
    if randomNumberEasyLL==1:
        jump loopLogic_easy5

label binaryEasy:
    #if (tutorial_binaryEasy == False):
        #jump tutorial_2Bit
    call binaryMatchEasy

#label tutorial_LLEasy:
    
#label tutorial_2Bit:
    


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