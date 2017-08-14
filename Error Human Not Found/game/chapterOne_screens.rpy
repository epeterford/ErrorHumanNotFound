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
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "no.png" 
            hover "no_hover.png" 
            xpos 925
            ypos 610
            focus_mask True
            action Jump("exploreHiroseOffice")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen lgEasyLose_scr:
        imagebutton:
            idle "yes.png" 
            hover "yes_hover.png" 
            xpos 705
            ypos 610 
            focus_mask True
            action Jump("pickNextPuzzleLGEasy")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "no.png" 
            hover "no_hover.png" 
            xpos 925
            ypos 610 
            focus_mask True
            action Jump("exploreHiroseOffice")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen lgEasyDone_scr:
        imagebutton:
            idle "finish.png" 
            hover "finish_hover.png" 
            xpos 815
            ypos 610
            focus_mask True
            action Jump("lgEasyDone_talk")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen lgEasyWin_scr:
        imagebutton:
            idle "yes.png" 
            hover "yes_hover.png" 
            xpos 705
            ypos 610 
            focus_mask True
            action Jump("pickNextPuzzleLGEasy")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "no.png" 
            hover "no_hover.png" 
            xpos 925
            ypos 610
            focus_mask True
            action Jump("exploreHiroseOffice")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
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
            
    screen doorPuzzle_scr:
        imagebutton:
            idle "objects/hiroseDoor.png" 
            hover "objects/hiroseDoor_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action Jump("chooseEasyGram")
            hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
            activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
            
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
            
    screen tutorial_scrInv_1:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_Inv_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrInv_2:
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_Inv_1")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"

        imagebutton:
            idle "finish.png" 
            hover "finish_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("hiroseOffice_actions")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen tutorial_scrGramEasy_1:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_GramEasy_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrGramEasy_2:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_GramEasy_3")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"

        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_GramEasy_1")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrGramEasy_3:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_GramEasy_4")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_GramEasy_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrGramEasy_4:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940  
            focus_mask True
            action Jump("tutorial_GramEasy_5")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_GramEasy_3")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrGramEasy_5:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940  
            focus_mask True
            action Jump("tutorial_GramEasy_6")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_GramEasy_4")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrGramEasy_6:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940  
            focus_mask True
            action Jump("tutorial_GramEasy_7")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_GramEasy_5")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrGramEasy_7:
        imagebutton:
            idle "finish.png" 
            hover "finish_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("chooseEasyGram")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_GramEasy_6")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrLGEasy_1:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_LGEasy_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrLGEasy_2:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_LGEasy_3")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_LGEasy_1")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrLGEasy_3:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("tutorial_LGEasy_4")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_LGEasy_2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrLGEasy_4:
        imagebutton:
            idle "next.png" 
            hover "next_hover.png" 
            xpos 1650
            ypos 940  
            focus_mask True
            action Jump("tutorial_LGEasy_5")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
            focus_mask True
            action Jump("tutorial_LGEasy_3")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen tutorial_scrLGEasy_5:
        imagebutton:
            idle "finish.png" 
            hover "finish_hover.png" 
            xpos 1650
            ypos 940 
            focus_mask True
            action Jump("easyLGAPuzzle")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "back.png" 
            hover "back_hover.png" 
            xpos 0
            ypos 940 
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
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("exploreOffice")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
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
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        imagebutton:
            idle "arrow.png"
            hover "arrow_hover.png"
            xpos 1340
            ypos 700
            focus_mask True
            action Jump("hiroseOffice2")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("hiroseOffice_actions")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            
    screen hiroseOffice2_scr:
        imagebutton:
            idle "arrow.png" 
            hover "arrow_hover.png" 
            xpos 1288 
            ypos 308 
            focus_mask True
            action Jump("exploreHiroseOffice")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrowL.png" 
            hover "arrowL_hover.png" 
            xpos 127 
            ypos 308 
            focus_mask True
            action Jump("exploreOffice")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
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
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        if (hiroseTea_inv == False):
            imagebutton:
                idle "objects/hiroseTea.png" 
                hover "objects/hiroseTea_hover.png" 
                xpos 0
                ypos 0
                focus_mask True
                action Jump("hiroseTea_label")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if (hiroseRecorder_inv == False):
            imagebutton:
                idle "objects/hiroseRecorder.png" 
                hover "objects/hiroseRecorder_hover.png" 
                xpos 0 
                ypos 0 
                focus_mask True
                action Jump("hiroseRecorder_label")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if (hiroseOfficeComputer == False):
            imagebutton:
                idle "objects/hiroseOfficialComputer.png" 
                hover "objects/hiroseOfficialComputer_hover.png" 
                xpos 0
                ypos 0
                focus_mask True
                action Jump("adaActualPuzzle1")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
                
    screen hirosePersonalArea_scr:
        imagebutton:
            idle "adaTalk.png" 
            hover "adaTalk_hover.png" 
            xpos 0
            ypos 0 
            focus_mask True
            action Jump("talkAdaHirosePersonal")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "investigate.png" 
            hover "investigate_hover.png" 
            xpos 0
            ypos 200
            focus_mask True
            action Jump("hirosePersonalArea_inv")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
            
    screen hirosePersonalArea_invScr:
        imagebutton:
            idle "arrowL.png"
            hover "arrowL_hover.png"
            xpos 794
            ypos 351
            focus_mask True
            action Jump("hirosePersonalComputer")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "arrow.png"
            hover "arrow_hover.png"
            xpos 1596
            ypos 650
            focus_mask True
            action Jump("hiroseBed")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("hirosePersonalArea_actions")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"

            
    screen investigateHirosePC:
        imagebutton:
            idle "arrowD.png"
            hover "arrowD_hover.png"
            xpos 865
            ypos 890
            focus_mask True
            action Jump("hirosePersonalArea_inv")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        imagebutton:
            idle "objects/hiroseComputer.png"
            hover "objects/hiroseComputer_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("hirosePC_label")
            hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
            activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
            
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
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg"
        if (hiroseBed_inv == False):
            imagebutton:
                idle "objects/hiroseBed.png" 
                hover "objects/hiroseBed_hover.png" 
                xpos 0
                ypos 0 
                focus_mask True
                action Jump("hiroseBed_label")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if (hiroseWindow_inv == False):
            imagebutton:
                idle "objects/hiroseWindow.png" 
                hover "objects/hiroseWindow_hover.png" 
                xpos 0 
                ypos 0
                focus_mask True
                action Jump("hiroseWindow_label")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
        if (hirosePhoto_inv == False):
            imagebutton:
                idle "hirosePhoto.png" 
                hover "hirosePhoto_hover.png" 
                xpos 1512
                ypos 729 
                focus_mask True
                action Jump("hirosePhoto_label")
                hover_sound "music/UI/Investigate/ENHF_Investigate_Highlight.ogg"
                activate_sound "music/Object/Misc_Audio/EHNF_Item_Pickup.ogg"
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
    
label tutorial_GramEasy_1:
    play music "music/BGM/Puzzle_BGM.ogg"
    window hide
    $ quick_menu = False
    scene bg gramEasy1 
    call screen tutorial_scrGramEasy_1
    
label tutorial_GramEasy_2:
    window hide
    $ quick_menu = False
    scene bg gramEasy2 
    call screen tutorial_scrGramEasy_2
        
label tutorial_GramEasy_3:
    play sound ["<silence 3.0>"]
    window hide
    $ quick_menu = False
    scene bg gramEasy3 
    call screen tutorial_scrGramEasy_3
    
label tutorial_GramEasy_4:
    window hide
    $ quick_menu = False
    scene bg gramEasy4 
    call screen tutorial_scrGramEasy_4
    
label tutorial_GramEasy_5:
    window hide
    $ quick_menu = False
    scene bg gramEasy5 
    call screen tutorial_scrGramEasy_5
    
label tutorial_GramEasy_6:
    window hide
    $ quick_menu = False
    scene bg gramEasy6 
    call screen tutorial_scrGramEasy_6

label tutorial_GramEasy_7:
    window hide
    $ quick_menu = False
    scene bg gramEasy7 
    call screen tutorial_scrGramEasy_7
    
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
    show other darken
    show image "objects/hiroseTea_closeup.png" at centerScreen
    window show
    "{i}A lukewarm cup of herbal tea. The lids on these reusable cups have a tendency to be slightly too big, and thus pop open without warning. This is truly the worst nightmare of any late-working scientist."
    hide image "objects/hiroseTea_closeup.png"
    hide other darken
    show Ada neutral at right
    a "It makes me nervous, seeing that drink sitting by her computer."
    show Grace snarky at left
    g "Wow. The AI hasn't even been physical for a day and she recognizes that the lids here are suspicious at best."
    show Ada surprised
    a "The lid is structurally unstable as well?"
    g "Yes! I swear these things barely stay on even when the cup's standing still!"
    show Grace neutral
    g "Wait, how does it even feel to have stuff spilled on you?" 
    show Ada neutral
    a "When I was young, a technician spilled some coffee onto a section of my servers. I suppose you would liken it to being set on fire."
    show Grace surprised
    g "Oh..."
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
    "{i}A collection of exotic trees with seeds imported from Earth. It's rare to see this much plant-life in the office of a space station. "
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
    "{i}A sizeable bed in Hirose's office. A control panel by the edge of the bed platform allows a user to inflate a memory foam mattress out of the center of the bed and customize it to their needs."
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
    "{i}This desk is made for Hirose's stenographer. This old-fashion style of recording events is rarely seen anymore, but dedicated practitioners in the art of writing shorthand have kept the profession alive."
    hide other darken
    hide image "objects/hiroseRecorder_closeup.png"
    show Grace frustrated at left
    g "Why Hirose insists on having an actual person transcribe her meetings instead of just getting an audio recorder is beyond me."
    show Ada neutral at right
    a "It does not seem that odd to me. The Director must always work at peak efficiency."
    show Grace neutral
    g "What does efficiency have to do with it?"
    "{i}Ada shrugs, although the motion is stiff."
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
    show other darken
    show image "objects/hiroseWindow_closeup.png" at centerScreen
    "{i}An expansive view of the vibrant nebula. Only some of the offices on the Noah Sphere have windows facing out into the galaxy."
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
    g "Right. Hotel metaphors remain the exclusive domain of humans for the forseeable future."
    window hide
    $ quick_menu = False
    jump hiroseBed
    
label LGEasyHintsA1:
    show screen disable_hide
    $ remainder = LGEasyHints%3
    show eatile100 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken onlayer screens
        hide eatile100 onlayer screens
        jump gamefileA1
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken onlayer screens
        hide eatile100 onlayer screens
        jump gamefileA1
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken onlayer screens
        hide eatile100 onlayer screens
        jump gamefileA1
    $ quick_menu = False
    jump gamefileA1
    
label LGEasyHintsA2:
    show screen disable_hide
    $ remainder = LGEasyHints%3
    show ea1tile100 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken onlayer screens
        hide ea1tile100 onlayer screens
        jump gamefileA2
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken onlayer screens
        hide ea1tile100 onlayer screens
        jump gamefileA2
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken onlayer screens
        hide ea1tile100 onlayer screens
        jump gamefileA2
    jump gamefileA2
    
label LGEasyHintsA3:
    show screen disable_hide
    $ remainder = LGEasyHints%3
    show ea3tile100 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken onlayer screens
        hide ea3tile100 onlayer screens
        jump gamefileA3
    if (remainder ==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken onlayer screens
        hide ea3tile100 onlayer screens
        jump gamefileA3
    if (remainder ==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken onlayer screens
        hide ea3tile100 onlayer screens
        jump gamefileA3
    jump gamefileA3
    
label LGEasyHintsB1:
    show screen disable_hide
    $ remainder = LGEasyHints%3
    show EB111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0) onlayer screens
    show EB111tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken onlayer screens
        hide EB111tile07_02 onlayer screens
        hide EB111tile07_08 onlayer screens
        jump gamefileB1
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken onlayer screens
        hide EB111tile07_02 onlayer screens
        hide EB111tile07_08 onlayer screens
        jump gamefileB1
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken onlayer screens
        hide EB111tile07_02 onlayer screens
        hide EB111tile07_08 onlayer screens
        jump gamefileB1
    jump gamefileB1
    
label LGEasyHintsB2:
    show screen disable_hide
    $ remainder = LGEasyHints%3
    show EB211tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0) onlayer screens
    show EB211tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    if (remainder== 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken onlayer screens
        hide EB211tile07_02 onlayer screens
        hide EB211tile07_08 onlayer screens
        jump gamefileB2
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken onlayer screens
        hide EB211tile07_02 onlayer screens
        hide EB211tile07_08 onlayer screens
        jump gamefileB2
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken onlayer screens
        hide EB211tile07_02 onlayer screens
        hide EB211tile07_08 onlayer screens
        jump gamefileB2
    jump gamefileB2
    
label LGEasyHintsB3:
    show EB311tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0) onlayer screens
    show EB311tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    show screen disable_hide
    $ remainder = LGEasyHints%3
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken onlayer screens
        hide EB311tile07_02 onlayer screens
        hide EB311tile07_08 onlayer screens
        jump gamefileB3
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken onlayer screens
        hide EB311tile07_02 onlayer screens
        hide EB311tile07_08 onlayer screens
        jump gamefileB3
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken onlayer screens
        hide EB311tile07_02 onlayer screens
        hide EB311tile07_08 onlayer screens
        jump gamefileB3
    jump gamefileB3
    
label LGEasyHintsC1:
    show EC111tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0) onlayer screens
    show EC111tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0) onlayer screens
    show EC111tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    show screen disable_hide
    $ remainder = LGEasyHints%3
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide other darken onlayer screens
        hide EC111tile02_09 onlayer screens
        hide EC111tile07_02 onlayer screens
        hide EC111tile07_08 onlayer screens
        jump gamefileC1
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide other darken onlayer screens
        hide EC111tile02_09 onlayer screens
        hide EC111tile07_02 onlayer screens
        hide EC111tile07_08 onlayer screens
        jump gamefileC1
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide other darken onlayer screens
        hide EC111tile02_09 onlayer screens
        hide EC111tile07_02 onlayer screens
        hide EC111tile07_08 onlayer screens
        jump gamefileC1
    hide other darken onlayer screens
    jump gamefileC1
    
label LGEasyHintsC2:
    show screen disable_hide
    show EC211tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0) onlayer screens
    show EC211tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0) onlayer screens
    show EC211tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    $ remainder = LGEasyHints%3
    if (remainder==0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide EC211tile02_09 onlayer screens
        hide EC211tile07_02 onlayer screens
        hide EC211tile07_08 onlayer screens
        hide other darken onlayer screens
        jump gamefileC2
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide EC211tile02_09 onlayer screens
        hide EC211tile07_02 onlayer screens
        hide EC211tile07_08 onlayer screens
        hide other darken onlayer screens
        jump gamefileC2
    if (remainder==2):
        $ LGEasyHints +=1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide EC211tile02_09 onlayer screens
        hide EC211tile07_02 onlayer screens
        hide EC211tile07_08 onlayer screens
        hide other darken onlayer screens
        jump gamefileC2
    hide other darken onlayer screens
    jump gamefileC2
    
label LGEasyHintsC3:
    show screen disable_hide
    show EC311tile02_09 at Position(xpos = not1x, xanchor = 0, ypos = not1y, yanchor = 0) onlayer screens
    show EC311tile07_02 at Position(xpos = and1x, xanchor = 0, ypos = and1y, yanchor = 0) onlayer screens
    show EC311tile07_08 at Position(xpos = or1x, xanchor = 0, ypos = or1y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    $ remainder = LGEasyHints%3
    if (remainder == 0):
        $ LGEasyHints +=1
        g "Remember Ada, the crescent shaped one is the OR gate. As long as one of the pipes is green, or true, the output will be true."
        hide EC311tile02_09 onlayer screens
        hide EC311tile07_02 onlayer screens
        hide EC311tile07_08 onlayer screens
        hide other darken onlayer screens
        jump gamefileC3
    if (remainder==1):
        $ LGEasyHints +=1
        g "Here's a hint: the half moon is the AND gate. If both pipes feeding into it are green, the output will be green. Otherwise it will output red."
        hide EC311tile02_09 onlayer screens
        hide EC311tile07_02 onlayer screens
        hide EC311tile07_08 onlayer screens
        hide other darken onlayer screens
        jump gamefileC3
    if (remainder==2):
        $ LGEasyHints += 1
        g "The easy one is the triangle with the circle on the end. It only works when there is one input, and flips it. Green goes to red, red goes to green. NOT gate is easy as it comes."
        hide EC311tile02_09 onlayer screens
        hide EC311tile07_02 onlayer screens
        hide EC311tile07_08 onlayer screens
        hide other darken onlayer screens
        jump gamefileC3
    hide other darken onlayer screens
    jump gamefileC3
    
label gramEasyHints1:
    show screen disable_hide
    $ remainder = gramEasyHints%3
    show eaeng_e1_tile226 at Position(xpos = eae1and5x, xanchor = 0, ypos = eae1and5y, yanchor = 0) onlayer screens
    show eaeng_e1_tile227 at Position(xpos = eae1and1x, xanchor = 0, ypos = eae1and1y, yanchor = 0) onlayer screens
    show eaeng_e1_tile228 at Position(xpos = eae1and3x, xanchor = 0, ypos = eae1and3y, yanchor = 0) onlayer screens
    show eaeng_e1_tile229 at Position(xpos = eae1and6x, xanchor = 0, ypos = eae1and6y, yanchor = 0) onlayer screens
    show eaeng_e1_tile230 at Position(xpos = eae1and4x, xanchor = 0, ypos = eae1and4y, yanchor = 0) onlayer screens
    show eaeng_e1_tile231 at Position(xpos = eae1and2x, xanchor = 0, ypos = eae1and2y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    if (remainder == 0):
        $ gramEasyHints +=1
        a "N, L, M, and K are all terminal or final substitutions since they are replaced by strings. I would use them on the bottom row only."
        hide eaeng_e1_tile226 onlayer screens
        hide eaeng_e1_tile227 onlayer screens
        hide eaeng_e1_tile228 onlayer screens
        hide eaeng_e1_tile229 onlayer screens
        hide eaeng_e1_tile230 onlayer screens
        hide eaeng_e1_tile231 onlayer screens
        hide other darken onlayer screens
        $ quick_menu = False
        jump gamefile_e1
    if (remainder==1):
        $ gramEasyHints +=1
        a "Remember if a tile is red, nothing below it will receive power. You will not be able to tell if it is correct or not until all tiles above a tile are green. "
        hide eaeng_e1_tile226 onlayer screens
        hide eaeng_e1_tile227 onlayer screens
        hide eaeng_e1_tile228 onlayer screens
        hide eaeng_e1_tile229 onlayer screens
        hide eaeng_e1_tile230 onlayer screens
        hide eaeng_e1_tile231 onlayer screens
        hide other darken onlayer screens
        jump gamefile_e1
    if (remainder==2):
        $ gramEasyHints +=1
        a "P and J both must be replaced by other letters. That means they cannot go in the bottom row and be correct."
        hide eaeng_e1_tile226 onlayer screens
        hide eaeng_e1_tile227 onlayer screens
        hide eaeng_e1_tile228 onlayer screens
        hide eaeng_e1_tile229 onlayer screens
        hide eaeng_e1_tile230 onlayer screens
        hide eaeng_e1_tile231 onlayer screens
        hide other darken onlayer screens
        jump gamefile_e1
    $ quick_menu = False
    jump gamefile_e1
    
label gramEasyHints2:
    $ remainder = gramEasyHints%3
    show screen disable_hide
    show eaeng_e2_tile107 at Position(xpos = eae2and1x, xanchor = 0, ypos = eae2and1y, yanchor = 0) onlayer screens
    show eaeng_e2_tile111 at Position(xpos = eae2and2x, xanchor = 0, ypos = eae2and2y, yanchor = 0) onlayer screens
    show eaeng_e2_tile108 at Position(xpos = eae2and3x, xanchor = 0, ypos = eae2and3y, yanchor = 0) onlayer screens
    show eaeng_e2_tile110 at Position(xpos = eae2and4x, xanchor = 0, ypos = eae2and4y, yanchor = 0) onlayer screens
    show eaeng_e2_tile106 at Position(xpos = eae2and5x, xanchor = 0, ypos = eae2and5y, yanchor = 0) onlayer screens
    show eaeng_e2_tile109 at Position(xpos = eae2and6x, xanchor = 0, ypos = eae2and6y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    if (remainder == 0):
        $ gramEasyHints +=1
        a "You have to use all the available slots. Just because they are green does not mean they will give us the correct answer."
        hide other darken onlayer screens
        hide eaeng_e2_tile107 onlayer screens
        hide eaeng_e2_tile111 onlayer screens
        hide eaeng_e2_tile108 onlayer screens
        hide eaeng_e2_tile110 onlayer screens
        hide eaeng_e2_tile106 onlayer screens
        hide eaeng_e2_tile109 onlayer screens        
        jump gamefile_e2
    if (remainder==1):
        $ gramEasyHints +=1
        a "M and Q are terminal and go to string. They have no further substitutions, so I would put them in the final row."
        hide other darken onlayer screens
        hide eaeng_e2_tile107 onlayer screens
        hide eaeng_e2_tile111 onlayer screens
        hide eaeng_e2_tile108 onlayer screens
        hide eaeng_e2_tile110 onlayer screens
        hide eaeng_e2_tile106 onlayer screens
        hide eaeng_e2_tile109 onlayer screens   
        jump gamefile_e2
    if (remainder==2):
        $ gramEasyHints +=1
        a "N can only be substituted as PN, which is a substitution for K. That means K has to be above N."
        hide other darken onlayer screens
        hide eaeng_e2_tile107 onlayer screens
        hide eaeng_e2_tile111 onlayer screens
        hide eaeng_e2_tile108 onlayer screens
        hide eaeng_e2_tile110 onlayer screens
        hide eaeng_e2_tile106 onlayer screens
        hide eaeng_e2_tile109 onlayer screens   
        jump gamefile_e2
    $ quick_menu = False
    jump gamefile_e2
    
label gramEasyHints3:
    $ remainder = gramEasyHints%3
    show screen disable_hide
    show eaeng_e3_tile202 at Position(xpos = eae3and1x, xanchor = 0, ypos = eae3and1y, yanchor = 0) onlayer screens
    show eaeng_e3_tile206 at Position(xpos = eae3and2x, xanchor = 0, ypos = eae3and2y, yanchor = 0) onlayer screens
    show eaeng_e3_tile203 at Position(xpos = eae3and3x, xanchor = 0, ypos = eae3and3y, yanchor = 0) onlayer screens
    show eaeng_e3_tile205 at Position(xpos = eae3and4x, xanchor = 0, ypos = eae3and4y, yanchor = 0) onlayer screens
    show eaeng_e3_tile201 at Position(xpos = eae3and5x, xanchor = 0, ypos = eae3and5y, yanchor = 0) onlayer screens
    show eaeng_e3_tile204 at Position(xpos = eae3and6x, xanchor = 0, ypos = eae3and6y, yanchor = 0) onlayer screens
    show other darken onlayer screens
    if (remainder == 0):
        $ gramEasyHints +=1
        a "I do believe you should fill in the tree from the top to the bottom. The first rule, S can be substituted by SK, might be a good place to start."
        hide other darken onlayer screens
        hide eaeng_e3_tile202 onlayer screens
        hide eaeng_e3_tile206 onlayer screens
        hide eaeng_e3_tile203 onlayer screens
        hide eaeng_e3_tile205 onlayer screens
        hide eaeng_e3_tile201 onlayer screens
        hide eaeng_e3_tile204 onlayer screens
        $ quick_menu = False
        jump gamefile_e3
    if (remainder==1):
        $ gramEasyHints +=1
        $ hintYes = True
        a "S can also be substituted by MJ. Maybe try those on the left?"
        hide other darken onlayer screens
        hide eaeng_e3_tile202 onlayer screens
        hide eaeng_e3_tile206 onlayer screens
        hide eaeng_e3_tile203 onlayer screens
        hide eaeng_e3_tile205 onlayer screens
        hide eaeng_e3_tile201 onlayer screens
        hide eaeng_e3_tile204 onlayer screens
        $ quick_menu = False
        jump gamefile_e3
    if (remainder==2):
        $ gramEasyHints +=1
        a "S is also a terminal letter in two cases, so it should be on the bottom twice."
        hide other darken onlayer screens
        hide eaeng_e3_tile202 onlayer screens
        hide eaeng_e3_tile206 onlayer screens
        hide eaeng_e3_tile203 onlayer screens
        hide eaeng_e3_tile205 onlayer screens
        hide eaeng_e3_tile201 onlayer screens
        hide eaeng_e3_tile204 onlayer screens
        $ quick_menu = False
        jump gamefile_e3
    $ quick_menu = False
    jump gamefile_e3
    
screen disable_hide():
    key 'h' action NullAction() #action Hide("")
    key 'K_PAGEUP' action NullAction() #action Hide("")
    key 'repeat_K_PAGEUP' action NullAction() #action Hide("")
    key 'K_AC_BACK' action NullAction() #action Hide("")
    key 'mousedown_4' action NullAction() #action Hide("")
    key 'K_LCTRL' action NullAction() #action Skip("")
    key 'K_RCTRL' action NullAction() #action Skip("")
    key 'K_TAB' action NullAction() #action Hide("")
    key '>' action NullAction() #action Skip("")
    
label gramEasyHints4:
    show screen disable_hide
    $ remainder = gramEasyHints%3
    show eaeng_e4_tile202 at Position(xpos = eae4and1x, xanchor = 0, ypos = eae4and1y, yanchor = 0)onlayer screens
    show eaeng_e4_tile206 at Position(xpos = eae4and2x, xanchor = 0, ypos = eae4and2y, yanchor = 0)onlayer screens
    show eaeng_e4_tile203 at Position(xpos = eae4and3x, xanchor = 0, ypos = eae4and3y, yanchor = 0)onlayer screens
    show eaeng_e4_tile205 at Position(xpos = eae4and4x, xanchor = 0, ypos = eae4and4y, yanchor = 0)onlayer screens
    show eaeng_e4_tile201 at Position(xpos = eae4and5x, xanchor = 0, ypos = eae4and5y, yanchor = 0)onlayer screens
    show eaeng_e4_tile204 at Position(xpos = eae4and6x, xanchor = 0, ypos = eae4and6y, yanchor = 0)onlayer screens
    show other darken onlayer screens
    if (remainder == 0):
        $ gramEasyHints +=1
        a "S can only be substituted by GH. I would try those in the middle row."
        hide other darken onlayer screens
        hide eaeng_e4_tile202 onlayer screens
        hide eaeng_e4_tile206 onlayer screens
        hide eaeng_e4_tile203 onlayer screens
        hide eaeng_e4_tile205 onlayer screens
        hide eaeng_e4_tile201 onlayer screens
        hide eaeng_e4_tile204 onlayer screens
        jump gamefile_e4
    if (remainder==1):
        $ gramEasyHints +=1
        $ hintYes = True
        a "If I were you, Grace, I might try using P, B, R, and K in the bottom row, since the substitutions for those are strings."
        hide other darken onlayer screens
        hide eaeng_e4_tile202 onlayer screens
        hide eaeng_e4_tile206 onlayer screens
        hide eaeng_e4_tile203 onlayer screens
        hide eaeng_e4_tile205 onlayer screens
        hide eaeng_e4_tile201 onlayer screens
        hide eaeng_e4_tile204 onlayer screens
        jump gamefile_e4
    if (remainder==2):
        $ gramEasyHints +=1
        a "If a tile is red, none of the tiles below it will light up. Try to work from the top down, making sure every slot is green."
        hide other darken onlayer screens
        hide eaeng_e4_tile202 onlayer screens
        hide eaeng_e4_tile206 onlayer screens
        hide eaeng_e4_tile203 onlayer screens
        hide eaeng_e4_tile205 onlayer screens
        hide eaeng_e4_tile201 onlayer screens
        hide eaeng_e4_tile204 onlayer screens
        jump gamefile_e4
    $ quick_menu = False
    jump gamefile_e4
    
label gramEasyHints5:
    show screen disable_hide
    $ remainder = gramEasyHint
    show eaeng_e5_tile202 at Position(xpos = eae5and1x, xanchor = 0, ypos = eae5and1y, yanchor = 0) onlayer screens
    show eaeng_e5_tile206 at Position(xpos = eae5and2x, xanchor = 0, ypos = eae5and2y, yanchor = 0)onlayer screens
    show eaeng_e5_tile203 at Position(xpos = eae5and3x, xanchor = 0, ypos = eae5and3y, yanchor = 0)onlayer screens
    show eaeng_e5_tile205 at Position(xpos = eae5and4x, xanchor = 0, ypos = eae5and4y, yanchor = 0)onlayer screens
    show eaeng_e5_tile201 at Position(xpos = eae5and5x, xanchor = 0, ypos = eae5and5y, yanchor = 0)onlayer screens
    show eaeng_e5_tile204 at Position(xpos = eae5and6x, xanchor = 0, ypos = eae5and6y, yanchor = 0)onlayer screens
    show other darken onlayer screens
    if (remainder == 0):
        $ gramEasyHints +=1
        a "K must be substituted by two other letters, which means wherever it goes, it must have two children slots."
        hide other darken onlayer screens
        hide eaeng_e5_tile202 onlayer screens
        hide eaeng_e5_tile206 onlayer screens
        hide eaeng_e5_tile203 onlayer screens
        hide eaeng_e5_tile205 onlayer screens
        hide eaeng_e5_tile201 onlayer screens
        hide eaeng_e5_tile204 onlayer screens
        jump gamefile_e5
    if (remainder==1):
        $ gramEasyHints +=1
        $ hintYes = True
        a "Remember the order of substitution is important. S cannot be substituted by K on the left and J on the right; it has to be JK."
        hide other darken onlayer screens
        hide eaeng_e5_tile202 onlayer screens
        hide eaeng_e5_tile206 onlayer screens
        hide eaeng_e5_tile203 onlayer screens
        hide eaeng_e5_tile205 onlayer screens
        hide eaeng_e5_tile201 onlayer screens
        hide eaeng_e5_tile204 onlayer screens
        jump gamefile_e5
    if (remainder==2):
        $ gramEasyHints +=1
        a "If a tile is not lighting up, make sure its parent, or the tile above it, is green, and that the other part of the substitution is also filled."
        hide other darken onlayer screens
        hide eaeng_e5_tile202 onlayer screens
        hide eaeng_e5_tile206 onlayer screens
        hide eaeng_e5_tile203 onlayer screens
        hide eaeng_e5_tile205 onlayer screens
        hide eaeng_e5_tile201 onlayer screens
        hide eaeng_e5_tile204 onlayer screens
        jump gamefile_e5
    $ quick_menu = False
    jump gamefile_e5
    
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
    
label gramEasyDone:
    show other darken
    image passwordAccepted = "passwordAccepted.png"
    show passwordAccepted at centerScreen2
    call screen gramEasyDone_scr
    
label gramEasyLose:
    show other darken
    image gramEasyLoseFail = "passwordFail.png"
    show gramEasyLoseFail at centerScreen2
    call screen gramEasyLose_scr
