screen watsonJournal_1_scr:
    imagemap:
        ground "watsonJournal_idle.png"
        idle "watsonJournal_idle.png"
        hover "watsonJournal_hover.png"
        hotspot (1588, 792, 82, 132) action Jump("watsonJournal_2") activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
    imagebutton:
        idle "wj_entry1.png"
        xpos 0
        ypos 0
    if(wj_read==True):
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("wj_return")
        
screen watsonJournal_2_scr:
    imagemap:
        ground "watsonJournal_idle.png"
        idle "watsonJournal_idle.png"
        hover "watsonJournal_hover.png"
        hotspot (1588, 792, 82, 132) action Jump("watsonJournal_3a") activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1588, 924, 82, 130) action Jump("watsonJournal_1") activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
    imagebutton:
        idle "wj_entry2.png"
        xpos 0
        ypos 0
    if(wj_read==True):
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("wj_return")
            
screen watsonJournal_3a_scr:
    imagemap:
        ground "watsonJournal_idle.png"
        idle "watsonJournal_idle.png"
        hover "watsonJournal_hover.png"
        hotspot (1588, 792, 82, 132) action Jump("watsonJournal_3b") activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1588, 924, 82, 130) action Jump("watsonJournal_2") activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
    imagebutton:
        idle "wj_entry3a.png"
        xpos 0
        ypos 0
    if(wj_read==True):
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("wj_return")
        
screen watsonJournal_3b_scr:
    imagemap:
        ground "watsonJournal_idle.png"
        idle "watsonJournal_idle.png"
        hover "watsonJournal_hover.png"
            
        hotspot (1588, 792, 82, 132) action Jump("watsonJournal_4") activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
        hotspot (1588, 924, 82, 130) action Jump("watsonJournal_3a") activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
    imagebutton:
        idle "wj_entry3b.png"
        xpos 0
        ypos 0
    if(wj_read==True):
        imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("wj_return")
        
screen watsonJournal_4_scr:
    imagemap:
        ground "watsonJournal_idle.png"
        idle "watsonJournal_idle.png"
        hover "watsonJournal_hover.png"
        hotspot (1588, 924, 82, 130) action Jump("watsonJournal_3b") activate_sound "music/UI/ENHF_UI_Menu_Enter.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
    imagebutton:
        idle "wj_entry4.png"
        xpos 0
        ypos 0
    imagebutton:
            idle "back.png"
            hover "back_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            action Jump("wj_return")
            
label watsonJournal_1:
    show other darken
    call screen watsonJournal_1_scr
    
label watsonJournal_2:
    show other darken
    call screen watsonJournal_2_scr
    
label watsonJournal_3a:
    show other darken
    call screen watsonJournal_3a_scr

label watsonJournal_3b:
    show other darken
    call screen watsonJournal_3b_scr
    
label watsonJournal_4:
    $wj_read = True
    show other darken
    call screen watsonJournal_4_scr
    
label wj_return:
    if(resume=="S"):
        jump ch5_S_resume
    if(resume=="SbE"):
        jump ch5_SbE_resume
    if(resume=="E"):
        jump ch5_E_resume