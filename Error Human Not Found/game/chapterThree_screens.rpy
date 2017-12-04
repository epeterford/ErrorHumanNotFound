#OBJECT SCREENS
screen nightShift_scr:
    if(gramMed_solved==False):
        imagebutton:
            idle "objects/nightShift_idle.png"
            hover "objects/nightShift_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("investigateNightShift")
            hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
            activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
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
            
screen lab2Table_scr:
    imagebutton:
        idle "button_empty.png"
        xpos 1630
        ypos 10
    text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
    text ": " xpos 1780 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
    text "[lab2Items_table]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
    text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
    text "1" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
    imagebutton:
        idle "objects/cable_idle.png"
        hover "objects/cable_hover.png"
        xpos 0
        ypos 0 
        focus_mask True
        action Jump("lab2Table_resume")
        hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
        activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
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

screen ivanComp_scr:
    if(talkIvan_count>0) and (llMed_solved==False):
        imagebutton:
            idle "objects/ivanComp_idle.png"
            hover "objects/ivanComp_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("choose_llMed")
            hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
            activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
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
    text ": " xpos 1780 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
    text "[lab2Items]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
    text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
    if (not(llMed_solved) and llMed_attempts ==0):
        text "2" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
    else:
        text "3" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
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
        
label lab2_inv:
    stop music fadeout 1.0
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L0.ogg", channel='channel00', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L1.ogg", channel='channel01', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
#    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L2.ogg", channel='channel02', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
#    $renpy.music.play("music/Amb/Lab2/EHNF_LAB2_L3.ogg", channel='channel03', loop=True, fadeout=1.0, synchro_start=True, fadein=1.0, tight=True, if_changed=True)
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
    $quick_menu = False
    if(ivanComp_lock==True):
        scene bg lab2Ivan_locked with fade
    else:
        scene bg lab2Ivan_unlocked with fade
    call screen lab2_inv_scr
    
label investigateIvan:
    hide screen disable_hide
    hide screen loopLogicMed_5Scr
    hide screen loopLogicMed_4Scr
    hide screen loopLogicMed_3Scr
    hide screen loopLogicMed_2Scr
    hide screen loopLogicMed_1Scr
    $quick_menu = False
    if(ivanComp_lock==True):
        scene bg lab2Ivan_locked with fade
    else:
        scene bg lab2Ivan_unlocked with fade
    call screen ivanComp_scr
    
label investigateIvanNotes:
    hide screen disable_hide
    hide screen ivanComp_scr
    $config.skipping = None
    $renpy.block_rollback()
    $config.rollback_enabled = True
    $config.allow_skipping = True
    $ivanNotes_inv = True
    $lab2Items +=1
    show other darken
    show image "objects/ivanNotes_closeup.png" at centerScreen
    $quick_menu = True
    "{i}A stack of tablets with Ivan's research notes about the Markov Project. There is a stark contrast between the neatly stacked tablets which Ivan keeps his notes on and the sprawl of post-it notes and papers on Grace's desk.{/i}"
    hide other darken
    hide image "objects/ivanNotes_closeup.png"
    show Grace snarky at left
    show Ivan dour at right
    g "Well, what do we have--"
    "{i}Ivan snatches his notes away.{/i}"
    show Ivan defensive
    ivan "And just what are you doing?"
    show Grace annoyed
    g "I wanted to look at your notes. You know, compare them to mine and all that."
    show Ivan disgusted
    ivan "And what, you think you can just peer into somone else's notes like that?"
    g "Ivan, we're working on the {i}same project{/i}. There's literally no reason for you to act like this."
    show Ivan dour
    ivan "Here's a reason: I don't want you looking at my notes."
    hide Grace
    hide Ivan
    $quick_menu = False
    window hide
    jump investigateIvan
    
label investigateCatPhoto:
    hide screen disable_hide
    hide screen ivanComp_scr
    $config.skipping = None
    $renpy.block_rollback()
    $config.rollback_enabled = True
    $config.allow_skipping = True
    $catPhoto_inv = True
    $lab2Items +=1
    show other darken
    show image "objects/catPhoto_closeup.png" at centerScreen
    $quick_menu = True
    "{i}A framed picture of Ivan's overweight black cat, Mr. Frillywhiskers.  A large, yellow bowtie lies around his neck, and his expression shows that he is not amused.{/i}"
    hide other darken
    hide image "objects/catPhoto_closeup.png"
    show Grace happy at left
    show Ivan dour at right
    g "Your cat's adorable, Ivan. Too bad it has to live with {i}you{/i}"
    show Ivan disgusted
    ivan "I'll have you know that Mr. Frillywiskers and I were fated to be together."
    show Ivan phony
    ivan "I absolutely disdain anything that isn't him, and he reciprocates the feeling."
    show Grace snarky
    g "Just marry your cat while you're at it, Ivan. Who needs people?"
    show Ivan dour
    ivan "For once, we're in agreement on something."
    hide Ivan
    hide Grace
    window hide
    $quick_menu = False
    jump investigateIvan
    
label talkIvan:
    hide screen disable_hide
    $config.skipping = None
    $renpy.block_rollback()
    $config.rollback_enabled = True
    $config.allow_skipping = True
    $quick_menu=True
    if(talkIvan_count==0):
        if(resume=="S"):
            jump talkIvanLab2_S
        if(resume=="E"):
            jump talkIvanLab2_E
        if(resume=="SbE"):
            jump talkIvanLab2_SbE
    if(lab2Items==3 and talkIvan_count>0):
        if(resume=="S"):
            jump finishLab2Inv_S
        if(resume=="E"):
            jump finishLab2Inv_E
        if(resume=="SbE"):
            jump finishLab2Inv_SbE
            
    if(talkIvan_count==1):
        $talkIvan_count +=1
        show Grace neutral at left
        show Ivan dour at right
        g "Hey, Ivan, about what we talked about..."
        ivan "Not again, Fortran. There's only so much of you I can take."
        show Grace annoyed
        g "I was just going to say--"
        show Ivan disgusted
        ivan "What part of 'there's only so much of you I can take' do you not understand?"
        show Ivan defensive
        ivan "Stop harassing me."
        show Grace neutral
        g "Fine. So grumpy..."
        hide Grace
        hide Ivan
        window hide
        $quick_menu = False
        jump lab2_inv
        
    if(talkIvan_count==2):
        $talkIvan_count +=1
        show Grace neutral at left
        show Ivan dour at right
        g "Ivan, there was another thing I wanted to talk about."
        show Ivan disgusted
        ivan "Enough, Fortran! You are wasting my time."
        show Ivan defensive
        ivan "Every passing second is insufferable with you here."
        show Ivan phony
        ivan "Why don't you spend less time making me miserable and more time completing your little fool's errand so you can leave me in peace?"
        show Grace snarky
        g "..."
        g "So you {i}don't{/i} want to talk?"
        show Ivan disgusted
        ivan "{i}No{/i}."
        hide Grace
        hide Ivan
        window hide
        $quick_menu=False
        jump lab2_inv

    if(talkIvan_count>2):
        $talkIvan_count +=1
        show Grace snarky at left
        show Ivan dour at right
        g "Hey, Ivan?"
        ivan "..."
        g "You're not gonna talk?"
        ivan "..."
        show Grace neutral
        g "I think he's ignoring me."
        $quick_menu = False
        hide Grace
        hide Ivan
        window hide
        jump lab2_inv
            
label lab2Table:
    show bg lab2_cord
    hide Grace
    hide Ivan
    $quick_menu = False
    window hide
    call screen lab2Table_scr
    
label lab2Table_resume:
    show bg lab2_noCord
    $quick_menu = True
    show Grace neutral at left
    show Ivan dour at right
    hide screen disable_hide
    $config.skipping = None
    $renpy.block_rollback()
    $config.rollback_enabled = True
    $config.allow_skipping = True
    "{i}Grace retrieves a burnt power cord.{/i}"
    hide Grace
    hide Ivan
    show other darken
    show image "objects/cord_closeup.png" at centerScreen
    "{i}A small section of burnt-out cord. It looks similar to the cords used in the body of the androids for Alpha and Ada.{/i}"
    hide other darken
    hide image "objects/cord_closeup.png"
    show Grace surprised at left
    show Ivan dour at right
    g "Aha!"
    show Grace happy
    g "What do we have here?"
    show Ivan disgusted
    ivan "A defective power cord. Do I really have to remind you what that is?"
    g "But why was it tucked away behind a desk like this?"
    show Ivan dour
    ivan "It must have fallen out of the disposal bin. MOPRS are efficient, but they're clumsy sometimes."
    show Grace snarky
    g "Really?"
    show Ivan defensive
    ivan "What the--? There's no way that came from my team!"
    show Ivan dour
    ivan "It was probably Ellen and her team of chumps. They're an incompetent lot."
    show Grace snarky
    g "Yeah, everyone is incompetent besides you and your little researchers, huh?"
    show Ivan phony
    ivan "Yes, you included."
    show Grace angry
    g "What exactly is your problem with me?"
    show Ivan disgusted
    ivan "Other than the fact that you receive special treatment for being the daughter of the Director, nothing."
    g "You know that I don't receive special treatment."
    show Grace neutral
    g "I worked just as hard as you to be where I am today."
    show Ivan phony
    ivan "That's debatable. I'm not sure anyone works as hard as I do."
    show Grace annoyed
    g "Oh please."
    show Grace snarky
    g "If that's what helps you sleep at night, by all means, believe yourself."
    ivan "I sleep just fine at night, and I will continue to do so, thank you."
    "{i}Grace rolls her eyes.{/i}"
    show Grace neutral
    g "When is Ellen's shift?"
    show Ivan dour
    ivan "Precisely after mine."
    ivan "This way to her computer. And don't touch anything else!"
    jump nightShift_comp
    
label nightShift_comp:
    hide screen disable_hide
    hide screen logicGates_med1
    hide screen logicGates_med2
    hide screen logicGates_med3
    hide screen logicGates_med4
    hide screen logicGates_med5
    hide screen lab2Table_scr
    if (gramMed_attempts>0):
        scene bg lab2WS_locked with fade
        $quick_menu = True
        show Grace annoyed at left
        show Ivan dour at right
        hide screen disable_hide
        $config.skipping = None
        $renpy.block_rollback()
        $config.rollback_enabled = True
        $config.allow_skipping = True
        g "Ivan, normal people either make sure they have access to all the information they might need, or they ensure that they know the passwords to get it."
        show Ivan phony
        ivan "I have everything {i}I{/i} need."
        show Grace snarky
        g "Right. I'm going to get it in a minute anyways."
    $quick_menu = False
    hide Grace
    hide Ivan
    scene bg lab2WS_locked with fade
    call screen nightShift_scr
    
label investigateNightShift:
    if(gramMed_attempts==0):
        hide screen disable_hide
        $config.skipping = None
        $renpy.block_rollback()
        $config.rollback_enabled = True
        $config.allow_skipping = True
        show other darken
        show image "objects/nightShift_closeup.png" at centerScreen
        "{i}The main computer used by the night crew. Ivan has a habit of leaving aggressive notes on here when disatisfied with the state that the lab is left in.{/i}"
        hide other darken
        hide image "objects/nightShift_closeup.png"
        #dialogue displayed before the puzzle starts
        show Grace neutral at left
        show Ivan dour at right
        g "This one's Ellen's, right?"
        ivan "Of course, Doctor Fortran. Do you have any other obvious questions."
        show Grace annoyed
        g "Right. Because asking something about a lab I don't work in is an obvious question." 
        jump choose_gramMed
    else:
        jump choose_gramMed