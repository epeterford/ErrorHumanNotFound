label loopLogic_easy2: #loopLogic_easy5
    $config.skipping=None
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    scene bg looplogic_bg
    
   
    image LLE_2_tile1 = "W_horizontal.png"
    show LLE_2_tile1 at Position(xpos = 279, xanchor = 0, ypos = 251, yanchor = 0)
    image LLE_2_tile2 = "blank_node.png"
    show LLE_2_tile2 at Position(xpos = 180, xanchor = 0, ypos = 220, yanchor = 0)  
    image LLE_2_tile3 = "W_vertical.png"
    show LLE_2_tile3 at Position(xpos = 212, xanchor = 0, ypos = 320, yanchor = 0)
    image LLE_2_tile4 = "B_end_off.png"
    show LLE_2_tile4 at Position(xpos = 180, xanchor = 0, ypos = 397, yanchor = 0)
    image LLE_2_tile5 = "W_vertical.png"
    show LLE_2_tile5 at Position(xpos = 376, xanchor = 0, ypos = 303, yanchor = 0)
    image LLE_2_tile6 = "W_vertical.png"
    show LLE_2_tile6 at Position(xpos = 376, xanchor = 0, ypos = 378, yanchor = 0)
    image LLE_2_tile7 = "W_corner_LB.png"
    show LLE_2_tile7 at Position(xpos = 354, xanchor = 0, ypos = 228, yanchor = 0)

    image LLE_2_tile8 = "B_horizontal.png"
    show LLE_2_tile8 at Position(xpos = 431, xanchor = 0, ypos = 512, yanchor = 0)
    image LLE_2_tile9 = "G_horizontal_ll.png"
    show LLE_2_tile9 at Position(xpos = 446, xanchor = 0, ypos = 450, yanchor = 0)
    image LLE_2_tile10 = "G_horizontal_short.png"
    show LLE_2_tile10 at Position(xpos = 521, xanchor = 0, ypos = 450, yanchor = 0)
    #image LLE_2_tile2 = "blank_node.png"
    #show LLE_2_tile2 at Position(xpos = 336, xanchor = 0, ypos = 458, yanchor = 0)  
    


    
    image LLE_2_tile11 = "B_corner_LB.png"
    show LLE_2_tile11 at Position(xpos = 506, xanchor = 0, ypos = 489, yanchor = 0)
    image LLE_2_tile12 = "G_corner_LB.png"
    show LLE_2_tile12 at Position(xpos = 571, xanchor = 0, ypos = 427, yanchor = 0)
    
    image LLE_2_tile13 = "B_vertical.png"
    show LLE_2_tile13 at Position(xpos = 528, xanchor = 0, ypos = 564, yanchor = 0) 
    image LLE_2_tile14 = "G_vertical_short.png"
    show LLE_2_tile14 at Position(xpos = 592, xanchor = 0, ypos = 502, yanchor = 0)
    image LLE_2_tile15 = "G_vertical_ll.png"
    show LLE_2_tile15 at Position(xpos = 593, xanchor = 0, ypos = 552, yanchor = 0)  
    image LLE_2_tile16 = "W_connect_horizontal.png"
    show LLE_2_tile16 at Position(xpos = 528, xanchor = 0, ypos = 580, yanchor = 0)
    image LLE_2_tile17 = "start.png"
    show LLE_2_tile17 at Position(xpos = 346, xanchor = 0, ypos = 454, yanchor = 0) 
    image LLE_2_tile18 = "W_vertical_short.png"
    show LLE_2_tile18 at Position(xpos = 528, xanchor = 0, ypos = 640, yanchor = 0) 
    image LLE_2_tile19 = "W_vertical_short.png"
    show LLE_2_tile19 at Position(xpos = 594, xanchor = 0, ypos = 640, yanchor = 0) 
    image LLE_2_tile20 = "blank_node.png"
    show LLE_2_tile20 at Position(xpos = 530, xanchor = 0, ypos = 680, yanchor = 0)
    image LLE_2_tile21 = "W_horizontal.png"
    show LLE_2_tile21 at Position(xpos = 455, xanchor = 0, ypos = 715, yanchor = 0)
    image LLE_2_tile22 = "W_horizontal.png"
    show LLE_2_tile22 at Position(xpos = 380, xanchor = 0, ypos = 715, yanchor = 0)
    image LLE_2_tile23 = "B_end_off.png"
    show LLE_2_tile23 at Position(xpos = 310, xanchor = 0, ypos = 680, yanchor = 0)


    image LLE_2_tile24 = "W_horizontal.png"
    show LLE_2_tile24 at Position(xpos = 628, xanchor = 0, ypos = 615, yanchor = 0)
    image LLE_2_tile25 = "W_horizontal.png"
    show LLE_2_tile25 at Position(xpos = 703, xanchor = 0, ypos = 615, yanchor = 0)
    image LLE_2_tile26 = "W_corner_LB.png"
    show LLE_2_tile26 at Position(xpos = 778, xanchor = 0, ypos = 592, yanchor = 0)
    image LLE_2_tile27 = "W_vertical_short.png"
    show LLE_2_tile27 at Position(xpos = 799, xanchor = 0, ypos = 667, yanchor = 0)
    image LLE_2_tile28 = "blank_node.png"
    show LLE_2_tile28 at Position(xpos = 770, xanchor = 0, ypos = 715, yanchor = 0)
    image LLE_2_tile29 = "W_horizontal.png"
    show LLE_2_tile29 at Position(xpos = 870, xanchor = 0, ypos = 745, yanchor = 0)
    image LLE_2_tile30 = "W_horizontal.png"
    show LLE_2_tile30 at Position(xpos = 945, xanchor = 0, ypos = 745, yanchor = 0)
    image LLE_2_tile31 = "G_end_off.png"
    show LLE_2_tile31 at Position(xpos = 1020, xanchor = 0, ypos = 715, yanchor = 0)

        
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        


    #initial value assignment for dragables
    $ if1x = 1445
    $ if1y = 645
    
    $ else1x = 1625
    $ else1y = 645
    
    $ if2x = 1445
    $ if2y = 645
            
    #gate values
    $ gate1x = 182
    $ gate1y = 220
    $ gate2x = 530
    $ gate2y = 680
    $ gate3x = 770
    $ gate3y = 715
   
    # check conditons for locations
    $ if1in1 = False
    $ if1in2 = False
    $ if1in3 = False

    $ if2in1 = False
    $ if2in2 = False
    $ if2in3 = False

    $ else1in1 = False
    $ else1in2 = False
    $ else1in3 = False

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

     
    #attempts for players
    $ attempts = 4
 
    jump gamefile_lle2
    
    
label gamefile_lle2:
    $config.skipping=None
    #calls game screen
    call screen loopLogic_easy2Scr
    



#*******************************************
#************image zone********************* 
#*******************************************

    #the first logic gate *******************************************************************************
    if gate_name == "B_if_gate1":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if2in1 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in1 = False

            #sets values for checks
            $ if1x = gate1x
            $ if1y = gate1y
            $ if1in1 = True
            $ if1in2 = False
            $ if1in3 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if2in2 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in2 = False
            #sets values for checks
            $ if1x = gate2x
            $ if1y = gate2y
            $ if1in1 = False
            $ if1in2 = True
            $ if1in3 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if2in3 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in3 = False
            #sets values for checks
            $ if1x = gate3x
            $ if1y = gate3y
            $ if1in1 = False
            $ if1in2 = False
            $ if1in3 = True
            
    #the first logic gate *******************************************************************************
    if gate_name == "B_if_gate2":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if1in1 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in1 = False

            #sets values for checks
            $ if2x = gate1x
            $ if2y = gate1y
            $ if2in1 = True
            $ if2in2 = False
            $ if2in3 = False
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if1in2 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in2 = False
            #sets values for checks
            $ if2x = gate2x
            $ if2y = gate2y
            $ if2in1 = False
            $ if2in2 = True
            $ if2in3 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if1in3 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 645
                $ else1in3 = False
            #sets values for checks
            $ if2x = gate3x
            $ if2y = gate3y
            $ if2in1 = False
            $ if2in2 = False
            $ if2in3 = True
            
    #the third logic gate *******************************************************************************
    if gate_name == "G_else_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if2in1 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in1 = False
            if if1in1 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in1 = False

            #sets values for checks
            $ else1x = gate1x
            $ else1y = gate1y
            $ else1in1 = True
            $ else1in2 = False
            $ else1in3 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if2in2 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in2 = False
            if if1in2 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in2 = False
            #sets values for checks
            $ else1x = gate2x
            $ else1y = gate2y
            $ else1in1 = False
            $ else1in2 = True
            $ else1in3 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if2in3 == True:
                $ if2x = 1445
                $ if2y = 645
                $ if2in3 = False
            if if1in3 == True:
                $ if1x = 1445
                $ if1y = 645
                $ if1in3 = False
            #sets values for checks
            $ else1x = gate3x
            $ else1y = gate3y
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = True

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

#    #if 1 section*******************************************************************************************     
    if if1in2 == True or if2in2 == True:
        image LLE_2_tile34 = "B_vertical_short.png"
        show LLE_2_tile34 at Position(xpos = 528, xanchor = 0, ypos = 640, yanchor = 0)
        image LLE_2_tile35 = "B_horizontal.png"
        show LLE_2_tile35 at Position(xpos = 455, xanchor = 0, ypos = 715, yanchor = 0)
        image LLE_2_tile36 = "B_horizontal.png"
        show LLE_2_tile36 at Position(xpos = 380, xanchor = 0, ypos = 715, yanchor = 0)
        image LLE_2_tile37 = "B_end_on.png"
        show LLE_2_tile37 at Position(xpos = 310, xanchor = 0, ypos = 680, yanchor = 0)
        
        if else1in3 == True:
            image LLE_2_tile38 = "G_connect_node.png"
            show LLE_2_tile38 at Position(xpos = 595, xanchor = 0, ypos = 615, yanchor = 0)
            #show LLE_2_tile38 at Position(xpos = 594, xanchor = 0, ypos = 640, yanchor = 0)
            image LLE_2_tile39 = "G_horizontal_ll.png"
            show LLE_2_tile39 at Position(xpos = 628, xanchor = 0, ypos = 615, yanchor = 0)
            image LLE_2_tile40 = "G_horizontal_ll.png"
            show LLE_2_tile40 at Position(xpos = 703, xanchor = 0, ypos = 615, yanchor = 0)
            image LLE_2_tile41 = "G_corner_LB.png"
            show LLE_2_tile41 at Position(xpos = 778, xanchor = 0, ypos = 592, yanchor = 0)
            image LLE_2_tile42 = "G_vertical_short.png"
            show LLE_2_tile42 at Position(xpos = 799, xanchor = 0, ypos = 667, yanchor = 0)
            image LLE_2_tile43 = "G_horizontal_ll.png"
            show LLE_2_tile43 at Position(xpos = 870, xanchor = 0, ypos = 745, yanchor = 0)
            image LLE_2_tile44 = "G_horizontal_ll.png"
            show LLE_2_tile44 at Position(xpos = 945, xanchor = 0, ypos = 745, yanchor = 0)
            image LLE_2_tile45 = "G_end_on.png"
            show LLE_2_tile45 at Position(xpos = 1020, xanchor = 0, ypos = 715, yanchor = 0)

        if else1in3 == False:
            hide LLE_2_tile38
            hide LLE_2_tile39
            hide LLE_2_tile40
            hide LLE_2_tile41
            hide LLE_2_tile42
            hide LLE_2_tile43
            hide LLE_2_tile44
            hide LLE_2_tile45
   
    if if1in2 == False and if2in2 == False:
        hide LLE_2_tile34
        hide LLE_2_tile35
        hide LLE_2_tile36
        hide LLE_2_tile37
        hide LLE_2_tile38
        hide LLE_2_tile39
        hide LLE_2_tile40
        hide LLE_2_tile41
        hide LLE_2_tile42
        hide LLE_2_tile43
        hide LLE_2_tile44
        hide LLE_2_tile45


    if if2in1 == True or if1in1 == True:
        image LLE_2_tile46 = "B_vertical.png"
        show LLE_2_tile46 at Position(xpos = 212, xanchor = 0, ypos = 320, yanchor = 0)
        image LLE_2_tile47 = "B_end_on.png"
        show LLE_2_tile47 at Position(xpos = 180, xanchor = 0, ypos = 397, yanchor = 0)

        image LLE_2_tile48B = "B_horizontal.png"
        show LLE_2_tile48B at Position(xpos = 279, xanchor = 0, ypos = 251, yanchor = 0)
        image LLE_2_tile49B = "B_vertical.png"
        show LLE_2_tile49B at Position(xpos = 376, xanchor = 0, ypos = 303, yanchor = 0)
        image LLE_2_tile50B = "B_vertical.png"
        show LLE_2_tile50B at Position(xpos = 376, xanchor = 0, ypos = 378, yanchor = 0)
        image LLE_2_tile51B = "B_corner_LB.png"
        show LLE_2_tile51B at Position(xpos = 354, xanchor = 0, ypos = 228, yanchor = 0)
        
    if if2in1 == False and if1in1 == False:
        hide LLE_2_tile46B
        hide LLE_2_tile47B
        hide LLE_2_tile48B
        hide LLE_2_tile49B
        hide LLE_2_tile50B
        hide LLE_2_tile51B
        
#win conditions ********
    if (if1in2 == True or if2in2 == True) and else1in3 == True and (if2in1 == True or if1in1 == True):
        image LLE_2_tile48 = "B_end_on.png"
        show LLE_2_tile48 at Position(xpos = 310, xanchor = 0, ypos = 680, yanchor = 0)
        image LLE_2_tile49 = "G_end_on.png"
        show LLE_2_tile49 at Position(xpos = 1020, xanchor = 0, ypos = 715, yanchor = 0)
        image LLE_2_tile50 = "B_end_on.png"
        show LLE_2_tile50 at Position(xpos = 180, xanchor = 0, ypos = 397, yanchor = 0)
        image LLE_2_tile51 = "B_if.png"
        show LLE_2_tile51 at Position(xpos = 180, xanchor = 0, ypos = 220, yanchor = 0)
        image LLE_2_tile52 = "B_if.png"
        show LLE_2_tile52 at Position(xpos = 530, xanchor = 0, ypos = 680, yanchor = 0)
        image LLE_2_tile53 = "G_else.png"
        show LLE_2_tile53 at Position(xpos = 770, xanchor = 0, ypos = 715, yanchor = 0)

        "game"
        jump balcony_alpha

    if attempts == 0:
        show LLE_2_tile51 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
        show LLE_2_tile52 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
        show LLE_2_tile53 at Position(xpos = else1x, xanchor = 0, ypos =else1y, yanchor = 0)
        "you lose try again"
        jump balcony_alpha
    
    jump gamefile_lle2

screen loopLogic_easy2Scr:
    key 'h'action NullAction()# action Hide("")
    key 'K_PAGEUP' action NullAction()# action Hide("")
    key 'repeat_K_PAGEUP' action NullAction()# action Hide("")
    key 'K_AC_BACK' action NullAction()#action Hide("")
    key 'mousedown_4'action NullAction()# action Hide("")
    key 'K_LCTRL' action NullAction()# action Skip("")
    key 'K_RCTRL' action NullAction() #action Skip("")
    key 'K_TAB' action NullAction() #action Hide("")
    key '>' action NullAction() #action Skip("")
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 1545
        ypos 220
        focus_mask True
        action Jump("loopLogic_EasyHints2")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 1463
        ypos 295
    text "Attempts" xpos 1470 ypos 315 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 1650 ypos 304 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 1665 ypos 313 color "#0060db" font "United Kingdom DEMO.otf" size 27
    #drags and drop location
    draggroup:
            #if gates
            drag:
                drag_name "B_if_gate1"
                child "B_if.png"
                droppable False
                dragged gate_dragged
                xpos if1x ypos if1y
            drag:
                drag_name "B_if_gate2"
                child "B_if.png"
                droppable False
                dragged gate_dragged
                xpos if2x ypos if2y  
            #else gate
            drag:
                drag_name "G_else_gate"
                child "G_else.png"
                droppable False
                dragged gate_dragged
                xpos else1x ypos else1y

            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover.png"
                draggable False
                xpos gate1x ypos gate1y
           
            drag:
                drag_name "gate slot two"
                child "cover.png"
                draggable False
                xpos gate2x ypos gate2y
                
            drag:
                drag_name "gate slot three"
                child "cover.png"
                draggable False
                xpos gate3x ypos gate3y

