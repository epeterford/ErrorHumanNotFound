screen mmCredits_start:
    tag menu
    imagebutton:
        idle "mmCredits_start.png"
        xpos 0
        ypos 0
    imagebutton:
        idle "arrowR.png"
        hover "arrowR_hover.png"
        xpos 1750
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_0")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    if (main_menu):
        use navigation_mm
    if (not main_menu):
        use navigation
    
screen mmCredits_0:
    tag menu
    imagebutton:
        idle "mmCredits_0.png"
        xpos 0
        ypos 0
    imagebutton:
        idle "arrowL.png"
        hover "arrowL_hover.png"
        xpos 450
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_start")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "arrowR.png"
        hover "arrowR_hover.png"
        xpos 1750
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    if (main_menu):
        use navigation_mm
    if (not main_menu):
        use navigation
    
screen mmCredits_1:
    tag menu
    imagebutton:
        idle "mmCredits_1.png"
        xpos 0
        ypos 0
    imagebutton:
        idle "arrowL.png"
        hover "arrowL_hover.png"
        xpos 450
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_0")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "arrowR.png"
        hover "arrowR_hover.png"
        xpos 1750
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_2")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    if (main_menu):
        use navigation_mm
    if (not main_menu):
        use navigation
    
screen mmCredits_2:
    tag menu
    imagebutton:
        idle "mmCredits_2.png"
        xpos 0
        ypos 0
    imagebutton:
        idle "arrowL.png"
        hover "arrowL_hover.png"
        xpos 450
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "arrowR.png"
        hover "arrowR_hover.png"
        xpos 1750
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_3")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    if (main_menu):
        use navigation_mm
    if (not main_menu):
        use navigation
    
screen mmCredits_3:
    tag menu
    imagebutton:
        idle "mmCredits_3.png"
        xpos 0
        ypos 0
    imagebutton:
        idle "arrowL.png"
        hover "arrowL_hover.png"
        xpos 450
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_2")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "arrowR.png"
        hover "arrowR_hover.png"
        xpos 1750
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_4")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    if (main_menu):
        use navigation_mm
    if (not main_menu):
        use navigation
    
screen mmCredits_4:
    tag menu
    imagebutton:
        idle "mmCredits_4.png"
        xpos 0
        ypos 0
    imagebutton:
        idle "arrowL.png"
        hover "arrowL_hover.png"
        xpos 450
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_3")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "arrowR.png"
        hover "arrowR_hover.png"
        xpos 1750
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_5")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    if (main_menu):
        use navigation_mm
    if (not main_menu):
        use navigation
    
screen mmCredits_5:
    tag menu
    imagebutton:
        idle "mmCredits_5.png"
        xpos 0
        ypos 0
    imagebutton:
        idle "arrowL.png"
        hover "arrowL_hover.png"
        xpos 450
        ypos 423
        focus_mask True
        action ShowMenu("mmCredits_4")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    if (main_menu):
        use navigation_mm
    if (not main_menu):
        use navigation
