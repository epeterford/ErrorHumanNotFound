
label logicGate_easyA2:  #logicGate_easyA2
    $config.skipping=None
    $renpy.block_rollback()
    $quick_menu = False
    #loads background
    scene bg Logic_Gate 
    

    #all sections are broken down into their rows
    #the first set of values declares images for the show call
    #the second set show the image at a certain positon
    #row 1
    image ea2tile1 = "g_horizontal.png"
    image ea2tile2 = "g_horizontal.png"
    image ea2tile3 = "g_horizontal.png"
    image ea2tile4 = "g_horizontal.png"
    image ea2tile5 = "g_elbow_bl.png"
    
    show ea2tile1 at Position(xpos = 436, xanchor = 0, ypos = 308, yanchor = 0)
    show ea2tile2 at Position(xpos = 511, xanchor = 0, ypos = 308, yanchor = 0)
    show ea2tile3 at Position(xpos = 586, xanchor = 0, ypos = 308, yanchor = 0)
    show ea2tile4 at Position(xpos = 661, xanchor = 0, ypos = 308, yanchor = 0)
    show ea2tile5 at Position(xpos = 736, xanchor = 0, ypos = 308, yanchor = 0)

    #row 2
    image ea2tile6 = "g_g.png"
    image ea2tile7 = "AND_Gate_blue.png"
    image ea2tile8 = "g_horizontal.png"
    image ea2tile9 = "g_horizontal.png"
    image ea2tile10 = "g_elbow_bl.png"

    show ea2tile6 at Position(xpos = 736, xanchor = 0, ypos = 383, yanchor = 0)
    show ea2tile7 at Position(xpos = 811, xanchor = 0, ypos = 383, yanchor = 0)
    show ea2tile8 at Position(xpos = 886, xanchor = 0, ypos = 383, yanchor = 0)
    show ea2tile9 at Position(xpos = 961, xanchor = 0, ypos = 383, yanchor = 0)
    show ea2tile10 at Position(xpos = 1036, xanchor = 0, ypos = 383, yanchor = 0)
 
    #row 3
    image ea2tile11 = "g_horizontal.png"
    image ea2tile12 = "g_horizontal.png"
    image ea2tile13 = "g_t_down.png"
    image ea2tile14 = "g_horizontal.png"
   
    image eahelpme = "g_elbow_tl.png"
    image ea2tile16 = "g_vertical.png"
    
    show ea2tile11 at Position(xpos = 436, xanchor = 0, ypos = 458, yanchor = 0)
    show ea2tile12 at Position(xpos = 511, xanchor = 0, ypos = 458, yanchor = 0)
    show ea2tile13 at Position(xpos = 586, xanchor = 0, ypos = 458, yanchor = 0)
    show ea2tile14 at Position(xpos = 661, xanchor = 0, ypos = 458, yanchor = 0)
    show eahelpme at Position(xpos = 736, xanchor = 0, ypos = 458, yanchor = 0)
    show ea2tile16 at Position(xpos = 1036, xanchor = 0, ypos = 458, yanchor = 0)
    
    #row 4
    image ea2tile17 = "g_vertical.png"
    image ea2tile18 = "g_vertical.png"
    
    show ea2tile17 at Position(xpos = 586, xanchor = 0, ypos = 533, yanchor = 0)
    show ea2tile18 at Position(xpos = 1036, xanchor = 0, ypos = 533, yanchor = 0)
    
    #row 5
    image ea2tile19 = "g_elbow_tr.png"
    image ea2tile20 = "g_horizontal.png"
    image ea2tile21 = "g_elbow_bl.png"
    image ea2tile22 = "g_r.png"
    image ea2tile28 = "NONE_Gate.png"
    image ea2tile29 = "y_horizontal.png"
    image ea2tile30 = "y_horizontal.png"
    image ea2tile31 = "y_horizontal.png"
    image ea2tile32 = "y_horizontal.png"
    
    show ea2tile19 at Position(xpos = 586, xanchor = 0, ypos = 608, yanchor = 0)
    show ea2tile20 at Position(xpos = 661, xanchor = 0, ypos = 608, yanchor = 0)
    show ea2tile21 at Position(xpos = 736, xanchor = 0, ypos = 608, yanchor = 0)
    show ea2tile22 at Position(xpos = 1036, xanchor = 0, ypos = 608, yanchor = 0)
    show ea2tile28 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
    show ea2tile29 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
    show ea2tile30 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
    show ea2tile31 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
    show ea2tile32 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
    
    #row6
    image ea2tile23 = "g_r.png"
    image ea2tile24 = "AND_Gate_blue.png"
    image ea2tile25 = "r_horizontal.png"
    image ea2tile26 = "r_horizontal.png"
    image ea2tile27 = "r_elbow_tl.png"
    
    show ea2tile23 at Position(xpos = 736, xanchor = 0, ypos = 683, yanchor = 0)
    show ea2tile24 at Position(xpos = 811, xanchor = 0, ypos = 683, yanchor = 0)
    show ea2tile25 at Position(xpos = 886, xanchor = 0, ypos = 683, yanchor = 0)
    show ea2tile26 at Position(xpos = 961, xanchor = 0, ypos = 683, yanchor = 0)
    show ea2tile27 at Position(xpos = 1036, xanchor = 0, ypos = 683, yanchor = 0)
    
    #row7
    image ea2tile34 = "r_horizontal.png"
    image ea2tile35 = "r_horizontal.png"
    image ea2tile36 = "r_horizontal.png"
    image ea2tile37 = "r_horizontal.png"
    image ea2tile38 = "r_elbow_tl.png"
    
    show ea2tile34 at Position(xpos = 436, xanchor = 0, ypos = 758, yanchor = 0)
    show ea2tile35 at Position(xpos = 511, xanchor = 0, ypos = 758, yanchor = 0)
    show ea2tile36 at Position(xpos = 586, xanchor = 0, ypos = 758, yanchor = 0)
    show ea2tile37 at Position(xpos = 661, xanchor = 0, ypos = 758, yanchor = 0)
    show ea2tile38 at Position(xpos = 736, xanchor = 0, ypos = 758, yanchor = 0)
    
    #logicGate_easyA1 and end points
    image logicGate_easyA21 = "light_g_on.png"
    show logicGate_easyA21 at Position(xpos = 238, xanchor = 0, ypos = 308, yanchor = 0)
    image logicGate_easyA22 = "light_g_on.png"
    show logicGate_easyA22 at Position(xpos = 238, xanchor = 0, ypos = 458, yanchor = 0)
    image logicGate_easyA23 = "light_r_on.png"
    show logicGate_easyA23 at Position(xpos = 238, xanchor = 0, ypos = 758, yanchor = 0)
    image end2 = "light_g_off.png"
    show end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
    
    
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
 
    jump gamefileA2
    
    
label gamefileA2:
    
    #calls game screen
    call screen logicGatesEasyA2
    
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
        image ea2tile39 = "g_horizontal.png"
        image ea2tile40 = "g_horizontal.png"
        image ea2tile41 = "g_horizontal.png"
        image ea2tile42 = "g_horizontal.png"
        image ea2end2 = "light_g_on.png"

        #shows tiles
        show ea2tile39 at Position(xpos = 1186, xanchor = 0, ypos = 608, yanchor = 0)
        show ea2tile40 at Position(xpos = 1261, xanchor = 0, ypos = 608, yanchor = 0)
        show ea2tile41 at Position(xpos = 1336, xanchor = 0, ypos = 608, yanchor = 0)
        show ea2tile42 at Position(xpos = 1411, xanchor = 0, ypos = 608, yanchor = 0)
        show ea2end2 at Position(xpos = 1595, xanchor = 0, ypos = 608, yanchor = 0)
        
        
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
        image ea2tile100 = "OR_Gate.png"
        show ea2tile100 at Position(xpos = 1111, xanchor = 0, ypos = 608, yanchor = 0)
        queue sound lgWin
        $ renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_lgEasyAWin
        $ Logic_A_solved = True
        jump nextLGEasy
        #jump logicGate_easyA2

    if attempts == 0:
        jump exploreHiroseOffice
    
    jump gamefileA2
    
#area for dragables
screen logicGatesEasyA2:
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
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 240
        ypos 890
        focus_mask True
        action Jump("LGEasyHintsA2")
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
