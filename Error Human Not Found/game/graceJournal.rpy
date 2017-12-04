init -2 python:
    date_ref = ""
    time_ref = ""
    loc_ref = ""
    current_journal_page = 0
    unlocked_journal_pages = 3
    
###MAIN JOURNAL SCREEN
screen journal():
    tag menu
    imagemap:
        ground "journal_mm_idle.png"
        idle "journal_mm_idle.png"
        hover "journal_mm_hover.png"
            
        hotspot (600, 145, 1175, 150):
            if(currentPage_journal==0):
                action ShowMenu("personalLog_0")
            if(currentPage_journal==1):
                action ShowMenu("personalLog_1")
            if(currentPage_journal==2):
                action ShowMenu("personalLog_2")
            if(currentPage_journal==3):
                action ShowMenu("personalLog_3")
            if(currentPage_journal==4):
                action ShowMenu("personalLog_4")
            if(currentPage_journal==5):
                action ShowMenu("personalLog_5")
            if(currentPage_journal==6):
                action ShowMenu("personalLog_6")
            if(currentPage_journal==7):
                action ShowMenu("personalLog_7a")
            if(currentPage_journal==8):
                action ShowMenu("personalLog_7b")
            if(currentPage_journal==9):
                action ShowMenu("personalLog_8")
            if(currentPage_journal==10):
                action ShowMenu("personalLog_9")
            if(currentPage_journal==11):
                action ShowMenu("personalLog_10")
            if(currentPage_journal==12):
                action ShowMenu("personalLog_11")
            if(currentPage_journal==13):
                action ShowMenu("personalLog_12")
            if(currentPage_journal==14):
                action ShowMenu("personalLog_13")
            if(currentPage_journal==15):
                action ShowMenu("personalLog_14")
            if(currentPage_journal==16):
                action ShowMenu("personalLog_15")
            if(currentPage_journal==17):
                action ShowMenu("personalLog_16")
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
        if pageUnlocked_notes>0:
            hotspot (600, 500, 1175, 150):
                if(currentPage_notes==0 and not(tutorial_gramEasy)):
                    action ShowMenu("notes_0")
                if(currentPage_notes==1):
                    action ShowMenu("notes_1")
                if(currentPage_notes==2):
                    action ShowMenu("notes_2")
                if(currentPage_notes==3):
                    action ShowMenu("notes_3")
                if(currentPage_notes==4):
                    action ShowMenu("notes_4")
                if(currentPage_notes==5):
                    action ShowMenu("notes_5")
                if(currentPage_notes==6):
                    action ShowMenu("notes_6")
                if(currentPage_notes==7):
                    action ShowMenu("notes_7")
                if(currentPage_notes==8):
                    action ShowMenu("notes_8")
                if(currentPage_notes==9):
                    action ShowMenu("notes_9")
                if(currentPage_notes==10):
                    action ShowMenu("notes_10")
                if(currentPage_notes==11):
                    action ShowMenu("notes_11")
                if(currentPage_notes==12):
                    action ShowMenu("notes_12")
                if(currentPage_notes==13):
                    action ShowMenu("notes_13")
                if(currentPage_notes==14):
                    action ShowMenu("notes_14")
                if(currentPage_notes==15):
                    action ShowMenu("notes_15")
                if(currentPage_notes==16):
                    action ShowMenu("notes_16")
                    
                activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
                hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
                selected_hover_sound "<silence 0.5>" 
                selected_activate_sound "<silence 0.5>"
    use navigation

    