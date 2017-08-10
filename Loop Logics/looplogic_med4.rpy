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

label loopLogic_med4: #loopLogic_easy5
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    scene bg looplogic_bg
    
    image LLM_4_tile1 = "Start.png"
    show LLM_4_tile1 at Position(xpos = 600, xanchor = 0, ypos = 515, yanchor = 0)

    # top of start
    image LLM_4_tile2 = "G_vertical_ll.png"
    show LLM_4_tile2 at Position(xpos = 630, xanchor = 0, ypos = 440, yanchor = 0)
    image LLM_4_tile3 = "G_vertical_ll.png"
    show LLM_4_tile3 at Position(xpos = 630, xanchor = 0, ypos = 365, yanchor = 0)
    image LLM_4_tile4 = "blank_node.png"
    show LLM_4_tile4 at Position(xpos = 600, xanchor = 0, ypos = 265, yanchor = 0)

    # right of start
    image LLM_4_tile5 = "G_horizontal_ll.png"
    show LLM_4_tile5 at Position(xpos = 700, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_4_tile6 = "G_horizontal_ll.png"
    show LLM_4_tile6 at Position(xpos = 775, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_4_tile7 = "W_connect_node.png"
    show LLM_4_tile7 at Position(xpos = 850, xanchor = 0, ypos = 550, yanchor = 0)

    # top part of connect
    image LLM_4_tile8 = "W_vertical.png"
    show LLM_4_tile8 at Position(xpos = 850, xanchor = 0, ypos = 470, yanchor = 0)
    image LLM_4_tile9 = "W_vertical.png"
    show LLM_4_tile9 at Position(xpos = 850, xanchor = 0, ypos = 370, yanchor = 0)
    image LLM_4_tile10 = "W_corner_LB.png"
    show LLM_4_tile10 at Position(xpos = 829, xanchor = 0, ypos = 270, yanchor = 0)
    image LLM_4_tile11 = "W_horizontal_short.png"
    show LLM_4_tile11 at Position(xpos = 765, xanchor = 0, ypos = 293, yanchor = 0)
    image LLM_4_tile12 = "W_horizontal_short.png"
    show LLM_4_tile12 at Position(xpos = 700, xanchor = 0, ypos = 293, yanchor = 0)

    # right of connect
    image LLM_4_tile13 = "W_horizontal.png"
    show LLM_4_tile13 at Position(xpos = 882, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_4_tile14 = "W_connect_node.png"
    show LLM_4_tile14 at Position(xpos = 957, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_4_tile15 = "W_horizontal.png"
    show LLM_4_tile15 at Position(xpos = 990, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_4_tile16 = "G_end_off.png"
    show LLM_4_tile16 at Position(xpos = 1059, xanchor = 0, ypos = 515, yanchor = 0)

    # bottom of start
    image LLM_4_tile17 = "G_vertical_ll.png"
    show LLM_4_tile17 at Position(xpos = 630, xanchor = 0, ypos = 615, yanchor = 0)  
    image LLM_4_tile18 = "G_vertical_ll.png"
    show LLM_4_tile18 at Position(xpos = 630, xanchor = 0, ypos = 690, yanchor = 0)
    image LLM_4_tile19 = "G_corner_RT.png"
    show LLM_4_tile19 at Position(xpos = 608, xanchor = 0, ypos = 765, yanchor = 0) 
    image LLM_4_tile20 = "G_horizontal_ll.png"
    show LLM_4_tile20 at Position(xpos = 683, xanchor = 0, ypos = 786, yanchor = 0)
    image LLM_4_tile21 = "blank_node.png"
    show LLM_4_tile21 at Position(xpos = 761, xanchor = 0, ypos = 750, yanchor = 0)
    image LLM_4_tile22 = "W_horizontal_short.png"
    show LLM_4_tile22 at Position(xpos = 872, xanchor = 0, ypos = 788, yanchor = 0)
    image LLM_4_tile23 = "W_corner_LT.png"
    show LLM_4_tile23 at Position(xpos = 938, xanchor = 0, ypos = 766, yanchor = 0)

    # bottom of connect
    image LLM_4_tile24 = "W_Vertical_short.png"
    show LLM_4_tile24 at Position(xpos = 957, xanchor = 0, ypos = 590, yanchor = 0)
    image LLM_4_tile25 = "W_Vertical_short.png"
    show LLM_4_tile25 at Position(xpos = 957, xanchor = 0, ypos = 650, yanchor = 0)
    image LLM_4_tile26 = "W_Vertical_short.png"
    show LLM_4_tile26 at Position(xpos = 957, xanchor = 0, ypos = 710, yanchor = 0)

    # left of start
    image LLM_4_tile27 = "G_horizontal_ll.png"
    show LLM_4_tile27 at Position(xpos = 525, xanchor = 0, ypos = 515, yanchor = 0)  
    image LLM_4_tile28 = "G_horizontal_short.png"
    show LLM_4_tile28 at Position(xpos = 475, xanchor = 0, ypos = 515, yanchor = 0) 
    image LLM_4_tile29 = "B_horizontal.png"
    show LLM_4_tile29 at Position(xpos = 525, xanchor = 0, ypos = 580, yanchor = 0)  
    image LLM_4_tile30 = "B_horizontal_short.png"
    show LLM_4_tile30 at Position(xpos = 475, xanchor = 0, ypos = 580, yanchor = 0) 
    image LLM_4_tile31 = "W_connect_vertical.png"
    show LLM_4_tile31 at Position(xpos = 415, xanchor = 0, ypos = 513, yanchor = 0)
    image LLM_4_tile32 = "W_horizontal_short.png"
    show LLM_4_tile32 at Position(xpos = 398, xanchor = 0, ypos = 515, yanchor = 0) 
    image LLM_4_tile33 = "W_horizontal_short.png"
    show LLM_4_tile33 at Position(xpos = 397, xanchor = 0, ypos = 580, yanchor = 0)
    image LLM_4_tile34 = "blank_node.png"
    show LLM_4_tile34 at Position(xpos = 295, xanchor = 0, ypos = 515, yanchor = 0)
    image LLM_4_tile35 = "W_horizontal_short.png"
    show LLM_4_tile35 at Position(xpos = 245, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_4_tile36 = "B_end_off.png"
    show LLM_4_tile36 at Position(xpos = 145, xanchor = 0, ypos = 515, yanchor = 0)

    #top of connected nodes for start left
    image LLM_4_tile37 = "W_vertical.png"
    show LLM_4_tile37 at Position(xpos = 448, xanchor = 0, ypos = 438, yanchor = 0)
    image LLM_4_tile38 = "blank_node.png"
    show LLM_4_tile38 at Position(xpos = 413, xanchor = 0, ypos = 338, yanchor = 0)
    image LLM_4_tile39 = "W_vertical_short.png"
    show LLM_4_tile39 at Position(xpos = 448, xanchor = 0, ypos = 288, yanchor = 0)
    image LLM_4_tile40 = "G_end_off.png"
    show LLM_4_tile40 at Position(xpos = 418, xanchor = 0, ypos = 185, yanchor = 0)

        
    
    
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
            

    $ gate1x = 600
    $ gate1y = 265

    $ gate2x = 761
    $ gate2y = 750

    $ gate3x = 295
    $ gate3y = 515

    $ gate4x = 413
    $ gate4y = 338
   
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
 
    jump gamefile_llm4
    
    
label gamefile_llm4:
    
    #calls game screen
    call screen logicGatesMA1




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

            #if if1x == gate3x and if1y == gate3y:
            #    $ attempts -= 1
            #    "[attempts]"
            
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

            #if if1x == gate3x and if1y == gate3y:
            #    $ attempts -= 1
            #    "[attempts]"

            
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

            #if if1x == gate3x and if1y == gate3y:
            #    $ attempts -= 1
            #    "[attempts]"


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

            #if if1x == gate3x and if1y == gate3y:
            #    $ attempts -= 1
            #    "[attempts]"



    #"[gate_name] [slot_name] [temp_slot] [temp_gate]"
    if temp_slot == "" and temp_gate == "" and slot_name != "":
            $ temp_slot = slot_name
            $ temp_gate = gate_name
            $ attempts -=1
            #"empty"
    else:
        if slot_name != "":
            if (temp_slot != slot_name and gate_name == temp_gate) or (temp_slot == slot_name and gate_name != temp_gate) or (temp_slot != slot_name and gate_name != temp_gate):
                $ attempts -=1
                $ temp_slot = slot_name
                $ temp_gate = gate_name
                #"main loop"


#*******************************************
#************image zone********************* 
#*******************************************

#    #if 1 section*******************************************************************************************     
    if if1in3 == True:
        image LLM_4_tile57 = "B_horizontal_short.png"
        show LLM_4_tile57 at Position(xpos = 245, xanchor = 0, ypos = 550, yanchor = 0)
        image LLM_4_tile41 = "B_horizontal_short.png"
        show LLM_4_tile41 at Position(xpos = 397, xanchor = 0, ypos = 580, yanchor = 0)
        image LLM_4_tile42 = "B_end_on.png"
        show LLM_4_tile42 at Position(xpos = 145, xanchor = 0, ypos = 515, yanchor = 0)
        
        if else1in4 == True:
            image LLM_4_tile43 = "G_connect_node.png"
            show LLM_4_tile43 at Position(xpos = 448, xanchor = 0, ypos = 512, yanchor = 0)
            #show LLE_2_tile44 at Position(xpos = 594, xanchor = 0, ypos = 640, yanchor = 0)
            image LLM_4_tile44 = "G_vertical_ll.png"
            show LLM_4_tile44 at Position(xpos = 448, xanchor = 0, ypos = 438, yanchor = 0)
            image LLM_4_tile45 = "G_vertical_short.png"
            show LLM_4_tile45 at Position(xpos = 448, xanchor = 0, ypos = 288, yanchor = 0)
            image LLM_4_tile46 = "G_end_on.png"
            show LLM_4_tile46 at Position(xpos = 418, xanchor = 0, ypos = 185, yanchor = 0)


        if else1in4 == False:
            hide LLM_4_tile43
            hide LLM_4_tile44
            hide LLM_4_tile45
            hide LLM_4_tile46
   
    if if1in3 == False:
        hide LLM_4_tile57
        hide LLM_4_tile41
        hide LLM_4_tile42
        hide LLM_4_tile43
        hide LLM_4_tile44
        hide LLM_4_tile45
        hide LLM_4_tile46


    if if2in1 == True:
        image LLM_4_tile50 = "G_connect_node.png"
        show LLM_4_tile50 at Position(xpos = 850, xanchor = 0, ypos = 550, yanchor = 0)
        image LLM_4_tile51 = "G_horizontal_ll.png"
        show LLM_4_tile51 at Position(xpos = 882, xanchor = 0, ypos = 550, yanchor = 0)

        if while1in2 == True:
            image LLM_4_tile52 = "G_connect_node.png"
            show LLM_4_tile52 at Position(xpos = 957, xanchor = 0, ypos = 550, yanchor = 0)
            image LLM_4_tile53 = "G_horizontal_ll.png"
            show LLM_4_tile53 at Position(xpos = 990, xanchor = 0, ypos = 550, yanchor = 0)
            image LLM_4_tile54 = "G_end_on.png"
            show LLM_4_tile54 at Position(xpos = 1059, xanchor = 0, ypos = 515, yanchor = 0)

        if while1in2 == False:
            hide LLM_4_tile52
            hide LLM_4_tile53
            hide LLM_4_tile54

    if if2in1 == False:
        hide LLM_4_tile50
        hide LLM_4_tile51
        hide LLM_4_tile52
        hide LLM_4_tile53
        hide LLM_4_tile54


        
#win conditions ********
    if (if1in3 == True) and else1in4 == True and (if2in1 == True) and (while1in2 == True):
        image LLM_4_tile60 = "B_end_on.png"
        show LLM_4_tile60 at Position(xpos = 145, xanchor = 0, ypos = 515, yanchor = 0)
        image LLM_4_tile61 = "G_connect_node.png"
        show LLM_4_tile61 at Position(xpos = 448, xanchor = 0, ypos = 512, yanchor = 0)
        image LLM_4_tile62 = "G_end_on.png"
        show LLM_4_tile62 at Position(xpos = 418, xanchor = 0, ypos = 185, yanchor = 0)
        image LLM_4_tile63 = "G_connect_node.png"
        show LLM_4_tile63 at Position(xpos = 850, xanchor = 0, ypos = 550, yanchor = 0)
        image LLM_4_tile68 = "G_connect_node.png"
        show LLM_4_tile68 at Position(xpos = 957, xanchor = 0, ypos = 550, yanchor = 0)
        image LLM_4_tile69 = "G_end_on.png"
        show LLM_4_tile69 at Position(xpos = 1059, xanchor = 0, ypos = 515, yanchor = 0)

        image LLM_4_tile64 = "B_if.png"
        show LLM_4_tile64 at Position(xpos = 295, xanchor = 0, ypos = 515, yanchor = 0)
        image LLM_4_tile65 = "G_if.png"
        show LLM_4_tile65 at Position(xpos = 600, xanchor = 0, ypos = 265, yanchor = 0)
        image LLM_4_tile66 = "G_else.png"
        show LLM_4_tile66 at Position(xpos = 413, xanchor = 0, ypos = 338, yanchor = 0)
        image LLM_4_tile67 = "R_if.png"
        show LLM_4_tile67 at Position(xpos = 761, xanchor = 0, ypos = 750, yanchor = 0)

        "game"
        jump loopLogic_med4

    #if slot_name == "null":
    #    $attempts +=1

        
    #$ attempts -= 1
    if attempts == 0:


        "you lose try again"
        jump loopLogic_med4
    
    jump gamefile_llm4

screen logicGatesMA1:
    
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
                child "R_if.png"
                droppable False
                dragged gate_dragged
                xpos while1x ypos while1y  

            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover.png"
                #child "Placeholder2.png"
                draggable False
                xpos gate1x ypos gate1y
           
            drag:
                drag_name "gate slot two"
                child "cover.png"
                #child "Placeholder2.png"
                draggable False
                xpos gate2x ypos gate2y
                
            drag:
                drag_name "gate slot three"
                child "cover.png"
                #child "Placeholder2.png"
                draggable False
                xpos gate3x ypos gate3y

            drag:
                drag_name "gate slot four"
                child "cover.png"
                #child "Placeholder2.png"
                draggable False
                xpos gate4x ypos gate4y

