label chapterOne_screens:
    screen lgEasyWin_scr:
        imagebutton:
            idle "yes.png" 
            hover "yes_hover.png" 
            xpos 705
            ypos 610 
            focus_mask True
            action Jump("pickNextPuzzleLGEasy")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "no.png" 
            hover "no_hover.png" 
            xpos 925
            ypos 610
            focus_mask True
            action Jump("exploreHiroseOffice")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
    screen lgEasyLose_scr:
        imagebutton:
            idle "yes.png" 
            hover "yes_hover.png" 
            xpos 705
            ypos 610 
            focus_mask True
            action Jump("pickNextPuzzleLGEasy")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "no.png" 
            hover "no_hover.png" 
            xpos 925
            ypos 610 
            focus_mask True
            action Jump("exploreHiroseOffice")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
    screen lgEasyDone_scr:
        imagebutton:
            idle "finish.png" 
            hover "finish_hover.png" 
            xpos 815
            ypos 610
            focus_mask True
            action Jump("lgEasyDone_talk")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrInv_1:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1670
            ypos 960 
            focus_mask True
            action Jump("tutorial_Inv_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrInv_2:
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos -15
            ypos 960 
            focus_mask True
            action Jump("tutorial_Inv_1")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "finish.png" 
            hover "finish_hover.png" 
            xpos 1670
            ypos 960 
            focus_mask True
            action Jump("hiroseOffice_actions")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrLGEasy_1:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1670
            ypos 960 
            focus_mask True
            action Jump("tutorial_LGEasy_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrLGEasy_2:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1670
            ypos 960 
            focus_mask True
            action Jump("tutorial_LGEasy_3")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos -15
            ypos 960 
            focus_mask True
            action Jump("tutorial_LGEasy_1")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrLGEasy_3:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1670
            ypos 960 
            focus_mask True
            action Jump("tutorial_LGEasy_4")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos -15
            ypos 960 
            focus_mask True
            action Jump("tutorial_LGEasy_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrLGEasy_4:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1670
            ypos 960  
            focus_mask True
            action Jump("tutorial_LGEasy_5")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos -15
            ypos 960 
            focus_mask True
            action Jump("tutorial_LGEasy_3")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrLGEasy_5:
        imagebutton:
            idle "finish.png" 
            hover "finish_hover.png" 
            xpos 1670
            ypos 960 
            focus_mask True
            action Jump("easyLGAPuzzle")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos -15
            ypos 960 
            focus_mask True
            action Jump("tutorial_LGEasy_4")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen hiroseOfficeAction:
        imagebutton:
            idle "adaTalk.png" 
            hover "adaTalk_hover.png" 
            xpos 0
            ypos 0 
            focus_mask True
            action Jump("talkAdaHiroseOffice")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("exploreOffice")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen hiroseOffice1_scr:
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[hiroseTransitionItems]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "1" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        if (hiroseTree_inv == False):
            imagebutton: 
                idle "objects/hiroseTree.png"
                hover "objects/hiroseTree_hover.png"
                xpos 0
                ypos 0
                focus_mask True
                action Jump("hiroseTree")
                hover_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrow.png"
            hover "arrow_hover.png"
            xpos 1340
            ypos 700
            focus_mask True
            action Jump("hiroseOffice2")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("hiroseOffice_actions")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen hiroseOffice2_scr:
        imagebutton:
            idle "arrow.png" 
            hover "arrow_hover.png" 
            xpos 1288 
            ypos 308 
            focus_mask True
            action Jump("exploreHiroseOffice")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrowL.png" 
            hover "arrowL_hover.png" 
            xpos 127 
            ypos 308 
            focus_mask True
            action Jump("exploreOffice")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen investigateOffice:
        #text "Items: [hiroseOfficeItems]/3" xpos 1750 ypos 10 color "#dddddd"
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[hiroseOfficeItems]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "3" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        imagebutton:
            idle "arrowL.png" 
            hover "arrowL_hover.png" 
            xpos 0 
            ypos 345 
            focus_mask True
            action Jump("hiroseOffice2")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        if (hiroseTea_inv == False):
            imagebutton:
                idle "hiroseTea.png" 
                hover "hiroseTea_hover.png" 
                xpos 591 
                ypos 385 
                focus_mask True
                action Jump("hiroseTea_label")
                hover_sound "audio/ENHF_UI_Highlight.ogg"
        if (hiroseRecorder_inv == False):
            imagebutton:
                idle "objects/hiroseRecorder.png" 
                hover "objects/hiroseRecorder_hover.png" 
                xpos 0 
                ypos 0 
                focus_mask True
                action Jump("hiroseRecorder_label")
                hover_sound "audio/ENHF_UI_Highlight.ogg"
        if (hiroseOfficeComputer == False):
            imagebutton:
                idle "objects/hiroseOfficialComputer.png" 
                hover "objects/hiroseOfficialComputer_hover.png" 
                xpos 0
                ypos 0
                focus_mask True
                action Jump("adaActualPuzzle1")
                hover_sound "audio/ENHF_UI_Highlight.ogg"
                
    screen hirosePersonalArea_scr:
        imagebutton:
            idle "adaTalk.png" 
            hover "adaTalk_hover.png" 
            xpos 0
            ypos 0 
            focus_mask True
            action Jump("talkAdaHirosePersonal")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("hirosePersonalArea_inv")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen hirosePersonalArea_invScr:
        imagebutton:
            idle "arrowL.png"
            hover "arrowL_hover.png"
            xpos 794
            ypos 351
            focus_mask True
            action Jump("hirosePersonalComputer")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrow.png"
            hover "arrow_hover.png"
            xpos 1596
            ypos 650
            focus_mask True
            action Jump("hiroseBed")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("hirosePersonalArea_actions")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen investigateHirosePC:
        imagebutton:
            idle "arrowD.png"
            hover "arrowD_hover.png"
            xpos 865
            ypos 890
            focus_mask True
            action Jump("hirosePersonalArea_inv")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "objects/hiroseComputer.png"
            hover "objects/hiroseComputer_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("hirosePC_label")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen investigateHiroseBed:
        imagebutton:
            idle "button_empty.png"
            xpos 1630
            ypos 10
        text "Items" xpos 1650 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text ": " xpos 1775 ypos 8 color "#0060db" font "Bitter-Bold.otf" size 50
        text "[hirosePersonalItems_value]" xpos 1800 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        text "/" xpos 1827 ypos 25 color "#0060db" font "Bitter-Bold.otf"
        text "3" xpos 1850 ypos 25 color "#0060db" font "United Kingdom DEMO.otf"
        imagebutton:
            idle "arrowD.png" 
            hover "arrowD_hover.png" 
            xpos 865
            ypos 890 
            focus_mask True
            action Jump("hirosePersonalArea_inv")
            hover_sound "audio/ENHF_UI_Button_v1.ogg"
        if (hiroseBed_inv == False):
            imagebutton:
                idle "objects/hiroseBed.png" 
                hover "objects/hiroseBed_hover.png" 
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("hiroseBed_label")
                hover_sound "audio/ENHF_UI_Highlight.ogg"
        if (hiroseWindow_inv == False):
            imagebutton:
                idle "objects/hiroseWindow.png" 
                hover "objects/hiroseWindow_hover.png" 
                xpos 0 
                ypos 0
                focus_mask True
                action Jump("hiroseWindow_label")
                hover_sound "audio/ENHF_UI_Highlight.ogg"
        if (hirosePhoto_inv == False):
            imagebutton:
                idle "hirosePhoto.png" 
                hover "hirosePhoto_hover.png" 
                xpos 1512
                ypos 729 
                focus_mask True
                action Jump("hirosePhoto_label")
                hover_sound "audio/ENHF_UI_Highlight.ogg"
    jump tutorial_Inv_1
            
label tutorial_Inv_1:
    window hide
    $ quick_menu = False
    scene bg tutorial_inv_1
    call screen tutorial_scrInv_1
    
label tutorial_Inv_2:
    window hide
    $ quick_menu = False
    scene bg tutorial_inv_2
    call screen tutorial_scrInv_2
    
label tutorial_LGEasy_1:
    play music "music/BGM/Puzzle_BGM.ogg"
    window hide
    $ quick_menu = False
    scene bg lgEasy1 
    call screen tutorial_scrLGEasy_1
    
label tutorial_LGEasy_2:
    window hide
    $ quick_menu = False
    scene bg lgEasy2 
    call screen tutorial_scrLGEasy_2
        
label tutorial_LGEasy_3:
    window hide
    $ quick_menu = False
    scene bg lgEasy3 
    call screen tutorial_scrLGEasy_3
    
label tutorial_LGEasy_4:
    window hide
    $ quick_menu = False
    scene bg lgEasy4 
    call screen tutorial_scrLGEasy_4
    
label tutorial_LGEasy_5:
    window hide
    $ quick_menu = False
    scene bg lgEasy5 
    call screen tutorial_scrLGEasy_5
    
label hiroseOffice_actions:
    window hide
    $ quick_menu = False
    scene bg hiroseOfficeMain 
    if talkAdaHiroseOffice_value>0 and hiroseOfficeItems == 3 and hiroseTransitionItems == 1:
        jump wegotthedeets
    call screen hiroseOfficeAction
    
label hiroseTea_label:
    $ quick_menu = True
    $ hiroseTea_inv = True
    $ hiroseOfficeItems +=1
    show image "hiroseTea_closeup.png" at centerScreen
    window show
    "A cup containing the dregs of a hybrid floral tea."
    g "Roberta does drink some of the strangest teas. I'll stick to my coffee, thanks."
    a "Humans and their caffeine..."
    hide image "hiroseTea_closeup.png"
    window hide
    $ quick_menu = False
    jump exploreHiroseOffice

label hiroseTree:
    $ quick_menu = True
    $ hiroseTree_inv = True
    $ hiroseTransitionItems +=1
    show other darken
    show image "objects/hiroseTree_closeup.png" at centerScreen
    window show
    "A collection of exotic trees with seeds imported from Earth. It's rare to see this much plant-life in the office of a space station. "
    hide image "objects/hiroseTree_closeup.png"
    hide other darken
    show Grace frustrated at left
    g "I never understood how it's fine that Hirose can have a small forest to herself in her office when I can barely get the clearance to have some potted plants."
    show Ada neutral at right
    a "Is it not natural for humans to allocate more resources to their leaders?"
    show Grace snarky 
    g "You're talking like we're still in tribes or something."
    a "Robotocists, botanists, Conclave members, all of these groups with their own identities. Is this not the definition of tribalism?"
    g "I... well, I suppose. Just because you're technically right doesn't mean you won this one."
    a "I was not aware we were debating. Would you like to?"
    g "This is really not the place, Ada. I don't want to spend anymore time in this amazing office than necessary."
    window hide
    $ quick_menu = False
    jump exploreOffice
    
label hiroseBed_label:
    $ quick_menu = True
    $ hiroseBed_inv = True
    $ hirosePersonalItems_value += 1
    show other darken
    show image "objects/hiroseBed_closeup.png" at centerScreen
    window show
    "A sizeable bed in Hirose's office. A control panel by the edge of the bed platform allows a user to inflate a memory foam mattress out of the center of the bed and customize it to their needs."
    hide other darken
    hide image "objects/hiroseBed_closeup.png"
    show Ada amused at right
    a "This room's layout hardly seems standard."
    show Grace snarky at left
    g "I wonder what tipped you off."
    show Ada neutral
    a "Well, these sleeping arrangements are placed in a work area, for one."
    show Grace neutral
    g "That's Hirose for you. Dad and I used to be worried when she wouldn't come home from work."
    g "We learned that there's other places she'd rather be, apparently."
    $ quick_menu = False
    window hide
    jump hiroseBed
    
label hiroseRecorder_label:
    $ quick_menu = True
    $ hiroseRecorder_inv = True
    $ hiroseOfficeItems += 1
    show other darken
    show image "objects/hiroseRecorder_closeup.png" at centerScreen
    window show
    "This desk is made for Hirose's stenographer. This old-fashion style of recording events is rarely seen anymore, but dedicated practitioners in the art of writing shorthand have kept the profession alive."
    hide other darken
    hide image "objects/hiroseRecorder_closeup.png"
    show Grace frustrated at left
    g "Why Hirose insists on having an actual person transcribe her meetings instead of just getting an audio recorder is beyond me."
    show Ada neutral at right
    a "It does not seem that odd to me. The Director must always work at peak efficiency."
    show Grace neutral
    g "What does efficiency have to do with it?"
    "Ada shrugs, although the motion is stiff."
    a "Perhaps she just prefers to read?"
    g "..."
    g "You've got me there."
    window hide
    $ quick_menu = False
    jump exploreHiroseOffice
    
label hiroseWindow_label:
    $ quick_menu = True
    $ hiroseWindow_inv = True
    $ hirosePersonalItems_value += 1
    show other darkenR
    show image "objects/hiroseWindow_closeup.png" at centerScreen
    window show
    "An expansive view of the vibrant nebula. Only some of the offices on the Noah Sphere have windows facing out into the galaxy."
    hide image "objects/hiroseWindow_closeup.png"
    hide other darken
    show Grace happy at left
    g "The view from up here never gets old."
    g "If it's got a bed in it, I suppose even an office can be a room with a view."
    show Ada amused at right
    a "It already has windows, Grace. Is it not already a room with a view?"
    show Grace snarky
    g "All this time around humans, and no ear for metaphors?" 
    show Ada neutral
    a "My memory banks are far from exhaustive, Grace."
    show Grace neutral
    g "Right Hotel metaphors remain the exclusive domain of humans for the forseeable future."
    window hide
    $ quick_menu = False
    jump hiroseBed
    
label LGEasyHintsA1:
    $ quick_menu = True
    $ remainder = LGEasyHints%3
    image EB111tile07_02 = "and_Gate.png"
    show EB111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show other darken
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyA1
    if (remainder==1):
        $ LGEasyHints +=1
        $ hintYes = True
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyA1
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyA1
    $ quick_menu = False
    jump logicGate_easyA1
    
label LGEasyHintsA2:
    $ quick_menu = True
    $ remainder = LGEasyHints%3
    image EB111tile07_02A2 = "OR_Gate.png"
    show EB111tile07_02A2 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show other darken
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyA2
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyA2
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyA2
    $ quick_menu = False
    jump logicGate_easyA2
    
label LGEasyHintsA3:
    $ quick_menu = True
    $ remainder = LGEasyHints%3
    image EB111tile07_02A3 = "OR_Gate.png"
    show EB111tile07_02A3 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    show other darken
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyA3
    if (remainder ==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyA3
    if (remainder ==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyA3
    $ quick_menu = False
    jump logicGate_easyA3
    
label LGEasyHintsB1:
    $ quick_menu = True
    $ remainder = LGEasyHints%3
    image EB111tile07_02 = "and_Gate.png"
    show EB111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    image EB111tile07_08 = "or_Gate.png"
    show EB111tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show other darken
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyB1
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyB1
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyB1
    $ quick_menu = False
    jump logicGate_easyB1
    
label LGEasyHintsB2:
    $ quick_menu = True
    $ remainder = LGEasyHints%3
    image EB25end1 = "light_g_on.png"
    show EB25end1 at Position(xpos = 1595, xanchor = 0, ypos = 308, yanchor = 0)
    image EB25tile04_03 = "and_Gate.png"
    show EB25tile04_03 at Position(xpos = 661, xanchor = 0, ypos = 533, yanchor = 0)
    image EB25tile01_07 = "or_Gate.png"
    show EB25tile01_07 at Position(xpos = 961, xanchor = 0, ypos = 308, yanchor = 0)
    show other darken
    if (remainder== 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyB2
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyB2
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyB2
    $ quick_menu = False
    jump logicGate_easyB2
    
label LGEasyHintsB3:
    image EB311tile07_02 = "and_Gate.png"
    show EB311tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    image EB311tile07_08 = "or_Gate.png"
    show EB311tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show other darken
    $ quick_menu = True
    $ remainder = LGEasyHints%3
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyB3
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyB3
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken
        $ quick_menu = False
        jump logicGate_easyB3
    $ quick_menu = False
    jump logicGate_easyB3
    
label LGEasyHintsC1:
    image EC111tile02_09 = "not_Gate.png"
    show EC111tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
    image EC111tile07_02 = "and_Gate.png"
    show EC111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    image EC111tile07_08 = "or_Gate.png"
    show EC111tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show other darken
    $ quick_menu = True
    $ remainder = LGEasyHints%3
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        $ quick_menu = False
        hide other darken
        jump logicGate_easyC1
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        $ quick_menu = False
        hide other darken
        jump logicGate_easyC1
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        $ quick_menu = False
        hide other darken
        jump logicGate_easyC1
    $ quick_menu = False
    hide other darken
    jump logicGate_easyC1
    
label LGEasyHintsC2:
    $ quick_menu = True
    image EC211tile02_09 = "not_Gate.png"
    show EC211tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
    image EC211tile07_02 = "and_Gate.png"
    show EC211tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    image EC211tile07_08 = "or_Gate.png"
    show EC211tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show other darken
    $ remainder = LGEasyHints%3
    if (remainder==0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        $ quick_menu = False
        hide other darken
        jump _easyC2
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        $ quick_menu = False
        hide other darken
        jump logicGate_easyC2
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        $ quick_menu = False
        hide other darken
        jump logicGate_easyC2
    $ quick_menu = False
    hide other darken
    jump logicGate_easyC2
    
label LGEasyHintsC3:
    $ quick_menu = True
    image EC311tile02_09 = "not_Gate.png"
    show EC311tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0)
    image EC311tile07_02 = "and_Gate.png"
    show EC311tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0)
    image EC311tile07_08 = "or_Gate.png"
    show EC311tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0)
    show other darken
    $ remainder = LGEasyHints%3
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        $ quick_menu = False
        hide other darken
        jump logicGate_easyC3
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        $ quick_menu = False
        hide other darken
        jump logicGate_easyC3
    if (remainder==2):
        $ LGEasyHints += 1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        $ quick_menu = False
        hide other darken
        jump logicGate_easyC3
    $ quick_menu = False
    hide other darken
    jump logicGate_easyC3

label nextLGEasy:
    show other darken
    image segmentComplete = "segmentComplete.png"
    show segmentComplete at centerScreen2
    call screen lgEasyWin_scr
        
label repeatLGEasy:
    show other darken
    image segmentFailed = "segmentFailed.png"
    show segmentFailed at centerScreen2
    call screen lgEasyLose_scr

label lgEasyDone:
    show other darken
    image passwordAccepted = "passwordAccepted.png"
    show passwordAccepted at centerScreen2
    call screen lgEasyDone_scr
