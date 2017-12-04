
label logicGate_easyA3:  #logicGate_easyA3
    $config.skipping=None
    $renpy.block_rollback()
    $quick_menu = False
    #loads background
    scene bg Logic_Gate
    
 #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 1
    image ea3tile1 = "r_horizontal.png"
    image ea3tile2 = "r_horizontal.png"
    image ea3tile3 = "r_horizontal.png"
    image ea3tile4 = "r_horizontal.png"
    image ea3tile5 = "r_elbow_bl.png"
    
    show ea3tile1 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show ea3tile2 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show ea3tile3 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show ea3tile4 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show ea3tile5 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)

    #row 2
    image ea3tile6 = "r_g.png"
    image ea3tile7 = "OR_Gate_blue.png"
    image ea3tile8 = "g_horizontal.png"
    image ea3tile9 = "g_horizontal.png"
    image ea3tile10 = "g_elbow_bl.png"

    show ea3tile6 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show ea3tile7 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show ea3tile8 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show ea3tile9 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show ea3tile10 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
 
    #row 3
    image ea3tile11 = "g_horizontal.png"
    image ea3tile12 = "g_horizontal.png"
    image ea3tile13 = "g_t_down.png"
    image ea3tile14 = "g_horizontal.png"
    image eahelpme = "g_elbow_tl.png"
    image ea3tile16 = "g_vertical.png"
    
    show ea3tile11 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show ea3tile12 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show ea3tile13 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show ea3tile14 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show eahelpme at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show ea3tile16 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4
    image ea3tile17 = "g_vertical.png"
    image ea3tile18 = "g_vertical.png"
    
    show ea3tile17 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show ea3tile18 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5
    image ea3tile19 = "g_elbow_tr.png"
    image ea3tile20 = "g_horizontal.png"
    image ea3tile21 = "g_elbow_bl.png"
    image ea3tile22 = "g_r.png"
    image ea3tile28 = "NONE_Gate.png"
    image ea3tile29 = "y_horizontal.png"
    image ea3tile30 = "y_horizontal.png"
    image ea3tile31 = "y_horizontal.png"
    image ea3tile32 = "y_horizontal.png"
    
    show ea3tile19 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show ea3tile20 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show ea3tile21 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show ea3tile22 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show ea3tile28 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show ea3tile29 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    show ea3tile30 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    show ea3tile31 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
    show ea3tile32 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row6
    image ea3tile23 = "g_r.png"
    image ea3tile24 = "AND_Gate_blue.png"
    image ea3tile25 = "r_horizontal.png"
    image ea3tile26 = "r_horizontal.png"
    image ea3tile27 = "r_elbow_tl.png"
    
    show ea3tile23 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show ea3tile24 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show ea3tile25 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show ea3tile26 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show ea3tile27 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row7
    image ea3tile34 = "r_horizontal.png"
    image ea3tile35 = "r_horizontal.png"
    image ea3tile36 = "r_horizontal.png"
    image ea3tile37 = "r_horizontal.png"
    image ea3tile38 = "r_elbow_tl.png"
    
    show ea3tile34 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show ea3tile35 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show ea3tile36 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show ea3tile37 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show ea3tile38 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    
    #logicGate_easyA1 and end points
    image logicGate_easyA31 = "light_r_on.png"
    show logicGate_easyA31 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image logicGate_easyA32 = "light_g_on.png"
    show logicGate_easyA32 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image logicGate_easyA33 = "light_r_on.png"
    show logicGate_easyA33 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    image end3 = "light_g_off.png"
    show end3 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************



    #initial value assignment for dragables
    $ and1x = 848
    $ and1y = 88
   
    # check conditons for locations
    $ and1in1 = False
   
    #attempts for players
    $ attempts = 3
 
    jump gamefileA3
    
    
label gamefileA3:
    
    #calls game screen
    call screen logicGatesEasyA3
    
    #the first logic gate *******************************************************************************
    if gate_name == "and_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            #sets values for checks
            $ and1x = 1111
            $ and1y = 608
            $ and1in1 = True


#*******************************************
#************image zone********************* 
#*******************************************
    $lgNormal = renpy.random.randint(0,2)
    if (lgNormal==0):
        play sound pipeFlowR
    if (lgNormal==1):
        play sound pipeFlowG
    if (lgNormal==2):
        play sound pipeFlowN
#first slot for and 1
    if and1in1 == True:
        image ea3tile39 = "g_horizontal.png"
        image ea3tile40 = "g_horizontal.png"
        image ea3tile41 = "g_horizontal.png"
        image ea3tile42 = "g_horizontal.png"
        image ea3end2 = "light_g_on.png"

        #shows tiles
        show ea3tile39 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        show ea3tile40 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        show ea3tile41 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show ea3tile42 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        show ea3end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
        
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
        
#win conditions ********
    if and1in1 == True: 
        image ea3tile100 = "OR_Gate.png"
        show ea3tile100 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        queue sound lgWin
        $ renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgEasyAWin
        $ Logic_A_solved = True
        jump nextLGEasy

        
    if attempts == 0:
        "you lose try again"
        jump exploreHiroseOffice
    
    jump gamefileA3
    
#area for dragables
screen logicGatesEasyA3:
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
        action Jump("LGEasyHintsA3")
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
                child "OR_Gate.png"
                droppable False
                dragged gate_dragged
                xpos and1x ypos and1y


            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover.png"
                draggable False
                xpos 1111 ypos 608
