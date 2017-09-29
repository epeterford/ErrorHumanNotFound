
label logicGate_easyA1:
    $quick_menu = False
    $config.skipping=None
    $renpy.block_rollback()
    #loads background
    scene bg Logic_Gate
    
    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 1
    image eatile1 = "r_horizontal.png"
    image eatile2 = "r_horizontal.png"
    image eatile3 = "r_horizontal.png"
    image eatile4 = "r_horizontal.png"
    image eatile5 = "r_elbow_bl.png"
    
    show eatile1 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show eatile2 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show eatile3 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show eatile4 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show eatile5 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)

    #row 2
    image eatile6 = "r_g.png"
    image eatile7 = "OR_Gate_blue.png"
    image eatile8 = "g_horizontal.png"
    image eatile9 = "g_horizontal.png"
    image eatile10 = "g_elbow_bl.png"

    show eatile6 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show eatile7 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show eatile8 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show eatile9 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show eatile10 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
 
    #row 3
    image eatile11 = "g_horizontal.png"
    image eatile12 = "g_horizontal.png"
    image eatile13 = "g_t_down.png"
    image eatile14 = "g_horizontal.png"
   
    image eahelpme = "g_elbow_tl.png"
    image eatile16 = "g_vertical.png"
    
    show eatile11 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show eatile12 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show eatile13 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show eatile14 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show eahelpme at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show eatile16 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4
    image eatile17 = "g_vertical.png"
    image eatile18 = "g_vertical.png"
    
    show eatile17 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show eatile18 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5
    image eatile19 = "g_elbow_tr.png"
    image eatile20 = "g_horizontal.png"
    image eatile21 = "g_elbow_bl.png"
    image eatile22 = "g_g.png"
    image eatile28 = "NONE_Gate.png"
    image eatile29 = "y_horizontal.png"
    image eatile30 = "y_horizontal.png"
    image eatile31 = "y_horizontal.png"
    image eatile32 = "y_horizontal.png"
    
    show eatile19 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show eatile20 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show eatile21 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show eatile22 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show eatile28 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show eatile29 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    show eatile30 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    show eatile31 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
    show eatile32 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row6
    image eatile23 = "g_r.png"
    image eatile24 = "OR_Gate_blue.png"
    image eatile25 = "g_horizontal.png"
    image eatile26 = "g_horizontal.png"
    image eatile27 = "g_elbow_tl.png"
    
    show eatile23 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show eatile24 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show eatile25 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show eatile26 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show eatile27 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row7
    image eatile34 = "r_horizontal.png"
    image eatile35 = "r_horizontal.png"
    image eatile36 = "r_horizontal.png"
    image eatile37 = "r_horizontal.png"
    image eatile38 = "r_elbow_tl.png"
    
    show eatile34 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show eatile35 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show eatile36 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show eatile37 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show eatile38 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    
    #logicGate_easyA1 and end points
    image logicGate_easyA11 = "light_r_on.png"
    show logicGate_easyA11 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image logicGate_easyA12 = "light_g_on.png"
    show logicGate_easyA12 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image logicGate_easyA13 = "light_r_on.png"
    show logicGate_easyA13 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    image lga1end = "light_g_off.png"
    show lga1end at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
    
    #initial value assignment for dragables
    $ and1x = 698
    $ and1y = 88
   
    # check conditons for locations
    $ and1in1 = False
   
    #attempts for players
    $ attempts = 3
 
    jump gamefileA1
    
    
label gamefileA1:
    
    #calls game screen
    call screen logicGatesEasyA1
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #sets values for checks
            $ and1x = 1111
            $ and1y = 608
            $ and1in1 = True
            
    if (temp_slot == "" and temp_gate == "" and slot_name != "null"):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
      
    else:
        if slot_name != "null" and ((temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate)):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name
    
#*******************************************
#************image zone*********************
#*******************************************

#first slot for and 1
    if and1in1 == True:
        play sound pipeFlowG
        image eatile39 = "g_horizontal.png"
        image eatile40 = "g_horizontal.png"
        image eatile41 = "g_horizontal.png"
        image eatile42 = "g_horizontal.png"
        image eaend2 = "light_g_on.png"

        #shows tiles
        show eatile39 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        show eatile40 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        show eatile41 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show eatile42 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        show eaend2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
        
#win conditions ********
    if and1in1 == True: 
        image eatile100 = "AND_Gate.png"
        show eatile100 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        play sound lgWin
        $ renpy.pause(1.0)
        $ Logic_A_solved = True
        jump nextLGEasy
    
    if attempts == 0:
        #"you lose try again"
        jump exploreHiroseOffice
    
    jump gamefileA1
    
screen logicGatesEasyA1:
    key 'h'action NullAction()# action Hide("")
    key 'K_PAGEUP' action NullAction()# action Hide("")
    key 'repeat_K_PAGEUP' action NullAction()# action Hide("")
    key 'K_AC_BACK' action NullAction()#action Hide("")
    key 'mousedown_4'action NullAction()# action Hide("")
    key 'K_LCTRL' action NullAction()# action Skip("")
    key 'K_RCTRL' action NullAction() #action Skip("")
    key 'K_TAB' action NullAction() #action Hide("")
    key '>' action NullAction() #action Skip("")
    $config.skipping=None
    $renpy.block_rollback()
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 240
        ypos 890
        focus_mask True
        action Jump("LGEasyHintsA1")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty.png"
        xpos 1515
        ypos 890
    text "Moves" xpos 1550 ypos 908 color "#0060db" font "United Kingdom DEMO.otf" size 27
    text ": " xpos 1670 ypos 895 color "#0060db" font "Bitter-Bold.otf" size 42
    text "[attempts]" xpos 1705 ypos 908 color "#0060db" font "United Kingdom DEMO.otf" size 27
    #drags and drop location
    draggroup:
            #and gates
            drag:
                drag_name "and_gate"
                child "AND_Gate.png"
                droppable False
                dragged gate_dragged
                xpos and1x ypos and1y


            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover.png"
                draggable False
                xpos 1111 ypos 608
