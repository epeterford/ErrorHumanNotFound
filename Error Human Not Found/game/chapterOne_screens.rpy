label chapterOne_screens:
    
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
            action Jump("adaActualPuzzle1")
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
            idle "arrow.png"
            hover "arrow_hover.png"
            xpos 1340
            ypos 419
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
        if (hiroseSafe_inv == False):
            imagebutton:
                idle "hiroseSafe.png" 
                hover "hiroseSafe_hover.png" 
                xpos 468 
                ypos 570 
                focus_mask True
                action Jump("hiroseSafe_label")
                hover_sound "audio/ENHF_UI_Highlight.ogg"
        if (hiroseOfficeComputer == False):
            imagebutton:
                idle "hiroseOfficialComputer.png" 
                hover "hiroseOfficialComputer_hover.png" 
                xpos 596
                ypos 61 
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
    if talkAdaHiroseOffice_value>0 and hiroseOfficeItems == 3:
        jump wegotthedeets
    call screen hiroseOfficeAction