screen personalLog_0():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        
#        hotspot (462, 225, 98, 397) action ShowMenu("personalLogs_screen") activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133) action (ShowMenu("personalLog_1"), SetVariable("currentPage_journal",currentPage_journal + 1)) activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
    tag menu
    imagebutton: 
        idle "preGame_entry0.png"
        xpos 0
        ypos 0
    use navigation
    
screen personalLog_1():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133) action (ShowMenu("personalLog_2"), SetVariable("currentPage_journal",currentPage_journal + 1)) activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131) action (ShowMenu("personalLog_0"), SetVariable("currentPage_journal",currentPage_journal - 1)) activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "preGame_entry1.png"
        xpos 0
        ypos 0
    use navigation 
    
screen personalLog_2():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133) action (ShowMenu("personalLog_3"), SetVariable("currentPage_journal",currentPage_journal + 1)) activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131) action (ShowMenu("personalLog_1"), SetVariable("currentPage_journal",currentPage_journal - 1)) activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "preGame_entry2a.png"
        xpos 0
        ypos 0
    use navigation 
    
screen personalLog_3():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133) action (ShowMenu("personalLog_4"), SetVariable("currentPage_journal",currentPage_journal + 1)) activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131) action (ShowMenu("personalLog_2"), SetVariable("currentPage_journal",currentPage_journal - 1)) activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "preGame_entry2b.png"
        xpos 0
        ypos 0
    use navigation 
    
screen personalLog_4():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133) action (ShowMenu("personalLog_5"), SetVariable("currentPage_journal",currentPage_journal + 1)) activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131) action (ShowMenu("personalLog_3"), SetVariable("currentPage_journal",currentPage_journal - 1)) activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "preGame_entry3.png"
        xpos 0
        ypos 0
    use navigation 
    
screen personalLog_5():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133) action (ShowMenu("personalLog_6"), SetVariable("currentPage_journal",currentPage_journal + 1)) activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131) action (ShowMenu("personalLog_4"), SetVariable("currentPage_journal",currentPage_journal - 1)) activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "preGame_entry4a.png"
        xpos 0
        ypos 0
    use navigation 
    
screen personalLog_6():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal) and (journal1==True):
            hotspot (1811, 791, 83, 133) action (ShowMenu("personalLog_7a"), SetVariable("currentPage_journal",currentPage_journal + 1)) activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131) action (ShowMenu("personalLog_5"), SetVariable("currentPage_journal",currentPage_journal - 1)) activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "preGame_entry4b.png"
        xpos 0
        ypos 0
    use navigation 

#END PREGAME JOURNALS
screen personalLog_7a():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133) action (ShowMenu("personalLog_7b"), SetVariable("currentPage_journal",currentPage_journal + 1)) activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131) action (ShowMenu("personalLog_6"), SetVariable("currentPage_journal",currentPage_journal - 1)) activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "gameJournal_1a.png"
        xpos 0
        ypos 0
    use navigation 
    
screen personalLog_7b():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal) and (journal2!=""):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("personalLog_8"), SetVariable("currentPage_journal",currentPage_journal + 1))
                activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("personalLog_7a"), SetVariable("currentPage_journal",currentPage_journal - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "gameJournal_1b.png"
        xpos 0
        ypos 0
    use navigation 
    
screen personalLog_8():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal) and (journal3!=""):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("personalLog_9"), SetVariable("currentPage_journal",currentPage_journal + 1))
                activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("personalLog_7b"), SetVariable("currentPage_journal",currentPage_journal - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(journal2=="S"):
        imagebutton:
            idle "gameJournal_2S.png"
            xpos 0
            ypos 0
    if(journal2=="SbE"):
        imagebutton:
            idle "gameJournal_2SbE.png"
            xpos 0
            ypos 0
    if(journal2=="E"):
        imagebutton:
            idle "gameJournal_2E.png"
            xpos 0
            ypos 0
    use navigation 
    
screen personalLog_9():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133):
                if (journal3=="S"):
                    action (ShowMenu("personalLog_10"), SetVariable("currentPage_journal",currentPage_journal + 1))
                elif ((journal3=="SbE") or (journal3=="E"))and (journal4!=""):
                    action (ShowMenu("personalLog_11"), SetVariable("currentPage_journal",currentPage_journal + 2))
                activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("personalLog_8"), SetVariable("currentPage_journal",currentPage_journal - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(journal3=="S"):
        imagebutton:
            idle "gameJournal_3Sa.png"
            xpos 0
            ypos 0
    if(journal3=="SbE"):
        imagebutton:
            idle "gameJournal_3SbE.png"
            xpos 0
            ypos 0
    if(journal3=="E"):
        imagebutton:
            idle "gameJournal_3E.png"
            xpos 0
            ypos 0
    use navigation 
    
screen personalLog_10():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal) and (journal4!=""):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("personalLog_11"), SetVariable("currentPage_journal",currentPage_journal + 1))
                activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("personalLog_9"), SetVariable("currentPage_journal",currentPage_journal - 1)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    imagebutton:
        idle "gameJournal_3Sb.png"
        xpos 0
        ypos 0
        
screen personalLog_11():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("personalLog_12"), SetVariable("currentPage_journal",currentPage_journal + 1))
                activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131):
                if (journal3=="S"):
                    action (ShowMenu("personalLog_10"), SetVariable("currentPage_journal",currentPage_journal - 1)) 
                elif (journal3=="SbE") or (journal3=="E"):
                    action (ShowMenu("personalLog_9"), SetVariable("currentPage_journal",currentPage_journal - 2)) 
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(journal4=="S"):
        imagebutton:
            idle "gameJournal_4Sa.png"
            xpos 0
            ypos 0
    if(journal4=="SbE"):
        imagebutton:
            idle "gameJournal_4SbEa.png"
            xpos 0
            ypos 0
    if(journal4=="E"):
        imagebutton:
            idle "gameJournal_4Ea.png"
            xpos 0
            ypos 0
    use navigation 
    
screen personalLog_12():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("personalLog_13"), SetVariable("currentPage_journal",currentPage_journal + 1))
                activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("personalLog_11"), SetVariable("currentPage_journal",currentPage_journal - 1))  
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(journal4=="S"):
        imagebutton:
            idle "gameJournal_4Sb.png"
            xpos 0
            ypos 0
    if(journal4=="SbE"):
        imagebutton:
            idle "gameJournal_4SbEb.png"
            xpos 0
            ypos 0
    if(journal4=="E"):
        imagebutton:
            idle "gameJournal_4Eb.png"
            xpos 0
            ypos 0
    use navigation 
    
screen personalLog_13():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("personalLog_14"), SetVariable("currentPage_journal",currentPage_journal + 1))
                activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("personalLog_12"), SetVariable("currentPage_journal",currentPage_journal - 1))  
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(journal5=="S"):
        imagebutton:
            idle "gameJournal_5Sa.png"
            xpos 0
            ypos 0
    if(journal5=="SbE"):
        imagebutton:
            idle "gameJournal_5SbEa.png"
            xpos 0
            ypos 0
    if(journal5=="E"):
        imagebutton:
            idle "gameJournal_5Ea.png"
            xpos 0
            ypos 0
    use navigation 
    
screen personalLog_14():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("personalLog_15"), SetVariable("currentPage_journal",currentPage_journal + 1))
                activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("personalLog_13"), SetVariable("currentPage_journal",currentPage_journal - 1))  
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(journal5=="S"):
        imagebutton:
            idle "gameJournal_5Sb.png"
            xpos 0
            ypos 0
    if(journal5=="SbE"):
        imagebutton:
            idle "gameJournal_5SbEb.png"
            xpos 0
            ypos 0
    if(journal5=="E"):
        imagebutton:
            idle "gameJournal_5Eb.png"
            xpos 0
            ypos 0
    use navigation 
    
screen personalLog_15():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal<pageUnlocked_journal):
            hotspot (1811, 791, 83, 133):
                action (ShowMenu("personalLog_16"), SetVariable("currentPage_journal",currentPage_journal + 1))
                activate_sound "music/UI/ENHF_UI_Menu_Exit.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("personalLog_14"), SetVariable("currentPage_journal",currentPage_journal - 1))  
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(journal6=="S"):
        imagebutton:
            idle "gameJournal_6Sa.png"
            xpos 0
            ypos 0
    if(journal6=="SbE"):
        imagebutton:
            idle "gameJournal_6SbEa.png"
            xpos 0
            ypos 0
    if(journal6=="E"):
        imagebutton:
            idle "gameJournal_6Ea.png"
            xpos 0
            ypos 0
    use navigation 
    
screen personalLog_16():
    imagemap:
        ground "graceJournal_journal_idle.png"
        idle "graceJournal_journal_idle.png"
        hover "graceJournal_journal_hover.png"
        
        hotspot (462, 622, 98, 398) action ShowMenu("notes_screen") activate_sound "music/UI/ENHF_UI_Button_v2.ogg" hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"selected_hover_sound "<silence 0.5>" selected_activate_sound "<silence 0.5>"
        if(currentPage_journal>0):
            hotspot (1811, 924, 83, 131):
                action (ShowMenu("personalLog_15"), SetVariable("currentPage_journal",currentPage_journal - 1))  
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    tag menu 
    if(journal6=="S"):
        imagebutton:
            idle "gameJournal_6Sb.png"
            xpos 0
            ypos 0
    if(journal6=="SbE"):
        imagebutton:
            idle "gameJournal_6SbEb.png"
            xpos 0
            ypos 0
    if(journal6=="E"):
        imagebutton:
            idle "gameJournal_6Eb.png"
            xpos 0
            ypos 0
    imagebutton:
        idle "theEnd_idle.png"
        hover "theEnd_hover.png"
        action Jump("Epilogue")
        xpos 0
        ypos 0
        focus_mask True
        activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
        hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg" 
        selected_hover_sound "<silence 0.5>" 
        selected_activate_sound "<silence 0.5>"
    use navigation
    
label journal15:
    call screen personalLog_15