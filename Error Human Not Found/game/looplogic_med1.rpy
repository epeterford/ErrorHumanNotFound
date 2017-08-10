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
        #return True 
        return

init:
    image bg looplogic_bg = "LoopLogic_background.png"

label loopLogic_med1: #loopLogic_easy5
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    scene bg looplogic_bg
    
    image LLM_1_tile1 = "Start.png"
    show LLM_1_tile1 at Position(xpos = 550, xanchor = 0, ypos = 465, yanchor = 0)   

    # right of start
    image LLM_1_tile2 = "B_horizontal.png"
    show LLM_1_tile2 at Position(xpos = 650, xanchor = 0, ypos = 465, yanchor = 0)
    image LLM_1_tile3 = "B_horizontal.png"
    show LLM_1_tile3 at Position(xpos = 725, xanchor = 0, ypos = 465, yanchor = 0)
    image LLM_1_tile4 = "G_horizontal_ll.png"
    show LLM_1_tile4 at Position(xpos = 650, xanchor = 0, ypos = 530, yanchor = 0)
    image LLM_1_tile5 = "G_horizontal_ll.png"
    show LLM_1_tile5 at Position(xpos = 725, xanchor = 0, ypos = 530, yanchor = 0)
    image LLM_1_tile6 = "W_connect_vertical.png"
    show LLM_1_tile6 at Position(xpos = 766, xanchor = 0, ypos = 465, yanchor = 0)
    
    # top part of connect
    image LLM_1_tile7 = "W_vertical_short.png"
    show LLM_1_tile7 at Position(xpos = 800, xanchor = 0, ypos = 420, yanchor = 0)
    image LLM_1_tile8 = "blank_node.png"
    show LLM_1_tile8 at Position(xpos = 770, xanchor = 0, ypos = 320, yanchor = 0)
    image LLM_1_tile9 = "W_vertical_short.png"
    show LLM_1_tile9 at Position(xpos = 800, xanchor = 0, ypos = 270, yanchor = 0)
    image LLM_1_tile10 = "B_end_off.png"
    show LLM_1_tile10 at Position(xpos = 770, xanchor = 0, ypos = 168, yanchor = 0)
    
    # right of connect
    image LLM_1_tile11 = "W_horizontal_short.png"
    show LLM_1_tile11 at Position(xpos = 832, xanchor = 0, ypos = 465, yanchor = 0)
    image LLM_1_tile12 = "W_horizontal_short.png"
    show LLM_1_tile12 at Position(xpos = 832, xanchor = 0, ypos = 532, yanchor = 0)
    image LLM_1_tile13 = "blank_node.png"
    show LLM_1_tile13 at Position(xpos = 881, xanchor = 0, ypos = 465, yanchor = 0)
    image LLM_1_tile14 = "W_horizontal_short.png"
    show LLM_1_tile14 at Position(xpos = 982, xanchor = 0, ypos = 500, yanchor = 0)
    image LLM_1_tile15 = "G_end_off.png"
    show LLM_1_tile15 at Position(xpos = 1029, xanchor = 0, ypos = 465, yanchor = 0)


    # top of start
    image LLM_1_tile16 = "B_vertical.png"
    show LLM_1_tile16 at Position(xpos = 580, xanchor = 0, ypos = 390, yanchor = 0)
    image LLM_1_tile17 = "B_corner_LB.png"
    show LLM_1_tile17 at Position(xpos = 558, xanchor = 0, ypos = 315, yanchor = 0)
    image LLM_1_tile18 = "B_horizontal.png"
    show LLM_1_tile18 at Position(xpos = 483, xanchor = 0, ypos = 338, yanchor = 0)
    image LLM_1_tile19 = "blank_node.png"
    show LLM_1_tile19 at Position(xpos = 385, xanchor = 0, ypos = 300, yanchor = 0)
    image LLM_1_tile20 = "W_horizontal_short.png"
    show LLM_1_tile20 at Position(xpos = 335, xanchor = 0, ypos = 338, yanchor = 0)
    image LLM_1_tile21 = "B_end_off.png"
    show LLM_1_tile21 at Position(xpos = 235, xanchor = 0, ypos = 300, yanchor = 0)


    # left of start
    image LLM_1_tile22 = "G_horizontal_ll.png"
    show LLM_1_tile22 at Position(xpos = 475, xanchor = 0, ypos = 495, yanchor = 0)  
    image LLM_1_tile23 = "G_horizontal_ll.png"
    show LLM_1_tile23 at Position(xpos = 400, xanchor = 0, ypos = 495, yanchor = 0) 
    image LLM_1_tile24 = "G_horizontal_ll.png"
    show LLM_1_tile24 at Position(xpos = 325, xanchor = 0, ypos = 495, yanchor = 0) 
    image LLM_1_tile25 = "G_corner_RB.png"
    show LLM_1_tile25 at Position(xpos = 250, xanchor = 0, ypos = 473, yanchor = 0) 
    image LLM_1_tile26 = "G_vertical_ll.png"
    show LLM_1_tile26 at Position(xpos = 273, xanchor = 0, ypos = 548, yanchor = 0) 
    image LLM_1_tile27 = "G_vertical_short.png"
    show LLM_1_tile27 at Position(xpos = 272, xanchor = 0, ypos = 623, yanchor = 0)


    # bottom of start
    image LLM_1_tile28 = "B_vertical.png"
    show LLM_1_tile28 at Position(xpos = 580, xanchor = 0, ypos = 565, yanchor = 0)  
    #image LLM_1_tile28 = "B_vertical_short.png"
    #show LLM_1_tile28 at Position(xpos = 529, xanchor = 0, ypos = 640, yanchor = 0) 
    image LLM_1_tile29 = "B_corner_LT.png"
    show LLM_1_tile29 at Position(xpos = 559, xanchor = 0, ypos = 640, yanchor = 0) 
    #image LLM_1_tile30 = "B_horizontal_short.png"
    #show LLM_1_tile30 at Position(xpos = 459, xanchor = 0, ypos = 662, yanchor = 0)
    image LLM_1_tile31 = "blank_node.png"
    show LLM_1_tile31 at Position(xpos = 460, xanchor = 0, ypos = 630, yanchor = 0)
    image LLM_1_tile32 = "W_horizontal_short3.png"
    show LLM_1_tile32 at Position(xpos = 429, xanchor = 0, ypos = 662, yanchor = 0)
    image LLM_1_tile33 = "W_horizontal_short3.png"
    show LLM_1_tile33 at Position(xpos = 384, xanchor = 0, ypos = 662, yanchor = 0)
    image LLM_1_tile34 = "W_horizontal_short3.png"
    show LLM_1_tile34 at Position(xpos = 344, xanchor = 0, ypos = 662, yanchor = 0)
    image LLM_1_tile35 = "W_horizontal_short3.png"
    show LLM_1_tile35 at Position(xpos = 304, xanchor = 0, ypos = 662, yanchor = 0)

    # left bottom
    image LLM_1_tile36 = "W_connect_node.png"
    show LLM_1_tile36 at Position(xpos = 275, xanchor = 0, ypos = 662, yanchor = 0)
    image LLM_1_tile37 = "W_vertical.png"
    show LLM_1_tile37 at Position(xpos = 274, xanchor = 0, ypos = 695, yanchor = 0)
    image LLM_1_tile38 = "G_end_off.png"
    show LLM_1_tile38 at Position(xpos = 243, xanchor = 0, ypos = 772, yanchor = 0)  
    
    
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

    $ gate3x = 385
    $ gate3y = 300

    $ gate4x = 460
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
    if if2in2 == True:
        image LLM_1_tile40 = "G_horizontal_short.png"
        show LLM_1_tile40 at Position(xpos = 832, xanchor = 0, ypos = 532, yanchor = 0)
        image LLM_1_tile41 = "G_horizontal_short.png"
        show LLM_1_tile41 at Position(xpos = 982, xanchor = 0, ypos = 500, yanchor = 0)
        image LLM_1_tile42 = "G_end_on.png"
        show LLM_1_tile42 at Position(xpos = 1029, xanchor = 0, ypos = 465, yanchor = 0)
        
        if else1in1 == True:
            image LLM_1_tile43 = "B_connect_node.png"
            show LLM_1_tile43 at Position(xpos = 800, xanchor = 0, ypos = 465, yanchor = 0)
            #show LLE_2_tile44 at Position(xpos = 594, xanchor = 0, ypos = 640, yanchor = 0)
            image LLM_1_tile44 = "B_vertical_short.png"
            show LLM_1_tile44 at Position(xpos = 800, xanchor = 0, ypos = 420, yanchor = 0)
            image LLM_1_tile45 = "B_vertical_short.png"
            show LLM_1_tile45 at Position(xpos = 800, xanchor = 0, ypos = 270, yanchor = 0)
            image LLM_1_tile46 = "B_end_on.png"
            show LLM_1_tile46 at Position(xpos = 770, xanchor = 0, ypos = 168, yanchor = 0)


        if else1in1 == False:
            hide LLM_1_tile43
            hide LLM_1_tile44
            hide LLM_1_tile45
            hide LLM_1_tile46
   
    if if2in2 == False:
        hide LLM_1_tile40
        hide LLM_1_tile41
        hide LLM_1_tile42
        hide LLM_1_tile43
        hide LLM_1_tile44
        hide LLM_1_tile45
        hide LLM_1_tile46


    if if1in3 == True:
        image LLM_1_tile50 = "B_horizontal_short.png"
        show LLM_1_tile50 at Position(xpos = 335, xanchor = 0, ypos = 338, yanchor = 0)
        image LLM_1_tile51 = "B_end_on.png"
        show LLM_1_tile51 at Position(xpos = 235, xanchor = 0, ypos = 300, yanchor = 0)
        
    if if1in3 == False:
        hide LLM_1_tile50
        hide LLM_1_tile51

    if while1in4 == True:
        image LLM_1_tile52 = "B_horizontal.png"
        show LLM_1_tile52 at Position(xpos = 384, xanchor = 0, ypos = 662, yanchor = 0)
        image LLM_1_tile53 = "B_connect_node.png"
        show LLM_1_tile53 at Position(xpos = 275, xanchor = 0, ypos = 662, yanchor = 0)
        image LLM_1_tile54 = "G_vertical_ll.png"
        show LLM_1_tile54 at Position(xpos = 274, xanchor = 0, ypos = 695, yanchor = 0)
        image LLM_1_tile55 = "G_end_on.png"
        show LLM_1_tile55 at Position(xpos = 243, xanchor = 0, ypos = 772, yanchor = 0)

    if while1in4 == False:
        hide LLM_1_tile52
        hide LLM_1_tile53
        hide LLM_1_tile54
        hide LLM_1_tile55
  
#win conditions ********
    if (if2in2 == True) and else1in1 == True and (if1in3 == True) and (while1in4 == True):
        image LLM_1_tile60 = "G_end_on.png"
        show LLM_1_tile60 at Position(xpos = 1029, xanchor = 0, ypos = 465, yanchor = 0)
        image LLM_1_tile61 = "B_end_on.png"
        show LLM_1_tile61 at Position(xpos = 770, xanchor = 0, ypos = 168, yanchor = 0)
        image LLM_1_tile62 = "B_end_on.png"
        show LLM_1_tile62 at Position(xpos = 235, xanchor = 0, ypos = 300, yanchor = 0)
        image LLM_1_tile63 = "G_end_on.png"
        show LLM_1_tile63 at Position(xpos = 243, xanchor = 0, ypos = 772, yanchor = 0)

        image LLM_1_tile64 = "B_if.png"
        show LLM_1_tile64 at Position(xpos = 385, xanchor = 0, ypos = 300, yanchor = 0)
        image LLM_1_tile65 = "G_if.png"
        show LLM_1_tile65 at Position(xpos = 881, xanchor = 0, ypos = 465, yanchor = 0)
        image LLM_1_tile66 = "G_else.png"
        show LLM_1_tile66 at Position(xpos = 770, xanchor = 0, ypos = 320, yanchor = 0)
        image LLM_1_tile67 = "R_if.png"
        show LLM_1_tile67 at Position(xpos = 460, xanchor = 0, ypos = 630, yanchor = 0)

        "game"
        jump loopLogic_med1

    #if slot_name == "null":
    #    $attempts +=1

        
    #$ attempts -= 1
    if attempts == 0:


        "you lose try again"
        jump loopLogic_med1
    
    jump gamefile_llm1

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

