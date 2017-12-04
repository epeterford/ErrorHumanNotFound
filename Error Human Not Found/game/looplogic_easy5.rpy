init:
    image bg looplogic_bg = "LoopLogic_background.png"

label loopLogic_easy5: #loopLogic_easy5
    $config.skipping=None
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    scene bg looplogic_bg
    
    
    image LLE5_tile = "B_end_off.png"
    show LLE5_tile at Position(xpos = 196, xanchor = 0, ypos = 435, yanchor = 0)
    
    image LLE5_tile1 = "w_horizontal.png"
    show LLE5_tile1 at Position(xpos = 295, xanchor = 0, ypos = 468, yanchor = 0)
    image LLE5_tile2 = "blank_node.png"
    show LLE5_tile2 at Position(xpos = 368, xanchor = 0, ypos = 435, yanchor = 0)
    image LLE5_tile3 = "W_vertical.png"
    show LLE5_tile3 at Position(xpos = 404, xanchor = 0, ypos = 360, yanchor = 0)
    image LLE5_tile4 = "W_corner_RB.png"
    show LLE5_tile4 at Position(xpos = 377, xanchor = 0, ypos = 290, yanchor = 0)
    image LLE5_tile5 = "W_horizontal.png"
    show LLE5_tile5 at Position(xpos = 452, xanchor = 0, ypos = 315, yanchor = 0)
    image LLE5_tile20 = "W_horizontal.png"
    show LLE5_tile20 at Position(xpos = 527, xanchor = 0, ypos = 315, yanchor = 0)
    image LLE5_tile10 = "W_horizontal.png"
    show LLE5_tile10 at Position(xpos = 602, xanchor = 0, ypos = 315, yanchor = 0)
    image LLE5_tile6 = "start.png"
    show LLE5_tile6 at Position(xpos = 677, xanchor = 0, ypos = 285, yanchor = 0)

    image LLE5_tile7 = "g_vertical_ll.png"
    show LLE5_tile7 at Position(xpos = 677, xanchor = 0, ypos = 387, yanchor = 0)
    image LLE5_tile8 = "B_vertical.png"
    show LLE5_tile8 at Position(xpos = 745, xanchor = 0, ypos = 387, yanchor = 0)
        
    image LLE5_tile0 = "w_vertical.png"
    show LLE5_tile0 at Position(xpos = 680, xanchor = 0, ypos = 462, yanchor = 0)
    image LLE5_tile11 = "w_vertical.png"
    show LLE5_tile11 at Position(xpos = 745, xanchor = 0, ypos = 462, yanchor = 0)

        
    image LLE5_tile9 = "W_connect_horizontal.png"
    show LLE5_tile9 at Position(xpos = 677, xanchor = 0, ypos = 420, yanchor = 0)
    image LLE5_tile13 = "blank_node.png"
    show LLE5_tile13 at Position(xpos = 678, xanchor = 0, ypos = 537, yanchor = 0)
    image LLE5_tile14 = "w_horizontal.png"
    show LLE5_tile14 at Position(xpos = 777, xanchor = 0, ypos = 570, yanchor = 0)
    image LLE5_tile15 = "G_end_off.png"
    show LLE5_tile15 at Position(xpos = 851, xanchor = 0, ypos = 537, yanchor = 0)
    
    image LLE5_tile21 = "W_horizontal.png"
    show LLE5_tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
    image LLE5_tile12 = "W_corner_RB.png"
    show LLE5_tile12 at Position(xpos = 527, xanchor = 0, ypos = 430, yanchor = 0)
    image LLE5_tile16 = "W_vertical.png"
    show LLE5_tile16 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0)
    image LLE5_tile17 = "blank_node.png"
    show LLE5_tile17 at Position(xpos = 516, xanchor = 0, ypos =583, yanchor = 0)
    image LLE5_tile18 = "W_vertical.png"
    show LLE5_tile18 at Position(xpos = 553, xanchor = 0, ypos = 683, yanchor = 0)
    image LLE5_tile19 = "B_end_off.png"
    show LLE5_tile19 at Position(xpos = 516, xanchor = 0, ypos = 755, yanchor = 0)
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        


    #initial value assignment for dragables
    $ if1x = 1525
    $ if1y = 645
    $ if2x = 1395
    $ if2y = 645
    $ else3x = 1655
    $ else3y = 645

            
    #gate values
    $ gate1x = 368
    $ gate1y = 435
    $ gate2x = 678
    $ gate2y = 537
    $ gate3x = 516
    $ gate3y = 583

    image LLE_5_ifBT = "B_if_idle.png"
    image LLE_5_ifGT = "G_if_idle.png"
    image LLE_5_elseT = "G_else_idle.png"
    show LLE_5_ifGT at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLE_5_ifBT at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
    show LLE_5_elseT at Position(xpos = else3x, xanchor = 0, ypos = else3y, yanchor = 0)
   
    # check conditons for locations
    $ if1in1 = False
    $ if1in2 = False
    $ if1in3 = False
    $ if2in1 = False
    $ if2in2 = False
    $ if2in3 = False
    $ else3in1 = False
    $ else3in2 = False
    $ else3in3 = False

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""

     
    #attempts for players
    $ attempts = 4
 
    jump gamefile_lle5
    
    
label gamefile_lle5:
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
            if else3in1 == True:
                $ else3x = 1655
                $ else3y = 645
                $ else3in1 = False

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
            if else3in2 == True:
                $ else3x = 1655
                $ else3y = 645
                $ else3in2 = False
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
            if else3in3 == True:
                $ else3x = 1655
                $ else3y = 645
                $ else3in3 = False
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
            if else3in1 == True:
                $ else3x = 1655
                $ else3y = 645
                $ else3in1 = False

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
            if else3in2 == True:
                $ else3x = 1655
                $ else3y = 645
                $ else3in2 = False
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
            if else3in3 == True:
                $ else3x = 1655
                $ else3y = 645
                $ else3in3 = False
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
            $ else3x = gate1x
            $ else3y = gate1y
            $ else3in1 = True
            $ else3in2 = False
            $ else3in3 = False
            
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
            $ else3x = gate2x
            $ else3y = gate2y
            $ else3in1 = False
            $ else3in2 = True
            $ else3in3 = False
            
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
            $ else3x = gate3x
            $ else3y = gate3y
            $ else3in1 = False
            $ else3in2 = False
            $ else3in3 = True

    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not (slot_name == "G_if_gate_return" or slot_name == "B_if_gate_return" or slot_name == "G_else_gate_return")):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
      
    else:
        if slot_name != "null" and (temp_slot != slot_name or gate_name != temp_gate):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name

            if slot_name == "B_if_gate_return":
                $ attempts +=1
                if gate_name == "B_if_gate":
                    $ if2x = 1395
                    $ if2y = 645
                    $ if2in1 = False
                    $ if2in2 = False
                    $ if2in3 = False
            if slot_name == "G_if_gate_return":
                $ attempts +=1
                if gate_name == "G_if_gate":
                    $ if1x = 1525
                    $ if1y = 645
                    $ if1in1 = False
                    $ if1in2 = False
                    $ if1in3 = False
            if slot_name == "G_else_gate_return":
                $ attempts +=1
                if gate_name == "G_else_gate":
                    $ else3x = 1655
                    $ else3y = 645
                    $ else3in1 = False
                    $ else3in2 = False
                    $ else3in3 = False


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
    hide LLE5_2tile1
    hide LLE5_2tile
    hide LLE5_tile101
    hide LLE5_tile102
    hide LLE5_tile103
    hide LLE5_tile104
    hide LLE5_tile105
    hide LLE5_tile106
    hide LLE5_tile107
    hide LLE5_tile108
    hide LLE5_tile109
    hide LLE5_tile110
    hide LLE5_2tile1111
    hide LLE5_1tile0
    hide LLE5_1tile14
    hide LLE5_1tile9
    hide LLE5_1tile15
    hide LLE5_2tile11
    hide LLE5_2tile14
    hide LLE5_2tile9
    hide LLE5_1tile21
    hide LLE5_1tile12
    hide LLE5_1tile16
    hide LLE5_1tile18
    hide LLE5_1tile91
    hide LLE5_1tile93
    hide LLE5_2tile19
    hide LLE5_2tile92
    hide LLE5_32tile21
    hide LLE5_32tile12
    hide LLE5_32tile16
    hide LLE5_32tile18
    hide LLE5_31tile21
    hide LLE5_31tile12
    hide LLE5_31tile16
    hide LLE5_3tile19
    hide LLE5_3tile18
    hide LLE5_3tile92
    hide LLE5_3tile91
    hide LLE5_3tile93
    hide LLE5_3tile94
    hide LLE5_2tile21
    hide LLE5_2tile12
    hide LLE5_2tile16
    hide LLE5_2tile18
    hide LLE5_2tile19
    hide LLE5_2tile92
    hide LLE5_2tile91
    hide LLE5_31tile21
    hide LLE5_31tile12
    hide LLE5_31tile16


    if if2in1 == True:
        image LLE5_2tile1 = "b_horizontal.png"
        show LLE5_2tile1 at Position(xpos = 295, xanchor = 0, ypos = 468, yanchor = 0)
        image LLE5_2tile = "B_end_on.png"
        show LLE5_2tile at Position(xpos = 196, xanchor = 0, ypos = 435, yanchor = 0)

        image LLE5_tile101 = "b_vertical.png"
        show LLE5_tile101 at Position(xpos = 404, xanchor = 0, ypos = 360, yanchor = 0)
        image LLE5_tile102 = "W_corner_RB.png"
        show LLE5_tile102 at Position(xpos = 377, xanchor = 0, ypos = 290, yanchor = 0)
        image LLE5_tile103 = "b_horizontal.png"
        show LLE5_tile103 at Position(xpos = 452, xanchor = 0, ypos = 315, yanchor = 0)
        image LLE5_tile104 = "b_horizontal.png"
        show LLE5_tile104 at Position(xpos = 527, xanchor = 0, ypos = 315, yanchor = 0)
        image LLE5_tile105 = "b_horizontal.png"
        show LLE5_tile105 at Position(xpos = 602, xanchor = 0, ypos = 315, yanchor = 0)
        if (light1Sound ==0):
            play soundP01 llLightOn1
            $light1Sound +=1
            
    if if2in1 == False:
        if (light1Sound ==1):
            play soundP01 llLightOff1
            $light1Sound -=1
    
    if if1in1:
        image LLE5_tile106 = "g_vertical_ll.png"
        show LLE5_tile106 at Position(xpos = 400, xanchor = 0, ypos = 360, yanchor = 0)
        image LLE5_tile107 = "W_corner_RB.png"
        show LLE5_tile107 at Position(xpos = 377, xanchor = 0, ypos = 290, yanchor = 0)
        image LLE5_tile108 = "g_horizontal_ll.png"
        show LLE5_tile108 at Position(xpos = 452, xanchor = 0, ypos = 315, yanchor = 0)
        image LLE5_tile109 = "g_horizontal_ll.png"
        show LLE5_tile109 at Position(xpos = 527, xanchor = 0, ypos = 315, yanchor = 0)
        image LLE5_tile110 = "g_horizontal_ll.png"
        show LLE5_tile110 at Position(xpos = 602, xanchor = 0, ypos = 315, yanchor = 0)
        image LLE5_2tile1111 = "G_horizontal_ll.png"
        show LLE5_2tile1111 at Position(xpos = 295, xanchor = 0, ypos = 468, yanchor = 0)
    
    if if1in2:
        image LLE5_1tile0 = "g_vertical_ll.png"
        show LLE5_1tile0 at Position(xpos = 676, xanchor = 0, ypos = 462, yanchor = 0)
        image LLE5_1tile14 = "g_horizontal_ll.png"
        show LLE5_1tile14 at Position(xpos = 777, xanchor = 0, ypos = 569, yanchor = 0)
        image LLE5_1tile9 = "W_connect_horizontal.png"
        show LLE5_1tile9 at Position(xpos = 677, xanchor = 0, ypos = 420, yanchor = 0)
        image LLE5_1tile15 = "G_end_on.png"
        show LLE5_1tile15 at Position(xpos = 852, xanchor = 0, ypos = 537, yanchor = 0)  
        if (light2Sound ==0):
            play soundP02 llLightOn2
            $light2Sound +=1
        
    if if1in2 == False:
        if (light2Sound ==1):
            play soundP02 llLightOff2
            $light2Sound -=1

    if if2in2:
        image LLE5_2tile11 = "b_vertical.png"
        show LLE5_2tile11 at Position(xpos = 744, xanchor = 0, ypos = 462, yanchor = 0)
        image LLE5_2tile14 = "b_horizontal.png"
        show LLE5_2tile14 at Position(xpos = 777, xanchor = 0, ypos = 569, yanchor = 0)
        image LLE5_2tile9 = "W_connect_horizontal.png"
        show LLE5_2tile9 at Position(xpos = 677, xanchor = 0, ypos = 420, yanchor = 0)
        
    if if1in3:            
        image LLE5_1tile21 = "g_horizontal_ll.png"
        show LLE5_1tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
        image LLE5_1tile12 = "W_corner_RB.png"
        show LLE5_1tile12 at Position(xpos = 527, xanchor = 0, ypos = 430, yanchor = 0)
        image LLE5_1tile16 = "g_vertical_ll.png"
        show LLE5_1tile16 at Position(xpos = 550, xanchor = 0, ypos = 508, yanchor = 0)
        image LLE5_1tile18 = "g_vertical_ll.png"
        show LLE5_1tile18 at Position(xpos = 550, xanchor = 0, ypos = 683, yanchor = 0) 
        image LLE5_1tile91 = "g_connect_node.png"
        show LLE5_1tile91 at Position(xpos = 678, xanchor = 0, ypos = 453, yanchor = 0)
   
    if if2in3:
        image LLE5_2tile21 = "b_horizontal.png"
        show LLE5_2tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
        image LLE5_2tile12 = "W_corner_RB.png"
        show LLE5_2tile12 at Position(xpos = 527, xanchor = 0, ypos = 430, yanchor = 0)
        image LLE5_2tile16 = "b_vertical.png"
        show LLE5_2tile16 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0)
        image LLE5_2tile18 = "b_vertical.png"
        show LLE5_2tile18 at Position(xpos = 553, xanchor = 0, ypos = 683, yanchor = 0)
        image LLE5_2tile19 = "B_end_on.png"
        show LLE5_2tile19 at Position(xpos = 516, xanchor = 0, ypos = 755, yanchor = 0)
        image LLE5_2tile92 = "b_connect_pipe.png"
        show LLE5_2tile92 at Position(xpos = 707, xanchor = 0, ypos = 466, yanchor = 0)
        image LLE5_2tile91 = "b_connect_node.png"
        show LLE5_2tile91 at Position(xpos = 745, xanchor = 0, ypos = 453, yanchor = 0)
        image LLE5_1tile93 = "b_connect_node.png"
        show LLE5_1tile93 at Position(xpos = 678, xanchor = 0, ypos = 453, yanchor = 0)
        if (light3Sound ==0):
            play soundP03 llLightOn3
            $light3Sound +=1
            
    if else3in3 == True:
        if if1in2 == True:            
            image LLE5_31tile21 = "b_horizontal.png"
            show LLE5_31tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
            image LLE5_31tile12 = "W_corner_RB.png"
            show LLE5_31tile12 at Position(xpos = 527, xanchor = 0, ypos = 430, yanchor = 0)
            image LLE5_31tile16 = "b_vertical.png"
            show LLE5_31tile16 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0)
            image LLE5_3tile18 = "b_vertical.png"
            show LLE5_3tile18 at Position(xpos = 553, xanchor = 0, ypos = 683, yanchor = 0)
            image LLE5_3tile19 = "B_end_on.png"
            show LLE5_3tile19 at Position(xpos = 516, xanchor = 0, ypos = 755, yanchor = 0)
            image LLE5_3tile92 = "b_connect_pipe.png"
            show LLE5_3tile92 at Position(xpos = 707, xanchor = 0, ypos = 466, yanchor = 0)
            image LLE5_3tile91 = "b_connect_node.png"
            show LLE5_3tile91 at Position(xpos = 745, xanchor = 0, ypos = 453, yanchor = 0)
            image LLE5_3tile93 = "b_connect_node.png"
            show LLE5_3tile93 at Position(xpos = 678, xanchor = 0, ypos = 453, yanchor = 0)
            if (light3Sound ==0):
                play soundP03 llLightOn3
                $light3Sound +=1
                
        if if2in2 == True:
            image LLE5_32tile21 = "g_horizontal_ll.png"
            show LLE5_32tile21 at Position(xpos = 602, xanchor = 0, ypos = 455, yanchor = 0)
            image LLE5_32tile12 = "W_corner_RB.png"
            show LLE5_32tile12 at Position(xpos = 527, xanchor = 0, ypos = 430, yanchor = 0)
            image LLE5_32tile16 = "g_vertical_ll.png"
            show LLE5_32tile16 at Position(xpos = 550, xanchor = 0, ypos = 508, yanchor = 0)
            image LLE5_32tile18 = "g_vertical_ll.png"
            show LLE5_32tile18 at Position(xpos = 550, xanchor = 0, ypos = 683, yanchor = 0) 
            image LLE5_3tile94 = "g_connect_node.png"
            show LLE5_3tile94 at Position(xpos = 678, xanchor = 0, ypos = 453, yanchor = 0)

    if not(if2in3 or (else3in3 and if1in2)):
        if (light3Sound ==1):
            play soundP03 llLightOff3
            $light3Sound -=1   
        
#win conditions ********
    if if1in2 == True and if2in1 == True and else3in3 == True:
        image LLE5_99tile2 = "G_if.png"
        show LLE5_99tile2 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)

        image LLE5_99tile13 = "B_if.png"
        show LLE5_99tile13 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)

        image LLE5_99tile17 = "G_else.png"
        show LLE5_99tile17 at Position(xpos = else3x, xanchor = 0, ypos =else3y, yanchor = 0)
        queue sound llWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_llEasyWin
        hide LLE5_99tile2
        hide LLE5_99tile13
        hide LLE5_99tile17
        jump llEasyWin

    if attempts == 0:
        show LLE5_99tile2 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
        show LLE5_99tile13 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
        show LLE5_99tile17 at Position(xpos = else3x, xanchor = 0, ypos =else3y, yanchor = 0)
        queue sound llLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 5
            jump pg_llEasyLose
        $loopLogicEasy_tries +=1
        hide LLE5_99tile2
        hide LLE5_99tile13
        hide LLE5_99tile17
        jump llEasyLose
    
    jump gamefile_lle5

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
    text "Moves" xpos 1480 ypos 315 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 1605 ypos 304 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 1640 ypos 313 color "#0060db" font "United Kingdom DEMO.otf" size 27
    imagebutton:
        idle "G_if_idle.png"
        xpos 1525
        ypos 645
    imagebutton:
        idle "B_if_idle.png"
        xpos 1395
        ypos 645
    imagebutton: 
        idle "G_Else_idle.png"
        xpos 1655
        ypos 645
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
                xpos else3x ypos else3y
                

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

            drag:
                drag_name "G_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1515 ypos 634
          
            drag:
                drag_name "B_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1385 ypos 634

            drag:
                drag_name "G_else_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1645 ypos 634