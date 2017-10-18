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

label loopLogic_hard2: #start
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    $ quick_menu = False
    $ game_menu = True
    scene bg looplogic_bg

    #Down of Top Green End
    image LLH_2_tile9 = "W_vertical.png"
    show LLH_2_tile9 at Position(xpos = 200, xanchor = 0, ypos = 275, yanchor = 0)
    
    #Down of Top Blue End
    image LLH_2_tile10 = "W_vertical.png"
    show LLH_2_tile10 at Position(xpos = 675, xanchor = 0, ypos = 275, yanchor = 0)

    #Down of Gate Down of Top Green End
    image LLH_2_tile11 = "W_vertical.png"
    show LLH_2_tile11 at Position(xpos = 200, xanchor = 0, ypos = 400, yanchor = 0)
    
    #Down of Gate Down of Top Blue End
    image LLH_2_tile12 = "W_vertical.png"
    show LLH_2_tile12 at Position(xpos = 675, xanchor = 0, ypos = 400, yanchor = 0)
    
    #T End
    image LLH_2_tile13 = "W_T_left.png"
    show LLH_2_tile13 at Position(xpos = 130, xanchor = 0, ypos = 508, yanchor = 0)
    
    #Left of Start
    image LLH_2_tile14 = "W_horizontal.png"
    show LLH_2_tile14 at Position(xpos = 250, xanchor = 0, ypos = 470, yanchor = 0)
    image LLH_2_tile15 = "W_horizontal.png"
    show LLH_2_tile15 at Position(xpos = 250, xanchor = 0, ypos = 510, yanchor = 0)
    image LLH_2_tile16 = "W_horizontal.png"
    show LLH_2_tile16 at Position(xpos = 250, xanchor = 0, ypos = 550, yanchor = 0)
    image LLH_2_tile17 = "W_connect_pipe_vertical.png"
    show LLH_2_tile17 at Position(xpos = 324, xanchor = 0, ypos = 480, yanchor = 0)
    image LLH_2_tile18 = "W_connect_pipe_vertical.png"
    show LLH_2_tile18 at Position(xpos = 324, xanchor = 0, ypos = 520, yanchor = 0)
    image LLH_2_tile19 = "R_horizontal_ll.png"
    show LLH_2_tile19 at Position(xpos = 335, xanchor = 0, ypos = 470, yanchor = 0)
    image LLH_2_tile20 = "G_horizontal_ll.png"
    show LLH_2_tile20 at Position(xpos = 335, xanchor = 0, ypos = 510, yanchor = 0)
    image LLH_2_tile21 = "B_horizontal.png"
    show LLH_2_tile21 at Position(xpos = 335, xanchor = 0, ypos = 550, yanchor = 0)
    
    #Right of Start
    image LLH_2_tile22 = "R_horizontal_ll.png"
    show LLH_2_tile22 at Position(xpos = 490, xanchor = 0, ypos = 470, yanchor = 0)
    image LLH_2_tile23 = "G_horizontal_ll.png"
    show LLH_2_tile23 at Position(xpos = 490, xanchor = 0, ypos = 510, yanchor = 0)
    image LLH_2_tile24 = "B_horizontal.png"
    show LLH_2_tile24 at Position(xpos = 490, xanchor = 0, ypos = 550, yanchor = 0)
    image LLH_2_tile25 = "W_connect_pipe_vertical.png"
    show LLH_2_tile25 at Position(xpos = 564, xanchor = 0, ypos = 480, yanchor = 0)
    image LLH_2_tile26 = "W_connect_pipe_vertical.png"
    show LLH_2_tile26 at Position(xpos = 564, xanchor = 0, ypos = 520, yanchor = 0)    
    image LLH_2_tile27 = "W_horizontal.png"
    show LLH_2_tile27 at Position(xpos = 575, xanchor = 0, ypos = 470, yanchor = 0)
    image LLH_2_tile28 = "W_horizontal.png"
    show LLH_2_tile28 at Position(xpos = 575, xanchor = 0, ypos = 510, yanchor = 0)
    image LLH_2_tile29 = "W_horizontal.png"
    show LLH_2_tile29 at Position(xpos = 575, xanchor = 0, ypos = 550, yanchor = 0)
    
    #Right of Gate Right of Start
    image LLH_2_tile30 = "W_horizontal.png"
    show LLH_2_tile30 at Position(xpos = 730, xanchor = 0, ypos = 510, yanchor = 0)
    image LLH_2_tile31 = "W_horizontal.png"
    show LLH_2_tile31 at Position(xpos = 805, xanchor = 0, ypos = 510, yanchor = 0)
    
    #Left of Red End
    image LLH_2_tile32 = "W_horizontal.png"
    show LLH_2_tile32 at Position(xpos = 975, xanchor = 0, ypos = 510, yanchor = 0)
    
    #Down of Gate Left of Red End
    image LLH_2_tile38 = "W_vertical.png"
    show LLH_2_tile38 at Position(xpos = 910, xanchor = 0, ypos = 520, yanchor = 0)
    image LLH_2_tile39 = "W_vertical.png"
    show LLH_2_tile39 at Position(xpos = 910, xanchor = 0, ypos = 595, yanchor = 0)
    image LLH_2_tile40 = "W_horizontal_short.png"
    show LLH_2_tile40 at Position(xpos = 850, xanchor = 0, ypos = 685, yanchor = 0)
    image LLH_2_tile41 = "W_corner_LT.png"
    show LLH_2_tile41 at Position(xpos = 889, xanchor = 0, ypos = 663, yanchor = 0)
    
    #Down of Left Connector
    image LLH_2_tile33 = "W_vertical.png"
    show LLH_2_tile33 at Position(xpos = 315, xanchor = 0, ypos = 575, yanchor = 0)
    
    #Top of Bottom Blue End
    image LLH_2_tile34 = "W_vertical.png"
    show LLH_2_tile34 at Position(xpos = 315, xanchor = 0, ypos = 750, yanchor = 0)
    
    #Down of Right Connector
    image LLH_2_tile35 = "W_vertical.png"
    show LLH_2_tile35 at Position(xpos = 555, xanchor = 0, ypos = 575, yanchor = 0)
    
    #Top of Bottom Green End
    image LLH_2_tile36 = "W_vertical_short.png"
    show LLH_2_tile36 at Position(xpos = 555, xanchor = 0, ypos = 730, yanchor = 0)
    image LLH_2_tile37 = "W_vertical_short.png"
    show LLH_2_tile37 at Position(xpos = 555, xanchor = 0, ypos = 790, yanchor = 0)
    
    #Bottom Dotted Line
    image LLH_2_tile43 = "y_horizontal_short_off.png"
    show LLH_2_tile43 at Position(xpos = 570, xanchor = 0, ypos = 775, yanchor = 0)
    image LLH_2_tile44 = "y_horizontal_short_off.png"
    show LLH_2_tile44 at Position(xpos = 630, xanchor = 0, ypos = 775, yanchor = 0)
    image LLH_2_tile45 = "y_horizontal_short_off.png"
    show LLH_2_tile45 at Position(xpos = 690, xanchor = 0, ypos = 775, yanchor = 0)
    image LLH_2_tile46 = "y_horizontal_short_off.png"
    show LLH_2_tile46 at Position(xpos = 750, xanchor = 0, ypos = 775, yanchor = 0)
    image LLH_2_tile47 = "y_vertical_short_off.png"
    show LLH_2_tile47 at Position(xpos = 790, xanchor = 0, ypos = 740, yanchor = 0)
    
    #*********************************************************
    #********************* start points **********************
    #*********************************************************
    image LLH_2_Start = "Start.png"
    show LLH_2_Start at Position(xpos = 400, xanchor = 0, ypos = 475, yanchor = 0)
    
    #*********************************************************
    #********************** end points ***********************
    #*********************************************************    
    image LLH_2_BlueEnd1 = "B_end_off.png"
    show LLH_2_BlueEnd1 at Position(xpos = 640, xanchor = 0, ypos = 175, yanchor = 0)
    image LLH_2_BlueEnd2 = "B_end_off.png"
    show LLH_2_BlueEnd2 at Position(xpos = 280, xanchor = 0, ypos = 820, yanchor = 0)
    image LLH_2_GreenEnd1 = "G_end_off.png"
    show LLH_2_GreenEnd1 at Position(xpos = 165, xanchor = 0, ypos = 175, yanchor = 0)
    image LLH_2_GreenEnd2 = "G_end_off.png"
    show LLH_2_GreenEnd2 at Position(xpos = 520, xanchor = 0, ypos = 820, yanchor = 0)
    image LLH_2_RedEnd = "R_end_off.png"
    show LLH_2_RedEnd at Position(xpos = 1050, xanchor = 0, ypos = 475, yanchor = 0)

    #*********************************************************
    #********************* connect nodes *********************
    #*********************************************************      
    image LLH_2_tile48 = "W_connect_node.png"
    show LLH_2_tile48 at Position(xpos = 313, xanchor = 0, ypos = 468, yanchor = 0)
    image LLH_2_tile49 = "W_connect_node.png"
    show LLH_2_tile49 at Position(xpos = 313, xanchor = 0, ypos = 508, yanchor = 0)
    image LLH_2_tile50 = "W_connect_node.png"
    show LLH_2_tile50 at Position(xpos = 313, xanchor = 0, ypos = 548, yanchor = 0)
    
    image LLH_2_tile51 = "W_connect_node.png"
    show LLH_2_tile51 at Position(xpos = 553, xanchor = 0, ypos = 468, yanchor = 0)
    image LLH_2_tile52 = "W_connect_node.png"
    show LLH_2_tile52 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0)
    image LLH_2_tile53 = "W_connect_node.png"
    show LLH_2_tile53 at Position(xpos = 553, xanchor = 0, ypos = 548, yanchor = 0)
    
    image LLH_2_tile55 = "r_while_off.png"
    show LLH_2_tile55 at Position(xpos = 553, xanchor = 0, ypos = 772, yanchor = 0)
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    #initial value assignment for dragables
    $ whileRx = 1445
    $ whileRy = 500
    $ else1x = 1585
    $ else1y = 500
    $ else2x = 1585
    $ else2y = 500
    $ ifRx = 1395
    $ ifRy = 645
    $ ifGx = 1525
    $ ifGy = 645
    $ ifBx = 1655
    $ ifBy = 645
    $ ifGRx = 1445
    $ ifGRy = 790
    $ ifBRx = 1585
    $ ifBRy = 790
    

    $ gate1x = 165
    $ gate1y = 325
    $ gate2x = 640
    $ gate2y = 325
    $ gate3x = 165
    $ gate3y = 475
    $ gate4x = 640
    $ gate4y = 475
    $ gate5x = 875
    $ gate5y = 475
    $ gate6x = 280
    $ gate6y = 650
    $ gate7x = 520
    $ gate7y = 650
    $ gate8x = 755
    $ gate8y = 650
    
    image LLH_2_ifRT = "R_if_idle.png"
    image LLH_2_ifGT = "G_if_idle.png"
    image LLH_2_ifBT = "B_if_idle.png"
    image LLH_2_ifGRT = "RG_if_idle.png"
    image LLH_2_ifBRT = "BR_if_idle.png"
    image LLH_2_elseT = "G_else_idle.png"
    image LLH_2_whileRT = "R_while_idle.png"
    show LLH_2_ifRT at Position(xpos = ifRx, xanchor = 0, ypos = ifRy, yanchor = 0)
    show LLH_2_ifGT at Position(xpos = ifGx, xanchor = 0, ypos = ifGy, yanchor = 0)
    show LLH_2_ifBT at Position(xpos = ifBx, xanchor = 0, ypos = ifBy, yanchor = 0)
    show LLH_2_ifGRT at Position(xpos = ifGRx, xanchor = 0, ypos = ifGRy, yanchor = 0)
    show LLH_2_ifBRT at Position(xpos = ifBRx, xanchor = 0, ypos = ifBRy, yanchor = 0)
    show LLH_2_elseT at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLH_2_whileRT at Position(xpos = whileRx, xanchor = 0, ypos = whileRy, yanchor = 0)
   
    # check conditons for locations
    $ whileRin1 = False
    $ whileRin2 = False
    $ whileRin3 = False
    $ whileRin4 = False
    $ whileRin5 = False
    $ whileRin6 = False
    $ whileRin7 = False
    $ whileRin8 = False

    $ else1in1 = False
    $ else1in2 = False
    $ else1in3 = False
    $ else1in4 = False
    $ else1in5 = False
    $ else1in6 = False
    $ else1in7 = False
    $ else1in8 = False
    
    $ else2in1 = False
    $ else2in2 = False
    $ else2in3 = False
    $ else2in4 = False
    $ else2in5 = False
    $ else2in6 = False
    $ else2in7 = False
    $ else2in8 = False
    
    $ ifRin1 = False
    $ ifRin2 = False
    $ ifRin3 = False
    $ ifRin4 = False
    $ ifRin5 = False
    $ ifRin6 = False
    $ ifRin7 = False
    $ ifRin8 = False
    
    $ ifGin1 = False
    $ ifGin2 = False
    $ ifGin3 = False
    $ ifGin4 = False
    $ ifGin5 = False
    $ ifGin6 = False
    $ ifGin7 = False
    $ ifGin8 = False
    
    $ ifBin1 = False
    $ ifBin2 = False
    $ ifBin3 = False
    $ ifBin4 = False
    $ ifBin5 = False
    $ ifBin6 = False
    $ ifBin7 = False
    $ ifBin8 = False
    
    $ ifGRin1 = False
    $ ifGRin2 = False
    $ ifGRin3 = False
    $ ifGRin4 = False
    $ ifGRin5 = False
    $ ifGRin6 = False
    $ ifGRin7 = False
    $ ifGRin8 = False
    
    $ ifBRin1 = False
    $ ifBRin2 = False
    $ ifBRin3 = False
    $ ifBRin4 = False
    $ ifBRin5 = False
    $ ifBRin6 = False
    $ ifBRin7 = False
    $ ifBRin8 = False
    
    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""
     
    #attempts for players
    $ attempts = 10    
    
    #*********************************************************
    #********************** show gates ***********************
    #*********************************************************  
    image LLH_2_tile1 = "blank_node.png"
    show LLH_2_tile1 at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
    image LLH_2_tile2 = "blank_node.png"
    show LLH_2_tile2 at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
    image LLH_2_tile3 = "blank_node.png"
    show LLH_2_tile3 at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
    image LLH_2_tile4 = "blank_node.png"
    show LLH_2_tile4 at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
    image LLH_2_tile5 = "blank_node.png"
    show LLH_2_tile5 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
    image LLH_2_tile6 = "blank_node.png"
    show LLH_2_tile6 at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
    image LLH_2_tile7 = "blank_node.png"
    show LLH_2_tile7 at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
    image LLH_2_tile8 = "blank_node.png"
    show LLH_2_tile8 at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)
 
    jump gamefile_llh2
    
    
label gamefile_llh2:
    
    #calls game screen
    call screen loopLogicHard_2Scr




#*******************************************
#************image zone********************* 
#*******************************************

    #the first logic gate *******************************************************************************
    if gate_name == "if_R_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBRin1 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin1 = False
            if whileRin1 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin1 = False
            if else1in1 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in1 = False
            if else2in1 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in1 = False

            #sets values for checks
            $ ifRx = gate1x
            $ ifRy = gate1y
            $ ifRin1 = True
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBRin2 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin2 = False
            if whileRin2 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin2 = False
            if else1in2 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in2 = False
            if else2in2 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in2 = False

            #sets values for checks
            $ ifRx = gate2x
            $ ifRy = gate2y
            $ ifRin1 = False
            $ ifRin2 = True
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBRin3 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin3 = False
            if whileRin3 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin3 = False
            if else1in3 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in3 = False
            if else2in3 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in3 = False

            #sets values for checks
            $ ifRx = gate3x
            $ ifRy = gate3y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = True
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBRin4 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin4 = False
            if whileRin4 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin4 = False
            if else1in4 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in4 = False
            if else2in4 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in4 = False

            #sets values for checks
            $ ifRx = gate4x
            $ ifRy = gate4y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = True
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBRin5 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin5 = False
            if whileRin5 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin5 = False
            if else1in5 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in5 = False
            if else2in5 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in5 = False

            #sets values for checks
            $ ifRx = gate5x
            $ ifRy = gate5y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = True
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBRin6 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin6 = False
            if whileRin6 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin6 = False
            if else1in6 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in6 = False
            if else2in6 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in6 = False

            #sets values for checks
            $ ifRx = gate6x
            $ ifRy = gate6y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = True
            $ ifRin7 = False
            $ ifRin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBRin7 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin7 = False
            if whileRin7 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin7 = False
            if else1in7 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in7 = False
            if else2in7 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in7 = False

            #sets values for checks
            $ ifRx = gate7x
            $ ifRy = gate7y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = True
            $ ifRin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBRin8 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin8 = False
            if whileRin8 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin8 = False
            if else1in8 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in8 = False
            if else2in8 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in8 = False

            #sets values for checks
            $ ifRx = gate8x
            $ ifRy = gate8y
            $ ifRin1 = False
            $ ifRin2 = False
            $ ifRin3 = False
            $ ifRin4 = False
            $ ifRin5 = False
            $ ifRin6 = False
            $ ifRin7 = False
            $ ifRin8 = True
      
      
    #the second logic gate *******************************************************************************
    if gate_name == "if_G_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifBin1 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBRin1 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin1 = False
            if whileRin1 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin1 = False
            if else1in1 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in1 = False
            if else2in1 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in1 = False

            #sets values for checks
            $ ifGx = gate1x
            $ ifGy = gate1y
            $ ifGin1 = True
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifBin2 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBRin2 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin2 = False
            if whileRin2 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin2 = False
            if else1in2 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in2 = False
            if else2in2 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in2 = False

            #sets values for checks
            $ ifGx = gate2x
            $ ifGy = gate2y
            $ ifGin1 = False
            $ ifGin2 = True
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifBin3 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBRin3 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin3 = False
            if whileRin3 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin3 = False
            if else1in3 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in3 = False
            if else2in3 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in3 = False

            #sets values for checks
            $ ifGx = gate3x
            $ ifGy = gate3y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = True
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifBin4 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBRin4 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin4 = False
            if whileRin4 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin4 = False
            if else1in4 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in4 = False
            if else2in4 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in4 = False

            #sets values for checks
            $ ifGx = gate4x
            $ ifGy = gate4y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = True
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifBin5 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBRin5 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin5 = False
            if whileRin5 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin5 = False
            if else1in5 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in5 = False
            if else2in5 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in5 = False

            #sets values for checks
            $ ifGx = gate5x
            $ ifGy = gate5y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = True
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifBin6 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBRin6 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin6 = False
            if whileRin6 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin6 = False
            if else1in6 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in6 = False
            if else2in6 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in6 = False

            #sets values for checks
            $ ifGx = gate6x
            $ ifGy = gate6y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = True
            $ ifGin7 = False
            $ ifGin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifBin7 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBRin7 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin7 = False
            if whileRin7 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin7 = False
            if else1in7 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in7 = False
            if else2in7 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in7 = False

            #sets values for checks
            $ ifGx = gate7x
            $ ifGy = gate7y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = True
            $ ifGin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifBin8 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBRin8 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin8 = False
            if whileRin8 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin8 = False
            if else1in8 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in8 = False
            if else2in8 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in8 = False

            #sets values for checks
            $ ifGx = gate8x
            $ ifGy = gate8y
            $ ifGin1 = False
            $ ifGin2 = False
            $ ifGin3 = False
            $ ifGin4 = False
            $ ifGin5 = False
            $ ifGin6 = False
            $ ifGin7 = False
            $ ifGin8 = True
            
            
    #the third logic gate *******************************************************************************
    if gate_name == "if_B_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBRin1 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin1 = False
            if whileRin1 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin1 = False
            if else1in1 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in1 = False
            if else2in1 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in1 = False

            #sets values for checks
            $ ifBx = gate1x
            $ ifBy = gate1y
            $ ifBin1 = True
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBRin2 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin2 = False
            if whileRin2 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin2 = False
            if else1in2 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in2 = False
            if else2in2 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in2 = False

            #sets values for checks
            $ ifBx = gate2x
            $ ifBy = gate2y
            $ ifBin1 = False
            $ ifBin2 = True
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBRin3 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin3 = False
            if whileRin3 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin3 = False
            if else1in3 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in3 = False
            if else2in3 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in3 = False

            #sets values for checks
            $ ifBx = gate3x
            $ ifBy = gate3y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = True
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBRin4 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin4 = False
            if whileRin4 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin4 = False
            if else1in4 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in4 = False
            if else2in4 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in4 = False

            #sets values for checks
            $ ifBx = gate4x
            $ ifBy = gate4y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = True
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBRin5 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin5 = False
            if whileRin5 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin5 = False
            if else1in5 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in5 = False
            if else2in5 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in5 = False

            #sets values for checks
            $ ifBx = gate5x
            $ ifBy = gate5y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = True
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBRin6 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin6 = False
            if whileRin6 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin6 = False
            if else1in6 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in6 = False
            if else2in6 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in6 = False

            #sets values for checks
            $ ifBx = gate6x
            $ ifBy = gate6y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = True
            $ ifBin7 = False
            $ ifBin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBRin7 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin7 = False
            if whileRin7 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin7 = False
            if else1in7 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in7 = False
            if else2in7 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in7 = False

            #sets values for checks
            $ ifBx = gate7x
            $ ifBy = gate7y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = True
            $ ifBin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBRin8 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin8 = False
            if whileRin8 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin8 = False
            if else1in8 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in8 = False
            if else2in8 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in8 = False

            #sets values for checks
            $ ifBx = gate8x
            $ ifBy = gate8y
            $ ifBin1 = False
            $ ifBin2 = False
            $ ifBin3 = False
            $ ifBin4 = False
            $ ifBin5 = False
            $ ifBin6 = False
            $ ifBin7 = False
            $ ifBin8 = True


    #the fourth logic gate *******************************************************************************
    if gate_name == "if_GR_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin1 = False
            if ifBRin1 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin1 = False
            if whileRin1 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin1 = False
            if else1in1 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in1 = False
            if else2in1 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in1 = False

            #sets values for checks
            $ ifGRx = gate1x
            $ ifGRy = gate1y
            $ ifGRin1 = True
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin2 = False
            if ifBRin2 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin2 = False
            if whileRin2 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin2 = False
            if else1in2 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in2 = False
            if else2in2 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in2 = False

            #sets values for checks
            $ ifGRx = gate2x
            $ ifGRy = gate2y
            $ ifGRin1 = False
            $ ifGRin2 = True
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin3 = False
            if ifBRin3 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin3 = False
            if whileRin3 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin3 = False
            if else1in3 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in3 = False
            if else2in3 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in3 = False

            #sets values for checks
            $ ifGRx = gate3x
            $ ifGRy = gate3y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = True
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin4 = False
            if ifBRin4 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin4 = False
            if whileRin4 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin4 = False
            if else1in4 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in4 = False
            if else2in4 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in4 = False

            #sets values for checks
            $ ifGRx = gate4x
            $ ifGRy = gate4y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = True
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin5 = False
            if ifBRin5 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin5 = False
            if whileRin5 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin5 = False
            if else1in5 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in5 = False
            if else2in5 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in5 = False

            #sets values for checks
            $ ifGRx = gate5x
            $ ifGRy = gate5y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = True
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin6 = False
            if ifBRin6 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin6 = False
            if whileRin6 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin6 = False
            if else1in6 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in6 = False
            if else2in6 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in6 = False

            #sets values for checks
            $ ifGRx = gate6x
            $ ifGRy = gate6y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = True
            $ ifGRin7 = False
            $ ifGRin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin7 = False
            if ifBRin7 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin7 = False
            if whileRin7 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin7 = False
            if else1in7 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in7 = False
            if else2in7 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in7 = False

            #sets values for checks
            $ ifGRx = gate7x
            $ ifGRy = gate7y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = True
            $ ifGRin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin8 = False
            if ifBRin8 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin8 = False
            if whileRin8 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin8 = False
            if else1in8 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in8 = False
            if else2in8 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in8 = False

            #sets values for checks
            $ ifGRx = gate8x
            $ ifGRy = gate8y
            $ ifGRin1 = False
            $ ifGRin2 = False
            $ ifGRin3 = False
            $ ifGRin4 = False
            $ ifGRin5 = False
            $ ifGRin6 = False
            $ ifGRin7 = False
            $ ifGRin8 = True
            
            
    #the fifth logic gate *******************************************************************************
    if gate_name == "if_BR_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if whileRin1 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin1 = False
            if else1in1 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in1 = False
            if else2in1 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in1 = False

            #sets values for checks
            $ ifBRx = gate1x
            $ ifBRy = gate1y
            $ ifBRin1 = True
            $ ifBRin2 = False
            $ ifBRin3 = False
            $ ifBRin4 = False
            $ ifBRin5 = False
            $ ifBRin6 = False
            $ ifBRin7 = False
            $ ifBRin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if whileRin2 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin2 = False
            if else1in2 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in2 = False
            if else2in2 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in2 = False

            #sets values for checks
            $ ifBRx = gate2x
            $ ifBRy = gate2y
            $ ifBRin1 = False
            $ ifBRin2 = True
            $ ifBRin3 = False
            $ ifBRin4 = False
            $ ifBRin5 = False
            $ ifBRin6 = False
            $ ifBRin7 = False
            $ ifBRin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if whileRin3 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin3 = False
            if else1in3 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in3 = False
            if else2in3 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in3 = False

            #sets values for checks
            $ ifBRx = gate3x
            $ ifBRy = gate3y
            $ ifBRin1 = False
            $ ifBRin2 = False
            $ ifBRin3 = True
            $ ifBRin4 = False
            $ ifBRin5 = False
            $ ifBRin6 = False
            $ ifBRin7 = False
            $ ifBRin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if whileRin4 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin4 = False
            if else1in4 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in4 = False
            if else2in4 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in4 = False

            #sets values for checks
            $ ifBRx = gate4x
            $ ifBRy = gate4y
            $ ifBRin1 = False
            $ ifBRin2 = False
            $ ifBRin3 = False
            $ ifBRin4 = True
            $ ifBRin5 = False
            $ ifBRin6 = False
            $ ifBRin7 = False
            $ ifBRin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if whileRin5 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin5 = False
            if else1in5 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in5 = False
            if else2in5 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in5 = False

            #sets values for checks
            $ ifBRx = gate5x
            $ ifBRy = gate5y
            $ ifBRin1 = False
            $ ifBRin2 = False
            $ ifBRin3 = False
            $ ifBRin4 = False
            $ ifBRin5 = True
            $ ifBRin6 = False
            $ ifBRin7 = False
            $ ifBRin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if whileRin6 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin6 = False
            if else1in6 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in6 = False
            if else2in6 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in6 = False

            #sets values for checks
            $ ifBRx = gate6x
            $ ifBRy = gate6y
            $ ifBRin1 = False
            $ ifBRin2 = False
            $ ifBRin3 = False
            $ ifBRin4 = False
            $ ifBRin5 = False
            $ ifBRin6 = True
            $ ifBRin7 = False
            $ ifBRin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if whileRin7 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin7 = False
            if else1in7 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in7 = False
            if else2in7 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in7 = False

            #sets values for checks
            $ ifBRx = gate7x
            $ ifBRy = gate7y
            $ ifBRin1 = False
            $ ifBRin2 = False
            $ ifBRin3 = False
            $ ifBRin4 = False
            $ ifBRin5 = False
            $ ifBRin6 = False
            $ ifBRin7 = True
            $ ifBRin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if whileRin8 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin8 = False
            if else1in8 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in8 = False
            if else2in8 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in8 = False

            #sets values for checks
            $ ifBRx = gate8x
            $ ifBRy = gate8y
            $ ifBRin1 = False
            $ ifBRin2 = False
            $ ifBRin3 = False
            $ ifBRin4 = False
            $ ifBRin5 = False
            $ ifBRin6 = False
            $ ifBRin7 = False
            $ ifBRin8 = True
            
            
    #the sixth logic gate *******************************************************************************
    if gate_name == "else1_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBRin1 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin1 = False
            if whileRin1 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin1 = False
            if else2in1 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in1 = False

            #sets values for checks
            $ else1x = gate1x
            $ else1y = gate1y
            $ else1in1 = True
            $ else1in2 = False
            $ else1in3 = False
            $ else1in4 = False
            $ else1in5 = False
            $ else1in6 = False
            $ else1in7 = False
            $ else1in8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBRin2 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin2 = False
            if whileRin2 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin2 = False
            if else2in2 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in2 = False

            #sets values for checks
            $ else1x = gate2x
            $ else1y = gate2y
            $ else1in1 = False
            $ else1in2 = True
            $ else1in3 = False
            $ else1in4 = False
            $ else1in5 = False
            $ else1in6 = False
            $ else1in7 = False
            $ else1in8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBRin3 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin3 = False
            if whileRin3 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin3 = False
            if else2in3 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in3 = False

            #sets values for checks
            $ else1x = gate3x
            $ else1y = gate3y
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = True
            $ else1in4 = False
            $ else1in5 = False
            $ else1in6 = False
            $ else1in7 = False
            $ else1in8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBRin4 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin4 = False
            if whileRin4 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin4 = False
            if else2in4 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in4 = False

            #sets values for checks
            $ else1x = gate4x
            $ else1y = gate4y
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = False
            $ else1in4 = True
            $ else1in5 = False
            $ else1in6 = False
            $ else1in7 = False
            $ else1in8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBRin5 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin5 = False
            if whileRin5 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin5 = False
            if else2in5 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in5 = False

            #sets values for checks
            $ else1x = gate5x
            $ else1y = gate5y
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = False
            $ else1in4 = False
            $ else1in5 = True
            $ else1in6 = False
            $ else1in7 = False
            $ else1in8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBRin6 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin6 = False
            if whileRin6 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin6 = False
            if else2in6 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in6 = False

            #sets values for checks
            $ else1x = gate6x
            $ else1y = gate6y
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = False
            $ else1in4 = False
            $ else1in5 = False
            $ else1in6 = True
            $ else1in7 = False
            $ else1in8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBRin7 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin7 = False
            if whileRin7 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin7 = False
            if else2in7 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in7 = False

            #sets values for checks
            $ else1x = gate7x
            $ else1y = gate7y
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = False
            $ else1in4 = False
            $ else1in5 = False
            $ else1in6 = False
            $ else1in7 = True
            $ else1in8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBRin8 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin8 = False
            if whileRin8 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin8 = False
            if else2in8 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in8 = False

            #sets values for checks
            $ else1x = gate8x
            $ else1y = gate8y
            $ else1in1 = False
            $ else1in2 = False
            $ else1in3 = False
            $ else1in4 = False
            $ else1in5 = False
            $ else1in6 = False
            $ else1in7 = False
            $ else1in8 = True


    #the seventh logic gate *******************************************************************************
    if gate_name == "else2_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBRin1 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin1 = False
            if whileRin1 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin1 = False
            if else1in1 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in1 = False

            #sets values for checks
            $ else2x = gate1x
            $ else2y = gate1y
            $ else2in1 = True
            $ else2in2 = False
            $ else2in3 = False
            $ else2in4 = False
            $ else2in5 = False
            $ else2in6 = False
            $ else2in7 = False
            $ else2in8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBRin2 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin2 = False
            if whileRin2 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin2 = False
            if else1in2 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in2 = False

            #sets values for checks
            $ else2x = gate2x
            $ else2y = gate2y
            $ else2in1 = False
            $ else2in2 = True
            $ else2in3 = False
            $ else2in4 = False
            $ else2in5 = False
            $ else2in6 = False
            $ else2in7 = False
            $ else2in8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBRin3 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin3 = False
            if whileRin3 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin3 = False
            if else1in3 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in3 = False

            #sets values for checks
            $ else2x = gate3x
            $ else2y = gate3y
            $ else2in1 = False
            $ else2in2 = False
            $ else2in3 = True
            $ else2in4 = False
            $ else2in5 = False
            $ else2in6 = False
            $ else2in7 = False
            $ else2in8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBRin4 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin4 = False
            if whileRin4 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin4 = False
            if else1in4 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in4 = False

            #sets values for checks
            $ else2x = gate4x
            $ else2y = gate4y
            $ else2in1 = False
            $ else2in2 = False
            $ else2in3 = False
            $ else2in4 = True
            $ else2in5 = False
            $ else2in6 = False
            $ else2in7 = False
            $ else2in8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBRin5 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin5 = False
            if whileRin5 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin5 = False
            if else1in5 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in5 = False

            #sets values for checks
            $ else2x = gate5x
            $ else2y = gate5y
            $ else2in1 = False
            $ else2in2 = False
            $ else2in3 = False
            $ else2in4 = False
            $ else2in5 = True
            $ else2in6 = False
            $ else2in7 = False
            $ else2in8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBRin6 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin6 = False
            if whileRin6 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin6 = False
            if else1in6 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in6 = False

            #sets values for checks
            $ else2x = gate6x
            $ else2y = gate6y
            $ else2in1 = False
            $ else2in2 = False
            $ else2in3 = False
            $ else2in4 = False
            $ else2in5 = False
            $ else2in6 = True
            $ else2in7 = False
            $ else2in8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBRin7 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin7 = False
            if whileRin7 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin7 = False
            if else1in7 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in7 = False

            #sets values for checks
            $ else2x = gate7x
            $ else2y = gate7y
            $ else2in1 = False
            $ else2in2 = False
            $ else2in3 = False
            $ else2in4 = False
            $ else2in5 = False
            $ else2in6 = False
            $ else2in7 = True
            $ else2in8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBRin8 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin8 = False
            if whileRin8 == True:
                $ whileRx = 1445
                $ whileRy = 500
                $ whileRin8 = False
            if else1in8 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in8 = False

            #sets values for checks
            $ else2x = gate8x
            $ else2y = gate8y
            $ else2in1 = False
            $ else2in2 = False
            $ else2in3 = False
            $ else2in4 = False
            $ else2in5 = False
            $ else2in6 = False
            $ else2in7 = False
            $ else2in8 = True


    #the fourth logic gate *******************************************************************************
    if gate_name == "while_R_gate":
        #gate slot numeber one *******************************
        if slot_name == "gate slot one":
            if ifRin1 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin1 = False
            if ifGin1 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin1 = False
            if ifBin1 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin1 = False
            if ifGRin1 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin1 = False
            if ifBRin1 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin1 = False
            if else1in1 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in1 = False
            if else2in1 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in1 = False

            #sets values for checks
            $ whileRx = gate1x
            $ whileRy = gate1y
            $ whileRin1 = True
            $ whileRin2 = False
            $ whileRin3 = False
            $ whileRin4 = False
            $ whileRin5 = False
            $ whileRin6 = False
            $ whileRin7 = False
            $ whileRin8 = False
            
        #gate slot numeber two *******************************
        if slot_name == "gate slot two":
            if ifRin2 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin2 = False
            if ifGin2 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin2 = False
            if ifBin2 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin2 = False
            if ifGRin2 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin2 = False
            if ifBRin2 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin2 = False
            if else1in2 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in2 = False
            if else2in2 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in2 = False

            #sets values for checks
            $ whileRx = gate2x
            $ whileRy = gate2y
            $ whileRin1 = False
            $ whileRin2 = True
            $ whileRin3 = False
            $ whileRin4 = False
            $ whileRin5 = False
            $ whileRin6 = False
            $ whileRin7 = False
            $ whileRin8 = False
            
        #gate slot numeber three *******************************
        if slot_name == "gate slot three":
            if ifRin3 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin3 = False
            if ifGin3 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin3 = False
            if ifBin3 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin3 = False
            if ifGRin3 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin3 = False
            if ifBRin3 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin3 = False
            if else1in3 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in3 = False
            if else2in3 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in3 = False

            #sets values for checks
            $ whileRx = gate3x
            $ whileRy = gate3y
            $ whileRin1 = False
            $ whileRin2 = False
            $ whileRin3 = True
            $ whileRin4 = False
            $ whileRin5 = False
            $ whileRin6 = False
            $ whileRin7 = False
            $ whileRin8 = False

        #gate slot numeber four *******************************
        if slot_name == "gate slot four":
            if ifRin4 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin4 = False
            if ifGin4 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin4 = False
            if ifBin4 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin4 = False
            if ifGRin4 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin4 = False
            if ifBRin4 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin4 = False
            if else1in4 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in4 = False
            if else2in4 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in4 = False

            #sets values for checks
            $ whileRx = gate4x
            $ whileRy = gate4y
            $ whileRin1 = False
            $ whileRin2 = False
            $ whileRin3 = False
            $ whileRin4 = True
            $ whileRin5 = False
            $ whileRin6 = False
            $ whileRin7 = False
            $ whileRin8 = False
            
        #gate slot numeber five *******************************
        if slot_name == "gate slot five":
            if ifRin5 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin5 = False
            if ifGin5 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin5 = False
            if ifBin5 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin5 = False
            if ifGRin5 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin5 = False
            if ifBRin5 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin5 = False
            if else1in5 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in5 = False
            if else2in5 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in5 = False

            #sets values for checks
            $ whileRx = gate5x
            $ whileRy = gate5y
            $ whileRin1 = False
            $ whileRin2 = False
            $ whileRin3 = False
            $ whileRin4 = False
            $ whileRin5 = True
            $ whileRin6 = False
            $ whileRin7 = False
            $ whileRin8 = False
            
        #gate slot numeber six *******************************
        if slot_name == "gate slot six":
            if ifRin6 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin6 = False
            if ifGin6 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin6 = False
            if ifBin6 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin6 = False
            if ifGRin6 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin6 = False
            if ifBRin6 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin6 = False
            if else1in6 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in6 = False
            if else2in6 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in6 = False

            #sets values for checks
            $ whileRx = gate6x
            $ whileRy = gate6y
            $ whileRin1 = False
            $ whileRin2 = False
            $ whileRin3 = False
            $ whileRin4 = False
            $ whileRin5 = False
            $ whileRin6 = True
            $ whileRin7 = False
            $ whileRin8 = False
            
        #gate slot numeber seven *******************************
        if slot_name == "gate slot seven":
            if ifRin7 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin7 = False
            if ifGin7 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin7 = False
            if ifBin7 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin7 = False
            if ifGRin7 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin7 = False
            if ifBRin7 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin7 = False
            if else1in7 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in7 = False
            if else2in7 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in7 = False

            #sets values for checks
            $ whileRx = gate7x
            $ whileRy = gate7y
            $ whileRin1 = False
            $ whileRin2 = False
            $ whileRin3 = False
            $ whileRin4 = False
            $ whileRin5 = False
            $ whileRin6 = False
            $ whileRin7 = True
            $ whileRin8 = False
            
        #gate slot numeber eight *******************************
        if slot_name == "gate slot eight":
            if ifRin8 == True:
                $ ifRx = 1395
                $ ifRy = 645
                $ ifRin8 = False
            if ifGin8 == True:
                $ ifGx = 1525
                $ ifGy = 645
                $ ifGin8 = False
            if ifBin8 == True:
                $ ifBx = 1655
                $ ifBy = 645
                $ ifBin8 = False
            if ifGRin8 == True:
                $ ifGRx = 1445
                $ ifGRy = 790
                $ ifGRin8 = False
            if ifBRin8 == True:
                $ ifBRx = 1585
                $ ifBRy = 790
                $ ifBRin8 = False
            if else1in8 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in8 = False
            if else2in8 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in8 = False

            #sets values for checks
            $ whileRx = gate8x
            $ whileRy = gate8y
            $ whileRin1 = False
            $ whileRin2 = False
            $ whileRin3 = False
            $ whileRin4 = False
            $ whileRin5 = False
            $ whileRin6 = False
            $ whileRin7 = False
            $ whileRin8 = True





    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not
        (slot_name == "if_R_gate_return" or slot_name == "if_G_gate_return" or slot_name == "if_B_gate_return" or slot_name == "if_GR_gate_return" or
        slot_name == "if_BR_gate_return" or slot_name == "else_gate_return" or slot_name == "while_R_gate_return")):
        $ temp_slot = slot_name
        $ temp_gate = gate_name
        if temp_slot != "" and temp_gate != "":
            $ attempts -=1
            
    else:
        if slot_name != "null" and (temp_slot != slot_name or gate_name != temp_gate):
            $ attempts -=1
            $ temp_slot = slot_name
            $ temp_gate = gate_name

            if slot_name == "if_R_gate_return":
                $ attempts +=1
                if gate_name == "if_R_gate":
                    $ ifRx = 1395
                    $ ifRy = 645
                    $ ifRin1 = False
                    $ ifRin2 = False
                    $ ifRin3 = False
                    $ ifRin4 = False
                    $ ifRin5 = False
                    $ ifRin6 = False
                    $ ifRin7 = False
                    $ ifRin8 = False
            if slot_name == "if_G_gate_return":
                $ attempts +=1
                if gate_name == "if_G_gate":
                    $ ifGx = 1525
                    $ ifGy = 645
                    $ ifGin1 = False
                    $ ifGin2 = False
                    $ ifGin3 = False
                    $ ifGin4 = False
                    $ ifGin5 = False
                    $ ifGin6 = False
                    $ ifGin7 = False
                    $ ifGin8 = False
            if slot_name == "if_B_gate_return":
                $ attempts +=1
                if gate_name == "if_B_gate":
                    $ ifBx = 1655
                    $ ifBy = 645
                    $ ifBin1 = False
                    $ ifBin2 = False
                    $ ifBin3 = False
                    $ ifBin4 = False
                    $ ifBin5 = False
                    $ ifBin6 = False
                    $ ifBin7 = False
                    $ ifBin8 = False
            if slot_name == "if_GR_gate_return":
                $ attempts +=1
                if gate_name == "if_GR_gate":
                    $ ifGRx = 1445
                    $ ifGRy = 790
                    $ ifGRin1 = False
                    $ ifGRin2 = False
                    $ ifGRin3 = False
                    $ ifGRin4 = False
                    $ ifGRin5 = False
                    $ ifGRin6 = False
                    $ ifGRin7 = False
                    $ ifGRin8 = False
            if slot_name == "if_BR_gate_return":
                $ attempts +=1
                if gate_name == "if_BR_gate":
                    $ ifBRx = 1585
                    $ ifBRy = 790
                    $ ifBRin1 = False
                    $ ifBRin2 = False
                    $ ifBRin3 = False
                    $ ifBRin4 = False
                    $ ifBRin5 = False
                    $ ifBRin6 = False
                    $ ifBRin7 = False
                    $ ifBRin8 = False
            if slot_name == "else_gate_return":
                $ attempts +=1
                if gate_name == "else1_gate":
                    $ else1x = 1585
                    $ else1y = 500
                    $ else1in1 = False
                    $ else1in2 = False
                    $ else1in3 = False
                    $ else1in4 = False
                    $ else1in5 = False
                    $ else1in6 = False
                    $ else1in7 = False
                    $ else1in8 = False
            if slot_name == "else_gate_return":
                $ attempts +=1
                if gate_name == "else2_gate":
                    $ else2x = 1585
                    $ else2y = 500
                    $ else2in1 = False
                    $ else2in2 = False
                    $ else2in3 = False
                    $ else2in4 = False
                    $ else2in5 = False
                    $ else2in6 = False
                    $ else2in7 = False
                    $ else2in8 = False
            if slot_name == "while_R_gate_return":
                $ attempts +=1
                if gate_name == "while_R_gate":
                    $ whileRx = 1445
                    $ whileRy = 500
                    $ whileRin1 = False
                    $ whileRin2 = False
                    $ whileRin3 = False
                    $ whileRin4 = False
                    $ whileRin5 = False
                    $ whileRin6 = False
                    $ whileRin7 = False
                    $ whileRin8 = False
                    

#*******************************************
#************image zone********************* 
#*******************************************
    $LLH_2_node1 = "None"
    $LLH_2_node2 = "None"
    $LLH_2_node3 = "None"
    $LLH_2_node4 = "None"
    $LLH_2_node5 = "None"
    $LLH_2_node6 = "None"
    
    $LLH_2_BEnd1 = "Off"
    $LLH_2_BEnd2 = "Off"
    $LLH_2_GEnd1 = "Off"
    $LLH_2_GEnd2 = "Off"
    $LLH_2_REnd = "Off"
    
    $LLH_2_RWhileNode = "Off"
          
    
    #Color Pipes ******************************************************************************
    if ifGRin3 == True:
        image LLH_2_colorTile1 = "R_horizontal_ll.png"
        show LLH_2_colorTile1 at Position(xpos = 250, xanchor = 0, ypos = 470, yanchor = 0)
        image LLH_2_colorTile2 = "G_horizontal_ll.png"
        show LLH_2_colorTile2 at Position(xpos = 250, xanchor = 0, ypos = 510, yanchor = 0)
            
        if ifRin1 == True:
            image LLH_2_colorTile3 = "R_vertical_ll.png"
            show LLH_2_colorTile3 at Position(xpos = 200, xanchor = 0, ypos = 275, yanchor = 0)
            image LLH_2_colorTile4 = "R_vertical_ll.png"
            show LLH_2_colorTile4 at Position(xpos = 200, xanchor = 0, ypos = 400, yanchor = 0)
            image LLH_2_colorTile5 = "G_T_leftLL.png"
            show LLH_2_colorTile5 at Position(xpos = 130, xanchor = 0, ypos = 508, yanchor = 0)
        else:
            hide LLH_2_colorTile3
            hide LLH_2_colorTile4
            hide LLH_2_colorTile5
            
        if ifGin1 == True:
            $LLH_2_GEnd1 = "On"
            image LLH_2_colorTile6 = "G_vertical_ll.png"
            show LLH_2_colorTile6 at Position(xpos = 197, xanchor = 0, ypos = 275, yanchor = 0)
            image LLH_2_colorTile7 = "G_vertical_ll.png"
            show LLH_2_colorTile7 at Position(xpos = 197, xanchor = 0, ypos = 400, yanchor = 0)
            image LLH_2_colorTile8 = "R_T_leftLL.png"
            show LLH_2_colorTile8 at Position(xpos = 130, xanchor = 0, ypos = 508, yanchor = 0)
        else:
            hide LLH_2_colorTile6
            hide LLH_2_colorTile7
            hide LLH_2_colorTile8
            
    else:
        hide LLH_2_colorTile1
        hide LLH_2_colorTile2
        hide LLH_2_colorTile3
        hide LLH_2_colorTile4
        hide LLH_2_colorTile5
        hide LLH_2_colorTile6
        hide LLH_2_colorTile7
        hide LLH_2_colorTile8
        
    if ifBRin3 == True:
        image LLH_2_colorTile9 = "R_horizontal_ll.png"
        show LLH_2_colorTile9 at Position(xpos = 250, xanchor = 0, ypos = 470, yanchor = 0)
        image LLH_2_colorTile10 = "B_horizontal.png"
        show LLH_2_colorTile10 at Position(xpos = 250, xanchor = 0, ypos = 550, yanchor = 0)
        
        if ifRin1 == True:
            image LLH_2_colorTile11 = "R_vertical_ll.png"
            show LLH_2_colorTile11 at Position(xpos = 200, xanchor = 0, ypos = 275, yanchor = 0)
            image LLH_2_colorTile12 = "R_vertical_ll.png"
            show LLH_2_colorTile12 at Position(xpos = 200, xanchor = 0, ypos = 400, yanchor = 0)
            image LLH_2_colorTile13 = "B_T_left.png"
            show LLH_2_colorTile13 at Position(xpos = 130, xanchor = 0, ypos = 508, yanchor = 0)
        else:
            hide LLH_2_colorTile11
            hide LLH_2_colorTile12
            hide LLH_2_colorTile13
            
        if ifBin1 == True:
            image LLH_2_colorTile14 = "B_vertical.png"
            show LLH_2_colorTile14 at Position(xpos = 200, xanchor = 0, ypos = 275, yanchor = 0)
            image LLH_2_colorTile15 = "B_vertical.png"
            show LLH_2_colorTile15 at Position(xpos = 200, xanchor = 0, ypos = 400, yanchor = 0)
            image LLH_2_colorTile16 = "R_T_leftLL.png"
            show LLH_2_colorTile16 at Position(xpos = 130, xanchor = 0, ypos = 508, yanchor = 0)
        else:
            hide LLH_2_colorTile14
            hide LLH_2_colorTile15
            hide LLH_2_colorTile16
            
    else:
        hide LLH_2_colorTile9
        hide LLH_2_colorTile10
        hide LLH_2_colorTile11
        hide LLH_2_colorTile12
        hide LLH_2_colorTile13
        hide LLH_2_colorTile14
        hide LLH_2_colorTile15
        hide LLH_2_colorTile16
        
    if ifRin3 == True:
        image LLH_2_colorTile17 = "R_horizontal_ll.png"
        show LLH_2_colorTile17 at Position(xpos = 250, xanchor = 0, ypos = 470, yanchor = 0)
    else:
        hide LLH_2_colorTile17
    
    if ifGin3 == True:
        image LLH_2_colorTile18 = "G_horizontal_ll.png"
        show LLH_2_colorTile18 at Position(xpos = 250, xanchor = 0, ypos = 510, yanchor = 0)
    else:
        hide LLH_2_colorTile18
        
    if ifBin3 == True:
        image LLH_2_colorTile19 = "B_horizontal.png"
        show LLH_2_colorTile19 at Position(xpos = 250, xanchor = 0, ypos = 550, yanchor = 0)
    else:
        hide LLH_2_colorTile19
        
    if (else1in6 == True or else2in6 == True):
        if ifRin3 == True:
            $LLH_2_node2 = "Green"
            $LLH_2_node3 = "Blue"
        elif ifGin3 == True:
            $LLH_2_node1 = "Red"
            $LLH_2_node3 = "Blue"
        elif ifBin3 == True:
            $LLH_2_node1 = "Red"
            $LLH_2_node2 = "Green"
        
        if ifGRin3 == True:
            $LLH_2_node3 = "Blue"
            $LLH_2_BEnd2 = "On"
            image LLH_2_colorTile20 = "B_vertical.png"
            show LLH_2_colorTile20 at Position(xpos = 315, xanchor = 0, ypos = 575, yanchor = 0)
            image LLH_2_colorTile21 = "B_vertical.png"
            show LLH_2_colorTile21 at Position(xpos = 315, xanchor = 0, ypos = 750, yanchor = 0)
        else:
            hide LLH_2_colorTile20
            hide LLH_2_colorTile21
            
        if ifBRin3 == True:
            $LLH_2_node2 = "Green"
            $LLH_2_node3 = "Green"
            image LLH_2_colorTile22 = "G_connect_pipe_vertical.png"
            show LLH_2_colorTile22 at Position(xpos = 324, xanchor = 0, ypos = 520, yanchor = 0)
            image LLH_2_colorTile23 = "G_vertical_ll.png"
            show LLH_2_colorTile23 at Position(xpos = 312, xanchor = 0, ypos = 575, yanchor = 0)
            image LLH_2_colorTile24 = "G_vertical_ll.png"
            show LLH_2_colorTile24 at Position(xpos = 312, xanchor = 0, ypos = 750, yanchor = 0)
        else:
            hide LLH_2_colorTile22
            hide LLH_2_colorTile23
            hide LLH_2_colorTile24
            
    else:
        hide LLH_2_colorTile20
        hide LLH_2_colorTile21
        hide LLH_2_colorTile22
        hide LLH_2_colorTile23
        hide LLH_2_colorTile24
        
    if ifRin6 == True:
        if (ifGin3 == True or ifBin3 == True or ifGRin3 == True or ifBRin3 == True):
            $LLH_2_node1 = "Red"
            $LLH_2_node2 = "Red"
            $LLH_2_node3 = "Red"
            image LLH_2_colorTile25 = "R_connect_pipe_vertical.png"
            show LLH_2_colorTile25 at Position(xpos = 324, xanchor = 0, ypos = 480, yanchor = 0)
            image LLH_2_colorTile26 = "R_connect_pipe_vertical.png"
            show LLH_2_colorTile26 at Position(xpos = 324, xanchor = 0, ypos = 520, yanchor = 0)
            image LLH_2_colorTile27 = "R_vertical_ll.png"
            show LLH_2_colorTile27 at Position(xpos = 315, xanchor = 0, ypos = 575, yanchor = 0)
            image LLH_2_colorTile28 = "R_vertical_ll.png"
            show LLH_2_colorTile28 at Position(xpos = 315, xanchor = 0, ypos = 750, yanchor = 0)
        else:
            hide LLH_2_colorTile25
            hide LLH_2_colorTile26
            hide LLH_2_colorTile27
            hide LLH_2_colorTile28
    else:
        hide LLH_2_colorTile25
        hide LLH_2_colorTile26
        hide LLH_2_colorTile27
        hide LLH_2_colorTile28
        
    if ifGin6 == True:
        if (ifRin3 == True or ifBin3 == True or ifGRin3 == True or ifBRin3 == True):
            $LLH_2_node2 = "Green"
            $LLH_2_node3 = "Green"
            image LLH_2_colorTile29 = "G_connect_pipe_vertical.png"
            show LLH_2_colorTile29 at Position(xpos = 324, xanchor = 0, ypos = 520, yanchor = 0)
            image LLH_2_colorTile30 = "G_vertical_ll.png"
            show LLH_2_colorTile30 at Position(xpos = 312, xanchor = 0, ypos = 575, yanchor = 0)
            image LLH_2_colorTile31 = "G_vertical_ll.png"
            show LLH_2_colorTile31 at Position(xpos = 312, xanchor = 0, ypos = 750, yanchor = 0)
        else:
            hide LLH_2_colorTile29
            hide LLH_2_colorTile30
            hide LLH_2_colorTile31
    else:
        hide LLH_2_colorTile29
        hide LLH_2_colorTile30
        hide LLH_2_colorTile31
        
    if ifBin6 == True:
        if (ifRin3 == True or ifGin3 == True or ifGRin3 == True or ifBRin3 == True):
            $LLH_2_node3 = "Blue"
            $LLH_2_BEnd2 = "On"
            image LLH_2_colorTile32 = "B_vertical.png"
            show LLH_2_colorTile32 at Position(xpos = 315, xanchor = 0, ypos = 575, yanchor = 0)
            image LLH_2_colorTile33 = "B_vertical.png"
            show LLH_2_colorTile33 at Position(xpos = 315, xanchor = 0, ypos = 750, yanchor = 0)
        else:
            hide LLH_2_colorTile32
            hide LLH_2_colorTile33
    else:
        hide LLH_2_colorTile32
        hide LLH_2_colorTile33
            

    if ifGRin4 == True:
        image LLH_2_colorTile34 = "R_horizontal_ll.png"
        show LLH_2_colorTile34 at Position(xpos = 575, xanchor = 0, ypos = 470, yanchor = 0)
        image LLH_2_colorTile35 = "G_horizontal_ll.png"
        show LLH_2_colorTile35 at Position(xpos = 575, xanchor = 0, ypos = 510, yanchor = 0)
            
        if ifRin2 == True:
            image LLH_2_colorTile36 = "R_vertical_ll.png"
            show LLH_2_colorTile36 at Position(xpos = 675, xanchor = 0, ypos = 275, yanchor = 0)
            image LLH_2_colorTile37 = "R_vertical_ll.png"
            show LLH_2_colorTile37 at Position(xpos = 675, xanchor = 0, ypos = 400, yanchor = 0)
        else:
            hide LLH_2_colorTile36
            hide LLH_2_colorTile37
            
        if ifGin2 == True:
            image LLH_2_colorTile39 = "G_vertical_ll.png"
            show LLH_2_colorTile39 at Position(xpos = 672, xanchor = 0, ypos = 275, yanchor = 0)
            image LLH_2_colorTile40 = "G_vertical_ll.png"
            show LLH_2_colorTile40 at Position(xpos = 672, xanchor = 0, ypos = 400, yanchor = 0)
        else:
            hide LLH_2_colorTile39
            hide LLH_2_colorTile40
            
    else:
        hide LLH_2_colorTile34
        hide LLH_2_colorTile35
        hide LLH_2_colorTile36
        hide LLH_2_colorTile37
        hide LLH_2_colorTile39
        hide LLH_2_colorTile40
        
    if ifBRin4 == True:
        image LLH_2_colorTile42 = "R_horizontal_ll.png"
        show LLH_2_colorTile42 at Position(xpos = 575, xanchor = 0, ypos = 470, yanchor = 0)
        image LLH_2_colorTile43 = "B_horizontal.png"
        show LLH_2_colorTile43 at Position(xpos = 575, xanchor = 0, ypos = 550, yanchor = 0)
            
        if ifRin2 == True:
            image LLH_2_colorTile44 = "R_vertical_ll.png"
            show LLH_2_colorTile44 at Position(xpos = 675, xanchor = 0, ypos = 275, yanchor = 0)
            image LLH_2_colorTile45 = "R_vertical_ll.png"
            show LLH_2_colorTile45 at Position(xpos = 675, xanchor = 0, ypos = 400, yanchor = 0)
        else:
            hide LLH_2_colorTile44
            hide LLH_2_colorTile45
            
        if ifBin2 == True:
            $LLH_2_BEnd1 = "On"
            image LLH_2_colorTile47 = "B_vertical.png"
            show LLH_2_colorTile47 at Position(xpos = 675, xanchor = 0, ypos = 275, yanchor = 0)
            image LLH_2_colorTile48 = "B_vertical.png"
            show LLH_2_colorTile48 at Position(xpos = 675, xanchor = 0, ypos = 400, yanchor = 0)
        else:
            hide LLH_2_colorTile47
            hide LLH_2_colorTile48
            
    else:
        hide LLH_2_colorTile42
        hide LLH_2_colorTile43
        hide LLH_2_colorTile44
        hide LLH_2_colorTile45
        hide LLH_2_colorTile47
        hide LLH_2_colorTile48
        
    if ifRin4 == True:
        image LLH_2_colorTile50 = "R_horizontal_ll.png"
        show LLH_2_colorTile50 at Position(xpos = 575, xanchor = 0, ypos = 470, yanchor = 0)
    else:
        hide LLH_2_colorTile50
    
    if ifGin4 == True:
        image LLH_2_colorTile51 = "G_horizontal_ll.png"
        show LLH_2_colorTile51 at Position(xpos = 575, xanchor = 0, ypos = 510, yanchor = 0)
    else:
        hide LLH_2_colorTile51
        
    if ifBin4 == True:
        image LLH_2_colorTile52 = "B_horizontal.png"
        show LLH_2_colorTile52 at Position(xpos = 575, xanchor = 0, ypos = 550, yanchor = 0)
    else:
        hide LLH_2_colorTile52
        
        
    if (else1in7 == True or else2in7 == True):
        if ifRin4 == True:
            $LLH_2_node5 = "Green"
            $LLH_2_node6 = "Blue"
        elif ifGin4 == True:
            $LLH_2_node4 = "Red"
            $LLH_2_node6 = "Blue"
        elif ifBin4 == True:
            $LLH_2_node4 = "Red"
            $LLH_2_node5 = "Green"
        
        if ifGRin4 == True:
            $LLH_2_node6 = "Blue"
            image LLH_2_colorTile53 = "B_vertical.png"
            show LLH_2_colorTile53 at Position(xpos = 555, xanchor = 0, ypos = 575, yanchor = 0)
            image LLH_2_colorTile54 = "B_vertical_short.png"
            show LLH_2_colorTile54 at Position(xpos = 555, xanchor = 0, ypos = 730, yanchor = 0)
            if whileRin8 == True and ifRin5 == True:
                image LLH_2_colorTile94 = "B_vertical_short.png"
                show LLH_2_colorTile94 at Position(xpos = 552, xanchor = 0, ypos = 790, yanchor = 0)
            else:
                hide LLH_2_colorTile94
        else:
            hide LLH_2_colorTile53
            hide LLH_2_colorTile54
            hide LLH_2_colorTile94
            
        if ifBRin4 == True:
            $LLH_2_node5 = "Green"
            $LLH_2_node6 = "Green"
            image LLH_2_colorTile58 = "G_connect_pipe_vertical.png"
            show LLH_2_colorTile58 at Position(xpos = 564, xanchor = 0, ypos = 520, yanchor = 0)
            image LLH_2_colorTile59 = "G_vertical_ll.png"
            show LLH_2_colorTile59 at Position(xpos = 552, xanchor = 0, ypos = 575, yanchor = 0)
            image LLH_2_colorTile60 = "G_vertical_short.png"
            show LLH_2_colorTile60 at Position(xpos = 552, xanchor = 0, ypos = 730, yanchor = 0)
            if whileRin8 == True and ifRin5 == True:
                $LLH_2_GEnd2 = "On"
                image LLH_2_colorTile63 = "G_vertical_short.png"
                show LLH_2_colorTile63 at Position(xpos = 552, xanchor = 0, ypos = 790, yanchor = 0)
            else:
                hide LLH_2_colorTile63
        else:
            hide LLH_2_colorTile58
            hide LLH_2_colorTile59
            hide LLH_2_colorTile60
            hide LLH_2_colorTile63
            
    else:
        hide LLH_2_colorTile53
        hide LLH_2_colorTile54
        hide LLH_2_colorTile58
        hide LLH_2_colorTile59
        hide LLH_2_colorTile60
        hide LLH_2_colorTile63
        hide LLH_2_colorTile94
        
    if ifRin7 == True:
        if (ifGin4 == True or ifBin4 == True or ifGRin4 == True or ifBRin4 == True):
            $LLH_2_node4 = "Red"
            $LLH_2_node5 = "Red"
            $LLH_2_node6 = "Red"
            image LLH_2_colorTile64 = "R_connect_pipe_vertical.png"
            show LLH_2_colorTile64 at Position(xpos = 564, xanchor = 0, ypos = 480, yanchor = 0)
            image LLH_2_colorTile65 = "R_connect_pipe_vertical.png"
            show LLH_2_colorTile65 at Position(xpos = 564, xanchor = 0, ypos = 520, yanchor = 0)
            image LLH_2_colorTile66 = "R_vertical_ll.png"
            show LLH_2_colorTile66 at Position(xpos = 555, xanchor = 0, ypos = 575, yanchor = 0)
            image LLH_2_colorTile67 = "R_vertical_short.png"
            show LLH_2_colorTile67 at Position(xpos = 555, xanchor = 0, ypos = 730, yanchor = 0)
        else:
            hide LLH_2_colorTile64
            hide LLH_2_colorTile65
            hide LLH_2_colorTile66
            hide LLH_2_colorTile67
    else:
        hide LLH_2_colorTile64
        hide LLH_2_colorTile65
        hide LLH_2_colorTile66
        hide LLH_2_colorTile67
        
    if ifGin7 == True:
        if (ifRin4 == True or ifBin4 == True or ifGRin4 == True or ifBRin4 == True):
            $LLH_2_node5 = "Green"
            $LLH_2_node6 = "Green"
            image LLH_2_colorTile69 = "G_connect_pipe_vertical.png"
            show LLH_2_colorTile69 at Position(xpos = 564, xanchor = 0, ypos = 520, yanchor = 0)
            image LLH_2_colorTile70 = "G_vertical_ll.png"
            show LLH_2_colorTile70 at Position(xpos = 552, xanchor = 0, ypos = 575, yanchor = 0)
            image LLH_2_colorTile71 = "G_vertical_short.png"
            show LLH_2_colorTile71 at Position(xpos = 552, xanchor = 0, ypos = 730, yanchor = 0)
            if whileRin8 == True and ifRin5 == True and (ifGRin4 == True or ifBRin4 == True):
                $LLH_2_GEnd2 = "On"
                image LLH_2_colorTile72 = "G_vertical_short.png"
                show LLH_2_colorTile72 at Position(xpos = 552, xanchor = 0, ypos = 790, yanchor = 0)
            else:
                hide LLH_2_colorTile72
        else:
            hide LLH_2_colorTile69
            hide LLH_2_colorTile70
            hide LLH_2_colorTile71
            hide LLH_2_colorTile72
    else:
        hide LLH_2_colorTile69
        hide LLH_2_colorTile70
        hide LLH_2_colorTile71
        hide LLH_2_colorTile72
        
    if ifBin7 == True:
        if (ifRin4 == True or ifGin4 == True or ifGRin4 == True or ifBRin4 == True):
            $LLH_2_node6 = "Blue"
            image LLH_2_colorTile73 = "B_vertical.png"
            show LLH_2_colorTile73 at Position(xpos = 555, xanchor = 0, ypos = 575, yanchor = 0)
            image LLH_2_colorTile74 = "B_vertical_short.png"
            show LLH_2_colorTile74 at Position(xpos = 555, xanchor = 0, ypos = 730, yanchor = 0)
            if whileRin8 == True and ifRin5 == True and (ifGRin4 == True or ifBRin4 == True):
                image LLH_2_colorTile96 = "B_vertical_short.png"
                show LLH_2_colorTile96 at Position(xpos = 552, xanchor = 0, ypos = 790, yanchor = 0)
            else:
                hide LLH_2_colorTile96
        else:
            hide LLH_2_colorTile73
            hide LLH_2_colorTile74
            hide LLH_2_colorTile96
    else:
        hide LLH_2_colorTile73
        hide LLH_2_colorTile74
        hide LLH_2_colorTile96
        
        
    if ifRin5 == True:
        if ifGRin4 == True or ifBRin4 == True:
            $LLH_2_REnd = "On"
            image LLH_2_colorTile76 = "R_horizontal_ll.png"
            show LLH_2_colorTile76 at Position(xpos = 730, xanchor = 0, ypos = 510, yanchor = 0)
            image LLH_2_colorTile77 = "R_horizontal_ll.png"
            show LLH_2_colorTile77 at Position(xpos = 805, xanchor = 0, ypos = 510, yanchor = 0)
            image LLH_2_colorTile78 = "R_horizontal_ll.png"
            show LLH_2_colorTile78 at Position(xpos = 975, xanchor = 0, ypos = 510, yanchor = 0)
        else:
            hide LLH_2_colorTile76
            hide LLH_2_colorTile77
            hide LLH_2_colorTile78
    else:
        hide LLH_2_colorTile76
        hide LLH_2_colorTile77
        hide LLH_2_colorTile78
        
    if ifGin5 == True and ifGRin4 == True:
        image LLH_2_colorTile79 = "G_horizontal_ll.png"
        show LLH_2_colorTile79 at Position(xpos = 730, xanchor = 0, ypos = 510, yanchor = 0)
        image LLH_2_colorTile83 = "G_horizontal_ll.png"
        show LLH_2_colorTile83 at Position(xpos = 805, xanchor = 0, ypos = 510, yanchor = 0)
        image LLH_2_colorTile84 = "G_horizontal_ll.png"
        show LLH_2_colorTile84 at Position(xpos = 975, xanchor = 0, ypos = 510, yanchor = 0)
    else:
        hide LLH_2_colorTile79
        hide LLH_2_colorTile83
        hide LLH_2_colorTile84
        
    if ifBin5 == True and ifBRin4 == True:
        image LLH_2_colorTile80 = "B_horizontal.png"
        show LLH_2_colorTile80 at Position(xpos = 730, xanchor = 0, ypos = 510, yanchor = 0)
        image LLH_2_colorTile81 = "B_horizontal.png"
        show LLH_2_colorTile81 at Position(xpos = 805, xanchor = 0, ypos = 510, yanchor = 0)
        image LLH_2_colorTile82 = "B_horizontal.png"
        show LLH_2_colorTile82 at Position(xpos = 975, xanchor = 0, ypos = 510, yanchor = 0)
    else:
        hide LLH_2_colorTile80
        hide LLH_2_colorTile81
        hide LLH_2_colorTile82
        
    if whileRin8 == True and (ifGRin4 == True or ifBRin4 == True) and ifRin5 == True:
        $LLH_2_RWhileNode = "On"
        image LLH_2_colorTile85 = "R_vertical_ll.png"
        show LLH_2_colorTile85 at Position(xpos = 910, xanchor = 0, ypos = 520, yanchor = 0)
        image LLH_2_colorTile86 = "R_vertical_ll.png"
        show LLH_2_colorTile86 at Position(xpos = 910, xanchor = 0, ypos = 595, yanchor = 0)
        image LLH_2_colorTile87 = "R_horizontal_short.png"
        show LLH_2_colorTile87 at Position(xpos = 850, xanchor = 0, ypos = 685, yanchor = 0)
        image LLH_2_colorTile93 = "W_corner_LT.png"
        show LLH_2_colorTile93 at Position(xpos = 889, xanchor = 0, ypos = 663, yanchor = 0)
        image LLH_2_colorTile88 = "y_horizontal_short_on.png"
        show LLH_2_colorTile88 at Position(xpos = 570, xanchor = 0, ypos = 775, yanchor = 0)
        image LLH_2_colorTile89 = "y_horizontal_short_on.png"
        show LLH_2_colorTile89 at Position(xpos = 630, xanchor = 0, ypos = 775, yanchor = 0)
        image LLH_2_colorTile90 = "y_horizontal_short_on.png"
        show LLH_2_colorTile90 at Position(xpos = 690, xanchor = 0, ypos = 775, yanchor = 0)
        image LLH_2_colorTile91 = "y_horizontal_short_on.png"
        show LLH_2_colorTile91 at Position(xpos = 750, xanchor = 0, ypos = 775, yanchor = 0)
        image LLH_2_colorTile92 = "y_vertical_short_on.png"
        show LLH_2_colorTile92 at Position(xpos = 790, xanchor = 0, ypos = 740, yanchor = 0)
    else:
        hide LLH_2_colorTile85
        hide LLH_2_colorTile86
        hide LLH_2_colorTile87
        hide LLH_2_colorTile88
        hide LLH_2_colorTile89
        hide LLH_2_colorTile90
        hide LLH_2_colorTile91
        hide LLH_2_colorTile92
        hide LLH_2_colorTile93
            
        
    #Redraw Connect Nodes *********************************************************************
    hide LLH_2_WNode1
    hide LLH_2_WNode2
    hide LLH_2_WNode3
    hide LLH_2_WNode4
    hide LLH_2_WNode5
    hide LLH_2_WNode6
    hide LLH_2_RNode1
    hide LLH_2_RNode2
    hide LLH_2_RNode3
    hide LLH_2_RNode4
    hide LLH_2_RNode5
    hide LLH_2_RNode6
    hide LLH_2_GNode1
    hide LLH_2_GNode2
    hide LLH_2_GNode3
    hide LLH_2_GNode4
    hide LLH_2_GNode5
    hide LLH_2_GNode6
    hide LLH_2_BNode1
    hide LLH_2_BNode2
    hide LLH_2_BNode3
    hide LLH_2_BNode4
    hide LLH_2_BNode5
    hide LLH_2_BNode6
    
    image LLH_2_WNode1 = "W_connect_node.png"
    image LLH_2_WNode2 = "W_connect_node.png"
    image LLH_2_WNode3 = "W_connect_node.png"
    image LLH_2_WNode4 = "W_connect_node.png"
    image LLH_2_WNode5 = "W_connect_node.png"
    image LLH_2_WNode6 = "W_connect_node.png"
    image LLH_2_RNode1 = "R_connect_node.png"
    image LLH_2_RNode2 = "R_connect_node.png"
    image LLH_2_RNode3 = "R_connect_node.png"
    image LLH_2_RNode4 = "R_connect_node.png"
    image LLH_2_RNode5 = "R_connect_node.png"
    image LLH_2_RNode6 = "R_connect_node.png"
    image LLH_2_GNode1 = "G_connect_node.png"
    image LLH_2_GNode2 = "G_connect_node.png"
    image LLH_2_GNode3 = "G_connect_node.png"
    image LLH_2_GNode4 = "G_connect_node.png"
    image LLH_2_GNode5 = "G_connect_node.png"
    image LLH_2_GNode6 = "G_connect_node.png"
    image LLH_2_BNode1 = "B_connect_node.png"
    image LLH_2_BNode2 = "B_connect_node.png"
    image LLH_2_BNode3 = "B_connect_node.png"
    image LLH_2_BNode4 = "B_connect_node.png"
    image LLH_2_BNode5 = "B_connect_node.png"
    image LLH_2_BNode6 = "B_connect_node.png"
    
    if LLH_2_node1 == "None":
        show LLH_2_WNode1 at Position(xpos = 313, xanchor = 0, ypos = 468, yanchor = 0) 
    elif LLH_2_node1 == "Red":
        show LLH_2_RNode1 at Position(xpos = 313, xanchor = 0, ypos = 468, yanchor = 0) 
    elif LLH_2_node1 == "Green":
        show LLH_2_GNode1 at Position(xpos = 313, xanchor = 0, ypos = 468, yanchor = 0) 
    elif LLH_2_node1 == "Blue":
        show LLH_2_BNode1 at Position(xpos = 313, xanchor = 0, ypos = 468, yanchor = 0) 
        
    if LLH_2_node2 == "None":
        show LLH_2_WNode2 at Position(xpos = 313, xanchor = 0, ypos = 508, yanchor = 0) 
    elif LLH_2_node2 == "Red":
        show LLH_2_RNode2 at Position(xpos = 313, xanchor = 0, ypos = 508, yanchor = 0) 
    elif LLH_2_node2 == "Green":
        show LLH_2_GNode2 at Position(xpos = 313, xanchor = 0, ypos = 508, yanchor = 0) 
    elif LLH_2_node2 == "Blue":
        show LLH_2_BNode2 at Position(xpos = 313, xanchor = 0, ypos = 508, yanchor = 0) 
        
    if LLH_2_node3 == "None":
        show LLH_2_WNode3 at Position(xpos = 313, xanchor = 0, ypos = 548, yanchor = 0) 
    elif LLH_2_node3 == "Red":
        show LLH_2_RNode3 at Position(xpos = 313, xanchor = 0, ypos = 548, yanchor = 0) 
    elif LLH_2_node3 == "Green":
        show LLH_2_GNode3 at Position(xpos = 313, xanchor = 0, ypos = 548, yanchor = 0) 
    elif LLH_2_node3 == "Blue":
        show LLH_2_BNode3 at Position(xpos = 313, xanchor = 0, ypos = 548, yanchor = 0) 
        
    if LLH_2_node4 == "None":
        show LLH_2_WNode4 at Position(xpos = 553, xanchor = 0, ypos = 468, yanchor = 0) 
    elif LLH_2_node4 == "Red":
        show LLH_2_RNode4 at Position(xpos = 553, xanchor = 0, ypos = 468, yanchor = 0) 
    elif LLH_2_node4 == "Green":
        show LLH_2_GNode4 at Position(xpos = 553, xanchor = 0, ypos = 468, yanchor = 0) 
    elif LLH_2_node4 == "Blue":
        show LLH_2_BNode4 at Position(xpos = 553, xanchor = 0, ypos = 468, yanchor = 0) 
        
    if LLH_2_node5 == "None":
        show LLH_2_WNode5 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0) 
    elif LLH_2_node5 == "Red":
        show LLH_2_RNode5 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0) 
    elif LLH_2_node5 == "Green":
        show LLH_2_GNode5 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0) 
    elif LLH_2_node5 == "Blue":
        show LLH_2_BNode5 at Position(xpos = 553, xanchor = 0, ypos = 508, yanchor = 0) 
        
    if LLH_2_node6 == "None":
        show LLH_2_WNode6 at Position(xpos = 553, xanchor = 0, ypos = 548, yanchor = 0) 
    elif LLH_2_node6 == "Red":
        show LLH_2_RNode6 at Position(xpos = 553, xanchor = 0, ypos = 548, yanchor = 0) 
    elif LLH_2_node6 == "Green":
        show LLH_2_GNode6 at Position(xpos = 553, xanchor = 0, ypos = 548, yanchor = 0) 
    elif LLH_2_node6 == "Blue":
        show LLH_2_BNode6 at Position(xpos = 553, xanchor = 0, ypos = 548, yanchor = 0) 
    
    #Redraw Ends *******************************************************************************
    hide LLH_2_BlueEnd1_Off
    hide LLH_2_BlueEnd2_Off
    hide LLH_2_GreenEnd1_Off
    hide LLH_2_GreenEnd2_Off
    hide LLH_2_RedEnd_Off
    hide LLH_2_BlueEnd1_On
    hide LLH_2_BlueEnd2_On
    hide LLH_2_GreenEnd1_On
    hide LLH_2_GreenEnd2_On
    hide LLH_2_RedEnd_On
    
    image LLH_2_BlueEnd1_Off = "B_end_off.png"
    image LLH_2_BlueEnd2_Off = "B_end_off.png"
    image LLH_2_GreenEnd1_Off = "G_end_off.png"
    image LLH_2_GreenEnd2_Off = "G_end_off.png"
    image LLH_2_RedEnd_Off = "R_end_off.png"
    image LLH_2_BlueEnd1_On = "B_end_on.png"
    image LLH_2_BlueEnd2_On = "B_end_on.png"
    image LLH_2_GreenEnd1_On = "G_end_on.png"
    image LLH_2_GreenEnd2_On = "G_end_on.png"
    image LLH_2_RedEnd_On = "R_end_on.png"
    
    if LLH_2_BEnd1 == "Off":
        show LLH_2_BlueEnd1_Off at Position(xpos = 640, xanchor = 0, ypos = 175, yanchor = 0)
    elif LLH_2_BEnd1 == "On":
        show LLH_2_BlueEnd1_On at Position(xpos = 640, xanchor = 0, ypos = 175, yanchor = 0)
        
    if LLH_2_BEnd2 == "Off":
        show LLH_2_BlueEnd2_Off at Position(xpos = 280, xanchor = 0, ypos = 820, yanchor = 0)
    elif LLH_2_BEnd2 == "On":
        show LLH_2_BlueEnd2_On at Position(xpos = 280, xanchor = 0, ypos = 820, yanchor = 0)
        
    if LLH_2_GEnd1 == "Off":
        show LLH_2_GreenEnd1_Off at Position(xpos = 165, xanchor = 0, ypos = 175, yanchor = 0)
    elif LLH_2_GEnd1 == "On":
        show LLH_2_GreenEnd1_On at Position(xpos = 165, xanchor = 0, ypos = 175, yanchor = 0)
        
    if LLH_2_GEnd2 == "Off":
        show LLH_2_GreenEnd2_Off at Position(xpos = 520, xanchor = 0, ypos = 820, yanchor = 0)
    elif LLH_2_GEnd2 == "On":
        show LLH_2_GreenEnd2_On at Position(xpos = 520, xanchor = 0, ypos = 820, yanchor = 0)
        
    if LLH_2_REnd == "Off":
        show LLH_2_RedEnd_Off at Position(xpos = 1050, xanchor = 0, ypos = 475, yanchor = 0)
    elif LLH_2_REnd == "On":
        show LLH_2_RedEnd_On at Position(xpos = 1050, xanchor = 0, ypos = 475, yanchor = 0)
    
    #Redraw While Nodes ***************************************************************************
    hide LLH_2_Red_While_Node_Off
    hide LLH_2_Red_While_Node_On
    
    image LLH_2_Red_While_Node_Off = "r_while_off.png"
    image LLH_2_Red_While_Node_On = "r_while_on.png"
        
    if LLH_2_RWhileNode == "Off":
        show LLH_2_Red_While_Node_Off at Position(xpos = 553, xanchor = 0, ypos = 772, yanchor = 0)
    elif LLH_2_RWhileNode == "On":
        show LLH_2_Red_While_Node_On at Position(xpos = 553, xanchor = 0, ypos = 772, yanchor = 0)
    
    #*********************************************************
    #********************* redraw gates **********************
    #*********************************************************  
    hide LLH_2_tile1
    hide LLH_2_tile2
    hide LLH_2_tile3
    hide LLH_2_tile4
    hide LLH_2_tile5
    hide LLH_2_tile6
    hide LLH_2_tile7
    hide LLH_2_tile8
    show LLH_2_tile1 at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
    show LLH_2_tile2 at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
    show LLH_2_tile3 at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
    show LLH_2_tile4 at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
    show LLH_2_tile5 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
    show LLH_2_tile6 at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
    show LLH_2_tile7 at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
    show LLH_2_tile8 at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)    

#win conditions ********
    if  ifGin1 == True and ifBin2 == True and ifGRin3 == True and ifBRin4 == True and ifRin5 == True and (else1in6 == True or else2in6 == True) and (else1in7 == True or else2in7 == True) and whileRin8 == True:
        image LLH_2_ifR = "R_if.png"
        show LLH_2_ifR at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
        image LLH_2_ifG = "G_if.png"
        show LLH_2_ifG at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
        image LLH_2_ifB = "B_if.png"
        show LLH_2_ifB at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
        image LLH_2_ifGR = "GR_if.png"
        show LLH_2_ifGR at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
        image LLH_2_ifBR = "BR_if.png"
        show LLH_2_ifBR at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
        image LLH_2_else1 = "G_else.png"
        show LLH_2_else1 at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
        image LLH_2_else2 = "G_else.png"
        show LLH_2_else2 at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
        image LLH_2_whileR = "R_while.png"
        show LLH_2_whileR at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)

        image LLH_2_ifRBorder = "placeholder3.png"
        show LLH_2_ifRBorder at Position(xpos = 1385, xanchor = 0, ypos = 635, yanchor = 0)
        image LLH_2_ifGBorder = "placeholder3.png"
        show LLH_2_ifGBorder at Position(xpos = 1515, xanchor = 0, ypos = 635, yanchor = 0)
        image LLH_2_ifBBorder = "placeholder3.png"
        show LLH_2_ifBBorder at Position(xpos = 1645, xanchor = 0, ypos = 635, yanchor = 0)
        image LLH_2_ifGRBorder = "placeholder3.png"
        show LLH_2_ifGRBorder at Position(xpos = 1435, xanchor = 0, ypos = 780, yanchor = 0)
        image LLH_2_ifBRBorder = "placeholder3.png"
        show LLH_2_ifBRBorder at Position(xpos = 1575, xanchor = 0, ypos = 780, yanchor = 0)
        image LLH_2_elseBorder = "placeholder3.png"
        show LLH_2_elseBorder at Position(xpos = 1575, xanchor = 0, ypos = 490, yanchor = 0)
        image LLH_2_whileRBorder = "placeholder3.png"
        show LLH_2_whileRBorder at Position(xpos = 1435, xanchor = 0, ypos = 490, yanchor = 0)
        
        "You Win!"
        jump loopLogic_hard2

#lose conditions ********
    if attempts == 0:
        hide LLH_2_colorTile1
        hide LLH_2_colorTile2
        hide LLH_2_colorTile3
        hide LLH_2_colorTile4
        hide LLH_2_colorTile5
        hide LLH_2_colorTile6
        hide LLH_2_colorTile7
        hide LLH_2_colorTile8
        hide LLH_2_colorTile9
        hide LLH_2_colorTile10
        hide LLH_2_colorTile11
        hide LLH_2_colorTile12
        hide LLH_2_colorTile13
        hide LLH_2_colorTile14
        hide LLH_2_colorTile15
        hide LLH_2_colorTile16
        hide LLH_2_colorTile17
        hide LLH_2_colorTile18
        hide LLH_2_colorTile19
        hide LLH_2_colorTile20
        hide LLH_2_colorTile21
        hide LLH_2_colorTile22
        hide LLH_2_colorTile23
        hide LLH_2_colorTile24
        hide LLH_2_colorTile25
        hide LLH_2_colorTile26
        hide LLH_2_colorTile27
        hide LLH_2_colorTile28
        hide LLH_2_colorTile29
        hide LLH_2_colorTile30
        hide LLH_2_colorTile31
        hide LLH_2_colorTile32
        hide LLH_2_colorTile33
        hide LLH_2_colorTile34
        hide LLH_2_colorTile35
        hide LLH_2_colorTile36
        hide LLH_2_colorTile37
        hide LLH_2_colorTile38
        hide LLH_2_colorTile39
        hide LLH_2_colorTile40
        hide LLH_2_colorTile41
        hide LLH_2_colorTile42
        hide LLH_2_colorTile43
        hide LLH_2_colorTile44
        hide LLH_2_colorTile45
        hide LLH_2_colorTile46
        hide LLH_2_colorTile47
        hide LLH_2_colorTile48
        hide LLH_2_colorTile49
        hide LLH_2_colorTile50
        hide LLH_2_colorTile51
        hide LLH_2_colorTile52
        hide LLH_2_colorTile53
        hide LLH_2_colorTile54
        hide LLH_2_colorTile55
        hide LLH_2_colorTile56
        hide LLH_2_colorTile57
        hide LLH_2_colorTile58
        hide LLH_2_colorTile59
        hide LLH_2_colorTile60
        hide LLH_2_colorTile61
        hide LLH_2_colorTile62
        hide LLH_2_colorTile63
        hide LLH_2_colorTile64
        hide LLH_2_colorTile65
        hide LLH_2_colorTile66
        hide LLH_2_colorTile67
        hide LLH_2_colorTile68
        hide LLH_2_colorTile69
        hide LLH_2_colorTile70
        hide LLH_2_colorTile71
        hide LLH_2_colorTile72
        hide LLH_2_colorTile73
        hide LLH_2_colorTile74
        hide LLH_2_colorTile75
        hide LLH_2_colorTile76
        hide LLH_2_colorTile77
        hide LLH_2_colorTile78
        hide LLH_2_colorTile79
        hide LLH_2_colorTile80
        hide LLH_2_colorTile81
        hide LLH_2_colorTile82
        hide LLH_2_colorTile83
        hide LLH_2_colorTile84
        hide LLH_2_colorTile85
        hide LLH_2_colorTile86
        hide LLH_2_colorTile87
        hide LLH_2_colorTile88
        hide LLH_2_colorTile89
        hide LLH_2_colorTile90
        hide LLH_2_colorTile91
        hide LLH_2_colorTile92
        hide LLH_2_colorTile93
        hide LLH_2_colorTile94
        hide LLH_2_colorTile95
        hide LLH_2_colorTile96
        hide LLH_2_colorTile97
        hide LLH_2_colorTile98
        hide LLH_2_colorTile99
        hide LLH_2_colorTile100
        hide LLH_2_colorTile101
        hide LLH_2_colorTile102
        hide LLH_2_colorTile103 
        hide LLH_2_colorTile104
        hide LLH_2_colorTile105 
        hide LLH_2_colorTile106
        hide LLH_2_colorTile107
        hide LLH_2_colorTile108
        hide LLH_2_colorTile109
        hide LLH_2_colorTile110
        hide LLH_2_colorTile111 
        hide LLH_2_colorTile112
        hide LLH_2_colorTile113
        hide LLH_2_colorTile114
        hide LLH_2_colorTile115
        hide LLH_2_colorTile116 
        hide LLH_2_colorTile117
        hide LLH_2_colorTile118
        hide LLH_2_colorTile119
        hide LLH_2_colorTile120
        hide LLH_2_colorTile121
        hide LLH_2_colorTile122
        hide LLH_2_colorTile123
        hide LLH_2_colorTile124
        hide LLH_2_colorTile125

        hide LLH_2_WNode1
        hide LLH_2_WNode2
        hide LLH_2_WNode3
        hide LLH_2_WNode4
        hide LLH_2_WNode5
        hide LLH_2_WNode6
        hide LLH_2_RNode1
        hide LLH_2_RNode2
        hide LLH_2_RNode3
        hide LLH_2_RNode4
        hide LLH_2_RNode5
        hide LLH_2_RNode6
        hide LLH_2_GNode1
        hide LLH_2_GNode2
        hide LLH_2_GNode3
        hide LLH_2_GNode4
        hide LLH_2_GNode5
        hide LLH_2_GNode6
        hide LLH_2_BNode1
        hide LLH_2_BNode2
        hide LLH_2_BNode3
        hide LLH_2_BNode4
        hide LLH_2_BNode5
        hide LLH_2_BNode6
    
        hide LLH_2_BlueEnd1_Off
        hide LLH_2_BlueEnd2_Off
        hide LLH_2_GreenEnd1_Off
        hide LLH_2_GreenEnd2_Off
        hide LLH_2_RedEnd_Off
        hide LLH_2_BlueEnd1_On
        hide LLH_2_BlueEnd2_On
        hide LLH_2_GreenEnd1_On
        hide LLH_2_GreenEnd2_On
        hide LLH_2_RedEnd_On

        hide LLH_2_Red_While_Node_Off
        hide LLH_2_Red_While_Node_On
    
        show LLH_2_ifR at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
        show LLH_2_ifG at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
        show LLH_2_ifB at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
        show LLH_2_ifGR at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
        show LLH_2_ifBR at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
        show LLH_2_else1 at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
        show LLH_2_else2 at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
        show LLH_2_whileR at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)
        
        show LLH_2_ifRBorder at Position(xpos = 1385, xanchor = 0, ypos = 635, yanchor = 0)
        show LLH_2_ifGBorder at Position(xpos = 1515, xanchor = 0, ypos = 635, yanchor = 0)
        show LLH_2_ifBBorder at Position(xpos = 1645, xanchor = 0, ypos = 635, yanchor = 0)
        show LLH_2_ifGRBorder at Position(xpos = 1435, xanchor = 0, ypos = 780, yanchor = 0)
        show LLH_2_ifBRBorder at Position(xpos = 1575, xanchor = 0, ypos = 780, yanchor = 0)
        show LLH_2_elseBorder at Position(xpos = 1575, xanchor = 0, ypos = 490, yanchor = 0)
        show LLH_2_whileRBorder at Position(xpos = 1435, xanchor = 0, ypos = 490, yanchor = 0)
        
        "You lose. Try again!"
        jump loopLogic_hard2
    
    jump gamefile_llh2

screen loopLogicHard_2Scr:
    
    #drags and drop location
    draggroup:

            #location to be dropped
            drag:
                drag_name "gate slot one"
                child "cover2.png"
                draggable False
                xpos gate1x ypos gate1y
           
            drag:
                drag_name "gate slot two"
                child "cover2.png"
                draggable False
                xpos gate2x ypos gate2y
                
            drag:
                drag_name "gate slot three"
                child "cover2.png"
                draggable False
                xpos gate3x ypos gate3y

            drag:
                drag_name "gate slot four"
                child "cover2.png"
                draggable False
                xpos gate4x ypos gate4y
                
            drag:
                drag_name "gate slot five"
                child "cover2.png"
                draggable False
                xpos gate5x ypos gate5y
           
            drag:
                drag_name "gate slot six"
                child "cover2.png"
                draggable False
                xpos gate6x ypos gate6y
                
            drag:
                drag_name "gate slot seven"
                child "cover2.png"
                draggable False
                xpos gate7x ypos gate7y

            drag:
                drag_name "gate slot eight"
                child "cover2.png"
                draggable False
                xpos gate8x ypos gate8y

            #Gate Slots
            drag:
                drag_name "while_R_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1435 ypos 490

            drag:
                drag_name "else_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1575 ypos 490
                
            drag:
                drag_name "if_R_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1385 ypos 635

            drag:
                drag_name "if_G_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1515 ypos 635

            drag:
                drag_name "if_B_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1645 ypos 635
                
            drag:
                drag_name "if_GR_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1435 ypos 780

            drag:
                drag_name "if_BR_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1575 ypos 780
                
            #if gates
            drag:
                drag_name "if_R_gate"
                child "R_if.png"
                droppable False
                dragged gate_dragged
                xpos ifRx ypos ifRy
                
            drag:
                drag_name "if_G_gate"
                child "G_if.png"
                droppable False
                dragged gate_dragged
                xpos ifGx ypos ifGy
                
            drag:
                drag_name "if_B_gate"
                child "B_if.png"
                droppable False
                dragged gate_dragged
                xpos ifBx ypos ifBy
                
            drag:
                drag_name "if_GR_gate"
                child "GR_if.png"
                droppable False
                dragged gate_dragged
                xpos ifGRx ypos ifGRy
                
            drag:
                drag_name "if_BR_gate"
                child "BR_if.png"
                droppable False
                dragged gate_dragged
                xpos ifBRx ypos ifBRy       

            #else gate
            drag:
                drag_name "else1_gate"
                child "G_else.png"
                droppable False
                dragged gate_dragged
                xpos else1x ypos else1y

            drag:
                drag_name "else2_gate"
                child "G_else.png"
                droppable False
                dragged gate_dragged
                xpos else2x ypos else2y
                
            #while gate
            drag:
                drag_name "while_R_gate"
                child "R_while.png"
                droppable False
                dragged gate_dragged
                xpos whileRx ypos whileRy  
