label choosePersonal_page:
    if(currentPage_journal==0):
        call screen personalLog_0()
    if(currentPage_journal==1):
       call screen personalLog_1()
    if(currentPage_journal==2):
        call screen personalLog_2()
    if(currentPage_journal==3):
        call screen personalLog_3()
    if(currentPage_journal==4):
        call screen personalLog_4()
    if(currentPage_journal==5):
        call screen personalLog_5()
    if(currentPage_journal==6):
        call screen personalLog_6()
    if(currentPage_journal==7):
        call screen personalLog_7a()
    if(currentPage_journal==8):
        call screen personalLog_7b()
    if(currentPage_journal==9):
        call screen personalLog_8()
    if(currentPage_journal==10):
        call screen personalLog_9()
    if(currentPage_journal==11):
        call screen personalLog_10()
    if(currentPage_journal==12):
        call screen personalLog_11()
    if(currentPage_journal==13):
        call screen personalLog_12()
    if(currentPage_journal==14):
        call screen personalLog_13()
    if(currentPage_journal==15):
        call screen personalLog_14()
    if(currentPage_journal==16):
        call screen personalLog_15()
    if(currentPage_journal==17):
        call screen personalLog_16()

screen notes_0():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
        if(currentPage_notes < pageUnlocked_notes):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_1"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu
    imagebutton: 
        idle "journal_gramEasy_1.png"
        xpos 0
        ypos 0
    use navigation
    
screen notes_1():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_2"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_0"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "journal_gramEasy_2.png"
        xpos 0
        ypos 0
    use navigation 
    
screen notes_2():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_3"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_1"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "journal_lgEasy1.png"
        xpos 0
        ypos 0
    use navigation 
    
screen notes_3():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_4"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_2"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "journal_lgEasy2.png"
        xpos 0
        ypos 0
    use navigation
    
screen notes_4():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_5"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_3"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "journal_llEasy1.png"
        xpos 0
        ypos 0
    use navigation
    
screen notes_5():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_6"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_4"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "journal_llEasy2.png"
        xpos 0
        ypos 0
    use navigation
    
screen notes_6():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_7"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_5"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "journal_binaryEasy.png"
        xpos 0
        ypos 0
    use navigation
    
screen notes_7():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_8"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_6"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "journal_lgMed.png"
        xpos 0
        ypos 0
    use navigation
    
screen notes_8():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_9"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_7"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "journal_binaryMed.png"
        xpos 0
        ypos 0
    use navigation
    
screen notes_9():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_10"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_8"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "journal_llMed.png"
        xpos 0
        ypos 0
    use navigation
    
screen notes_10():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_11"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_9"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "journal_gramMed.png"
        xpos 0
        ypos 0
    use navigation
    
screen notes_11():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_12"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>10):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_10"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "journal_gramHard.png"
        xpos 0
        ypos 0
    use navigation
    
screen notes_12():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_13"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>10):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_11"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(notes_hard1=="LL"):
        imagebutton:
            idle "journal_llHard.png"
            xpos 0
            ypos 0
    if(notes_hard1=="LG"):
        imagebutton:
            idle "journal_lgHard.png"
            xpos 0
            ypos 0
    use navigation
    
screen notes_13():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_14"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>10):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_12"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(notes_hard2=="LL"):
        imagebutton:
            idle "journal_llHard.png"
            xpos 0
            ypos 0
    if(notes_hard2=="LG"):
        imagebutton:
            idle "journal_lgHard.png"
            xpos 0
            ypos 0
    if(notes_hard2=="B"):
        imagebutton:
            idle "journal_binaryHard1.png"
            xpos 0
            ypos 0
    use navigation
    
screen notes_14():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_15"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>10):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_13"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(notes_hard2=="B"):
        imagebutton:
            idle "journal_binaryHard2.png"
            xpos 0
            ypos 0
    if(notes_hard3=="B"):
        imagebutton:
            idle "journal_binaryHard1.png"
            xpos 0
            ypos 0
    use navigation
    
screen notes_15():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes < (pageUnlocked_notes-1)):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("notes_16"), SetVariable("currentPage_notes",currentPage_notes + 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_notes>10):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_14"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(notes_hard2=="B"):
        imagebutton:
            idle "journal_binaryHard3.png"
            xpos 0
            ypos 0
    if(notes_hard3=="B"):
        imagebutton:
            idle "journal_binaryHard2.png"
            xpos 0
            ypos 0
    use navigation
    
screen notes_16():
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
    imagemap:
        ground "graceJournal_notes_idle.png"
        idle "graceJournal_notes_idle.png"
        hover "graceJournal_notes_hover.png"
        
        hotspot(462, 225, 98, 397): 
            action Jump("choosePersonal_page")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
        if(currentPage_notes>10):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("notes_15"), SetVariable("currentPage_notes",currentPage_notes - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(notes_hard3=="LG"):
        imagebutton:
            idle "journal_lgHard.png"
            xpos 0
            ypos 0
    if(notes_hard3=="B"):
        imagebutton:
            idle "journal_binaryHard3.png"
            xpos 0
            ypos 0
    use navigation