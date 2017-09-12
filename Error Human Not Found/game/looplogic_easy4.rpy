label loopLogic_easy4: #loopLogic_easy5
    $config.skipping=None
    $ gate_name= ""
    $ slot_name = ""
    #loads background
    scene bg looplogic_bg
    
    image LLE4tile = "G_end_off.png"
    show LLE4tile at Position(xpos = 196, xanchor = 0, ypos = 435, yanchor = 0)
    
    image LLE4tile1 = "w_horizontal.png"
    show LLE4tile1 at Position(xpos = 295, xanchor = 0, ypos = 468, yanchor = 0)
    image LLE4tile2 = "blank_node.png"
    show LLE4tile2 at Position(xpos = 368, xanchor = 0, ypos = 435, yanchor = 0)
    image LLE4tile3 = "W_vertical.png"
    show LLE4tile3 at Position(xpos = 404, xanchor = 0, ypos = 360, yanchor = 0)
    image LLE4tile4 = "W_corner_RB.png"
    show LLE4tile4 at Position(xpos = 377, xanchor = 0, ypos = 290, yanchor = 0)
    image LLE4tile5 = "W_horizontal.png"
    show LLE4tile5 at Position(xpos = 452, xanchor = 0, ypos = 315, yanchor = 0)
    image LLE4tile20 = "W_horizontal.png"
    show LLE4tile20 at Position(xpos = 527, xanchor = 0, ypos = 315, yanchor = 0)
    image LLE4tile10 = "W_horizontal.png"
    show LLE4tile10 at Position(xpos = 602, xanchor = 0, ypos = 315, yanchor = 0)
    image LLE4tile6 = "start.png"
    show LLE4tile6 at Position(xpos = 677, xanchor = 0, ypos = 285, yanchor = 0)

    image LLE4tile7 = "g_vertical_ll.png"
    show LLE4tile7 at Position(xpos = 677, xanchor = 0, ypos = 387, yanchor = 0)
    image LLE4tile8 = "B_vertical.png"
    show LLE4tile8 at Position(xpos = 745, xanchor = 0, ypos = 387, yanchor = 0)
        
    image LLE4tile0 = "w_vertical.png"
    show LLE4tile0 at Position(xpos = 680, xanchor = 0, ypos = 462, yanchor = 0)
    image LLE4tile11 = "w_vertical.png"
    show LLE4tile11 at Position(xpos = 745, xanchor = 0, ypos = 462, yanchor = 0)

        
    image LLE4tile9 = "W_connect_horizontal.png"
    show LLE4tile9 at Position(xpos = 677, xanchor = 0, ypos = 420, yanchor = 0)
    image LLE4tile13 = "blank_node.png"
    show LLE4tile13 at Position(xpos = 678, xanchor = 0, ypos = 537, yanchor = 0)
    image LLE4tile14 = "w_horizontal.png"
    show LLE4tile14 at Position(xpos = 777, xanchor = 0, ypos = 570, yanchor = 0)
    image LLE4tile15 = "B_end_off.png"
    show LLE4tile15 at Position(xpos = 851, xanchor = 0, ypos = 537, yanchor = 0)
    
    image LLE4tile21 = "W_horizontal.png"
    show LLE4tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
    image LLE4tile12 = "W_corner_RB.png"
    show LLE4tile12 at Position(xpos = 527, xanchor = 0, ypos = 430, yanchor = 0)
    image LLE4tile16 = "W_vertical.png"
    show LLE4tile16 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0)
    image LLE4tile17 = "blank_node.png"
    show LLE4tile17 at Position(xpos = 516, xanchor = 0, ypos =583, yanchor = 0)
    image LLE4tile18 = "W_vertical.png"
    show LLE4tile18 at Position(xpos = 553, xanchor = 0, ypos = 683, yanchor = 0)
    image LLE4tile19 = "G_end_off.png"
    show LLE4tile19 at Position(xpos = 516, xanchor = 0, ypos = 755, yanchor = 0)
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        


    #initial value assignment for dragables
    $ if1x = 1525
    $ if1y = 645
    $ if2x = 1395
    $ if2y = 645
    $ if3x = 1655
    $ if3y = 645

            
    #gate values
    $ gate1x = 368
    $ gate1y = 435
    $ gate2x = 678
    $ gate2y = 537
    $ gate3x = 516
    $ gate3y = 583
   
    # check conditons for locations
    $ if1in1 = False
    $ if1in2 = False
    $ if1in3 = False
    $ if2in1 = False
    $ if2in2 = False
    $ if2in3 = False
    $ if3in1 = False
    $ if3in2 = False
    $ if3in3 = False

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

     
    #attempts for players
    $ attempts = 4
 
    jump Gamefile_lle4
    
    
label Gamefile_lle4:
    $config.skipping=None
    #calls game screen
    call screen LoopLogicE4
    
    #the first logic gate *******************************************************************************
    if gate_name == "G_if_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if2in1 == True:
                $ if2x = 1395
                $ if2y = 645
                $ if2in1 = False
            if if3in1 == True:
                $ if3x = 1655
                $ if3y = 645
                $ if3in1 = False

            #sets values for checks
            $ if1x = gate1x
            $ if1y = gate1y
            $ if1in1 = True
            $ if1in2 = False
            $ if1in3 = False

            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if2in2 == True:
                $ if2x = 1395
                $ if2y = 645
                $ if2in2 = False
            if if3in2 == True:
                $ if3x = 1655
                $ if3y = 645
                $ if3in2 = False
            #sets values for checks
            $ if1x = gate2x
            $ if1y = gate2y
            $ if1in1 = False
            $ if1in2 = True
            $ if1in3 = False

            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if2in3 == True:
                $ if2x = 1395
                $ if2y = 645
                $ if2in3 = False
            if if3in3 == True:
                $ if3x = 1655
                $ if3y = 645
                $ if3in3 = False
            #sets values for checks
            $ if1x = gate3x
            $ if1y = gate3y
            $ if1in1 = False
            $ if1in2 = False
            $ if1in3 = True

            
    #the first logic gate *******************************************************************************
    if gate_name == "B_if_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if1in1 == True:
                $ if1x = 1525
                $ if1y = 645
                $ if1in1 = False
            if if3in1 == True:
                $ if3x = 1655
                $ if3y = 645
                $ if3in1 = False

            #sets values for checks
            $ if2x = gate1x
            $ if2y = gate1y
            $ if2in1 = True
            $ if2in2 = False
            $ if2in3 = False

            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if1in2 == True:
                $ if1x = 1525
                $ if1y = 645
                $ if1in2 = False
            if if3in2 == True:
                $ if3x = 1655
                $ if3y = 645
                $ if3in2 = False
            #sets values for checks
            $ if2x = gate2x
            $ if2y = gate2y
            $ if2in1 = False
            $ if2in2 = True
            $ if2in3 = False

            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if1in3 == True:
                $ if1x = 1525
                $ if1y = 645
                $ if1in3 = False
            if if3in3 == True:
                $ if3x = 1655
                $ if3y = 645
                $ if3in3 = False
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
                $ if2x = 1395
                $ if2y = 645
                $ if2in1 = False
            if if1in1 == True:
                $ if1x = 1525
                $ if1y = 645
                $ if1in1 = False

            #sets values for checks
            $ if3x = gate1x
            $ if3y = gate1y
            $ if3in1 = True
            $ if3in2 = False
            $ if3in3 = False

            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if2in2 == True:
                $ if2x = 1395
                $ if2y = 645
                $ if2in2 = False
            if if1in2 == True:
                $ if1x = 1525
                $ if1y = 645
                $ if1in2 = False
            #sets values for checks
            $ if3x = gate2x
            $ if3y = gate2y
            $ if3in1 = False
            $ if3in2 = True
            $ if3in3 = False

            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if2in3 == True:
                $ if2x = 1395
                $ if2y = 645
                $ if2in3 = False
            if if1in3 == True:
                $ if1x = 1525
                $ if1y = 645
                $ if1in3 = False
            #sets values for checks
            $ if3x = gate3x
            $ if3y = gate3y
            $ if3in1 = False
            $ if3in2 = False
            $ if3in3 = True

            
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
    $llNormal = renpy.random.randint(0,2)
    if (llNormal==0):
        play sound llPipe1
    if (llNormal==1):
        play sound llPipe2
    if (llNormal==2):
        play sound llPipe3
    if if1in1 == True:
        image LLE42tile1 = "g_horizontal_ll.png"
        show LLE42tile1 at Position(xpos = 295, xanchor = 0, ypos = 468, yanchor = 0)
        image LLE42tile = "g_end_on.png"
        show LLE42tile at Position(xpos = 196, xanchor = 0, ypos = 435, yanchor = 0)

        image LLE4tile101 = "g_vertical_ll.png"
        show LLE4tile101 at Position(xpos = 400, xanchor = 0, ypos = 360, yanchor = 0)
        image LLE4tile102 = "W_corner_RB.png"
        show LLE4tile102 at Position(xpos = 377, xanchor = 0, ypos = 290, yanchor = 0)
        image LLE4tile103 = "g_horizontal_ll.png"
        show LLE4tile103 at Position(xpos = 452, xanchor = 0, ypos = 315, yanchor = 0)
        image LLE4tile104 = "g_horizontal_ll.png"
        show LLE4tile104 at Position(xpos = 527, xanchor = 0, ypos = 315, yanchor = 0)
        image LLE4tile105 = "g_horizontal_ll.png"
        show LLE4tile105 at Position(xpos = 602, xanchor = 0, ypos = 315, yanchor = 0)
        if (light1Sound ==0):
            play soundP01 llLightOn1
            $light1Sound +=1
            
    if if1in1 == False:
        hide LLE42tile1
        hide LLE42tile
        hide LLE4tile101
        hide LLE4tile102
        hide LLE4tile103
        hide LLE4tile104
        hide LLE4tile105
        if (light1Sound ==1):
            play soundP01 llLightOff1
            $light1Sound -=1
            
    if if2in1 == True:

        image LLE4tile106 = "B_vertical.png"
        show LLE4tile106 at Position(xpos = 404, xanchor = 0, ypos = 360, yanchor = 0)
        image LLE4tile107 = "W_corner_RB.png"
        show LLE4tile107 at Position(xpos = 377, xanchor = 0, ypos = 290, yanchor = 0)
        image LLE4tile108 = "B_horizontal.png"
        show LLE4tile108 at Position(xpos = 452, xanchor = 0, ypos = 315, yanchor = 0)
        image LLE4tile109 = "B_horizontal.png"
        show LLE4tile109 at Position(xpos = 527, xanchor = 0, ypos = 315, yanchor = 0)
        image LLE4tile110 = "B_horizontal.png"
        show LLE4tile110 at Position(xpos = 602, xanchor = 0, ypos = 315, yanchor = 0)
        image LLE42tile1111 = "B_horizontal.png"
        show LLE42tile1111 at Position(xpos = 295, xanchor = 0, ypos = 468, yanchor = 0)
        
    
    if if2in1 == False:
        hide LLE4tile106
        hide LLE4tile107
        hide LLE4tile108
        hide LLE4tile109
        hide LLE4tile110
        hide LLE42tile1111

    
    if if2in2 == True:
        image LLE41tile0 = "b_vertical.png"
        show LLE41tile0 at Position(xpos = 744, xanchor = 0, ypos = 462, yanchor = 0)
        image LLE41tile14 = "b_horizontal.png"
        show LLE41tile14 at Position(xpos = 777, xanchor = 0, ypos = 569, yanchor = 0)
        image LLE41tile9 = "W_connect_horizontal.png"
        show LLE41tile9 at Position(xpos = 677, xanchor = 0, ypos = 420, yanchor = 0)
        image LLE41tile15 = "b_end_on.png"
        show LLE41tile15 at Position(xpos = 852, xanchor = 0, ypos = 537, yanchor = 0)  
        if (light2Sound ==0):
            play soundP02 llLightOn2
            $light2Sound +=1
            
    if if2in2 == False:
        hide LLE41tile0
        hide LLE41tile14
        hide LLE41tile9
        hide LLE41tile15
        if (light2Sound ==1):
            play soundP02 llLightOff2
            $light2Sound -=1
        
    if if1in2 == True:
        image LLE42tile11 = "g_vertical_ll.png"
        show LLE42tile11 at Position(xpos = 676, xanchor = 0, ypos = 462, yanchor = 0)
        image LLE42tile14 = "g_horizontal_ll.png"
        show LLE42tile14 at Position(xpos = 777, xanchor = 0, ypos = 569, yanchor = 0)
        image LLE42tile9 = "W_connect_horizontal.png"
        show LLE42tile9 at Position(xpos = 677, xanchor = 0, ypos = 420, yanchor = 0)
    if if1in2 == False:
        hide LLE42tile11
        hide LLE42tile14
        hide LLE42tile9
        
    if if1in3 == True:
        if if2in2 == True:            
            image LLE41tile21 = "g_horizontal_ll.png"
            show LLE41tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
            image LLE41tile12 = "W_corner_RB.png"
            show LLE41tile12 at Position(xpos = 527, xanchor = 0, ypos = 430, yanchor = 0)
            image LLE41tile16 = "g_vertical_ll.png"
            show LLE41tile16 at Position(xpos = 550, xanchor = 0, ypos = 508, yanchor = 0)
            image LLE41tile18 = "g_vertical_ll.png"
            show LLE41tile18 at Position(xpos = 550, xanchor = 0, ypos = 683, yanchor = 0) 
            image LLE41tile91 = "g_connect_node.png"
            show LLE41tile91 at Position(xpos = 678, xanchor = 0, ypos = 453, yanchor = 0)
            image LLE42tile19 = "g_end_on.png"
            show LLE42tile19 at Position(xpos = 516, xanchor = 0, ypos = 755, yanchor = 0)
            if (light3Sound ==0):
                play soundP03 llLightOn3
                $light3Sound +=1
    if if1in3 == False:
        hide LLE41tile21
        hide LLE41tile12
        hide LLE41tile16
        hide LLE41tile18
        hide LLE41tile91
        hide LLE42tile19
        if (light3Sound ==1):
            play soundP03 llLightOff3
            $light3Sound -=1
        
    if if2in3 == True:
        if if1in2 == True:            
            image LLE42tile21 = "b_horizontal.png"
            show LLE42tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
            image LLE42tile12 = "W_corner_RB.png"
            show LLE42tile12 at Position(xpos = 527, xanchor = 0, ypos = 430, yanchor = 0)
            image LLE42tile16 = "b_vertical.png"
            show LLE42tile16 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0)
            image LLE42tile18 = "b_vertical.png"
            show LLE42tile18 at Position(xpos = 553, xanchor = 0, ypos = 683, yanchor = 0)
            image LLE42tile92 = "b_connect_pipe.png"
            show LLE42tile92 at Position(xpos = 707, xanchor = 0, ypos = 466, yanchor = 0)
            image LLE42tile91 = "b_connect_node.png"
            show LLE42tile91 at Position(xpos = 745, xanchor = 0, ypos = 453, yanchor = 0)
            image LLE41tile93 = "b_connect_node.png"
            show LLE41tile93 at Position(xpos = 678, xanchor = 0, ypos = 453, yanchor = 0)
    if if2in3 == False or if1in2 == False:
        hide LLE42tile21
        hide LLE42tile12
        hide LLE42tile16
        hide LLE42tile18
        hide LLE42tile92
        hide LLE42tile91
        hide LLE41tile93
            
    if if3in3 == True:
        if if1in2 == True:            
            image LLE431tile21 = "b_horizontal.png"
            show LLE431tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
            image LLE431tile12 = "W_corner_RB.png"
            show LLE431tile12 at Position(xpos = 527, xanchor = 0, ypos = 430, yanchor = 0)
            image LLE431tile16 = "b_vertical.png"
            show LLE431tile16 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0)
            image LLE43tile18 = "b_vertical.png"
            show LLE43tile18 at Position(xpos = 553, xanchor = 0, ypos = 683, yanchor = 0)
            image LLE43tile92 = "b_connect_pipe.png"
            show LLE43tile92 at Position(xpos = 707, xanchor = 0, ypos = 466, yanchor = 0)
            image LLE43tile91 = "b_connect_node.png"
            show LLE43tile91 at Position(xpos = 745, xanchor = 0, ypos = 453, yanchor = 0)
            image LLE43tile93 = "b_connect_node.png"
            show LLE43tile93 at Position(xpos = 678, xanchor = 0, ypos = 453, yanchor = 0)
        if if2in2 == True:
            image LLE432tile21 = "g_horizontal_ll.png"
            show LLE432tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
            image LLE432tile12 = "W_corner_RB.png"
            show LLE432tile12 at Position(xpos = 527, xanchor = 0, ypos = 430, yanchor = 0)
            image LLE432tile16 = "g_vertical_ll.png"
            show LLE432tile16 at Position(xpos = 550, xanchor = 0, ypos = 508, yanchor = 0)
            image LLE432tile18 = "g_vertical_ll.png"
            show LLE432tile18 at Position(xpos = 550, xanchor = 0, ypos = 683, yanchor = 0) 
            image LLE43tile94 = "g_connect_node.png"
            show LLE43tile94 at Position(xpos = 678, xanchor = 0, ypos = 453, yanchor = 0)
            image LLE43tile19 = "g_end_on.png"
            show LLE43tile19 at Position(xpos = 516, xanchor = 0, ypos = 755, yanchor = 0)
            if (light3Sound ==0):
                play soundP03 llLightOn3
                $light3Sound +=1
    if if3in3 == False or if1in2 == False: 
        hide LLE431tile21
        hide LLE431tile12
        hide LLE431tile16
        hide LLE43tile18
        hide LLE43tile92
        hide LLE43tile91
        hide LLE43tile93
        if (light3Sound ==1):
            play soundP03 llLightOff3
            $light3Sound -=1
    if if3in3 == False or if2in2 == False:
        hide LLE432tile21
        hide LLE432tile12
        hide LLE432tile16
        hide LLE432tile18
        hide LLE43tile94
        hide LLE43tile19
        if (light3Sound ==1):
            play soundP03 llLightOff3
            $light3Sound -=1
        
        
#win conditions ********
    if if1in1 == True and if2in2 == True and if3in3 == True:
        image LLE499tile2 = "G_if.png"
        show LLE499tile2 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)

        image LLE499tile13 = "B_if.png"
        show LLE499tile13 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)

        image LLE499tile17 = "G_else.png"
        show LLE499tile17 at Position(xpos = if3x, xanchor = 0, ypos =if3y, yanchor = 0)
        queue sound llWin
        $renpy.pause(1.0)
        hide LLE499tile2
        hide LLE499tile13
        hide LLE4999tile17
        jump llEasyWin

    #$attempts -= 1
    if attempts == 0:
        image LLE4999tile2 = "G_if.png"
        show LLE4999tile2 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
        image LLE4999tile13 = "B_if.png"
        show LLE4999tile13 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
        image LLE4999tile17 = "G_else.png"
        show LLE4999tile17 at Position(xpos = if3x, xanchor = 0, ypos =if3y, yanchor = 0)
        queue sound llLose
        $renpy.pause(1.5)
        $loopLogicEasy_tries +=1
        hide LLE4999tile2
        hide LLE4999tile13
        hide LLE4999tile17
        jump llEasyLose
    
    jump Gamefile_lle4

screen LoopLogicE4:
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
        action Jump("loopLogic_EasyHints4")
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
                drag_name "G_if_gate"
                child "G_if.png"
                droppable False
                dragged gate_dragged
                xpos if1x ypos if1y
            drag:
                drag_name "B_if_gate"
                child "B_if.png"
                droppable False
                dragged gate_dragged
                xpos if2x ypos if2y
            drag:
                drag_name "G_else_gate"
                child "G_else.png"
                droppable False
                dragged gate_dragged
                xpos if3x ypos if3y
                

            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover2.png"
                draggable False
                xpos gate1x-25 ypos gate1y-25
           
            drag:
                drag_name "gate slot two"
                child "cover2.png"
                draggable False
                xpos gate2x-25 ypos gate2y-25
                
            drag:
                drag_name "gate slot three"
                child "cover2.png"
                draggable False
                xpos gate3x-25 ypos gate3y-25