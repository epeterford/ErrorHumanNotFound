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

label loopLogic_med1: #start
    $config.skipping=None
    $quick_menu = False
    $game_menu = True
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    scene bg looplogic_bg
    
    image LLM_1_tile1 = "Start.png"
    show LLM_1_tile1 at Position(xpos = 550, xanchor = 0, ypos = 465, yanchor = 0)   

    # right of start
    image LLM_1_tile2 = "B_horizontal.png"
    show LLM_1_tile2 at Position(xpos = 650, xanchor = 0, ypos = 468, yanchor = 0)
    image LLM_1_tile3 = "B_horizontal.png"
    show LLM_1_tile3 at Position(xpos = 725, xanchor = 0, ypos = 468, yanchor = 0)
    image LLM_1_tile4 = "G_horizontal_ll.png"
    show LLM_1_tile4 at Position(xpos = 650, xanchor = 0, ypos = 535, yanchor = 0)
    image LLM_1_tile5 = "G_horizontal_ll.png"
    show LLM_1_tile5 at Position(xpos = 725, xanchor = 0, ypos = 535, yanchor = 0)
    image LLM_1_tile6 = "W_connect_vertical.png"
    show LLM_1_tile6 at Position(xpos = 765, xanchor = 0, ypos = 465, yanchor = 0)
    
    # top part of connect
    image LLM_1_tile7 = "W_vertical_short.png"
    show LLM_1_tile7 at Position(xpos = 804, xanchor = 0, ypos = 416, yanchor = 0)
    image LLM_1_tile8 = "blank_node.png"
    show LLM_1_tile8 at Position(xpos = 770, xanchor = 0, ypos = 320, yanchor = 0)
    image LLM_1_tile9 = "W_vertical_short.png"
    show LLM_1_tile9 at Position(xpos = 805, xanchor = 0, ypos = 270, yanchor = 0)
    image LLM_1_tile10 = "B_end_off.png"
    show LLM_1_tile10 at Position(xpos = 770, xanchor = 0, ypos = 168, yanchor = 0)
    
    # right of connect
    image LLM_1_tile11 = "W_horizontal_short.png"
    show LLM_1_tile11 at Position(xpos = 832, xanchor = 0, ypos = 468, yanchor = 0)
    image LLM_1_tile12 = "W_horizontal_short.png"
    show LLM_1_tile12 at Position(xpos = 832, xanchor = 0, ypos = 535, yanchor = 0)
    image LLM_1_tile13 = "blank_node.png"
    show LLM_1_tile13 at Position(xpos = 881, xanchor = 0, ypos = 465, yanchor = 0)
    image LLM_1_tile14 = "W_horizontal_short.png"
    show LLM_1_tile14 at Position(xpos = 982, xanchor = 0, ypos = 500, yanchor = 0)
    image LLM_1_tile15 = "G_end_off.png"
    show LLM_1_tile15 at Position(xpos = 1029, xanchor = 0, ypos = 465, yanchor = 0)


    # top of start
    image LLM_1_tile16 = "W_vertical.png"
    show LLM_1_tile16 at Position(xpos = 585, xanchor = 0, ypos = 390, yanchor = 0)
    image LLM_1_tile17 = "W_corner_LB.png"
    show LLM_1_tile17 at Position(xpos = 563, xanchor = 0, ypos = 314, yanchor = 0)
    image LLM_1_tile18 = "W_horizontal.png"
    show LLM_1_tile18 at Position(xpos = 487, xanchor = 0, ypos = 341, yanchor = 0)
    image LLM_1_tile19 = "blank_node.png"
    show LLM_1_tile19 at Position(xpos = 387, xanchor = 0, ypos = 300, yanchor = 0)
    image LLM_1_tile20 = "W_horizontal_short.png"
    show LLM_1_tile20 at Position(xpos = 337, xanchor = 0, ypos = 338, yanchor = 0)
    image LLM_1_tile21 = "B_end_off.png"
    show LLM_1_tile21 at Position(xpos = 237, xanchor = 0, ypos = 300, yanchor = 0)


    # left of start
    image LLM_1_tile22 = "G_horizontal_ll.png"
    show LLM_1_tile22 at Position(xpos = 475, xanchor = 0, ypos = 495, yanchor = 0)  
    image LLM_1_tile23 = "G_horizontal_ll.png"
    show LLM_1_tile23 at Position(xpos = 400, xanchor = 0, ypos = 495, yanchor = 0) 
    image LLM_1_tile24 = "G_horizontal_ll.png"
    show LLM_1_tile24 at Position(xpos = 325, xanchor = 0, ypos = 495, yanchor = 0) 
    image LLM_1_tile25 = "W_corner_RB.png"
    show LLM_1_tile25 at Position(xpos = 250, xanchor = 0, ypos = 470, yanchor = 0) 
    image LLM_1_tile26 = "G_vertical_ll.png"
    show LLM_1_tile26 at Position(xpos = 274, xanchor = 0, ypos = 546, yanchor = 0) 
    image LLM_1_tile27 = "G_vertical_short.png"
    show LLM_1_tile27 at Position(xpos = 274, xanchor = 0, ypos = 621, yanchor = 0)


    # bottom of start
    image LLM_1_tile28 = "W_vertical.png"
    show LLM_1_tile28 at Position(xpos = 585, xanchor = 0, ypos = 565, yanchor = 0)  
    #image LLM_1_tile28 = "B_vertical_short.png"
    #show LLM_1_tile28 at Position(xpos = 529, xanchor = 0, ypos = 640, yanchor = 0) 
    image LLM_1_tile29 = "W_corner_LT.png"
    show LLM_1_tile29 at Position(xpos = 563, xanchor = 0, ypos = 640, yanchor = 0) 
    #image LLM_1_tile30 = "B_horizontal_short.png"
    #show LLM_1_tile30 at Position(xpos = 459, xanchor = 0, ypos = 662, yanchor = 0)
    image LLM_1_tile31 = "blank_node.png"
    show LLM_1_tile31 at Position(xpos = 411, xanchor = 0, ypos = 630, yanchor = 0)
    #image LLM_1_tile32 = "W_horizontal_short.png"
    #show LLM_1_tile32 at Position(xpos = 429, xanchor = 0, ypos = 662, yanchor = 0)
    image LLM_1_tile33 = "W_horizontal_short.png"
    show LLM_1_tile33 at Position(xpos = 513, xanchor = 0, ypos = 662, yanchor = 0)
    image LLM_1_tile34 = "y_horizontal_short_off.png"
    show LLM_1_tile34 at Position(xpos = 360, xanchor = 0, ypos = 663, yanchor = 0)
    image LLM_1_tile35 = "y_horizontal_short_off.png"
    show LLM_1_tile35 at Position(xpos = 290, xanchor = 0, ypos = 663, yanchor = 0)

    # left bottom
    image LLM_1_tile36 = "b_while_off.png"
    show LLM_1_tile36 at Position(xpos = 275, xanchor = 0, ypos = 662, yanchor = 0)
    image LLM_1_tile37 = "W_vertical.png"
    show LLM_1_tile37 at Position(xpos = 277, xanchor = 0, ypos = 694, yanchor = 0)
    image LLM_1_tile38 = "G_end_off.png"
    show LLM_1_tile38 at Position(xpos = 243, xanchor = 0, ypos = 770, yanchor = 0)  
    

    
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
            

    $ gate1x = 770
    $ gate1y = 320

    $ gate2x = 881
    $ gate2y = 465

    $ gate3x = 387
    $ gate3y = 300

    $ gate4x = 411
    $ gate4y = 630
   
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
 
    jump gamefile_llm1
    
    
label gamefile_llm1:
    $config.skipping=None
    $renpy.block_rollback()
    #calls game screen
    call screen loopLogicMed_1Scr




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

        if slot_name == "while_gate_blue_return":
            $ while1x = 1625
            $ while1y = 685
            $ while1in1 = False
            $ while1in2 = False
            $ while1in3 = False
            $ while1in4 = False



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

            if slot_name == "B_if_gate_return" and (gate_name == "B_if_gate" or gate_name == "G_if_gate" or gate_name == "G_else_gate" or gate_name == "While_gate"):
                $ attempts +=1
            if slot_name == "G_if_gate_return" and (gate_name == "B_if_gate" or gate_name == "G_if_gate" or gate_name == "G_else_gate" or gate_name == "While_gate"):
                $ attempts +=1
            if slot_name == "G_else_gate_return" and (gate_name == "B_if_gate" or gate_name == "G_if_gate" or gate_name == "G_else_gate" or gate_name == "While_gate"):
                $ attempts +=1
            if slot_name == "while_gate_blue_return" and (gate_name == "B_if_gate" or gate_name == "G_if_gate" or gate_name == "G_else_gate" or gate_name == "While_gate"):
                $ attempts +=1




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
    if if2in2 == True:
        image LLM_1_tile40 = "G_horizontal_short.png"
        show LLM_1_tile40 at Position(xpos = 832, xanchor = 0, ypos = 535, yanchor = 0)
        image LLM_1_tile41 = "G_horizontal_short.png"
        show LLM_1_tile41 at Position(xpos = 982, xanchor = 0, ypos = 500, yanchor = 0)
        image LLM_1_tile42 = "G_end_on.png"
        show LLM_1_tile42 at Position(xpos = 1029, xanchor = 0, ypos = 465, yanchor = 0)
        if (light2Sound==0):
            play soundP02 llLightOn2
            $light2Sound +=1
        if else1in1 == True or if1in1 == True:
            #show LLE_2_tile44 at Position(xpos = 594, xanchor = 0, ypos = 640, yanchor = 0)
            image LLM_1_tile44 = "B_vertical_short.png"
            show LLM_1_tile44 at Position(xpos = 804, xanchor = 0, ypos = 416, yanchor = 0)
            image LLM_1_tile45 = "B_vertical_short.png"
            show LLM_1_tile45 at Position(xpos = 805, xanchor = 0, ypos = 270, yanchor = 0)
            image LLM_1_tile43 = "B_connect_node.png"
            show LLM_1_tile43 at Position(xpos = 800, xanchor = 0, ypos = 465, yanchor = 0)
            image LLM_1_tile46 = "B_end_on.png"
            show LLM_1_tile46 at Position(xpos = 770, xanchor = 0, ypos = 168, yanchor = 0)
            if (light1Sound==0):
                play soundP01 llLightOn1
                $light1Sound +=1

        if else1in1 == False and if1in1 == False:
            hide LLM_1_tile43
            hide LLM_1_tile44
            hide LLM_1_tile45
            hide LLM_1_tile46
            if(light1Sound==1):
                play soundP01 llLightOff1
                $light1Sound -=1
   
    if if2in2 == False:
        hide LLM_1_tile40
        hide LLM_1_tile41
        hide LLM_1_tile42
        hide LLM_1_tile43
        hide LLM_1_tile44
        hide LLM_1_tile45
        hide LLM_1_tile46
        if(light2Sound==1):
            play soundP02 llLightOff2
            $light2Sound -+1
        if(light1Sound==1):
            play soundP01 llLightOff1
            $light1Sound -=1

    if if1in2 == True:
        image LLM_1_tile82 = "B_horizontal_short.png"
        show LLM_1_tile82 at Position(xpos = 832, xanchor = 0, ypos = 468, yanchor = 0)
        image LLM_1_tile83 = "B_horizontal_short.png"
        show LLM_1_tile83 at Position(xpos = 982, xanchor = 0, ypos = 500, yanchor = 0)
        
        if else1in1 == True or if2in1 == True:
            image LLM_1_tile84 = "G_vertical_short.png"
            show LLM_1_tile84 at Position(xpos = 800, xanchor = 0, ypos = 416, yanchor = 0)
            image LLM_1_tile85 = "G_vertical_short.png"
            show LLM_1_tile85 at Position(xpos = 800, xanchor = 0, ypos = 270, yanchor = 0)
            image LLM_1_tile87 = "G_connect_pipe_vertical.png"
            show LLM_1_tile87 at Position(xpos = 810, xanchor = 0, ypos = 490, yanchor = 0)
            image LLM_1_tile86 = "G_connect_node.png"
            show LLM_1_tile86 at Position(xpos = 800, xanchor = 0, ypos = 465, yanchor = 0)
            image LLM_1_tile88 = "G_connect_node.png"
            show LLM_1_tile88 at Position(xpos = 800, xanchor = 0, ypos = 532, yanchor = 0)


        if else1in1 == False and if2in1 == False:
            hide LLM_1_tile84
            hide LLM_1_tile85
            hide LLM_1_tile86
            hide LLM_1_tile87
            hide LLM_1_tile88
   
    if if1in2 == False:
        hide LLM_1_tile82
        hide LLM_1_tile83
        hide LLM_1_tile84
        hide LLM_1_tile85
        hide LLM_1_tile86
        hide LLM_1_tile87
        hide LLM_1_tile88


    if if1in3 == True:
        image LLM_1_tile68 = "B_vertical.png"
        show LLM_1_tile68 at Position(xpos = 585, xanchor = 0, ypos = 390, yanchor = 0)
        image LLM_1_tile69 = "B_horizontal.png"
        show LLM_1_tile69 at Position(xpos = 487, xanchor = 0, ypos = 341, yanchor = 0)
        image LLM_1_tile50 = "B_horizontal_short.png"
        show LLM_1_tile50 at Position(xpos = 335, xanchor = 0, ypos = 338, yanchor = 0)
        image LLM_1_tile51 = "B_end_on.png"
        show LLM_1_tile51 at Position(xpos = 235, xanchor = 0, ypos = 300, yanchor = 0)
        if(light3Sound==0):
            play soundP03 llLightOn3
            $light3Sound +=1
    if if1in3 == False:
        hide LLM_1_tile50
        hide LLM_1_tile51
        hide LLM_1_tile68
        hide LLM_1_tile69
        if(light3Sound==1):
            play soundP03 llLightOff3
            $light3Sound -=1

    if if2in3 == True:
        image LLM_1_tile70 = "G_vertical_ll.png"
        show LLM_1_tile70 at Position(xpos = 585, xanchor = 0, ypos = 390, yanchor = 0)
        image LLM_1_tile71 = "G_horizontal_ll.png"
        show LLM_1_tile71 at Position(xpos = 487, xanchor = 0, ypos = 341, yanchor = 0)
        image LLM_1_tile72 = "G_horizontal_short.png"
        show LLM_1_tile72 at Position(xpos = 335, xanchor = 0, ypos = 338, yanchor = 0)
        
    if if2in3 == False:
        hide LLM_1_tile70
        hide LLM_1_tile71
        hide LLM_1_tile72


    if while1in4 == True or if1in4 == True:
        image LLM_1_tile52 = "B_vertical.png"
        show LLM_1_tile52 at Position(xpos = 585, xanchor = 0, ypos = 565, yanchor = 0)   
        image LLM_1_tile54 = "B_horizontal_short.png"
        show LLM_1_tile54 at Position(xpos = 513, xanchor = 0, ypos = 662, yanchor = 0)
        image LLM_1_tile55 = "y_horizontal_short_on.png"
        show LLM_1_tile55 at Position(xpos = 360, xanchor = 0, ypos = 663, yanchor = 0)
        image LLM_1_tile53 = "y_horizontal_short_on.png"
        show LLM_1_tile53 at Position(xpos = 290, xanchor = 0, ypos = 663, yanchor = 0)
        image LLM_1_tile74 = "b_while_on.png"
        show LLM_1_tile74 at Position(xpos = 275, xanchor = 0, ypos = 662, yanchor = 0)
        image LLM_1_tile75 = "G_vertical_ll.png"
        show LLM_1_tile75 at Position(xpos = 277, xanchor = 0, ypos = 694, yanchor = 0)
        image LLM_1_tile76 = "G_end_on.png"
        show LLM_1_tile76 at Position(xpos = 243, xanchor = 0, ypos = 770, yanchor = 0) 
        if (light4Sound==0):
            play soundP04 llLightOn1
            $light4Sound +=1

    if while1in4 == False and if1in4 == False:
        hide LLM_1_tile52
        hide LLM_1_tile53
        hide LLM_1_tile54
        hide LLM_1_tile55
        hide LLM_1_tile74
        hide LLM_1_tile75
        hide LLM_1_tile76
        if (light4Sound==1):
            play soundP04 llLightOff1
            $light4Sound -=1

    if if2in4 == True:
        image LLM_1_tile77 = "G_vertical_ll.png"
        show LLM_1_tile77 at Position(xpos = 585, xanchor = 0, ypos = 565, yanchor = 0)   
        image LLM_1_tile78 = "G_horizontal_short.png"
        show LLM_1_tile78 at Position(xpos = 513, xanchor = 0, ypos = 662, yanchor = 0)
        image LLM_1_tile79 = "G_horizontal_short.png"
        show LLM_1_tile79 at Position(xpos = 360, xanchor = 0, ypos = 663, yanchor = 0)
        image LLM_1_tile80 = "G_horizontal_ll.png"
        show LLM_1_tile80 at Position(xpos = 285, xanchor = 0, ypos = 663, yanchor = 0)
        image LLM_1_tile81 = "W_connect_node.png"
        show LLM_1_tile81 at Position(xpos = 275, xanchor = 0, ypos = 662, yanchor = 0)

    if if2in4 == False:
        hide LLM_1_tile77
        hide LLM_1_tile78
        hide LLM_1_tile79
        hide LLM_1_tile80
        hide LLM_1_tile81
  
#win conditions ********
    if (if2in2 == True) and else1in1 == True and (if1in3 == True) and (while1in4 == True):
        image LLM_1_tile60 = "G_end_on.png"
        show LLM_1_tile60 at Position(xpos = 1029, xanchor = 0, ypos = 465, yanchor = 0)
        image LLM_1_tile61 = "B_end_on.png"
        show LLM_1_tile61 at Position(xpos = 770, xanchor = 0, ypos = 168, yanchor = 0)
        image LLM_1_tile62 = "B_end_on.png"
        show LLM_1_tile62 at Position(xpos = 237, xanchor = 0, ypos = 300, yanchor = 0)
        image LLM_1_tile63 = "G_end_on.png"
        show LLM_1_tile63 at Position(xpos = 243, xanchor = 0, ypos = 770, yanchor = 0)

        image LLM_1_tile64 = "B_if.png"
        show LLM_1_tile64 at Position(xpos = 387, xanchor = 0, ypos = 300, yanchor = 0)
        image LLM_1_tile65 = "G_if.png"
        show LLM_1_tile65 at Position(xpos = 881, xanchor = 0, ypos = 465, yanchor = 0)
        image LLM_1_tile66 = "G_else.png"
        show LLM_1_tile66 at Position(xpos = 770, xanchor = 0, ypos = 320, yanchor = 0)
        image LLM_1_tile67 = "B_while.png"
        show LLM_1_tile67 at Position(xpos = 411, xanchor = 0, ypos = 630, yanchor = 0)
        queue sound llWin
        $renpy.pause(1.0)
        hide LLM_1_tile60
        hide LLM_1_tile61
        hide LLM_1_tile62
        hide LLM_1_tile63
        hide LLM_1_tile64
        hide LLM_1_tile65
        hide LLM_1_tile66
        hide LLM_1_tile67
        jump llMedWin

    if attempts == 0:
        show LLM_1_tile64 at Position(xpos = if1x, xanchor = 0, ypos = if1y, yanchor = 0)
        show LLM_1_tile65 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
        show LLM_1_tile66 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
        show LLM_1_tile67 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
        queue sound llLose
        $renpy.pause(1.5)
        $llMed_attempts +=1
        hide LLM_1_tile60
        hide LLM_1_tile61
        hide LLM_1_tile62
        hide LLM_1_tile63
        hide LLM_1_tile64
        hide LLM_1_tile65
        hide LLM_1_tile66
        hide LLM_1_tile67
        jump llMedLose
    
    jump gamefile_llm1

screen loopLogicMed_1Scr:
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
        action Jump("hints_llMed_1")
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
        idle "B_while_idle.png"
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
                child "B_while.png"
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
                drag_name "while_gate_blue_return"
                child "placeholder3.png"
                draggable False
                xpos 1615 ypos 675

