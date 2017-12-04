screen database1():
    tag menu
    imagemap:
        ground "database_ground.png"
        idle "database_ground.png"
        hover "database_hover.png"
        hotspot(1811, 791, 83, 133):
            action (ShowMenu("database2"), SetVariable("databasePage", 2))
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
    if persistent.unlockGrace:
        imagebutton:
            idle "buttonsUnlocked_Grace_idle.png" 
            hover "buttonsUnlocked_Grace_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Grace_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockGrace== None:
        imagebutton:
            idle "buttonsLocked_Grace_idle.png" 
            hover "buttonsLocked_Grace_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_1_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockAda:
        imagebutton:
            idle "buttonsUnlocked_Ada_idle.png" 
            hover "buttonsUnlocked_Ada_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Ada_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockAda== None:
        imagebutton:
            idle "buttonsLocked_Ada_idle.png" 
            hover "buttonsLocked_Ada_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_1_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockHirose:
        imagebutton:
            idle "buttonsUnlocked_Hirose_idle.png" 
            hover "buttonsUnlocked_Hirose_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Hirose_unlocked1")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockHirose== None:
        imagebutton:
            idle "buttonsLocked_Hirose_idle.png" 
            hover "buttonsLocked_Hirose_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_1_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockIvan:
        imagebutton:
            idle "buttonsUnlocked_Ivan_idle.png" 
            hover "buttonsUnlocked_Ivan_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Ivan_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockIvan== None:
        imagebutton:
            idle "buttonsLocked_Ivan_idle.png" 
            hover "buttonsLocked_Ivan_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_1_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockBlue:
        imagebutton:
            idle "buttonsUnlocked_Blue_idle.png" 
            hover "buttonsUnlocked_Blue_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Blue_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockBlue== None:
        imagebutton:
            idle "buttonsLocked_Blue_idle.png" 
            hover "buttonsLocked_Blue_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_1_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockAlan:
        imagebutton:
            idle "buttonsUnlocked_Alan_idle.png" 
            hover "buttonsUnlocked_Alan_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Alan_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockAlan== None:
        imagebutton:
            idle "buttonsLocked_Alan_idle.png" 
            hover "buttonsLocked_Alan_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_1_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if (not main_menu):
        use navigation
    if (main_menu):
        use navigation_mm
    
screen database3():
    tag menu
    imagemap:
        ground "database_ground.png"
        idle "database_ground.png"
        hover "database_hover.png"
        hotspot(1811, 924, 83, 131):
            action (ShowMenu("database2"), SetVariable("databasePage", 2))
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
            
    if persistent.unlockAlpha:
        imagebutton:
            idle "buttonsUnlocked_Alpha_idle.png" 
            hover "buttonsUnlocked_Alpha_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Alpha_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockAlpha== None:
        imagebutton:
            idle "buttonsLocked_Alpha_idle.png" 
            hover "buttonsLocked_Alpha_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_3_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockWatson:
        imagebutton:
            idle "buttonsUnlocked_Watson_idle.png" 
            hover "buttonsUnlocked_Watson_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Watson_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockWatson== None:
        imagebutton:
            idle "buttonsLocked_Watson_idle.png" 
            hover "buttonsLocked_Watson_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_3_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockTosh:
        imagebutton:
            idle "buttonsUnlocked_Tosh_idle.png" 
            hover "buttonsUnlocked_Tosh_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Tosh_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockTosh== None:
        imagebutton:
            idle "buttonsLocked_Tosh_idle.png" 
            hover "buttonsLocked_Tosh_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_3_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockMopr:
        imagebutton:
            idle "buttonsUnlocked_Mopr_idle.png" 
            hover "buttonsUnlocked_Mopr_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Mopr_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockMopr== None:
        imagebutton:
            idle "buttonsLocked_Mopr_idle.png" 
            hover "buttonsLocked_Mopr_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_3_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if (not main_menu):
        use navigation
    if (main_menu):
        use navigation_mm
    
screen database2():
    tag menu
    imagemap:
        ground "database_ground.png"
        idle "database_ground.png"
        hover "database_hover.png"
        hotspot(1811, 791, 83, 133):
            action (ShowMenu("database3"),  SetVariable("databasePage", 3))
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
        hotspot(1811, 924, 83, 131):
            action (ShowMenu("database1"), SetVariable("databasePage", 1))
            activate_sound "music/UI/ENHF_UI_Button_v2.ogg" 
            hover_sound "music/UI/mainMenu/ENHF_UI_Highlight.ogg"
            selected_hover_sound "<silence 0.5>" 
            selected_activate_sound "<silence 0.5>"
        
    if persistent.unlockGodel:
        imagebutton:
            idle "buttonsUnlocked_Godel_idle.png" 
            hover "buttonsUnlocked_Godel_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Godel_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockGodel== None:
        imagebutton:
            idle "buttonsLocked_Godel_idle.png" 
            hover "buttonsLocked_Godel_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_2_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockColossus:
        imagebutton:
            idle "buttonsUnlocked_Colossus_idle.png" 
            hover "buttonsUnlocked_Colossus_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Colossus_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockColossus== None:
        imagebutton:
            idle "buttonsLocked_Colossus_idle.png" 
            hover "buttonsLocked_Colossus_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_2_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockLynn:
        imagebutton:
            idle "buttonsUnlocked_Lynn_idle.png" 
            hover "buttonsUnlocked_Lynn_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Lynn_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockLynn== None:
        imagebutton:
            idle "buttonsLocked_Lynn_idle.png" 
            hover "buttonsLocked_Lynn_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_2_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockCray:
        imagebutton:
            idle "buttonsUnlocked_Cray_idle.png" 
            hover "buttonsUnlocked_Cray_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Cray_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockCray== None:
        imagebutton:
            idle "buttonsLocked_Cray_idle.png" 
            hover "buttonsLocked_Cray_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_2_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockNevalinna:
        imagebutton:
            idle "buttonsUnlocked_Nevalinna_idle.png" 
            hover "buttonsUnlocked_Nevalinna_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Nevalinna_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockNevalinna== None:
        imagebutton:
            idle "buttonsLocked_Nevalinna_idle.png" 
            hover "buttonsLocked_Nevalinna_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_2_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
            
    if persistent.unlockKnuth:
        imagebutton:
            idle "buttonsUnlocked_Knuth_idle.png" 
            hover "buttonsUnlocked_Knuth_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_Knuth_unlocked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if persistent.unlockKnuth== None:
        imagebutton:
            idle "buttonsLocked_Knuth_idle.png" 
            hover "buttonsLocked_Knuth_hover.png" 
            xpos 0
            ypos 0
            focus_mask True
            action ShowMenu("database_2_locked")
            hover_sound "audio/ENHF_UI_Button_v2.ogg"
            activate_sound "audio/ENHF_UI_Button_v1.ogg" 
    if (not main_menu):
        use navigation
    if (main_menu):
        use navigation_mm
          
#PAGE 1 SCREENS
screen database_1_locked:
    tag menu
    imagemap:
        ground "databaseLocked.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database1")
screen database_Grace_unlocked:
    tag menu
    imagemap:
        ground "databaseGrace1.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database_Grace_unlocked2")
screen database_Grace_unlocked2:
    tag menu
    imagemap:
        ground "databaseGrace2.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database_Grace_unlocked3")
screen database_Grace_unlocked3:
    tag menu
    imagemap:
        ground "databaseGrace3.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database1")
        
screen database_Ada_unlocked:
    tag menu
    imagemap:
        ground "databaseAda1.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database_Ada_unlocked2")
screen database_Ada_unlocked2:
    tag menu
    imagemap:
        ground "databaseAda2.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database1")
        
screen database_Hirose_unlocked1:
    tag menu
    imagemap:
        ground "databaseHirose_1.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database_Hirose_unlocked2")
screen database_Hirose_unlocked2:
    tag menu
    imagemap:
        ground "databaseHirose_2.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database1")
        
screen database_Ivan_unlocked:
    tag menu
    imagemap:
        ground "databaseIvan_1.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database_Ivan_unlocked2")
screen database_Ivan_unlocked2:
    tag menu
    imagemap:
        ground "databaseIvan_2.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database1")
        
screen database_Blue_unlocked:
    tag menu
    imagemap:
        ground "databaseBlue.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database1")
        
screen database_Alan_unlocked:
    tag menu
    imagemap:
        ground "databaseAlan_1.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database_Alan_unlocked2")
screen database_Alan_unlocked2:
    tag menu
    imagemap:
        ground "databaseAlan_2.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database1")
        
#PAGE 2 SCREENS
screen database_2_locked:
    tag menu
    imagemap:
        ground "databaseLocked.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database2")
screen database_Godel_unlocked:
    tag menu
    imagemap:
        ground "databaseGodel.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database2")
screen database_Cray_unlocked:
    tag menu
    imagemap:
        ground "databaseCray.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database2")
screen database_Colossus_unlocked:
    tag menu
    imagemap:
        ground "databaseColossus.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database2")
screen database_Knuth_unlocked:
    tag menu
    imagemap:
        ground "databaseKnuth.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database2")
screen database_Lynn_unlocked:
    tag menu
    imagemap:
        ground "databaseLynn.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database2")
screen database_Nevalinna_unlocked:
    tag menu
    imagemap:
        ground "databaseNevalinna.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database2")
        
#PAGE 3 SCREENS
screen database_3_locked:
    tag menu
    imagemap:
        ground "databaseLocked.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database3")
screen database_Alpha_unlocked:
    tag menu
    imagemap:
        ground "databaseAlpha.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database3")
screen database_Watson_unlocked:
    tag menu
    imagemap:
        ground "databaseWatson.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database3")
screen database_Tosh_unlocked:
    tag menu
    imagemap:
        ground "databaseTosh.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database3")
screen database_Mopr_unlocked:
    tag menu
    imagemap:
        ground "databaseMopr.png"
        hotspot (0,0, 1920, 1080) action ShowMenu("database3")