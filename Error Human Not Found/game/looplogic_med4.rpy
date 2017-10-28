init python:
    def gate_dragged(drags,drop):
        if not drop:
            store.gate_name = drags[0].drag_name
            store.slot_name = "null"
            return True
                
        if drop:
            dragvarx = int(drags[0].w/2 + drags[0].x)  #finding the midpoint of the drag, horizontally    
            dragvary = int(drags[0].h/2 + drags[0].y)  #finding the midpoint of the drag, vertically
            dropbox = (drop.x, drop.y, int(drop.x + drop.w), int(drop.y + drop.h))  #making our box, top left corner and bottom right corner
            if dropbox[0] < dragvarx < dropbox[2] and dropbox[1] < dragvary < dropbox[3]:  #if the midpoint of the drag is within the rectangle...
                drags[0].snap(drop.x,drop.y)       #move the drag on top of the drop
                
                store.gate_name = drags[0].drag_name
                store.slot_name = drop.drag_name
            
                return True
        return True 

init:
    image bg looplogic_bg = "LoopLogic_background.png"

label loopLogic_med4: #start
    $config.skipping=None
    $quick_menu = False
    $game_menu = True
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    scene bg looplogic_bg
    
    image LLM_4_tile1 = "Start.png"
    show LLM_4_tile1 at Position(xpos = 600, xanchor = 0, ypos = 515, yanchor = 0)

    # top of start
    image LLM_4_tile2 = "W_vertical.png"
    show LLM_4_tile2 at Position(xpos = 630, xanchor = 0, ypos = 440, yanchor = 0)
    image LLM_4_tile3 = "W_vertical.png"
    show LLM_4_tile3 at Position(xpos = 630, xanchor = 0, ypos = 365, yanchor = 0)
    image LLM_4_tile4 = "blank_node.png"
    show LLM_4_tile4 at Position(xpos = 600, xanchor = 0, ypos = 265, yanchor = 0)

    # right of start
    image LLM_4_tile5 = "G_horizontal_ll.png"
    show LLM_4_tile5 at Position(xpos = 700, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_4_tile6 = "G_horizontal_ll.png"
    show LLM_4_tile6 at Position(xpos = 775, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_4_tile7 = "g_while_off.png"
    show LLM_4_tile7 at Position(xpos = 848, xanchor = 0, ypos = 548, yanchor = 0)

    # top part of connect
    image LLM_4_tile8 = "y_vertical_short_off.png"
    show LLM_4_tile8 at Position(xpos = 850, xanchor = 0, ypos = 484, yanchor = 0)
    image LLM_4_tile83 = "y_vertical_short_off.png"
    show LLM_4_tile83 at Position(xpos = 850, xanchor = 0, ypos = 424, yanchor = 0)
    image LLM_4_tile9 = "y_vertical_short_off.png"
    show LLM_4_tile9 at Position(xpos = 850, xanchor = 0, ypos = 360, yanchor = 0)
    image LLM_4_tile82 = "y_vertical_short_off.png"
    show LLM_4_tile82 at Position(xpos = 850, xanchor = 0, ypos = 300, yanchor = 0)
    image LLM_4_tile10 = "y_horizontal_short_off.png"
    show LLM_4_tile10 at Position(xpos = 820, xanchor = 0, ypos = 293, yanchor = 0)
    image LLM_4_tile11 = "y_horizontal_short_off.png"
    show LLM_4_tile11 at Position(xpos = 765, xanchor = 0, ypos = 293, yanchor = 0)
    image LLM_4_tile12 = "y_horizontal_short_off.png"
    show LLM_4_tile12 at Position(xpos = 700, xanchor = 0, ypos = 293, yanchor = 0)

    # right of connect
    image LLM_4_tile13 = "W_horizontal.png"
    show LLM_4_tile13 at Position(xpos = 880, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_4_tile14 = "g_while_off.png"
    show LLM_4_tile14 at Position(xpos = 955, xanchor = 0, ypos = 548, yanchor = 0)
    image LLM_4_tile15 = "W_horizontal.png"
    show LLM_4_tile15 at Position(xpos = 985, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_4_tile16 = "G_end_off.png"
    show LLM_4_tile16 at Position(xpos = 1059, xanchor = 0, ypos = 515, yanchor = 0)

    # bottom of start
    image LLM_4_tile17 = "W_vertical.png"
    show LLM_4_tile17 at Position(xpos = 632, xanchor = 0, ypos = 615, yanchor = 0)  
    image LLM_4_tile18 = "W_vertical.png"
    show LLM_4_tile18 at Position(xpos = 632, xanchor = 0, ypos = 690, yanchor = 0)
    image LLM_4_tile19 = "W_corner_RT.png"
    show LLM_4_tile19 at Position(xpos = 607, xanchor = 0, ypos = 766, yanchor = 0) 
    image LLM_4_tile20 = "W_horizontal.png"
    show LLM_4_tile20 at Position(xpos = 683, xanchor = 0, ypos = 786, yanchor = 0)
    image LLM_4_tile21 = "blank_node.png"
    show LLM_4_tile21 at Position(xpos = 758, xanchor = 0, ypos = 750, yanchor = 0)
    image LLM_4_tile22 = "y_horizontal_short_off.png"
    show LLM_4_tile22 at Position(xpos = 858, xanchor = 0, ypos = 788, yanchor = 0)
    image LLM_4_tile23 = "y_horizontal_short_off.png"
    show LLM_4_tile23 at Position(xpos = 925, xanchor = 0, ypos = 788, yanchor = 0)
    image LLM_4_tile84 = "y_vertical_short_off.png"
    show LLM_4_tile84 at Position(xpos = 957, xanchor = 0, ypos = 760, yanchor = 0)

    # bottom of connect
    image LLM_4_tile24 = "y_vertical_short_off.png"
    show LLM_4_tile24 at Position(xpos = 957, xanchor = 0, ypos = 580, yanchor = 0)
    image LLM_4_tile25 = "y_vertical_short_off.png"
    show LLM_4_tile25 at Position(xpos = 957, xanchor = 0, ypos = 640, yanchor = 0)
    image LLM_4_tile26 = "y_vertical_short_off.png"
    show LLM_4_tile26 at Position(xpos = 957, xanchor = 0, ypos = 705, yanchor = 0)

    # left of start
    image LLM_4_tile27 = "G_horizontal_ll.png"
    show LLM_4_tile27 at Position(xpos = 525, xanchor = 0, ypos = 515, yanchor = 0)  
    image LLM_4_tile28 = "G_horizontal_short.png"
    show LLM_4_tile28 at Position(xpos = 475, xanchor = 0, ypos = 515, yanchor = 0) 
    image LLM_4_tile29 = "B_horizontal.png"
    show LLM_4_tile29 at Position(xpos = 525, xanchor = 0, ypos = 582, yanchor = 0)  
    image LLM_4_tile30 = "B_horizontal_short.png"
    show LLM_4_tile30 at Position(xpos = 475, xanchor = 0, ypos = 582, yanchor = 0) 
    image LLM_4_tile31 = "W_connect_vertical.png"
    show LLM_4_tile31 at Position(xpos = 415, xanchor = 0, ypos = 513, yanchor = 0)
    image LLM_4_tile32 = "W_horizontal_short.png"
    show LLM_4_tile32 at Position(xpos = 401, xanchor = 0, ypos = 515, yanchor = 0) 
    image LLM_4_tile33 = "W_horizontal_short.png"
    show LLM_4_tile33 at Position(xpos = 401, xanchor = 0, ypos = 582, yanchor = 0)
    image LLM_4_tile34 = "blank_node.png"
    show LLM_4_tile34 at Position(xpos = 301, xanchor = 0, ypos = 515, yanchor = 0)
    image LLM_4_tile35 = "W_horizontal_short.png"
    show LLM_4_tile35 at Position(xpos = 250, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_4_tile36 = "B_end_off.png"
    show LLM_4_tile36 at Position(xpos = 150, xanchor = 0, ypos = 515, yanchor = 0)

    #top of connected nodes for start left
    image LLM_4_tile37 = "W_vertical.png"
    show LLM_4_tile37 at Position(xpos = 452, xanchor = 0, ypos = 439, yanchor = 0)
    image LLM_4_tile38 = "blank_node.png"
    show LLM_4_tile38 at Position(xpos = 415, xanchor = 0, ypos = 339, yanchor = 0)
    image LLM_4_tile39 = "W_vertical_short.png"
    show LLM_4_tile39 at Position(xpos = 450, xanchor = 0, ypos = 289, yanchor = 0)
    image LLM_4_tile40 = "G_end_off.png"
    show LLM_4_tile40 at Position(xpos = 415, xanchor = 0, ypos = 189, yanchor = 0)

    #**************************************************************************************************************
    #ADDED REDRAW OF GATE BORDERS TO DISPLAY ON WIN/LOSE
    #**************************************************************************************************************
    image LLM_4_ifBBorder = "placeholder3.png"
    show LLM_4_ifBBorder at Position(xpos = 1435, xanchor = 0, ypos = 535, yanchor = 0)
    image LLM_4_elseBorder = "placeholder3.png"
    show LLM_4_elseBorder at Position(xpos = 1615, xanchor = 0, ypos = 535, yanchor = 0)
    image LLM_4_whileGBorder = "placeholder3.png"
    show LLM_4_whileGBorder at Position(xpos = 1520, xanchor = 0, ypos = 675, yanchor = 0)

        
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        


    #initial value assignment for dragables
    $ if1x = 1445
    $ if1y = 545

    $ while2x = 1530
    $ while2y = 685
    
    $ else1x = 1625
    $ else1y = 545

    $ while1x = 1530
    $ while1y = 685
            

    $ gate1x = 600
    $ gate1y = 265

    $ gate2x = 758
    $ gate2y = 750

    $ gate3x = 301
    $ gate3y = 515

    $ gate4x = 415
    $ gate4y = 339

    #**************************************************************************************************************
    #ADDED TRANSPARENT GATES
    #**************************************************************************************************************
    image LLM_4_ifBT = "B_if_idle.png"
    image LLM_4_elseT = "G_else_idle.png"
    image LLM_4_whileGT = "G_while_idle.png"
    show LLM_4_ifBT at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLM_4_elseT at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_4_whileGT at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
   
    # check conditons for locations
    $ if1in1 = False
    $ if1in2 = False
    $ if1in3 = False
    $ if1in4 = False

    $ while2in1 = False
    $ while2in2 = False
    $ while2in3 = False
    $ while2in4 = False

    $ else1in1 = False
    $ else1in2 = False
    $ else1in3 = False
    $ else1in4 = False

    $ while1in1 = False
    $ while1in2 = False
    $ while1in3 = False
    $ while1in4 = False

    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""
     
    #attempts for players
    $ attempts = 6
 
    jump gamefile_llm4
    
    
label gamefile_llm4:
    
    #calls game screen
    call screen loopLogicMed_4Scr




#*******************************************
#************image zone********************* 
#*******************************************

    #the first logic gate *******************************************************************************
    if gate_name == "B_if_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if1in1 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in1 = False
            if while2in1 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in1 = False
            if while1in1 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in1 = False

            #sets values for checks
            $ if1x = gate1x
            $ if1y = gate1y
            $ if1in1 = True
            $ if1in2 = False
            $ if1in3 = False
            $ if1in4 = False

            #if if1x == gate1x and if1y == gate1y:
            #    $ attempts -= 1
            #    "[attempts]"
 

            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if1in2 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in2 = False
            if while2in2 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in2 = False
            if while1in2 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in2 = False
            #sets values for checks
            $ if1x = gate2x
            $ if1y = gate2y
            $ if1in1 = False
            $ if1in2 = True
            $ if1in3 = False
            $ if1in4 = False

            #if if1x == gate2x and if1y == gate2y:
            #    $ attempts -= 1
            #    "[attempts]"
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if1in3 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in3 = False
            if while2in3 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in3 = False
            if while1in3 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in3 = False
            #sets values for checks
            $ if1x = gate3x
            $ if1y = gate3y
            $ if1in1 = False
            $ if1in2 = False
            $ if1in3 = True
            $ if1in4 = False

            #if if1x == gate3x and if1y == gate3y:
            #    $ attempts -= 1
            #    "[attempts]"

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if if1in4 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in4 = False
            if while2in4 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in4 = False
            if else1in4 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in4 = False
            if while1in4 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in4 = False
            #sets values for checks
            $ if1x = gate4x
            $ if1y = gate4y
            $ if1in1 = False
            $ if1in2 = False
            $ if1in3 = False
            $ if1in4 = True

        if slot_name == "B_if_gate_return":
            $ if1x = 1445
            $ if1y = 545
            $ if1in1 = False
            $ if1in2 = False
            $ if1in3 = False
            $ if1in4 = False
            
    #the first logic gate *******************************************************************************
    if gate_name == "While_gate1":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if1in1 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in1 = False
            if while2in1 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in1 = False
            if while1in1 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in1 = False

            #sets values for checks
            $ while2x = gate1x
            $ while2y = gate1y
            $ while2in1 = True
            $ while2in2 = False
            $ while2in3 = False
            $ while2in4 = False

            #if while2x == gate1x and while2y == gate1y:
            #    $ attempts -= 1
            #    "[attempts]"


        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if1in2 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in2 = False
            if while2in2 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in2 = False
            if while1in2 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in2 = False
            #sets values for checks
            $ while2x = gate2x
            $ while2y = gate2y
            $ while2in1 = False
            $ while2in2 = True
            $ while2in3 = False
            $ while2in4 = False

            #if while2x == gate2x and while2y == gate2y:
            #    $ attempts -= 1
            #    "[attempts]"
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if1in3 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in3 = False
            if while2in3 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in3 = False
            if while1in3 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in3 = False
            #sets values for checks
            $ while2x = gate3x
            $ while2y = gate3y
            $ while2in1 = False
            $ while2in2 = False
            $ while2in3 = True
            $ while2in4 = False

            #if while2x == gate3x and while2y == gate3y:
            #    $ attempts -= 1
            #    "[attempts]"


        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if if1in4 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in4 = False
            if while2in4 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in4 = False
            if else1in4 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in4 = False
            if while1in4 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in4 = False
            #sets values for checks
            $ while2x = gate4x
            $ while2y = gate4y
            $ while2in1 = False
            $ while2in2 = False
            $ while2in3 = False
            $ while2in4 = True

        if slot_name == "While_gate_green_return":
            $ while2x = 1530
            $ while2y = 685
            $ while2in1 = False
            $ while2in2 = False
            $ while2in3 = False
            $ while2in4 = False

            
    #the third logic gate *******************************************************************************
    if gate_name == "G_else_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if while2in1 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in1 = False
            if if1in1 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in1 = False
            if while1in1 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in1 = False

            #sets values for checks
            $ else1x = gate1x
            $ else1y = gate1y
            $ else1in1 = True
            $ else1in2 = False
            $ else1in3 = False
            $ else1in4 = False

            #if else1x == gate1x and else1y == gate1y:
            #    $ attempts -= 1
            #    "[attempts]"
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if while2in2 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in2 = False
            if if1in2 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in2 = False
            if while1in2 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in2 = False
            #sets values for checks
            $ else1x = gate2x
            $ else1y = gate2y
            $ else1in1 = False
            $ else1in2 = True
            $ else1in3 = False
            $ else1in4 = False

            #if else1x == gate2x and else1y == gate2y:
            #    $ attempts -= 1
            #    "[attempts]"
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if while2in3 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in3 = False
            if if1in3 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in3 = False
            if while1in3 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in3 = False
            #sets values for checks
            $ else1x = gate3x
            $ else1y = gate3y
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = True
            $ else1in4 = False

            #if else1x == gate3x and else1y == gate3y:
            #    $ attempts -= 1
            #    "[attempts]"


        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if if1in4 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in4 = False
            if while2in4 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in4 = False
            if else1in4 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in4 = False
            if while1in4 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in4 = False
            #sets values for checks
            $ else1x = gate4x
            $ else1y = gate4y
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = False
            $ else1in4 = True

        if slot_name == "G_else_gate_return":
            $ else1x = 1625
            $ else1y = 545
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = False
            $ else1in4 = False


    #the third logic gate *******************************************************************************
    if gate_name == "While_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if while2in1 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in1 = False
            if if1in1 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in1 = False
            if while1in1 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in1 = False

            #sets values for checks
            $ while1x = gate1x
            $ while1y = gate1y
            $ while1in1 = True
            $ while1in2 = False
            $ while1in3 = False
            $ while1in4 = False

            #if else1x == gate1x and else1y == gate1y:
            #    $ attempts -= 1
            #    "[attempts]"
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if while2in2 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in2 = False
            if if1in2 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in2 = False
            if while1in2 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in2 = False
            #sets values for checks
            $ while1x = gate2x
            $ while1y = gate2y
            $ while1in1 = False
            $ while1in2 = True
            $ while1in3 = False
            $ while1in4 = False

            #if else1x == gate2x and else1y == gate2y:
            #    $ attempts -= 1
            #    "[attempts]"
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if while2in3 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in3 = False
            if if1in3 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in3 = False
            if while1in3 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in3 = False
            #sets values for checks
            $ while1x = gate3x
            $ while1y = gate3y
            $ while1in1 = False
            $ while1in2 = False
            $ while1in3 = True
            $ while1in4 = False

            #if else1x == gate3x and else1y == gate3y:
            #    $ attempts -= 1
            #    "[attempts]"

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if if1in4 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in4 = False
            if while2in4 == True:
                $ while2x = 1530
                $ while2y = 685
                $ while2in4 = False
            if else1in4 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in4 = False
            if while1in4 == True:
                $ while1x = 1530
                $ while1y = 685
                $ while1in4 = False
            #sets values for checks
            $ while1x = gate4x
            $ while1y = gate4y
            $ while1in1 = False
            $ while1in2 = False
            $ while1in3 = False
            $ while1in4 = True

        if slot_name == "While_gate_green_return":
            $ while1x = 1530
            $ while1y = 685
            $ while1in1 = False
            $ while1in2 = False
            $ while1in3 = False
            $ while1in4 = False



    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not
        (slot_name == "B_if_gate_return" or slot_name == "G_else_gate_return" or slot_name == "While_gate_green_return")):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
    else:
        if slot_name != "null" and (temp_slot != slot_name or gate_name != temp_gate):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name


#*******************************************
#************image zone********************* 
#*******************************************

#    #if 1 section*******************************************************************************************     
    $llNormal = renpy.random.randint(0,2)
    if (llNormal==0):
        play sound llPipe1
    if (llNormal==1):
        play sound llPipe2
    if (llNormal==2):
        play sound llPipe3
    if if1in3 == True:
        image LLM_4_tile57 = "B_horizontal_short.png"
        show LLM_4_tile57 at Position(xpos = 250, xanchor = 0, ypos = 550, yanchor = 0)
        image LLM_4_tile41 = "B_horizontal_short.png"
        show LLM_4_tile41 at Position(xpos = 401, xanchor = 0, ypos = 582, yanchor = 0)
        image LLM_4_tile42 = "B_end_on.png"
        show LLM_4_tile42 at Position(xpos = 150, xanchor = 0, ypos = 515, yanchor = 0)
        if(light5Sound ==0):
            play soundP05 llLightOn1
            $light5Sound +=1
        if else1in4 == True:
            image LLM_4_tile43 = "G_connect_node.png"
            show LLM_4_tile43 at Position(xpos = 450, xanchor = 0, ypos = 512, yanchor = 0)
            #show LLE_2_tile44 at Position(xpos = 594, xanchor = 0, ypos = 640, yanchor = 0)
            image LLM_4_tile44 = "G_vertical_ll.png"
            show LLM_4_tile44 at Position(xpos = 448, xanchor = 0, ypos = 438, yanchor = 0)
            image LLM_4_tile45 = "G_vertical_short.png"
            show LLM_4_tile45 at Position(xpos = 448, xanchor = 0, ypos = 288, yanchor = 0)
            image LLM_4_tile46 = "G_end_on.png"
            show LLM_4_tile46 at Position(xpos = 418, xanchor = 0, ypos = 185, yanchor = 0)
            if(light4Sound ==0):
                play soundP04 llLightOn3
                $light4Sound +=1

        if else1in4 == False:
            hide LLM_4_tile43
            hide LLM_4_tile44
            hide LLM_4_tile45
            hide LLM_4_tile46
            if(light4Sound ==1):
                play soundP04 llLightOff3
                $light4Sound -=1
            
    if if1in3 == False:
        hide LLM_4_tile57
        hide LLM_4_tile41
        hide LLM_4_tile42
        hide LLM_4_tile43
        hide LLM_4_tile44
        hide LLM_4_tile45
        hide LLM_4_tile46
        if(light4Sound ==1):
                play soundP04 llLightOff3
                $light4Sound -=1
        if(light5Sound ==1):
            play soundP05 llLightOff1
            $light5Sound -=1


    if if1in1 == True:
        image LLM_4_tile80_A = "B_vertical.png"
        show LLM_4_tile80_A at Position(xpos = 632, xanchor = 0, ypos = 440, yanchor = 0)
        image LLM_4_tile81_A = "B_vertical.png"
        show LLM_4_tile81_A at Position(xpos = 632, xanchor = 0, ypos = 365, yanchor = 0)

    if if1in1 == False:
        hide LLM_4_tile80_A
        hide LLM_4_tile81_A  

    if while2in1 == True or while1in1 == True:
        image LLM_4_tile50 = "g_while_on.png"
        show LLM_4_tile50 at Position(xpos = 848, xanchor = 0, ypos = 548, yanchor = 0)
        image LLM_4_tile51 = "G_horizontal_ll.png"
        show LLM_4_tile51 at Position(xpos = 880, xanchor = 0, ypos = 550, yanchor = 0)
        image LLM_4_tile70 = "G_vertical_ll.png"
        show LLM_4_tile70 at Position(xpos = 630, xanchor = 0, ypos = 440, yanchor = 0)
        image LLM_4_tile71 = "G_vertical_ll.png"
        show LLM_4_tile71 at Position(xpos = 630, xanchor = 0, ypos = 365, yanchor = 0)
        if(light1Sound ==0):
            play soundP01 llLightOn1
            $light1Sound +=1
        image LLM_4_tile91 = "y_vertical_short_on.png"
        show LLM_4_tile91 at Position(xpos = 850, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_4_tile92 = "y_vertical_short_on.png"
        show LLM_4_tile92 at Position(xpos = 850, xanchor = 0, ypos = 424, yanchor = 0)
        image LLM_4_tile93 = "y_vertical_short_on.png"
        show LLM_4_tile93 at Position(xpos = 850, xanchor = 0, ypos = 360, yanchor = 0)
        image LLM_4_tile94 = "y_vertical_short_on.png"
        show LLM_4_tile94 at Position(xpos = 850, xanchor = 0, ypos = 300, yanchor = 0)
        image LLM_4_tile95 = "y_horizontal_short_on.png"
        show LLM_4_tile95 at Position(xpos = 820, xanchor = 0, ypos = 293, yanchor = 0)
        image LLM_4_tile96 = "y_horizontal_short_on.png"
        show LLM_4_tile96 at Position(xpos = 765, xanchor = 0, ypos = 293, yanchor = 0)
        image LLM_4_tile97 = "y_horizontal_short_on.png"
        show LLM_4_tile97 at Position(xpos = 700, xanchor = 0, ypos = 293, yanchor = 0)

        if while1in2 == True or while2in2 == True:
            image LLM_4_tile52 = "g_while_on.png"
            show LLM_4_tile52 at Position(xpos = 955, xanchor = 0, ypos = 548, yanchor = 0)
            image LLM_4_tile53 = "G_horizontal_ll.png"
            show LLM_4_tile53 at Position(xpos = 985, xanchor = 0, ypos = 550, yanchor = 0)
            image LLM_4_tile54 = "G_end_on.png"
            show LLM_4_tile54 at Position(xpos = 1059, xanchor = 0, ypos = 515, yanchor = 0)
            show LLM_4_tile90 at Position(xpos = 957, xanchor = 0, ypos = 705, yanchor = 0)
            if(light2Sound ==0):
                play soundP02 llLightOn2
                $light2Sound +=1
            if(light3Sound==0):
                play soundP03 llLightOn3
                $light3Sound +=1
        if while1in2 == False and while2in2 == False:
            hide LLM_4_tile52
            hide LLM_4_tile53
            hide LLM_4_tile54
            if(light2Sound==1):
                play soundP02 llLightOff2
                $light2Sound -=1
            if(light3Sound==1):
                play soundP03 llLightOff3
                $light3Sound-=1

    if while2in1 == False and while1in1 == False:
        if(light1Sound ==1):
            play soundP01 llLightOff1
            $light1Sound -=1
        hide LLM_4_tile50
        hide LLM_4_tile51
        hide LLM_4_tile70
        hide LLM_4_tile71

        hide LLM_4_tile94
        hide LLM_4_tile91
        hide LLM_4_tile92
        hide LLM_4_tile93
        hide LLM_4_tile94
        hide LLM_4_tile95
        hide LLM_4_tile96
        hide LLM_4_tile97

        hide LLM_4_tile52
        hide LLM_4_tile53
        hide LLM_4_tile54

    if if1in2 == True:
        image LLM_4_tile74 = "B_vertical.png"
        show LLM_4_tile74 at Position(xpos = 632, xanchor = 0, ypos = 615, yanchor = 0)  
        image LLM_4_tile75 = "B_vertical.png"
        show LLM_4_tile75 at Position(xpos = 632, xanchor = 0, ypos = 690, yanchor = 0)
        image LLM_4_tile76 = "B_horizontal.png"
        show LLM_4_tile76 at Position(xpos = 683, xanchor = 0, ypos = 786, yanchor = 0)

    if if1in2 == False:
        hide LLM_4_tile74
        hide LLM_4_tile75
        hide LLM_4_tile76

    if while1in2 == True or while2in2 == True:
        image LLM_4_tile52 = "g_while_on.png"
        show LLM_4_tile52 at Position(xpos = 955, xanchor = 0, ypos = 548, yanchor = 0)
        image LLM_4_tile77 = "G_vertical_ll.png"
        show LLM_4_tile77 at Position(xpos = 630, xanchor = 0, ypos = 615, yanchor = 0)  
        image LLM_4_tile78 = "G_vertical_ll.png"
        show LLM_4_tile78 at Position(xpos = 630, xanchor = 0, ypos = 690, yanchor = 0)
        image LLM_4_tile79 = "G_horizontal_ll.png"
        show LLM_4_tile79 at Position(xpos = 683, xanchor = 0, ypos = 786, yanchor = 0)
        image LLM_4_tile85 = "y_horizontal_short_on.png"
        show LLM_4_tile85 at Position(xpos = 858, xanchor = 0, ypos = 788, yanchor = 0)
        image LLM_4_tile86 = "y_horizontal_short_on.png"
        show LLM_4_tile86 at Position(xpos = 925, xanchor = 0, ypos = 788, yanchor = 0)
        image LLM_4_tile87 = "y_vertical_short_on.png"
        show LLM_4_tile87 at Position(xpos = 957, xanchor = 0, ypos = 760, yanchor = 0)
        image LLM_4_tile88 = "y_vertical_short_on.png"
        show LLM_4_tile88 at Position(xpos = 957, xanchor = 0, ypos = 580, yanchor = 0)
        image LLM_4_tile89 = "y_vertical_short_on.png"
        show LLM_4_tile89 at Position(xpos = 957, xanchor = 0, ypos = 640, yanchor = 0)
        image LLM_4_tile90 = "y_vertical_short_on.png"
        show LLM_4_tile90 at Position(xpos = 957, xanchor = 0, ypos = 705, yanchor = 0)
        if(light2Sound ==0):
            play soundP02 llLightOn2
            $light2Sound +=1
    if while1in2 == False and while2in2 == False:
        hide LLM_4_tile52
        hide LLM_4_tile77
        hide LLM_4_tile78
        hide LLM_4_tile79
        hide LLM_4_tile85
        hide LLM_4_tile86
        hide LLM_4_tile87
        hide LLM_4_tile88
        hide LLM_4_tile89
        hide LLM_4_tile90
        if(light2Sound==1):
            play soundP02 llLightOff2
            $light2Sound -=1
        
#win conditions ********
    if (if1in3 == True) and else1in4 == True and (while2in1 == True or while1in1 == True) and (while1in2 == True or while2in2 == True):
        image LLM_4_tile60 = "B_end_on.png"
        show LLM_4_tile60 at Position(xpos = 150, xanchor = 0, ypos = 515, yanchor = 0)
        image LLM_4_tile61 = "G_connect_node.png"
        show LLM_4_tile61 at Position(xpos = 450, xanchor = 0, ypos = 512, yanchor = 0)
        image LLM_4_tile62 = "G_end_on.png"
        show LLM_4_tile62 at Position(xpos = 418, xanchor = 0, ypos = 185, yanchor = 0)
        image LLM_4_tile63 = "g_while_on.png"
        show LLM_4_tile63 at Position(xpos = 848, xanchor = 0, ypos = 548, yanchor = 0)
        image LLM_4_tile68 = "g_while_on.png"
        show LLM_4_tile68 at Position(xpos = 955, xanchor = 0, ypos = 548, yanchor = 0)
        image LLM_4_tile69 = "G_end_on.png"
        show LLM_4_tile69 at Position(xpos = 1059, xanchor = 0, ypos = 515, yanchor = 0)

        image LLM_4_tile64 = "B_if.png"
        show LLM_4_tile64 at Position(xpos = 301, xanchor = 0, ypos = 515, yanchor = 0)
        image LLM_4_tile65 = "G_while.png"
        show LLM_4_tile65 at Position(xpos = 600, xanchor = 0, ypos = 265, yanchor = 0)
        image LLM_4_tile66 = "G_else.png"
        show LLM_4_tile66 at Position(xpos = 415, xanchor = 0, ypos = 339, yanchor = 0)
        image LLM_4_tile67 = "G_while.png"
        show LLM_4_tile67 at Position(xpos = 758, xanchor = 0, ypos = 750, yanchor = 0)
        queue sound llWin
        $renpy.pause(1.0)
        hide LLM_4_tile60
        hide LLM_4_tile61
        hide LLM_4_tile62
        hide LLM_4_tile63
        hide LLM_4_tile64
        hide LLM_4_tile65
        hide LLM_4_tile66
        hide LLM_4_tile67
        jump llMedWin

    if attempts == 0:
        show LLM_4_tile64 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
        show LLM_4_tile65 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
        show LLM_4_tile66 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
        show LLM_4_tile67 at Position(xpos = while2x, xanchor = 0, ypos = while2y, yanchor = 0)
        queue sound llLose
        $renpy.pause(1.5)
        $llMed_attempts+=1
        hide LLM_4_tile60
        hide LLM_4_tile61
        hide LLM_4_tile62
        hide LLM_4_tile63
        hide LLM_4_tile64
        hide LLM_4_tile65
        hide LLM_4_tile66
        hide LLM_4_tile67
        jump llMedLose
    
    jump gamefile_llm4

screen loopLogicMed_4Scr:
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
        action Jump("hints_llMed_4")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 1463
        ypos 295
#    imagebutton:
#        idle "G_if_idle.png"
#        xpos 1445
#        ypos 685
    imagebutton:
        idle "B_if_idle.png"
        xpos 1445
        ypos 545
    imagebutton: 
        idle "G_Else_idle.png"
        xpos 1625
        ypos 545
    imagebutton:
        idle "G_while_idle.png"
        xpos 1530
        ypos 685
    text "Moves" xpos 1480 ypos 315 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 1605 ypos 304 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 1640 ypos 313 color "#0060db" font "United Kingdom DEMO.otf" size 27
    #drags and drop location
    draggroup:
            #if gates
            drag:
                drag_name "B_if_gate"
                child "B_if.png"
                droppable False
                dragged gate_dragged
                xpos if1x ypos if1y
            drag:
                drag_name "While_gate1"
                child "G_while.png"
                droppable False
                dragged gate_dragged
                xpos while2x ypos while2y  

            #else gate
            drag:
                drag_name "G_else_gate"
                child "G_Else.png"
                droppable False
                dragged gate_dragged
                xpos else1x ypos else1y

            #while gate
            drag:
                drag_name "While_gate"
                child "G_while.png"
                droppable False
                dragged gate_dragged
                xpos while1x ypos while1y  

            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover2.png"
                #child "Placeholder2.png"
                draggable False
                xpos gate1x-25 ypos gate1y-25
           
            drag:
                drag_name "gate slot two"
                child "cover2.png"
                #child "Placeholder2.png"
                draggable False
                xpos gate2x-25 ypos gate2y-25
                
            drag:
                drag_name "gate slot three"
                child "cover2.png"
                #child "Placeholder2.png"
                draggable False
                xpos gate3x-25 ypos gate3y-25

            drag:
                drag_name "gate slot four"
                child "cover2.png"
                #child "Placeholder2.png"
                draggable False
                xpos gate4x-25 ypos gate4y-25

            drag:
                drag_name "B_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1435 ypos 535

            drag:
                drag_name "G_else_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1615 ypos 535

            drag:
                drag_name "While_gate_green_return"
                child "placeholder3.png"
                draggable False
                xpos 1520 ypos 675

