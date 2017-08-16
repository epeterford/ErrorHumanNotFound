﻿init:
    image bg looplogic_bg = "LoopLogic_background.png"

label loopLogic_easy5: #loopLogic_easy5
    $config.skipping=None
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    scene bg looplogic_bg
    
    
    image LLE5tile = "B_end_off.png"
    show LLE5tile at Position(xpos = 186, xanchor = 0, ypos = 435, yanchor = 0)
    
    image LLE5tile1 = "w_horizontal.png"
    show LLE5tile1 at Position(xpos = 285, xanchor = 0, ypos = 468, yanchor = 0)
    image LLE5tile2 = "blank_node.png"
    show LLE5tile2 at Position(xpos = 360, xanchor = 0, ypos = 435, yanchor = 0)
    image LLE5tile3 = "W_vertical.png"
    show LLE5tile3 at Position(xpos = 404, xanchor = 0, ypos = 360, yanchor = 0)
    image LLE5tile4 = "W_corner_RB.png"
    show LLE5tile4 at Position(xpos = 377, xanchor = 0, ypos = 285, yanchor = 0)
    image LLE5tile5 = "W_horizontal.png"
    show LLE5tile5 at Position(xpos = 452, xanchor = 0, ypos = 310, yanchor = 0)
    image LLE5tile20 = "W_horizontal.png"
    show LLE5tile20 at Position(xpos = 527, xanchor = 0, ypos = 310, yanchor = 0)
    image LLE5tile10 = "W_horizontal.png"
    show LLE5tile10 at Position(xpos = 602, xanchor = 0, ypos = 310, yanchor = 0)
    image LLE5tile6 = "start.png"
    show LLE5tile6 at Position(xpos = 677, xanchor = 0, ypos = 285, yanchor = 0)

    image LLE5tile7 = "g_vertical_ll.png"
    show LLE5tile7 at Position(xpos = 677, xanchor = 0, ypos = 387, yanchor = 0)
    image LLE5tile8 = "B_vertical.png"
    show LLE5tile8 at Position(xpos = 745, xanchor = 0, ypos = 387, yanchor = 0)
        
    image LLE5tile0 = "w_vertical.png"
    show LLE5tile0 at Position(xpos = 680, xanchor = 0, ypos = 462, yanchor = 0)
    image LLE5tile11 = "w_vertical.png"
    show LLE5tile11 at Position(xpos = 745, xanchor = 0, ypos = 462, yanchor = 0)

        
    image LLE5tile9 = "W_connect_horizontal.png"
    show LLE5tile9 at Position(xpos = 677, xanchor = 0, ypos = 420, yanchor = 0)
    image LLE5tile13 = "blank_node.png"
    show LLE5tile13 at Position(xpos = 677, xanchor = 0, ypos = 537, yanchor = 0)
    image LLE5tile14 = "w_horizontal.png"
    show LLE5tile14 at Position(xpos = 777, xanchor = 0, ypos = 569, yanchor = 0)
    image LLE5tile15 = "G_end_off.png"
    show LLE5tile15 at Position(xpos = 852, xanchor = 0, ypos = 537, yanchor = 0)
    
    image LLE5tile21 = "W_horizontal.png"
    show LLE5tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
    image LLE5tile12 = "W_corner_RB.png"
    show LLE5tile12 at Position(xpos = 527, xanchor = 0, ypos = 430, yanchor = 0)
    image LLE5tile16 = "W_vertical.png"
    show LLE5tile16 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0)
    image LLE5tile17 = "blank_node.png"
    show LLE5tile17 at Position(xpos = 516, xanchor = 0, ypos =583, yanchor = 0)
    image LLE5tile18 = "W_vertical.png"
    show LLE5tile18 at Position(xpos = 549, xanchor = 0, ypos = 683, yanchor = 0)
    image LLE5tile19 = "B_end_off.png"
    show LLE5tile19 at Position(xpos = 516, xanchor = 0, ypos = 755, yanchor = 0)
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
    $ gate1x = 360
    $ gate1y = 435
    $ gate2x = 677
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
 
    jump Gamefile_lle5
    
    
label Gamefile_lle5:
    $config.skipping=None
    #calls game screen
    call screen LoopLogicE5
    
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
    if if2in1 == True:
        image LLE52tile1 = "b_horizontal.png"
        show LLE52tile1 at Position(xpos = 285, xanchor = 0, ypos = 468, yanchor = 0)
        image LLE52tile = "B_end_on.png"
        show LLE52tile at Position(xpos = 186, xanchor = 0, ypos = 435, yanchor = 0)

        image LLE5tile101 = "b_vertical.png"
        show LLE5tile101 at Position(xpos = 404, xanchor = 0, ypos = 360, yanchor = 0)
        image LLE5tile102 = "W_corner_RB.png"
        show LLE5tile102 at Position(xpos = 377, xanchor = 0, ypos = 285, yanchor = 0)
        image LLE5tile103 = "b_horizontal.png"
        show LLE5tile103 at Position(xpos = 452, xanchor = 0, ypos = 310, yanchor = 0)
        image LLE5tile104 = "b_horizontal.png"
        show LLE5tile104 at Position(xpos = 527, xanchor = 0, ypos = 310, yanchor = 0)
        image LLE5tile105 = "b_horizontal.png"
        show LLE5tile105 at Position(xpos = 602, xanchor = 0, ypos = 310, yanchor = 0)
        if (light1Sound ==0):
            play soundP01 llLightOn1
            $light1Sound +=1
            
    if if2in1 == False:
        hide LLE52tile1
        hide LLE52tile
        hide LLE5tile101
        hide LLE5tile102
        hide LLE5tile103
        hide LLE5tile104
        hide LLE5tile105
        if (light1Sound ==1):
            play soundP01 llLightOff1
            $light1Sound -=1
    
    if if1in1 == True:

        image LLE5tile106 = "g_vertical_ll.png"
        show LLE5tile106 at Position(xpos = 400, xanchor = 0, ypos = 360, yanchor = 0)
        image LLE5tile107 = "W_corner_RB.png"
        show LLE5tile107 at Position(xpos = 377, xanchor = 0, ypos = 285, yanchor = 0)
        image LLE5tile108 = "g_horizontal_ll.png"
        show LLE5tile108 at Position(xpos = 452, xanchor = 0, ypos = 310, yanchor = 0)
        image LLE5tile109 = "g_horizontal_ll.png"
        show LLE5tile109 at Position(xpos = 527, xanchor = 0, ypos = 310, yanchor = 0)
        image LLE5tile110 = "g_horizontal_ll.png"
        show LLE5tile110 at Position(xpos = 602, xanchor = 0, ypos = 310, yanchor = 0)

    if if1in1 == False:
        hide LLE5tile106
        hide LLE5tile107
        hide LLE5tile108
        hide LLE5tile109
        hide LLE5tile110
    
    if if1in2 == True:
        image LLE51tile0 = "g_vertical_ll.png"
        show LLE51tile0 at Position(xpos = 676, xanchor = 0, ypos = 462, yanchor = 0)
        image LLE51tile14 = "g_horizontal_ll.png"
        show LLE51tile14 at Position(xpos = 777, xanchor = 0, ypos = 569, yanchor = 0)
        image LLE51tile9 = "W_connect_horizontal.png"
        show LLE51tile9 at Position(xpos = 677, xanchor = 0, ypos = 420, yanchor = 0)
        image LLE51tile15 = "G_end_on.png"
        show LLE51tile15 at Position(xpos = 852, xanchor = 0, ypos = 537, yanchor = 0)  
        if (light2Sound ==0):
            play soundP02 llLightOn2
            $light2Sound +=1
        
    if if1in2 == False:
        hide LLE51tile0
        hide LLE51tile14
        hide LLE51tile9
        hide LLE51tile15
        if (light2Sound ==1):
            play soundP02 llLightOff2
            $light2Sound -=1

    if if2in2 == True:
        image LLE52tile11 = "b_vertical.png"
        show LLE52tile11 at Position(xpos = 744, xanchor = 0, ypos = 462, yanchor = 0)
        #image LLE52tile14 = "b_horizontal.png"
        #show LLE52tile14 at Position(xpos = 777, xanchor = 0, ypos = 569, yanchor = 0)
        image LLE52tile9 = "W_connect_horizontal.png"
        show LLE52tile9 at Position(xpos = 677, xanchor = 0, ypos = 420, yanchor = 0)
        
    if if2in2 == False:
        hide LLE52tile11
        hide LLE52tile14
        hide LLE52tile9
        
    if if1in3 == True:
        if if2in2 == True:            
            image LLE51tile21 = "g_horizontal_ll.png"
            show LLE51tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
            image LLE51tile12 = "W_corner_RB.png"
            show LLE51tile12 at Position(xpos = 527, xanchor = 0, ypos = 433, yanchor = 0)
            image LLE51tile16 = "g_vertical_ll.png"
            show LLE51tile16 at Position(xpos = 552, xanchor = 0, ypos = 508, yanchor = 0)
            image LLE51tile18 = "g_vertical_ll.png"
            show LLE51tile18 at Position(xpos = 549, xanchor = 0, ypos = 683, yanchor = 0) 
            image LLE51tile91 = "g_connect_node.png"
            show LLE51tile91 at Position(xpos = 676, xanchor = 0, ypos = 454, yanchor = 0)
   
    if if1in3 == False:
        hide LLE51tile21
        hide LLE51tile12
        hide LLE51tile16
        hide LLE51tile18
        hide LLE51tile91
        
    if if2in3 == True:
        if if1in2 == True:            
            image LLE52tile21 = "b_horizontal.png"
            show LLE52tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
            image LLE52tile12 = "W_corner_RB.png"
            show LLE52tile12 at Position(xpos = 527, xanchor = 0, ypos = 433, yanchor = 0)
            image LLE52tile16 = "b_vertical.png"
            show LLE52tile16 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0)
            image LLE52tile18 = "b_vertical.png"
            show LLE52tile18 at Position(xpos = 549, xanchor = 0, ypos = 683, yanchor = 0)
            image LLE52tile19 = "B_end_on.png"
            show LLE52tile19 at Position(xpos = 516, xanchor = 0, ypos = 755, yanchor = 0)
            image LLE52tile92 = "b_connect_pipe.png"
            show LLE52tile92 at Position(xpos = 707, xanchor = 0, ypos = 466, yanchor = 0)
            image LLE52tile91 = "b_connect_node.png"
            show LLE52tile91 at Position(xpos = 745, xanchor = 0, ypos = 454, yanchor = 0)
            image LLE51tile93 = "b_connect_node.png"
            show LLE51tile93 at Position(xpos = 676, xanchor = 0, ypos = 454, yanchor = 0)
            if (light3Sound ==1):
                play soundP03 llLightOn3
                $light3Sound +=1


    if if2in3 == False or if1in2 == False:
        hide LLE52tile21
        hide LLE52tile12
        hide LLE52tile16
        hide LLE52tile18
        hide LLE52tile19
        hide LLE52tile92
        hide LLE52tile91
        hide LLE51tile93
        if (light3Sound ==1):
            play soundP03 llLightOff3
            $light3Sound -=1    
            
    if if3in3 == True:
        if if1in2 == True:            
            image LLE531tile21 = "b_horizontal.png"
            show LLE531tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
            image LLE531tile12 = "W_corner_RB.png"
            show LLE531tile12 at Position(xpos = 527, xanchor = 0, ypos = 433, yanchor = 0)
            image LLE531tile16 = "b_vertical.png"
            show LLE531tile16 at Position(xpos = 549, xanchor = 0, ypos = 508, yanchor = 0)
            #image LLE53tile18 = "b_vertical.png"
            #show LLE53tile18 at Position(xpos = 549, xanchor = 0, ypos = 683, yanchor = 0)
            image LLE53tile19 = "B_end_on.png"
            show LLE53tile19 at Position(xpos = 516, xanchor = 0, ypos = 755, yanchor = 0)
            image LLE53tile92 = "b_connect_pipe.png"
            show LLE53tile92 at Position(xpos = 707, xanchor = 0, ypos = 466, yanchor = 0)
            image LLE53tile91 = "b_connect_node.png"
            show LLE53tile91 at Position(xpos = 745, xanchor = 0, ypos = 454, yanchor = 0)
            image LLE53tile93 = "b_connect_node.png"
            show LLE53tile93 at Position(xpos = 676, xanchor = 0, ypos = 454, yanchor = 0)
            if (light3Sound ==1):
                play soundP03 llLightOn3
                $light3Sound +=1
                
        if if2in2 == True:
            image LLE532tile21 = "g_horizontal_ll.png"
            show LLE532tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
            image LLE532tile12 = "W_corner_RB.png"
            show LLE532tile12 at Position(xpos = 527, xanchor = 0, ypos = 433, yanchor = 0)
            image LLE532tile16 = "g_vertical_ll.png"
            show LLE532tile16 at Position(xpos = 549, xanchor = 0, ypos = 508, yanchor = 0)
            image LLE532tile18 = "g_vertical_ll.png"
            show LLE532tile18 at Position(xpos = 549, xanchor = 0, ypos = 683, yanchor = 0) 
            image LLE53tile94 = "g_connect_node.png"
            show LLE53tile94 at Position(xpos = 676, xanchor = 0, ypos = 454, yanchor = 0)
    
    if if3in3 == False or if1in2 == False: 
        hide LLE531tile21
        hide LLE531tile12
        hide LLE531tile16
        hide LLE53tile18
        hide LLE53tile19
        hide LLE53tile92
        hide LLE53tile91
        hide LLE53tile93
        if (light3Sound ==1):
            play soundP03 llLightOff3
            $light3Sound -=1 

    if if3in3 == False or if2in2 == False:
        hide LLE532tile21
        hide LLE532tile12
        hide LLE532tile16
        hide LLE532tile18
        hide LLE53tile94
        
#win conditions ********
    if if1in2 == True and if2in1 == True and if3in3 == True:
        image LLE599tile2 = "G_if.png"
        show LLE599tile2 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)

        image LLE599tile13 = "B_if.png"
        show LLE599tile13 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)

        image LLE599tile17 = "G_else.png"
        show LLE599tile17 at Position(xpos = if3x, xanchor = 0, ypos =if3y, yanchor = 0)
        queue sound llWin
        $renpy.pause(1.0)
        hide LLE599tile2
        hide LLE599tile13
        hide LLE599tile17
        jump llEasyWin

    if attempts == 0:
        show LLE599tile2 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
        show LLE599tile13 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
        show LLE599tile17 at Position(xpos = if3x, xanchor = 0, ypos =if3y, yanchor = 0)
        queue sound llLose
        $renpy.pause(1.5)
        $loopLogicEasy_tries +=1
        hide LLE599tile2
        hide LLE599tile13
        hide LLE599tile17
        jump llEasyLose
    
    jump Gamefile_lle5

screen LoopLogicE5:
    key 'h'action NullAction()# action Hide("")
    key 'K_PAGEUP' action NullAction()# action Hide("")
    key 'repeat_K_PAGEUP' action NullAction()# action Hide("")
    key 'K_AC_BACK' action NullAction()#action Hide("")
    key 'mousedown_4'action NullAction()# action Hide("")
    key 'K_LCTRL' action NullAction()# action Skip("")
    key 'K_RCTRL' action NullAction() #action Skip("")
    key 'K_TAB' action NullAction() #action Hide("")
    key '>' action NullAction() #action Skip("")
    #drags and drop location
    imagebutton:
        idle "hints_idle.png"
        hover "hints_hover.png"
        xpos 1545
        ypos 220
        focus_mask True
        action Jump("loopLogic_EasyHints5")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 1463
        ypos 295
    text "Attempts" xpos 1470 ypos 315 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 1650 ypos 304 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 1665 ypos 313 color "#0060db" font "United Kingdom DEMO.otf" size 27
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