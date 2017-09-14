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

label loopLogic_med5: #start
    $config.skipping=None
    $quick_menu = False
    $game_menu = True
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    scene bg looplogic_bg
    
    image LLM_5_tile1 = "Start.png"
    show LLM_5_tile1 at Position(xpos = 600, xanchor = 0, ypos = 450, yanchor = 0)  


    image LLM_5_tile2 = "W_corner_LB.png"
    show LLM_5_tile2 at Position(xpos = 575, xanchor = 0, ypos = 375, yanchor = 0)
    image LLM_5_tile3 = "W_horizontal.png"
    show LLM_5_tile3 at Position(xpos = 500, xanchor = 0, ypos = 402, yanchor = 0)
    image LLM_5_tile4 = "W_horizontal.png"
    show LLM_5_tile4 at Position(xpos = 425, xanchor = 0, ypos = 402, yanchor = 0)
    
    image LLM_5_tile5 = "B_vertical.png"
    show LLM_5_tile5 at Position(xpos = 634, xanchor = 0, ypos = 375, yanchor = 0)
    image LLM_5_tile6 = "W_vertical.png"
    show LLM_5_tile6 at Position(xpos = 634, xanchor = 0, ypos = 300, yanchor = 0)
    
    # Right of start
    image LLM_5_tile7 = "W_horizontal.png"
    show LLM_5_tile7 at Position(xpos = 700, xanchor = 0, ypos = 484, yanchor = 0)
    image LLM_5_tile8 = "W_horizontal.png"
    show LLM_5_tile8 at Position(xpos = 775, xanchor = 0, ypos = 484, yanchor = 0)
    image LLM_5_tile9 = "W_horizontal.png"
    show LLM_5_tile9 at Position(xpos = 850, xanchor = 0, ypos = 484, yanchor = 0)
    image LLM_5_tile10 = "W_horizontal.png"
    show LLM_5_tile10 at Position(xpos = 925, xanchor = 0, ypos = 484, yanchor = 0)
    image LLM_5_tile11 = "W_corner_LT.png"
    show LLM_5_tile11 at Position(xpos = 1000, xanchor = 0, ypos = 462, yanchor = 0)
    image LLM_5_tile12 = "W_vertical_short.png"
    show LLM_5_tile12 at Position(xpos = 1021, xanchor = 0, ypos = 412, yanchor = 0)
    
    image LLM_5_tile13 = "W_horizontal.png"
    show LLM_5_tile13 at Position(xpos = 695, xanchor = 0, ypos = 595, yanchor = 0)
    
    #Bottom of start
    image LLM_5_tile14 = "G_vertical_short.png"
    show LLM_5_tile14 at Position(xpos = 600, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_5_tile15 = "B_vertical_short.png"
    show LLM_5_tile15 at Position(xpos = 667, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_5_tile16 = "W_connect_horizontal.png"
    show LLM_5_tile16 at Position(xpos = 600, xanchor = 0, ypos = 560, yanchor = 0)
    image LLM_5_tile17 = "W_vertical_short.png"
    show LLM_5_tile17 at Position(xpos = 600, xanchor = 0, ypos = 625, yanchor = 0)
    image LLM_5_tile18 = "W_vertical_short.png"
    show LLM_5_tile18 at Position(xpos = 667, xanchor = 0, ypos = 625, yanchor = 0)
    
    image LLM_5_tile19 = "W_horizontal.png"
    show LLM_5_tile19 at Position(xpos = 945, xanchor = 0, ypos = 595, yanchor = 0)
    image LLM_5_tile20 = "W_horizontal.png"
    show LLM_5_tile20 at Position(xpos = 870, xanchor = 0, ypos = 595, yanchor = 0)
    
    #Bottom left connect node
    image LLM_5_tile21 = "W_vertical.png"
    show LLM_5_tile21 at Position(xpos = 369, xanchor = 0, ypos = 755, yanchor = 0)
    image LLM_5_tile22 = "W_vertical.png"
    show LLM_5_tile22 at Position(xpos = 369, xanchor = 0, ypos = 680, yanchor = 0)
    
    #RIght of bottom left connect node
    image LLM_5_tile23 = "W_horizontal.png"
    show LLM_5_tile23 at Position(xpos = 375, xanchor = 0, ypos = 678, yanchor = 0)
    image LLM_5_tile24 = "W_horizontal.png"
    show LLM_5_tile24 at Position(xpos = 450, xanchor = 0, ypos = 678, yanchor = 0)
    image LLM_5_tile25 = "W_horizontal.png"
    show LLM_5_tile25 at Position(xpos = 525, xanchor = 0, ypos = 678, yanchor = 0)
    
    #Top of start, Right connect node
    image LLM_5_tile26 = "y_horizontal_short_off.png"
    show LLM_5_tile26 at Position(xpos = 655, xanchor = 0, ypos = 352, yanchor = 0)
    image LLM_5_tile27 = "y_horizontal_short_off.png"
    show LLM_5_tile27 at Position(xpos = 730, xanchor = 0, ypos = 352, yanchor = 0)
    image LLM_5_tile28 = "y_horizontal_short_off.png"
    show LLM_5_tile28 at Position(xpos = 805, xanchor = 0, ypos = 352, yanchor = 0)
    image LLM_5_tile29 = "y_horizontal_short_off.png"
    show LLM_5_tile29 at Position(xpos = 880, xanchor = 0, ypos = 352, yanchor = 0)
    image LLM_5_tile30 = "y_horizontal_short_off.png"
    show LLM_5_tile30 at Position(xpos = 955, xanchor = 0, ypos = 352, yanchor = 0)
    
    image LLM_5_tile31 = "y_vertical_short_off.png"
    show LLM_5_tile31 at Position(xpos = 369, xanchor = 0, ypos = 625, yanchor = 0)
    image LLM_5_tile32 = "y_vertical_short_off.png"
    show LLM_5_tile32 at Position(xpos = 369, xanchor = 0, ypos = 550, yanchor = 0)
    image LLM_5_tile33 = "y_vertical_short_off.png"
    show LLM_5_tile33 at Position(xpos = 369, xanchor = 0, ypos = 478, yanchor = 0)

    image LLM_5_tile34 = "blank_node.png"
    show LLM_5_tile34 at Position(xpos = 990, xanchor = 0, ypos = 310, yanchor = 0)
    image LLM_5_tile35 = "blank_node.png"
    show LLM_5_tile35 at Position(xpos = 325, xanchor = 0, ypos = 375, yanchor = 0)
    image LLM_5_tile36 = "blank_node.png"
    show LLM_5_tile36 at Position(xpos = 600, xanchor = 0, ypos = 670, yanchor = 0)
    image LLM_5_tile37 = "blank_node.png"
    show LLM_5_tile37 at Position(xpos = 770, xanchor = 0, ypos = 560, yanchor = 0)


    #*********************************************************
    #********************** end points ***********************
    #*********************************************************    
    image LLM_5_tile38 = "B_end_off.png"
    show LLM_5_tile38 at Position(xpos = 600, xanchor = 0, ypos = 200, yanchor = 0)
    image LLM_5_tile39 = "B_end_off.png"
    show LLM_5_tile39 at Position(xpos = 1000, xanchor = 0, ypos = 561, yanchor = 0)
    image LLM_5_tile40 = "G_end_off.png"
    show LLM_5_tile40 at Position(xpos = 340, xanchor = 0, ypos = 800, yanchor = 0)
    
    #*********************************************************
    #********************** conectors ************************
    #*********************************************************    
    image LLM_5_tile41 = "g_while_off.png"
    show LLM_5_tile41 at Position(xpos = 634, xanchor = 0, ypos = 350, yanchor = 0)
    image LLM_5_tile42 = "b_while_off.png"
    show LLM_5_tile42 at Position(xpos = 369, xanchor = 0, ypos = 675, yanchor = 0)

        
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        


    #initial value assignment for dragables
    $ while2x = 1445
    $ while2y = 545

    $ if2x = 1445
    $ if2y = 685
    
    $ else1x = 1625
    $ else1y = 545

    $ while1x = 1625
    $ while1y = 685
            

    $ gate1x = 990
    $ gate1y = 310

    $ gate2x = 325
    $ gate2y = 375

    $ gate3x = 600
    $ gate3y = 670

    $ gate4x = 770
    $ gate4y = 560
   
    # check conditons for locations
    $ while2in1 = False
    $ while2in2 = False
    $ while2in3 = False
    $ while2in4 = False

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
 
    jump gamefile_llm5
    
    
label gamefile_llm5:
    
    #calls game screen
    call screen loopLogicMed_5Scr




#*******************************************
#************image zone********************* 
#*******************************************

    #the first logic gate *******************************************************************************
    if gate_name == "while_gate_blue":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if while2in1 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in1 = False
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
            if while2in2 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in2 = False
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
            if while2in3 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in3 = False
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
            if while2in4 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in4 = False
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
            $ while2x = gate4x
            $ while2y = gate4y
            $ while2in1 = False
            $ while2in2 = False
            $ while2in3 = False
            $ while2in4 = True

        if slot_name == "while_gate_blue_return":
            $ while2x = 1445
            $ while2y = 545
            $ while2in1 = False
            $ while2in2 = False
            $ while2in3 = False
            $ while2in4 = False

            
    #the first logic gate *******************************************************************************
    if gate_name == "G_if_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if while2in1 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in1 = False
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
            if while2in2 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in2 = False
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
            if while2in3 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in3 = False
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
            if while2in4 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in4 = False
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
            if while2in1 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in1 = False
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
            if while2in2 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in2 = False
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
            if while2in3 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in3 = False
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
            if while2in4 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in4 = False
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
    if gate_name == "While_gate_green":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if if2in1 == True:
                $ if2x = 1445
                $ if2y = 685
                $ if2in1 = False
            if while2in1 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in1 = False
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
            if while2in2 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in2 = False
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
            if while2in3 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in3 = False
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
            if while2in4 == True:
                $ while2x = 1445
                $ while2y = 545
                $ while2in4 = False
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

            if slot_name == "while_gate_blue_return" and (gate_name == "while_gate_blue" or gate_name == "G_if_gate" or gate_name == "G_else_gate" or gate_name == "While_gate_green"):
                $ attempts +=1
            if slot_name == "G_if_gate_return" and (gate_name == "while_gate_blue" or gate_name == "G_if_gate" or gate_name == "G_else_gate" or gate_name == "While_gate_green"):
                $ attempts +=1
            if slot_name == "G_else_gate_return" and (gate_name == "while_gate_blue" or gate_name == "G_if_gate" or gate_name == "G_else_gate" or gate_name == "While_gate_green"):
                $ attempts +=1
            if slot_name == "While_gate_green_return" and (gate_name == "while_gate_blue" or gate_name == "G_if_gate" or gate_name == "G_else_gate" or gate_name == "While_gate_green"):
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
    if if2in3 == True:
        image LLM_5_tile43 = "G_vertical_short.png"
        show LLM_5_tile43 at Position(xpos = 600, xanchor = 0, ypos = 625, yanchor = 0)
        image LLM_5_tile44 = "G_horizontal_short.png"
        show LLM_5_tile44 at Position(xpos = 400, xanchor = 0, ypos = 678, yanchor = 0)
        image LLM_5_tile45 = "G_horizontal_ll.png"
        show LLM_5_tile45 at Position(xpos = 450, xanchor = 0, ypos = 678, yanchor = 0)
        image LLM_5_tile46 = "G_horizontal_ll.png"
        show LLM_5_tile46 at Position(xpos = 525, xanchor = 0, ypos = 678, yanchor = 0)
        
        if else1in4 == True:
            image LLM_5_tile47 = "B_connect_node.png"
            show LLM_5_tile47 at Position(xpos = 668, xanchor = 0, ypos = 595, yanchor = 0)
            image LLM_5_tile48 = "B_horizontal.png"
            show LLM_5_tile48 at Position(xpos = 700, xanchor = 0, ypos = 595, yanchor = 0)

            #show LLE_2_tile44 at Position(xpos = 594, xanchor = 0, ypos = 640, yanchor = 0)
            image LLM_5_tile49 = "B_horizontal.png"
            show LLM_5_tile49 at Position(xpos = 945, xanchor = 0, ypos = 595, yanchor = 0)
            image LLM_5_tile50 = "B_horizontal.png"
            show LLM_5_tile50 at Position(xpos = 870, xanchor = 0, ypos = 595, yanchor = 0)
            image LLM_5_tile51 = "B_end_on.png"
            show LLM_5_tile51 at Position(xpos = 1000, xanchor = 0, ypos = 561, yanchor = 0)
            if(light4Sound==0):
                play soundP04 llLightOn1
                $light4Sound +=1
            
        if else1in4 == False:
            hide LLM_5_tile47
            hide LLM_5_tile48
            hide LLM_5_tile49
            hide LLM_5_tile50
            hide LLM_5_tile51
            if(light4Sound==1):
                play soundP04 llLightOff1
                $light4Sound -=1
   
    if if2in3 == False:
        hide LLM_5_tile43
        hide LLM_5_tile44
        hide LLM_5_tile45
        hide LLM_5_tile46
        hide LLM_5_tile47
        hide LLM_5_tile48
        hide LLM_5_tile49
        hide LLM_5_tile50
        hide LLM_5_tile51
        if(light4Sound==1):
            play soundP04 llLightOff1
            $light4Sound -=1

    if while1in1 == True:
        image LLM_5_tile84 = "G_horizontal_ll.png"
        show LLM_5_tile84 at Position(xpos = 700, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile85 = "G_horizontal_ll.png"
        show LLM_5_tile85 at Position(xpos = 775, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile86 = "G_horizontal_ll.png"
        show LLM_5_tile86 at Position(xpos = 850, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile87 = "G_horizontal_ll.png"
        show LLM_5_tile87 at Position(xpos = 925, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile88 = "W_corner_LT.png"
        show LLM_5_tile88 at Position(xpos = 1000, xanchor = 0, ypos = 462, yanchor = 0)
        image LLM_5_tile89 = "G_vertical_Short.png"
        show LLM_5_tile89 at Position(xpos = 1018, xanchor = 0, ypos = 412, yanchor = 0)
        
        image LLM_5_tile53 = "B_vertical.png"
        show LLM_5_tile53 at Position(xpos = 634, xanchor = 0, ypos = 275, yanchor = 0)
        image LLM_5_tile54 = "B_end_on.png"
        show LLM_5_tile54 at Position(xpos = 600, xanchor = 0, ypos = 200, yanchor = 0)
        if(light1Sound==0):
            play soundP01 llLightOn1
            $light1Sound +=1
        image LLM_5_tile79 = "y_horizontal_short_on.png"
        show LLM_5_tile79 at Position(xpos = 655, xanchor = 0, ypos = 352, yanchor = 0)
        image LLM_5_tile80 = "y_horizontal_short_on.png"
        show LLM_5_tile80 at Position(xpos = 730, xanchor = 0, ypos = 352, yanchor = 0)
        image LLM_5_tile81 = "y_horizontal_short_on.png"
        show LLM_5_tile81 at Position(xpos = 805, xanchor = 0, ypos = 352, yanchor = 0)
        image LLM_5_tile82 = "y_horizontal_short_on.png"
        show LLM_5_tile82 at Position(xpos = 880, xanchor = 0, ypos = 352, yanchor = 0)
        image LLM_5_tile83 = "y_horizontal_short_on.png"
        show LLM_5_tile83 at Position(xpos = 955, xanchor = 0, ypos = 352, yanchor = 0)
        image LLM_5_tile52 = "g_while_on.png"
        show LLM_5_tile52 at Position(xpos = 634, xanchor = 0, ypos = 350, yanchor = 0)
        if(light2Sound==0):
            play soundP02 llLightOn2
            $light2Sound +=1
    if while1in1 == False:
        hide LLM_5_tile52
        hide LLM_5_tile53
        hide LLM_5_tile54
        hide LLM_5_tile79
        hide LLM_5_tile80
        hide LLM_5_tile81
        hide LLM_5_tile82
        hide LLM_5_tile83
        if(light1Sound==1):
            play soundP01 llLightOff1
            $light1Sound -=1
        if(light2Sound==1):
            play soundP02 llLightOff2
            $light2Sound -=1
        hide LLM_5_tile84
        hide LLM_5_tile85
        hide LLM_5_tile86
        hide LLM_5_tile87
        hide LLM_5_tile88
        hide LLM_5_tile89


    if while2in2 == True and if2in3 == True:
        image LLM_5_tile55 = "b_while_on.png"
        show LLM_5_tile55 at Position(xpos = 369, xanchor = 0, ypos = 675, yanchor = 0)
        image LLM_5_tile56 = "G_vertical_short.png"
        show LLM_5_tile56 at Position(xpos = 369, xanchor = 0, ypos = 705, yanchor = 0)
        image LLM_5_tile57 = "G_vertical_ll.png"
        show LLM_5_tile57 at Position(xpos = 369, xanchor = 0, ypos = 755, yanchor = 0)
        image LLM_5_tile58 = "G_end_on.png"
        show LLM_5_tile58 at Position(xpos = 340, xanchor = 0, ypos = 800, yanchor = 0)
        if(light3Sound==0):
            play soundP03 llLightOn3
            $light3Sound +=1
    if while2in2 == False or if2in3 == False:
        hide LLM_5_tile55
        hide LLM_5_tile56
        hide LLM_5_tile57
        hide LLM_5_tile58
        if(light3Sound==1):
            play soundP03 llLightOff3
            $light3Sound -=1
    if while2in2 == True:
        image LLM_5_tile59 = "B_horizontal.png"
        show LLM_5_tile59 at Position(xpos = 500, xanchor = 0, ypos = 402, yanchor = 0)
        image LLM_5_tile60 = "B_horizontal.png"
        show LLM_5_tile60 at Position(xpos = 425, xanchor = 0, ypos = 402, yanchor = 0)
        
        image LLM_5_tile104 = "y_vertical_short_on.png"
        show LLM_5_tile104 at Position(xpos = 369, xanchor = 0, ypos = 625, yanchor = 0)
        image LLM_5_tile105 = "y_vertical_short_on.png"
        show LLM_5_tile105 at Position(xpos = 369, xanchor = 0, ypos = 550, yanchor = 0)
        image LLM_5_tile106 = "y_vertical_short_on.png"
        show LLM_5_tile106 at Position(xpos = 369, xanchor = 0, ypos = 478, yanchor = 0)
        image LLM_5_tile107 = "b_while_on.png"
        show LLM_5_tile107 at Position(xpos = 369, xanchor = 0, ypos = 675, yanchor = 0)
        if(light5Sound==0):
            play soundP05 llLightOn1
            $light5Sound +=1
    if while2in2 == False:
        hide LLM_5_tile59
        hide LLM_5_tile60
        hide LLM_5_tile104
        hide LLM_5_tile105
        hide LLM_5_tile106
        hide LLM_5_tile107
        if(light5Sound==1):
            play soundP05 llLightOff1
            $light5Sound -=1

    if if2in1 == True:
        image LLM_5_tile90 = "G_horizontal_ll.png"
        show LLM_5_tile90 at Position(xpos = 700, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile91 = "G_horizontal_ll.png"
        show LLM_5_tile91 at Position(xpos = 775, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile92 = "G_horizontal_ll.png"
        show LLM_5_tile92 at Position(xpos = 850, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile93 = "G_horizontal_ll.png"
        show LLM_5_tile93 at Position(xpos = 925, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile94 = "W_corner_LT.png"
        show LLM_5_tile94 at Position(xpos = 1000, xanchor = 0, ypos = 462, yanchor = 0)
        image LLM_5_tile95 = "G_vertical_Short.png"
        show LLM_5_tile95 at Position(xpos = 1018, xanchor = 0, ypos = 412, yanchor = 0)
     
    if if2in1 == False:
        hide LLM_5_tile90
        hide LLM_5_tile91
        hide LLM_5_tile92
        hide LLM_5_tile93
        hide LLM_5_tile94
        hide LLM_5_tile95

    if while2in1 == True:
        image LLM_5_tile96 = "B_horizontal.png"
        show LLM_5_tile96 at Position(xpos = 700, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile97 = "B_horizontal.png"
        show LLM_5_tile97 at Position(xpos = 775, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile98 = "B_horizontal.png"
        show LLM_5_tile98 at Position(xpos = 850, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile99 = "B_horizontal.png"
        show LLM_5_tile99 at Position(xpos = 925, xanchor = 0, ypos = 484, yanchor = 0)
        image LLM_5_tile100 = "W_corner_LT.png"
        show LLM_5_tile100 at Position(xpos = 1000, xanchor = 0, ypos = 462, yanchor = 0)
        image LLM_5_tile101 = "B_vertical_Short.png"
        show LLM_5_tile101 at Position(xpos = 1020, xanchor = 0, ypos = 412, yanchor = 0)
     
    if while2in1 == False:
        hide LLM_5_tile96
        hide LLM_5_tile97
        hide LLM_5_tile98
        hide LLM_5_tile99
        hide LLM_5_tile100
        hide LLM_5_tile101

    if while1in2 == True or if2in2 == True:
        image LLM_5_tile102 = "G_horizontal_ll.png"
        show LLM_5_tile102 at Position(xpos = 500, xanchor = 0, ypos = 402, yanchor = 0)
        image LLM_5_tile103 = "G_horizontal_ll.png"
        show LLM_5_tile103 at Position(xpos = 425, xanchor = 0, ypos = 402, yanchor = 0)

    if while1in2 == False and if2in2 == False:
        hide LLM_5_tile102
        hide LLM_5_tile103

#win conditions ********
    if (if2in3 == True) and else1in4 == True and (while1in1 == True) and (while2in2 == True and if2in3 == True):
        image LLM_5_tile70 = "B_connect_node.png"
        show LLM_5_tile70 at Position(xpos = 668, xanchor = 0, ypos = 595, yanchor = 0)
        image LLM_5_tile71 = "B_end_on.png"
        show LLM_5_tile71 at Position(xpos = 1000, xanchor = 0, ypos = 561, yanchor = 0)
        image LLM_5_tile78 = "g_while_on.png"
        show LLM_5_tile78 at Position(xpos = 634, xanchor = 0, ypos = 350, yanchor = 0)
        image LLM_5_tile72 = "b_while_on.png"
        show LLM_5_tile72 at Position(xpos = 369, xanchor = 0, ypos = 675, yanchor = 0)
        image LLM_5_tile73 = "G_end_on.png"
        show LLM_5_tile73 at Position(xpos = 340, xanchor = 0, ypos = 800, yanchor = 0)

        image LLM_5_tile74 = "B_while.png"
        show LLM_5_tile74 at Position(xpos = 325, xanchor = 0, ypos = 375, yanchor = 0)
        image LLM_5_tile75 = "G_if.png"
        show LLM_5_tile75 at Position(xpos = 600, xanchor = 0, ypos = 670, yanchor = 0)
        image LLM_5_tile76 = "G_else.png"
        show LLM_5_tile76 at Position(xpos = 770, xanchor = 0, ypos = 560, yanchor = 0)
        image LLM_5_tile77 = "G_while.png"
        show LLM_5_tile77 at Position(xpos = 990, xanchor = 0, ypos = 310, yanchor = 0)
        queue sound llWin
        $renpy.pause(1.0)
        hide LLM_5_tile70
        hide LLM_5_tile71
        hide LLM_5_tile72
        hide LLM_5_tile73
        hide LLM_5_tile74
        hide LLM_5_tile75
        hide LLM_5_tile76
        hide LLM_5_tile77
        jump llMedWin

    if attempts == 0:
        show LLM_5_tile74 at Position(xpos = while2x, xanchor = 0, ypos = while2y, yanchor = 0)
        show LLM_5_tile75 at Position(xpos = if2x, xanchor = 0, ypos = if2y, yanchor = 0)
        show LLM_5_tile76 at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
        show LLM_5_tile77 at Position(xpos = while1x, xanchor = 0, ypos = while1y, yanchor = 0)
        queue sound llLose
        $renpy.pause(1.5)
        $llMed_attempts+=1
        hide LLM_5_tile70
        hide LLM_5_tile71
        hide LLM_5_tile72
        hide LLM_5_tile73
        hide LLM_5_tile74
        hide LLM_5_tile75
        hide LLM_5_tile76
        hide LLM_5_tile77
        jump llMedLose
    
    jump gamefile_llm5

screen loopLogicMed_5Scr:
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
        action Jump("hints_llMed_5")
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
        idle "B_while_idle.png"
        xpos 1445
        ypos 545
    imagebutton: 
        idle "G_Else_idle.png"
        xpos 1625
        ypos 545
    imagebutton:
        idle "g_while_idle.png"
        xpos 1625
        ypos 685
    text "Moves" xpos 1480 ypos 315 color "#0060db" font "United Kingdom DEMO.otf" size 25
    text ": " xpos 1605 ypos 304 color "#0060db" font "Bitter-Bold.otf" size 38
    text "[attempts]" xpos 1640 ypos 313 color "#0060db" font "United Kingdom DEMO.otf" size 27
    #drags and drop location
    draggroup:
            #if gates
            drag:
                drag_name "while_gate_blue"
                child "B_while.png"
                droppable False
                dragged gate_dragged
                xpos while2x ypos while2y
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
                drag_name "While_gate_green"
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
                drag_name "while_gate_blue_return"
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

