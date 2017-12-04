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

label loopLogic_med2: #start
    $config.skipping=None
    $quick_menu = False
    $game_menu = True
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    scene bg looplogic_bg
    
    image LLM_2_tile1 = "Start.png"
    show LLM_2_tile1 at Position(xpos = 500, xanchor = 0, ypos = 510, yanchor = 0)   

    # right of start
    image LLM_2_tile2 = "W_horizontal.png"
    show LLM_2_tile2 at Position(xpos = 600, xanchor = 0, ypos = 540, yanchor = 0)
    image LLM_2_tile3 = "W_horizontal.png"
    show LLM_2_tile3 at Position(xpos = 675, xanchor = 0, ypos = 540, yanchor = 0)
    image LLM_2_tile4 = "blank_node.png"
    show LLM_2_tile4 at Position(xpos = 750, xanchor = 0, ypos = 510, yanchor = 0)
    image LLM_2_tile5 = "W_horizontal.png"
    show LLM_2_tile5 at Position(xpos = 851, xanchor = 0, ypos = 540, yanchor = 0)
    image LLM_2_tile6 = "W_corner_LB.png"
    show LLM_2_tile6 at Position(xpos = 926, xanchor = 0, ypos = 515, yanchor = 0)
    image LLM_2_tile7 = "W_vertical_short.png"
    show LLM_2_tile7 at Position(xpos = 948, xanchor = 0, ypos = 592, yanchor = 0)
    image LLM_2_tile8 = "g_while_off.png"
    show LLM_2_tile8 at Position(xpos = 947, xanchor = 0, ypos = 642, yanchor = 0)
    image LLM_2_tile9 = "W_vertical_short.png"
    show LLM_2_tile9 at Position(xpos = 948, xanchor = 0, ypos = 675, yanchor = 0)
    image LLM_2_tile10 = "G_end_off.png"
    show LLM_2_tile10 at Position(xpos = 915, xanchor = 0, ypos = 725, yanchor = 0)

    #bottom Connect ndoe left
    image LLM_2_tile11 = "y_horizontal_short_off.png"
    show LLM_2_tile11 at Position(xpos = 897, xanchor = 0, ypos = 643, yanchor = 0)
    image LLM_2_tile12 = "y_horizontal_short_off.png"
    show LLM_2_tile12 at Position(xpos = 827, xanchor = 0, ypos = 643, yanchor = 0)
    image LLM_2_tile13 = "y_horizontal_short_off.png"
    show LLM_2_tile13 at Position(xpos = 762, xanchor = 0, ypos = 643, yanchor = 0)
    image LLM_2_tile69 = "y_vertical_short_off.png"
    show LLM_2_tile69 at Position(xpos = 755, xanchor = 0, ypos = 650, yanchor = 0)
    image LLM_2_tile14 = "y_vertical_short_off.png"
    show LLM_2_tile14 at Position(xpos = 755, xanchor = 0, ypos = 700, yanchor = 0)
    image LLM_2_tile70 = "y_vertical_short_off.png"
    show LLM_2_tile70 at Position(xpos = 755, xanchor = 0, ypos = 755, yanchor = 0)
    image LLM_2_tile15 = "y_horizontal_short_off.png"
    show LLM_2_tile15 at Position(xpos = 722, xanchor = 0, ypos = 784, yanchor = 0)
    image LLM_2_tile16 = "y_horizontal_short_off.png"
    show LLM_2_tile16 at Position(xpos = 665, xanchor = 0, ypos = 784, yanchor = 0)
    image LLM_2_tile17 = "y_horizontal_short_off.png"
    show LLM_2_tile17 at Position(xpos = 600, xanchor = 0, ypos = 784, yanchor = 0)

    # left of start
    image LLM_2_tile18 = "W_horizontal.png"
    show LLM_2_tile18 at Position(xpos = 425, xanchor = 0, ypos = 542, yanchor = 0)  
    image LLM_2_tile19 = "W_horizontal.png"
    show LLM_2_tile19 at Position(xpos = 350, xanchor = 0, ypos = 542, yanchor = 0) 
    image LLM_2_tile20 = "W_corner_RB.png"
    show LLM_2_tile20 at Position(xpos = 275, xanchor = 0, ypos = 516, yanchor = 0) 
    image LLM_2_tile21 = "W_vertical.png"
    show LLM_2_tile21 at Position(xpos = 298, xanchor = 0, ypos = 591, yanchor = 0) 
    image LLM_2_tile68 = "W_vertical_short.png"
    show LLM_2_tile68 at Position(xpos = 298, xanchor = 0, ypos = 666, yanchor = 0)
    image LLM_2_tile22 = "W_vertical_short.png"
    show LLM_2_tile22 at Position(xpos = 298, xanchor = 0, ypos = 716, yanchor = 0)
    image LLM_2_tile23 = "W_corner_RT.png"
    show LLM_2_tile23 at Position(xpos = 276, xanchor = 0, ypos = 763, yanchor = 0)
    image LLM_2_tile24 = "W_horizontal.png"
    show LLM_2_tile24 at Position(xpos = 351, xanchor = 0, ypos = 785, yanchor = 0)
    image LLM_2_tile25 = "W_horizontal.png"
    show LLM_2_tile25 at Position(xpos = 426, xanchor = 0, ypos = 785, yanchor = 0)
    image LLM_2_tile26 = "blank_node.png"
    show LLM_2_tile26 at Position(xpos = 500, xanchor = 0, ypos = 750, yanchor = 0)

    #top of start
    image LLM_2_tile29 = "W_connect_horizontal.png"
    show LLM_2_tile29 at Position(xpos = 500, xanchor = 0, ypos = 370, yanchor = 0)
    image LLM_2_tile27 = "G_vertical_ll.png"
    show LLM_2_tile27 at Position(xpos = 500, xanchor = 0, ypos = 435, yanchor = 0)
    image LLM_2_tile28 = "B_vertical.png"
    show LLM_2_tile28 at Position(xpos = 570, xanchor = 0, ypos = 435, yanchor = 0)

    #image LLM_2_tile29 = "W_connect_node.png"
    #show LLM_2_tile29 at Position(xpos = 500, xanchor = 0, ypos = 405, yanchor = 0)
    #image LLM_2_tile30 = "W_connect_node.png"
    #show LLM_2_tile30 at Position(xpos = 570, xanchor = 0, ypos = 405, yanchor = 0)

    
    #connected dots top
    image LLM_2_tile31 = "W_vertical_short.png"
    show LLM_2_tile31 at Position(xpos = 502, xanchor = 0, ypos = 355, yanchor = 0)
    image LLM_2_tile32 = "W_vertical_short.png"
    show LLM_2_tile32 at Position(xpos = 570, xanchor = 0, ypos = 355, yanchor = 0)
    image LLM_2_tile33 = "blank_node.png"
    show LLM_2_tile33 at Position(xpos = 500, xanchor = 0, ypos = 253, yanchor = 0) 
    image LLM_2_tile34 = "W_horizontal.png"
    show LLM_2_tile34 at Position(xpos = 600, xanchor = 0, ypos = 287, yanchor = 0)
    image LLM_2_tile35 = "W_horizontal.png"
    show LLM_2_tile35 at Position(xpos = 675, xanchor = 0, ypos = 287, yanchor = 0)
    image LLM_2_tile36 = "B_end_off.png"
    show LLM_2_tile36 at Position(xpos = 750, xanchor = 0, ypos = 253, yanchor = 0)

    #connected dots left
    image LLM_2_tile37 = "W_horizontal_short.png"
    show LLM_2_tile37 at Position(xpos = 450, xanchor = 0, ypos = 405, yanchor = 0)
    image LLM_2_tile38 = "blank_node.png"
    show LLM_2_tile38 at Position(xpos = 350, xanchor = 0, ypos = 373, yanchor = 0) 
    image LLM_2_tile39 = "W_horizontal.png"
    show LLM_2_tile39 at Position(xpos = 275, xanchor = 0, ypos = 405, yanchor = 0)
    image LLM_2_tile40 = "G_end_off.png"
    show LLM_2_tile40 at Position(xpos = 176, xanchor = 0, ypos = 370, yanchor = 0)

    #**************************************************************************************************************
    #ADDED REDRAW OF GATE BORDERS TO DISPLAY ON WIN/LOSE
    #**************************************************************************************************************
    image LLM_2_ifGBorder = "placeholder3.png"
    show LLM_2_ifGBorder at Position(xpos = 1435, xanchor = 0, ypos = 675, yanchor = 0)
    image LLM_2_ifBBorder = "placeholder3.png"
    show LLM_2_ifBBorder at Position(xpos = 1435, xanchor = 0, ypos = 535, yanchor = 0)
    image LLM_2_elseBorder = "placeholder3.png"
    show LLM_2_elseBorder at Position(xpos = 1615, xanchor = 0, ypos = 535, yanchor = 0)
    image LLM_2_whileGBorder = "placeholder3.png"
    show LLM_2_whileGBorder at Position(xpos = 1615, xanchor = 0, ypos = 675, yanchor = 0)

    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        


    #initial value assignment for dragables
    $ if1x = 1445
    $ if1y = 545

    $ if2x = 1445
    $ if2y = 685
    
    $ else1x = 1625
    $ else1y = 545

    $ while1x = 1625
    $ while1y = 685
            

    $ gate1x = 750
    $ gate1y = 510

    $ gate2x = 500
    $ gate2y = 750

    $ gate3x = 500
    $ gate3y = 253

    $ gate4x = 350
    $ gate4y = 373

    #**************************************************************************************************************
    #ADDED TRANSPARENT GATES
    #**************************************************************************************************************
    image LLM_2_ifGT = "G_if_idle.png"
    image LLM_2_ifBT = "B_if_idle.png"
    image LLM_2_elseT = "G_else_idle.png"
    image LLM_2_whileGT = "G_while_idle.png"
    show LLM_2_ifGT at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
    show LLM_2_ifBT at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
    show LLM_2_elseT at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLM_2_whileGT at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
   
    # check conditons for locations
    $ if1in1 = False
    $ if1in2 = False
    $ if1in3 = False
    $ if1in4 = False

    $ if2in1 = False
    $ if2in2 = False
    $ if2in3 = False
    $ if2in4 = False

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
 
    jump gamefile_llm2
    
    
label gamefile_llm2:
    
    #calls game screen
    call screen loopLogicMed_2Scr




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
            if if2in1 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in1 = False
            if while1in1 == True:
                $ while1x = 1625
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
            if if2in2 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in2 = False
            if while1in2 == True:
                $ while1x = 1625
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
            if if2in3 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in3 = False
            if while1in3 == True:
                $ while1x = 1625
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
            if if2in4 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in4 = False
            if else1in4 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in4 = False
            if while1in4 == True:
                $ while1x = 1625
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
    if gate_name == "G_if_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if1in1 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in1 = False
            if if2in1 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in1 = False
            if while1in1 == True:
                $ while1x = 1625
                $ while1y = 685
                $ while1in1 = False

            #sets values for checks
            $ if2x = gate1x
            $ if2y = gate1y
            $ if2in1 = True
            $ if2in2 = False
            $ if2in3 = False
            $ if2in4 = False

            #if if2x == gate1x and if2y == gate1y:
            #    $ attempts -= 1
            #    "[attempts]"


        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if if1in2 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in2 = False
            if if2in2 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in2 = False
            if while1in2 == True:
                $ while1x = 1625
                $ while1y = 685
                $ while1in2 = False
            #sets values for checks
            $ if2x = gate2x
            $ if2y = gate2y
            $ if2in1 = False
            $ if2in2 = True
            $ if2in3 = False
            $ if2in4 = False

            #if if2x == gate2x and if2y == gate2y:
            #    $ attempts -= 1
            #    "[attempts]"
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if if1in3 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in3 = False
            if if2in3 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in3 = False
            if while1in3 == True:
                $ while1x = 1625
                $ while1y = 685
                $ while1in3 = False
            #sets values for checks
            $ if2x = gate3x
            $ if2y = gate3y
            $ if2in1 = False
            $ if2in2 = False
            $ if2in3 = True
            $ if2in4 = False

            #if if2x == gate3x and if2y == gate3y:
            #    $ attempts -= 1
            #    "[attempts]"


        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if if1in4 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in4 = False
            if if2in4 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in4 = False
            if else1in4 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in4 = False
            if while1in4 == True:
                $ while1x = 1625
                $ while1y = 685
                $ while1in4 = False
            #sets values for checks
            $ if2x = gate4x
            $ if2y = gate4y
            $ if2in1 = False
            $ if2in2 = False
            $ if2in3 = False
            $ if2in4 = True

        if slot_name == "G_if_gate_return":
            $ if2x = 1445
            $ if2y = 685
            $ if2in1 = False
            $ if2in2 = False
            $ if2in3 = False
            $ if2in4 = False

            
    #the third logic gate *******************************************************************************
    if gate_name == "G_else_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if2in1 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in1 = False
            if if1in1 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in1 = False
            if while1in1 == True:
                $ while1x = 1625
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
            if if2in2 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in2 = False
            if if1in2 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in2 = False
            if while1in2 == True:
                $ while1x = 1625
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
            if if2in3 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in3 = False
            if if1in3 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in3 = False
            if while1in3 == True:
                $ while1x = 1625
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
            if if2in4 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in4 = False
            if else1in4 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in4 = False
            if while1in4 == True:
                $ while1x = 1625
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
            if if2in1 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in1 = False
            if if1in1 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in1 = False
            if else1in1 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in1 = False
            if while1in1 == True:
                $ while1x = 1625
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
            if if2in2 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in2 = False
            if if1in2 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in2 = False
            if else1in2 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in2 = False
            if while1in2 == True:
                $ while1x = 1625
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
            if if2in3 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in3 = False
            if if1in3 == True:
                $ if1x = 1445
                $ if1y = 545
                $ if1in3 = False
            if else1in3 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in3 = False
            if while1in3 == True:
                $ while1x = 1625
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
            if if2in4 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in4 = False
            if else1in4 == True:
                $ else1x = 1625
                $ else1y = 545
                $ else1in4 = False
            if while1in4 == True:
                $ while1x = 1625
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
            $ while1x = 1625
            $ while1y = 685
            $ while1in1 = False
            $ while1in2 = False
            $ while1in3 = False
            $ while1in4 = False



    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not
        (slot_name == "G_if_gate_return" or slot_name == "B_if_gate_return" or slot_name == "G_else_gate_return" or slot_name == "While_gate_green_return")):
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
                if slot_name == "B_if_gate":
                    $ if1x = 1445
                    $ if1y = 545
                    $ if1in1 = False
                    $ if1in2 = False
                    $ if1in3 = False
                    $ if1in4 = False
                    
            if slot_name == "G_if_gate_return":
                $ attempts +=1
                if slot_name == "G_if_gate":
                    $ if2x = 1445
                    $ if2y = 685
                    $ if2in1 = False
                    $ if2in2 = False
                    $ if2in3 = False
                    $ if2in4 = False
                    
            if slot_name == "G_else_gate_return":
                $ attempts +=1
                if slot_name == "G_else_gate":
                    $ else1x = 1625
                    $ else1y = 545
                    $ else1in1 = False
                    $ else1in2 = False
                    $ else1in3 = False
                    $ else1in4 = False
                    
            if slot_name == "While_gate_green_return":
                $ attempts +=1
                if slot_name == "While_gate":
                    $ while1x = 1625
                    $ while1y = 685
                    $ while1in1 = False
                    $ while1in2 = False
                    $ while1in3 = False
                    $ while1in4 = False


#*******************************************
#************image zone********************* 
#*******************************************

#    #if 1 section*******************************************************************************************     
    hide LLM_2_tile71
    hide LLM_2_tile73
    hide LLM_2_tile74
    hide LLM_2_tile72
    hide LLM_2_tile43
    hide LLM_2_tile44
    hide LLM_2_tile45
    hide LLM_2_tile46
    hide LLM_2_tile75
    hide LLM_2_tile76
    hide LLM_2_tile77
    hide LLM_2_tile78
    hide LLM_2_tile79
    hide LLM_2_tile80
    hide LLM_2_tile81
    hide LLM_2_tile82
    hide LLM_2_tile83
    hide LLM_2_tile84
    hide LLM_2_tile50
    hide LLM_2_tile51
    hide LLM_2_tile52
    hide LLM_2_tile85
    hide LLM_2_tile86
    hide LLM_2_tile87
    hide LLM_2_tile88
    hide LLM_2_tile89
    hide LLM_2_tileS55
    hide LLM_2_tile55
    hide LLM_2_tile56
    hide LLM_2_tile104
    hide LLM_2_tile105
    hide LLM_2_tile106
    hide LLM_2_tile107
    hide LLM_2_tile108
    hide LLM_2_tile109
    hide LLM_2_tile110
    hide LLM_2_tile111
    hide LLM_2_tile112
    hide LLM_2_tile90
    hide LLM_2_tile93
    hide LLM_2_tile94
    hide LLM_2_tile96
    hide LLM_2_tile97
    hide LLM_2_tile98
    hide LLM_2_tile101
    hide LLM_2_tile102
    hide LLM_2_tile120
    hide LLM_2_tile121
    hide LLM_2_tile122
    hide LLM_2_tile123
    hide LLM_2_tile124
    hide LLM_2_tile125
    hide LLM_2_tile126

    $llNormal = renpy.random.randint(0,2)
    if (llNormal==0):
        play sound llPipe1
    if (llNormal==1):
        play sound llPipe2
    if (llNormal==2):
        play sound llPipe3
    if if1in3:
        image LLM_2_tile71 = "B_vertical_short.png"
        show LLM_2_tile71 at Position(xpos = 570, xanchor = 0, ypos = 355, yanchor = 0)
        image LLM_2_tile73 = "B_horizontal.png"
        show LLM_2_tile73 at Position(xpos = 600, xanchor = 0, ypos = 287, yanchor = 0)
        image LLM_2_tile74 = "B_horizontal.png"
        show LLM_2_tile74 at Position(xpos = 675, xanchor = 0, ypos = 287, yanchor = 0)
        image LLM_2_tile72 = "B_end_on.png"
        show LLM_2_tile72 at Position(xpos = 750, xanchor = 0, ypos = 253, yanchor = 0)
        if(light3Sound==0):
            play soundP03 llLightOn3
            $light3Sound +=1
        
        if else1in4:
            image LLM_2_tile43 = "G_connect_node.png"
            show LLM_2_tile43 at Position(xpos = 500, xanchor = 0, ypos = 403, yanchor = 0)
            image LLM_2_tile44 = "G_horizontal_short.png"
            show LLM_2_tile44 at Position(xpos = 450, xanchor = 0, ypos = 405, yanchor = 0)
            image LLM_2_tile45 = "G_horizontal_ll.png"
            show LLM_2_tile45 at Position(xpos = 275, xanchor = 0, ypos = 405, yanchor = 0)
            image LLM_2_tile46 = "G_end_on.png"
            show LLM_2_tile46 at Position(xpos = 175, xanchor = 0, ypos = 373, yanchor = 0)
            if(light4Sound==0):
                play soundP04 llLightOn2
                $light4Sound +=1
    if if2in4:
        show LLM_2_tile43 at Position(xpos = 500, xanchor = 0, ypos = 403, yanchor = 0)
        show LLM_2_tile44 at Position(xpos = 450, xanchor = 0, ypos = 405, yanchor = 0)
        show LLM_2_tile45 at Position(xpos = 275, xanchor = 0, ypos = 405, yanchor = 0)
        show LLM_2_tile46 at Position(xpos = 175, xanchor = 0, ypos = 373, yanchor = 0)
        if(light4Sound==0):
            play soundP04 llLightOn2
            $light4Sound +=1
            
    if not(if2in4 or (if1in3 and else1in4)):
        if(light4Sound==1):
            play soundP04 llLightOff2
            $light4Sound -=1
   
    if if1in3 == False:
        if(light3Sound==1):
            play soundP03 llLightOff3
            $light3Sound -=1

    if if2in3:
        image LLM_2_tile75 = "G_vertical_short.png"
        show LLM_2_tile75 at Position(xpos = 500, xanchor = 0, ypos = 355, yanchor = 0)
        image LLM_2_tile76 = "G_horizontal_ll.png"
        show LLM_2_tile76 at Position(xpos = 600, xanchor = 0, ypos = 287, yanchor = 0)
        image LLM_2_tile77 = "G_horizontal_ll.png"
        show LLM_2_tile77 at Position(xpos = 675, xanchor = 0, ypos = 287, yanchor = 0)

        if else1in4:
            image LLM_2_tile81 = "B_horizontal_short.png"
            show LLM_2_tile81 at Position(xpos = 450, xanchor = 0, ypos = 405, yanchor = 0)
            image LLM_2_tile82 = "B_horizontal.png"
            show LLM_2_tile82 at Position(xpos = 275, xanchor = 0, ypos = 405, yanchor = 0)
            image LLM_2_tile78 = "B_connect_pipe.png"
            show LLM_2_tile78 at Position(xpos = 530, xanchor = 0, ypos = 415, yanchor = 0)
            image LLM_2_tile79 = "B_connect_node.png"
            show LLM_2_tile79 at Position(xpos = 568, xanchor = 0, ypos = 403, yanchor = 0)
            image LLM_2_tile80 = "B_connect_node.png"
            show LLM_2_tile80 at Position(xpos = 500, xanchor = 0, ypos = 403, yanchor = 0)

    if if1in4:
        show LLM_2_tile81 at Position(xpos = 450, xanchor = 0, ypos = 405, yanchor = 0)
        show LLM_2_tile82 at Position(xpos = 275, xanchor = 0, ypos = 405, yanchor = 0)
        show LLM_2_tile78 at Position(xpos = 530, xanchor = 0, ypos = 415, yanchor = 0)
        show LLM_2_tile79 at Position(xpos = 568, xanchor = 0, ypos = 403, yanchor = 0)
        show LLM_2_tile80 at Position(xpos = 500, xanchor = 0, ypos = 403, yanchor = 0)
    
    if if2in1:
        image LLM_2_tile83 = "G_horizontal_ll.png"
        show LLM_2_tile83 at Position(xpos = 600, xanchor = 0, ypos = 540, yanchor = 0)
        image LLM_2_tile84 = "G_horizontal_ll.png"
        show LLM_2_tile84 at Position(xpos = 675, xanchor = 0, ypos = 540, yanchor = 0)
        image LLM_2_tile50 = "G_horizontal_ll.png"
        show LLM_2_tile50 at Position(xpos = 851, xanchor = 0, ypos = 542, yanchor = 0)
        image LLM_2_tile51 = "W_corner_LB.png"
        show LLM_2_tile51 at Position(xpos = 926, xanchor = 0, ypos = 517, yanchor = 0)
        image LLM_2_tile52 = "G_vertical_short.png"
        show LLM_2_tile52 at Position(xpos = 945, xanchor = 0, ypos = 592, yanchor = 0)
        if(while1in2):
            image LLM_2_tile55 = "G_vertical_short.png"
            show LLM_2_tile55 at Position(xpos = 947, xanchor = 0, ypos = 675, yanchor = 0)
            image LLM_2_tile56 = "G_end_on.png"
            show LLM_2_tile56 at Position(xpos = 915, xanchor = 0, ypos = 727, yanchor = 0)
            if (light2Sound==0):
                play soundP02 llLightOn2
                $light2Sound +=1
            
    if if1in1:
        image LLM_2_tile85 = "B_horizontal.png"
        show LLM_2_tile85 at Position(xpos = 600, xanchor = 0, ypos = 540, yanchor = 0)
        image LLM_2_tile86 = "B_horizontal.png"
        show LLM_2_tile86 at Position(xpos = 675, xanchor = 0, ypos = 540, yanchor = 0)
        image LLM_2_tile87 = "B_horizontal.png"
        show LLM_2_tile87 at Position(xpos = 851, xanchor = 0, ypos = 540, yanchor = 0)
        image LLM_2_tile88 = "W_corner_LB.png"
        show LLM_2_tile88 at Position(xpos = 926, xanchor = 0, ypos = 517, yanchor = 0)
        image LLM_2_tile89 = "B_vertical_short.png"
        show LLM_2_tile89 at Position(xpos = 947, xanchor = 0, ypos = 592, yanchor = 0)
        if(while1in2):
            image LLM_2_tileS55 = "B_vertical_short.png"
            show LLM_2_tileS55 at Position(xpos = 947, xanchor = 0, ypos = 675, yanchor = 0)

    if not(while1in2 and if2in1):
        if(light2Sound==1):
            play soundP02 llLightOff2
            $light2Sound -=1

    if while1in2:
        image LLM_2_tile90 = "g_while_on.png"
        show LLM_2_tile90 at Position(xpos = 947, xanchor = 0, ypos = 642, yanchor = 0)
        image LLM_2_tile93 = "G_horizontal_ll.png"
        show LLM_2_tile93 at Position(xpos = 425, xanchor = 0, ypos = 542, yanchor = 0)  
        image LLM_2_tile94 = "G_horizontal_ll.png"
        show LLM_2_tile94 at Position(xpos = 350, xanchor = 0, ypos = 542, yanchor = 0) 
        image LLM_2_tile96 = "G_vertical_ll.png"
        show LLM_2_tile96 at Position(xpos = 298, xanchor = 0, ypos = 591, yanchor = 0) 
        image LLM_2_tile97 = "G_vertical_short.png"
        show LLM_2_tile97 at Position(xpos = 298, xanchor = 0, ypos = 666, yanchor = 0)
        image LLM_2_tile98 = "G_vertical_short.png"
        show LLM_2_tile98 at Position(xpos = 298, xanchor = 0, ypos = 716, yanchor = 0)
        image LLM_2_tile101 = "G_horizontal_ll.png"
        show LLM_2_tile101 at Position(xpos = 351, xanchor = 0, ypos = 785, yanchor = 0)
        image LLM_2_tile102 = "G_horizontal_ll.png"
        show LLM_2_tile102 at Position(xpos = 426, xanchor = 0, ypos = 785, yanchor = 0)
        if (charge1_sound1==0):
            play soundP05 llCharge
            $charge1_sound1 +=1
            
        image LLM_2_tile104 = "y_horizontal_short_on.png"
        show LLM_2_tile104 at Position(xpos = 897, xanchor = 0, ypos = 643, yanchor = 0)
        image LLM_2_tile105 = "y_horizontal_short_on.png"
        show LLM_2_tile105 at Position(xpos = 827, xanchor = 0, ypos = 643, yanchor = 0)
        image LLM_2_tile106 = "y_horizontal_short_on.png"
        show LLM_2_tile106 at Position(xpos = 762, xanchor = 0, ypos = 643, yanchor = 0)
        image LLM_2_tile107 = "y_vertical_short_on.png"
        show LLM_2_tile107 at Position(xpos = 755, xanchor = 0, ypos = 650, yanchor = 0)
        image LLM_2_tile108 = "y_vertical_short_on.png"
        show LLM_2_tile108 at Position(xpos = 755, xanchor = 0, ypos = 700, yanchor = 0)
        image LLM_2_tile109 = "y_vertical_short_on.png"
        show LLM_2_tile109 at Position(xpos = 755, xanchor = 0, ypos = 755, yanchor = 0)
        image LLM_2_tile110 = "y_horizontal_short_on.png"
        show LLM_2_tile110 at Position(xpos = 722, xanchor = 0, ypos = 784, yanchor = 0)
        image LLM_2_tile111 = "y_horizontal_short_on.png"
        show LLM_2_tile111 at Position(xpos = 665, xanchor = 0, ypos = 784, yanchor = 0)
        image LLM_2_tile112 = "y_horizontal_short_on.png"
        show LLM_2_tile112 at Position(xpos = 600, xanchor = 0, ypos = 784, yanchor = 0)

    if while1in2 == False:
        if(charge1_sound1==1):
            $charge1_sound1 -=1

    if if2in2:
        show LLM_2_tile93 at Position(xpos = 425, xanchor = 0, ypos = 542, yanchor = 0)  
        show LLM_2_tile94 at Position(xpos = 350, xanchor = 0, ypos = 542, yanchor = 0) 
        show LLM_2_tile96 at Position(xpos = 298, xanchor = 0, ypos = 591, yanchor = 0) 
        show LLM_2_tile97 at Position(xpos = 298, xanchor = 0, ypos = 666, yanchor = 0)
        show LLM_2_tile98 at Position(xpos = 298, xanchor = 0, ypos = 716, yanchor = 0)
        show LLM_2_tile101 at Position(xpos = 351, xanchor = 0, ypos = 785, yanchor = 0)
        show LLM_2_tile102 at Position(xpos = 426, xanchor = 0, ypos = 785, yanchor = 0)

    if if1in2:
        image LLM_2_tile120 = "B_horizontal.png"
        show LLM_2_tile120 at Position(xpos = 425, xanchor = 0, ypos = 542, yanchor = 0)  
        image LLM_2_tile121 = "B_horizontal.png"
        show LLM_2_tile121 at Position(xpos = 350, xanchor = 0, ypos = 542, yanchor = 0) 
        image LLM_2_tile122 = "B_vertical.png"
        show LLM_2_tile122 at Position(xpos = 298, xanchor = 0, ypos = 591, yanchor = 0) 
        image LLM_2_tile123 = "B_vertical_short.png"
        show LLM_2_tile123 at Position(xpos = 298, xanchor = 0, ypos = 666, yanchor = 0)
        image LLM_2_tile124 = "B_vertical_short.png"
        show LLM_2_tile124 at Position(xpos = 298, xanchor = 0, ypos = 716, yanchor = 0)
        image LLM_2_tile125 = "B_horizontal.png"
        show LLM_2_tile125 at Position(xpos = 351, xanchor = 0, ypos = 785, yanchor = 0)
        image LLM_2_tile126 = "B_horizontal.png"
        show LLM_2_tile126 at Position(xpos = 426, xanchor = 0, ypos = 785, yanchor = 0)

        
#win conditions ********
    if (if1in3) and else1in4 and (if2in1) and (while1in2):
        image LLM_2_tile60 = "B_end_on.png"
        show LLM_2_tile60 at Position(xpos = 750, xanchor = 0, ypos = 253, yanchor = 0)
        image LLM_2_tile61 = "G_end_on.png"
        show LLM_2_tile61 at Position(xpos = 176, xanchor = 0, ypos = 370, yanchor = 0)
        image LLM_2_tile63 = "G_end_on.png"
        show LLM_2_tile63 at Position(xpos = 915, xanchor = 0, ypos = 725, yanchor = 0)

        image LLM_2_tile64 = "B_if.png"
        show LLM_2_tile64 at Position(xpos = 500, xanchor = 0, ypos = 253, yanchor = 0)
        image LLM_2_tile65 = "G_if.png"
        show LLM_2_tile65 at Position(xpos = 750, xanchor = 0, ypos = 510, yanchor = 0)
        image LLM_2_tile66 = "G_else.png"
        show LLM_2_tile66 at Position(xpos = 350, xanchor = 0, ypos = 373, yanchor = 0) 
        image LLM_2_tile67 = "G_while.png"
        show LLM_2_tile67 at Position(xpos = 500, xanchor = 0, ypos = 750, yanchor = 0)
        queue sound llWin
        $renpy.pause(1.0)
        if(puzzleGallery):
            jump pg_llMedWin
        hide LLM_2_tile60
        hide LLM_2_tile61
        hide LLM_2_tile63
        hide LLM_2_tile64
        hide LLM_2_tile65
        hide LLM_2_tile66
        hide LLM_2_tile67
        jump llMedWin

    if attempts == 0:
        show LLM_2_tile64 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
        show LLM_2_tile65 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
        show LLM_2_tile66 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0) 
        show LLM_2_tile67 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
        queue sound llLose
        $renpy.pause(1.5)
        if(puzzleGallery):
            $repeat_number = 2
            jump pg_llMedLose
        $llMed_attempts+=1
        hide LLM_2_tile60
        hide LLM_2_tile61
        hide LLM_2_tile63
        hide LLM_2_tile64
        hide LLM_2_tile65
        hide LLM_2_tile66
        hide LLM_2_tile67
        jump llMedLose
    
    jump gamefile_llm2

screen loopLogicMed_2Scr:
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
        action Jump("hints_llMed_2")
        hover_sound "audio/ENHF_UI_Button_v2.ogg"
        activate_sound "audio/ENHF_UI_Button_v1.ogg"
    imagebutton:
        idle "button_empty2.png"
        xpos 1463
        ypos 295
    imagebutton:
        idle "G_if_idle.png"
        xpos 1445
        ypos 685
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
        xpos 1625
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
                drag_name "G_if_gate"
                child "G_if.png"
                droppable False
                dragged gate_dragged
                xpos if2x ypos if2y  

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
                drag_name "G_if_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1435 ypos 675

            drag:
                drag_name "G_else_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1615 ypos 535

            drag:
                drag_name "While_gate_green_return"
                child "placeholder3.png"
                draggable False
                xpos 1615 ypos 675

