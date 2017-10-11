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

label loopLogic_hard1: #start
    #loads background
    $ gate_name= ""
    $ slot_name = ""
    $ quick_menu = False
    $ game_menu = True
    scene bg looplogic_bg

    #Left of Start
    image LLH_1_tile1 = "W_horizontal.png"
    show LLH_1_tile1 at Position(xpos = 525, xanchor = 0, ypos = 390, yanchor = 0)
    image LLH_1_tile2 = "W_horizontal.png"
    show LLH_1_tile2 at Position(xpos = 525, xanchor = 0, ypos = 430, yanchor = 0)

    #Down of Start
    image LLH_1_tile3 = "W_vertical.png"
    show LLH_1_tile3 at Position(xpos = 620, xanchor = 0, ypos = 475, yanchor = 0)
    image LLH_1_tile4 = "W_vertical.png"
    show LLH_1_tile4 at Position(xpos = 660, xanchor = 0, ypos = 475, yanchor = 0)

    #Top of Start Connect Node
    image LLH_1_tile16 = "W_vertical.png"
    show LLH_1_tile16 at Position(xpos = 775, xanchor = 0, ypos = 300, yanchor = 0)

    #Right of Start
    image LLH_1_tile5 = "R_horizontal_ll.png"
    show LLH_1_tile5 at Position(xpos = 700, xanchor = 0, ypos = 370, yanchor = 0)
    image LLH_1_tile6 = "W_horizontal.png"
    show LLH_1_tile6 at Position(xpos = 800, xanchor = 0, ypos = 370, yanchor = 0)
    image LLH_1_tile7 = "G_horizontal_ll.png"
    show LLH_1_tile7 at Position(xpos = 700, xanchor = 0, ypos = 410, yanchor = 0)
    image LLH_1_tile8 = "W_horizontal.png"
    show LLH_1_tile8 at Position(xpos = 800, xanchor = 0, ypos = 410, yanchor = 0)
    image LLH_1_tile9 = "B_horizontal.png"
    show LLH_1_tile9 at Position(xpos = 700, xanchor = 0, ypos = 450, yanchor = 0)
    image LLH_1_tile10 = "W_horizontal.png"
    show LLH_1_tile10 at Position(xpos = 800, xanchor = 0, ypos = 450, yanchor = 0)
    image LLH_1_tile11 = "W_connect_pipe_vertical.png"
    show LLH_1_tile11 at Position(xpos = 783, xanchor = 0, ypos = 380, yanchor = 0)
    image LLH_1_tile12 = "W_connect_pipe_vertical.png"
    show LLH_1_tile12 at Position(xpos = 783, xanchor = 0, ypos = 420, yanchor = 0)
    
    #Left of Top Blue End
    image LLH_1_tile17 = "W_horizontal.png"
    show LLH_1_tile17 at Position(xpos = 840, xanchor = 0, ypos = 230, yanchor = 0)
    image LLH_1_tile18 = "W_horizontal.png"
    show LLH_1_tile18 at Position(xpos = 915, xanchor = 0, ypos = 230, yanchor = 0)
    
    #Left of Gate Left of Start
    image LLH_1_tile19 = "W_horizontal.png"
    show LLH_1_tile19 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
    
    #Down of Gate Left of Start
    image LLH_1_tile20 = "W_vertical.png"
    show LLH_1_tile20 at Position(xpos = 470, xanchor = 0, ypos = 475, yanchor = 0)
    
    #Right of Green End
    image LLH_1_tile21 = "W_horizontal.png"
    show LLH_1_tile21 at Position(xpos = 190, xanchor = 0, ypos = 410, yanchor = 0)
    
    #Top of Bottom Blue End
    image LLH_1_tile22 = "W_vertical.png"
    show LLH_1_tile22 at Position(xpos = 470, xanchor = 0, ypos = 650, yanchor = 0)
    
    #Dotted Line
    image LLH_1_tile23 = "y_horizontal_short_off.png"
    show LLH_1_tile23 at Position(xpos = 680, xanchor = 0, ypos = 565, yanchor = 0)
    image LLH_1_tile24 = "y_horizontal_short_off.png"
    show LLH_1_tile24 at Position(xpos = 755, xanchor = 0, ypos = 565, yanchor = 0)
    image LLH_1_tile25 = "y_vertical_short_off.png"
    show LLH_1_tile25 at Position(xpos = 790, xanchor = 0, ypos = 595, yanchor = 0)
    image LLH_1_tile26 = "y_horizontal_short_off.png"
    show LLH_1_tile26 at Position(xpos = 800, xanchor = 0, ypos = 650, yanchor = 0)
    image LLH_1_tile27 = "y_horizontal_short_off.png"
    show LLH_1_tile27 at Position(xpos = 870, xanchor = 0, ypos = 650, yanchor = 0)
    image LLH_1_tile28 = "y_horizontal_short_off.png"
    show LLH_1_tile28 at Position(xpos = 700, xanchor = 0, ypos = 610, yanchor = 0)
    image LLH_1_tile29 = "y_vertical_short_off.png"
    show LLH_1_tile29 at Position(xpos = 760, xanchor = 0, ypos = 620, yanchor = 0)
    image LLH_1_tile30 = "y_vertical_short_off.png"
    show LLH_1_tile30 at Position(xpos = 760, xanchor = 0, ypos = 685, yanchor = 0)
    image LLH_1_tile31 = "y_horizontal_short_off.png"
    show LLH_1_tile31 at Position(xpos = 790, xanchor = 0, ypos = 720, yanchor = 0)
    image LLH_1_tile32 = "y_horizontal_short_off.png"
    show LLH_1_tile32 at Position(xpos = 860, xanchor = 0, ypos = 720, yanchor = 0)

    #Right of Gate Right from Start
    image LLH_1_tile33 = "W_horizontal.png"
    show LLH_1_tile33 at Position(xpos = 975, xanchor = 0, ypos = 390, yanchor = 0)
    image LLH_1_tile34 = "W_horizontal_short.png"
    show LLH_1_tile34 at Position(xpos = 950, xanchor = 0, ypos = 430, yanchor = 0)
    image LLH_1_tile35 = "W_corner_LB.png"
    show LLH_1_tile35 at Position(xpos = 1050, xanchor = 0, ypos = 363, yanchor = 0)
    image LLH_1_tile36 = "W_corner_LB.png"
    show LLH_1_tile36 at Position(xpos = 1000, xanchor = 0, ypos = 403, yanchor = 0)
    image LLH_1_tile37 = "W_vertical.png"
    show LLH_1_tile37 at Position(xpos = 1072, xanchor = 0, ypos = 438, yanchor = 0)
    image LLH_1_tile38 = "W_vertical_short.png"
    show LLH_1_tile38 at Position(xpos = 1072, xanchor = 0, ypos = 513, yanchor = 0)
    image LLH_1_tile39 = "W_vertical.png"
    show LLH_1_tile39 at Position(xpos = 1022, xanchor = 0, ypos = 478, yanchor = 0)
    image LLH_1_tile40 = "W_vertical.png"
    show LLH_1_tile40 at Position(xpos = 1072, xanchor = 0, ypos = 568, yanchor = 0)
    image LLH_1_tile41 = "W_vertical.png"
    show LLH_1_tile41 at Position(xpos = 1022, xanchor = 0, ypos = 568, yanchor = 0)
    image LLH_1_tile42 = "W_connect_pipe.png"
    show LLH_1_tile42 at Position(xpos = 1037, xanchor = 0, ypos = 555, yanchor = 0)
    
    #Left of Red End Connector
    image LLH_1_tile45 = "W_horizontal_short.png"
    show LLH_1_tile45 at Position(xpos = 975, xanchor = 0, ypos = 548, yanchor = 0)    
    
    #Top of Red End
    image LLH_1_tile46 = "W_vertical.png"
    show LLH_1_tile46 at Position(xpos = 1045, xanchor = 0, ypos = 740, yanchor = 0)

    #Top of Bottom Green End
    image LLH_1_tile47 = "W_vertical_short.png"
    show LLH_1_tile47 at Position(xpos = 900, xanchor = 0, ypos = 600, yanchor = 0)
    image LLH_1_tile48 = "W_vertical_short.png"
    show LLH_1_tile48 at Position(xpos = 900, xanchor = 0, ypos = 679, yanchor = 0)
    image LLH_1_tile49 = "W_vertical_short.png"
    show LLH_1_tile49 at Position(xpos = 900, xanchor = 0, ypos = 750, yanchor = 0)
    image LLH_1_tile50 = "r_while_off.png"
    show LLH_1_tile50 at Position(xpos = 898, xanchor = 0, ypos = 648, yanchor = 0)
    image LLH_1_tile51 = "b_while_off.png"
    show LLH_1_tile51 at Position(xpos = 898, xanchor = 0, ypos = 719, yanchor = 0)

    #*********************************************************
    #********************* start points **********************
    #*********************************************************
    image LLH_1_Start = "Start.png"
    show LLH_1_Start at Position(xpos = 600, xanchor = 0, ypos = 375, yanchor = 0)
    
    #*********************************************************
    #********************** end points ***********************
    #*********************************************************    
    image LLH_1_BlueEnd1 = "B_end_off.png"
    show LLH_1_BlueEnd1 at Position(xpos = 980, xanchor = 0, ypos = 200, yanchor = 0)
    image LLH_1_BlueEnd2 = "B_end_off.png"
    show LLH_1_BlueEnd2 at Position(xpos = 435, xanchor = 0, ypos = 725, yanchor = 0)
    image LLH_1_GreenEnd1 = "G_end_off.png"
    show LLH_1_GreenEnd1 at Position(xpos = 100, xanchor = 0, ypos = 375, yanchor = 0)
    image LLH_1_GreenEnd2 = "G_end_off.png"
    show LLH_1_GreenEnd2 at Position(xpos = 865, xanchor = 0, ypos = 785, yanchor = 0)
    image LLH_1_RedEnd = "R_end_off.png"
    show LLH_1_RedEnd at Position(xpos = 1010, xanchor = 0, ypos = 810, yanchor = 0)

    #*********************************************************
    #********************* connect nodes *********************
    #*********************************************************      
    image LLH_1_tile13 = "W_connect_node.png"
    show LLH_1_tile13 at Position(xpos = 772, xanchor = 0, ypos = 365, yanchor = 0)
    image LLH_1_tile14 = "W_connect_node.png"
    show LLH_1_tile14 at Position(xpos = 772, xanchor = 0, ypos = 407, yanchor = 0)
    image LLH_1_tile15 = "W_connect_node.png"
    show LLH_1_tile15 at Position(xpos = 772, xanchor = 0, ypos = 450, yanchor = 0)
    
    image LLH_1_tile43 = "W_connect_node.png"
    show LLH_1_tile43 at Position(xpos = 1020, xanchor = 0, ypos = 545, yanchor = 0)
    image LLH_1_tile44 = "W_connect_node.png"
    show LLH_1_tile44 at Position(xpos = 1070, xanchor = 0, ypos = 545, yanchor = 0)
    
    
#    ****************************************************
#    **********template makers stop here*****************
#    ****************************************************
        
    #initial value assignment for dragables
    $ whileRBx = 1445
    $ whileRBy = 500
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
    $ ifRGx = 1445
    $ ifRGy = 790
    $ ifBGx = 1585
    $ ifBGy = 790
    

    $ gate1x = 740
    $ gate1y = 200
    $ gate2x = 265
    $ gate2y = 375
    $ gate3x = 435
    $ gate3y = 375
    $ gate4x = 875
    $ gate4y = 375
    $ gate5x = 435
    $ gate5y = 550
    $ gate6x = 600
    $ gate6y = 550
    $ gate7x = 875
    $ gate7y = 510
    $ gate8x = 1010
    $ gate8y = 640
    
    image LLH_1_ifRT = "R_T_if.png"
    image LLH_1_ifGT = "G_T_if.png"
    image LLH_1_ifBT = "B_T_if.png"
    image LLH_1_ifRGT = "RG_T_if.png"
    image LLH_1_ifBGT = "BG_T_if.png"
    image LLH_1_elseT = "G_T_else.png"
    image LLH_1_whileRBT = "RB_T_while.png"
    show LLH_1_ifRT at Position(xpos = ifRx, xanchor = 0, ypos = ifRy, yanchor = 0)
    show LLH_1_ifGT at Position(xpos = ifGx, xanchor = 0, ypos = ifGy, yanchor = 0)
    show LLH_1_ifBT at Position(xpos = ifBx, xanchor = 0, ypos = ifBy, yanchor = 0)
    show LLH_1_ifRGT at Position(xpos = ifRGx, xanchor = 0, ypos = ifRGy, yanchor = 0)
    show LLH_1_ifBGT at Position(xpos = ifBGx, xanchor = 0, ypos = ifBGy, yanchor = 0)
    show LLH_1_elseT at Position(xpos = else1x, xanchor = 0, ypos = else1y, yanchor = 0)
    show LLH_1_whileRBT at Position(xpos = whileRBx, xanchor = 0, ypos = whileRBy, yanchor = 0)
   
    # check conditons for locations
    $ whileRBin1 = False
    $ whileRBin2 = False
    $ whileRBin3 = False
    $ whileRBin4 = False
    $ whileRBin5 = False
    $ whileRBin6 = False
    $ whileRBin7 = False
    $ whileRBin8 = False

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
    
    $ ifRGin1 = False
    $ ifRGin2 = False
    $ ifRGin3 = False
    $ ifRGin4 = False
    $ ifRGin5 = False
    $ ifRGin6 = False
    $ ifRGin7 = False
    $ ifRGin8 = False
    
    $ ifBGin1 = False
    $ ifBGin2 = False
    $ ifBGin3 = False
    $ ifBGin4 = False
    $ ifBGin5 = False
    $ ifBGin6 = False
    $ ifBGin7 = False
    $ ifBGin8 = False
    
    #gate test vars
    $ temp_slot = ""
    $ temp_gate = ""
     
    #attempts for players
    $ attempts = 10    
    
    #*********************************************************
    #********************** show gates ***********************
    #*********************************************************  
    image LLH_1_tile52 = "blank_node.png"
    show LLH_1_tile52 at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
    image LLH_1_tile53 = "blank_node.png"
    show LLH_1_tile53 at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
    image LLH_1_tile54 = "blank_node.png"
    show LLH_1_tile54 at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
    image LLH_1_tile55 = "blank_node.png"
    show LLH_1_tile55 at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
    image LLH_1_tile56 = "blank_node.png"
    show LLH_1_tile56 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
    image LLH_1_tile57 = "blank_node.png"
    show LLH_1_tile57 at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
    image LLH_1_tile58 = "blank_node.png"
    show LLH_1_tile58 at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
    image LLH_1_tile59 = "blank_node.png"
    show LLH_1_tile59 at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)
 
    jump gamefile_llh1
    
    
label gamefile_llh1:
    
    #calls game screen
    call screen loopLogicHard_1Scr




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
            if ifRGin1 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileRBin1 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin1 = False
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
            if ifRGin2 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileRBin2 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin2 = False
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
            if ifRGin3 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileRBin3 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin3 = False
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
            if ifRGin4 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileRBin4 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin4 = False
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
            if ifRGin5 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileRBin5 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin5 = False
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
            if ifRGin6 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileRBin6 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin6 = False
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
            if ifRGin7 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileRBin7 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin7 = False
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
            if ifRGin8 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileRBin8 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin8 = False
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
            if ifRGin1 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileRBin1 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin1 = False
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
            if ifRGin2 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileRBin2 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin2 = False
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
            if ifRGin3 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileRBin3 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin3 = False
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
            if ifRGin4 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileRBin4 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin4 = False
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
            if ifRGin5 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileRBin5 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin5 = False
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
            if ifRGin6 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileRBin6 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin6 = False
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
            if ifRGin7 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileRBin7 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin7 = False
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
            if ifRGin8 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileRBin8 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin8 = False
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
            if ifRGin1 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileRBin1 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin1 = False
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
            if ifRGin2 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileRBin2 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin2 = False
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
            if ifRGin3 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileRBin3 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin3 = False
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
            if ifRGin4 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileRBin4 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin4 = False
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
            if ifRGin5 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileRBin5 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin5 = False
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
            if ifRGin6 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileRBin6 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin6 = False
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
            if ifRGin7 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileRBin7 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin7 = False
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
            if ifRGin8 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileRBin8 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin8 = False
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
    if gate_name == "if_RG_gate":
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
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileRBin1 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin1 = False
            if else1in1 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in1 = False
            if else2in1 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in1 = False

            #sets values for checks
            $ ifRGx = gate1x
            $ ifRGy = gate1y
            $ ifRGin1 = True
            $ ifRGin2 = False
            $ ifRGin3 = False
            $ ifRGin4 = False
            $ ifRGin5 = False
            $ ifRGin6 = False
            $ ifRGin7 = False
            $ ifRGin8 = False
            
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
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileRBin2 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin2 = False
            if else1in2 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in2 = False
            if else2in2 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in2 = False

            #sets values for checks
            $ ifRGx = gate2x
            $ ifRGy = gate2y
            $ ifRGin1 = False
            $ ifRGin2 = True
            $ ifRGin3 = False
            $ ifRGin4 = False
            $ ifRGin5 = False
            $ ifRGin6 = False
            $ ifRGin7 = False
            $ ifRGin8 = False
            
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
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileRBin3 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin3 = False
            if else1in3 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in3 = False
            if else2in3 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in3 = False

            #sets values for checks
            $ ifRGx = gate3x
            $ ifRGy = gate3y
            $ ifRGin1 = False
            $ ifRGin2 = False
            $ ifRGin3 = True
            $ ifRGin4 = False
            $ ifRGin5 = False
            $ ifRGin6 = False
            $ ifRGin7 = False
            $ ifRGin8 = False

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
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileRBin4 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin4 = False
            if else1in4 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in4 = False
            if else2in4 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in4 = False

            #sets values for checks
            $ ifRGx = gate4x
            $ ifRGy = gate4y
            $ ifRGin1 = False
            $ ifRGin2 = False
            $ ifRGin3 = False
            $ ifRGin4 = True
            $ ifRGin5 = False
            $ ifRGin6 = False
            $ ifRGin7 = False
            $ ifRGin8 = False
            
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
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileRBin5 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin5 = False
            if else1in5 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in5 = False
            if else2in5 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in5 = False

            #sets values for checks
            $ ifRGx = gate5x
            $ ifRGy = gate5y
            $ ifRGin1 = False
            $ ifRGin2 = False
            $ ifRGin3 = False
            $ ifRGin4 = False
            $ ifRGin5 = True
            $ ifRGin6 = False
            $ ifRGin7 = False
            $ ifRGin8 = False
            
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
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileRBin6 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin6 = False
            if else1in6 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in6 = False
            if else2in6 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in6 = False

            #sets values for checks
            $ ifRGx = gate6x
            $ ifRGy = gate6y
            $ ifRGin1 = False
            $ ifRGin2 = False
            $ ifRGin3 = False
            $ ifRGin4 = False
            $ ifRGin5 = False
            $ ifRGin6 = True
            $ ifRGin7 = False
            $ ifRGin8 = False
            
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
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileRBin7 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin7 = False
            if else1in7 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in7 = False
            if else2in7 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in7 = False

            #sets values for checks
            $ ifRGx = gate7x
            $ ifRGy = gate7y
            $ ifRGin1 = False
            $ ifRGin2 = False
            $ ifRGin3 = False
            $ ifRGin4 = False
            $ ifRGin5 = False
            $ ifRGin6 = False
            $ ifRGin7 = True
            $ ifRGin8 = False
            
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
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileRBin8 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin8 = False
            if else1in8 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in8 = False
            if else2in8 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in8 = False

            #sets values for checks
            $ ifRGx = gate8x
            $ ifRGy = gate8y
            $ ifRGin1 = False
            $ ifRGin2 = False
            $ ifRGin3 = False
            $ ifRGin4 = False
            $ ifRGin5 = False
            $ ifRGin6 = False
            $ ifRGin7 = False
            $ ifRGin8 = True
            
            
    #the fifth logic gate *******************************************************************************
    if gate_name == "if_BG_gate":
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
            if ifRGin1 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin1 = False
            if whileRBin1 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin1 = False
            if else1in1 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in1 = False
            if else2in1 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in1 = False

            #sets values for checks
            $ ifBGx = gate1x
            $ ifBGy = gate1y
            $ ifBGin1 = True
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = False
            
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
            if ifRGin2 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin2 = False
            if whileRBin2 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin2 = False
            if else1in2 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in2 = False
            if else2in2 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in2 = False

            #sets values for checks
            $ ifBGx = gate2x
            $ ifBGy = gate2y
            $ ifBGin1 = False
            $ ifBGin2 = True
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = False
            
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
            if ifRGin3 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin3 = False
            if whileRBin3 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin3 = False
            if else1in3 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in3 = False
            if else2in3 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in3 = False

            #sets values for checks
            $ ifBGx = gate3x
            $ ifBGy = gate3y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = True
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = False

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
            if ifRGin4 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin4 = False
            if whileRBin4 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin4 = False
            if else1in4 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in4 = False
            if else2in4 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in4 = False

            #sets values for checks
            $ ifBGx = gate4x
            $ ifBGy = gate4y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = True
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = False
            
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
            if ifRGin5 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin5 = False
            if whileRBin5 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin5 = False
            if else1in5 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in5 = False
            if else2in5 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in5 = False

            #sets values for checks
            $ ifBGx = gate5x
            $ ifBGy = gate5y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = True
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = False
            
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
            if ifRGin6 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin6 = False
            if whileRBin6 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin6 = False
            if else1in6 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in6 = False
            if else2in6 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in6 = False

            #sets values for checks
            $ ifBGx = gate6x
            $ ifBGy = gate6y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = True
            $ ifBGin7 = False
            $ ifBGin8 = False
            
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
            if ifRGin7 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin7 = False
            if whileRBin7 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin7 = False
            if else1in7 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in7 = False
            if else2in7 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in7 = False

            #sets values for checks
            $ ifBGx = gate7x
            $ ifBGy = gate7y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = True
            $ ifBGin8 = False
            
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
            if ifRGin8 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin8 = False
            if whileRBin8 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin8 = False
            if else1in8 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in8 = False
            if else2in8 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in8 = False

            #sets values for checks
            $ ifBGx = gate8x
            $ ifBGy = gate8y
            $ ifBGin1 = False
            $ ifBGin2 = False
            $ ifBGin3 = False
            $ ifBGin4 = False
            $ ifBGin5 = False
            $ ifBGin6 = False
            $ ifBGin7 = False
            $ ifBGin8 = True
            
            
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
            if ifRGin1 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileRBin1 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin1 = False
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
            if ifRGin2 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileRBin2 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin2 = False
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
            if ifRGin3 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileRBin3 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin3 = False
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
            if ifRGin4 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileRBin4 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin4 = False
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
            if ifRGin5 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileRBin5 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin5 = False
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
            if ifRGin6 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileRBin6 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin6 = False
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
            if ifRGin7 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileRBin7 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin7 = False
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
            if ifRGin8 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileRBin8 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin8 = False
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
            if ifRGin1 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if whileRBin1 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin1 = False
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
            if ifRGin2 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if whileRBin2 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin2 = False
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
            if ifRGin3 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if whileRBin3 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin3 = False
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
            if ifRGin4 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if whileRBin4 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin4 = False
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
            if ifRGin5 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if whileRBin5 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin5 = False
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
            if ifRGin6 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if whileRBin6 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin6 = False
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
            if ifRGin7 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if whileRBin7 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin7 = False
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
            if ifRGin8 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if whileRBin8 == True:
                $ whileRBx = 1445
                $ whileRBy = 500
                $ whileRBin8 = False
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
    if gate_name == "while_RB_gate":
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
            if ifRGin1 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin1 = False
            if ifBGin1 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin1 = False
            if else1in1 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in1 = False
            if else2in1 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in1 = False

            #sets values for checks
            $ whileRBx = gate1x
            $ whileRBy = gate1y
            $ whileRBin1 = True
            $ whileRBin2 = False
            $ whileRBin3 = False
            $ whileRBin4 = False
            $ whileRBin5 = False
            $ whileRBin6 = False
            $ whileRBin7 = False
            $ whileRBin8 = False
            
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
            if ifRGin2 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin2 = False
            if ifBGin2 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin2 = False
            if else1in2 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in2 = False
            if else2in2 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in2 = False

            #sets values for checks
            $ whileRBx = gate2x
            $ whileRBy = gate2y
            $ whileRBin1 = False
            $ whileRBin2 = True
            $ whileRBin3 = False
            $ whileRBin4 = False
            $ whileRBin5 = False
            $ whileRBin6 = False
            $ whileRBin7 = False
            $ whileRBin8 = False
            
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
            if ifRGin3 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin3 = False
            if ifBGin3 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin3 = False
            if else1in3 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in3 = False
            if else2in3 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in3 = False

            #sets values for checks
            $ whileRBx = gate3x
            $ whileRBy = gate3y
            $ whileRBin1 = False
            $ whileRBin2 = False
            $ whileRBin3 = True
            $ whileRBin4 = False
            $ whileRBin5 = False
            $ whileRBin6 = False
            $ whileRBin7 = False
            $ whileRBin8 = False

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
            if ifRGin4 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin4 = False
            if ifBGin4 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin4 = False
            if else1in4 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in4 = False
            if else2in4 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in4 = False

            #sets values for checks
            $ whileRBx = gate4x
            $ whileRBy = gate4y
            $ whileRBin1 = False
            $ whileRBin2 = False
            $ whileRBin3 = False
            $ whileRBin4 = True
            $ whileRBin5 = False
            $ whileRBin6 = False
            $ whileRBin7 = False
            $ whileRBin8 = False
            
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
            if ifRGin5 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin5 = False
            if ifBGin5 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin5 = False
            if else1in5 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in5 = False
            if else2in5 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in5 = False

            #sets values for checks
            $ whileRBx = gate5x
            $ whileRBy = gate5y
            $ whileRBin1 = False
            $ whileRBin2 = False
            $ whileRBin3 = False
            $ whileRBin4 = False
            $ whileRBin5 = True
            $ whileRBin6 = False
            $ whileRBin7 = False
            $ whileRBin8 = False
            
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
            if ifRGin6 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin6 = False
            if ifBGin6 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin6 = False
            if else1in6 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in6 = False
            if else2in6 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in6 = False

            #sets values for checks
            $ whileRBx = gate6x
            $ whileRBy = gate6y
            $ whileRBin1 = False
            $ whileRBin2 = False
            $ whileRBin3 = False
            $ whileRBin4 = False
            $ whileRBin5 = False
            $ whileRBin6 = True
            $ whileRBin7 = False
            $ whileRBin8 = False
            
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
            if ifRGin7 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin7 = False
            if ifBGin7 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin7 = False
            if else1in7 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in7 = False
            if else2in7 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in7 = False

            #sets values for checks
            $ whileRBx = gate7x
            $ whileRBy = gate7y
            $ whileRBin1 = False
            $ whileRBin2 = False
            $ whileRBin3 = False
            $ whileRBin4 = False
            $ whileRBin5 = False
            $ whileRBin6 = False
            $ whileRBin7 = True
            $ whileRBin8 = False
            
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
            if ifRGin8 == True:
                $ ifRGx = 1445
                $ ifRGy = 790
                $ ifRGin8 = False
            if ifBGin8 == True:
                $ ifBGx = 1585
                $ ifBGy = 790
                $ ifBGin8 = False
            if else1in8 == True:
                $ else1x = 1585
                $ else1y = 500
                $ else1in8 = False
            if else2in8 == True:
                $ else2x = 1585
                $ else2y = 500
                $ else2in8 = False

            #sets values for checks
            $ whileRBx = gate8x
            $ whileRBy = gate8y
            $ whileRBin1 = False
            $ whileRBin2 = False
            $ whileRBin3 = False
            $ whileRBin4 = False
            $ whileRBin5 = False
            $ whileRBin6 = False
            $ whileRBin7 = False
            $ whileRBin8 = True





    if ((temp_slot == "" and temp_gate == "" and slot_name != "null") and not
        (slot_name == "if_R_gate_return" or slot_name == "if_G_gate_return" or slot_name == "if_B_gate_return" or slot_name == "if_RG_gate_return" or
        slot_name == "if_BG_gate_return" or slot_name == "else_gate_return" or slot_name == "while_RB_gate_return")):
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
            if slot_name == "if_RG_gate_return":
                $ attempts +=1
                if gate_name == "if_RG_gate":
                    $ ifRGx = 1445
                    $ ifRGy = 790
                    $ ifRGin1 = False
                    $ ifRGin2 = False
                    $ ifRGin3 = False
                    $ ifRGin4 = False
                    $ ifRGin5 = False
                    $ ifRGin6 = False
                    $ ifRGin7 = False
                    $ ifRGin8 = False
            if slot_name == "if_BG_gate_return":
                $ attempts +=1
                if gate_name == "if_BG_gate":
                    $ ifBGx = 1585
                    $ ifBGy = 790
                    $ ifBGin1 = False
                    $ ifBGin2 = False
                    $ ifBGin3 = False
                    $ ifBGin4 = False
                    $ ifBGin5 = False
                    $ ifBGin6 = False
                    $ ifBGin7 = False
                    $ ifBGin8 = False
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
            if slot_name == "while_RB_gate_return":
                $ attempts +=1
                if gate_name == "while_RB_gate":
                    $ whileRBx = 1445
                    $ whileRBy = 500
                    $ whileRBin1 = False
                    $ whileRBin2 = False
                    $ whileRBin3 = False
                    $ whileRBin4 = False
                    $ whileRBin5 = False
                    $ whileRBin6 = False
                    $ whileRBin7 = False
                    $ whileRBin8 = False
                    

#*******************************************
#************image zone********************* 
#*******************************************
    $LLH_1_node1 = "None"
    $LLH_1_node2 = "None"
    $LLH_1_node3 = "None"
    $LLH_1_node4 = "None"
    $LLH_1_node5 = "None"
    
    $LLH_1_BEnd1 = "Off"
    $LLH_1_BEnd2 = "Off"
    $LLH_1_GEnd1 = "Off"
    $LLH_1_GEnd2 = "Off"
    $LLH_1_REnd = "Off"
    
    $LLH_1_RWhileNode = "Off"
    $LLH_1_BWhileNode = "Off"
          
    if (else1in1 == True or else2in1 == True):
        if ifRGin4 == True:
            image LLH_1_colorTile1 = "B_vertical.png"
            show LLH_1_colorTile1 at Position(xpos = 775, xanchor = 0, ypos = 300, yanchor = 0)
            image LLH_1_colorTile2 = "B_horizontal.png"
            show LLH_1_colorTile2 at Position(xpos = 840, xanchor = 0, ypos = 230, yanchor = 0)
            image LLH_1_colorTile3 = "B_horizontal.png"
            show LLH_1_colorTile3 at Position(xpos = 915, xanchor = 0, ypos = 230, yanchor = 0)
            $LLH_1_BEnd1 = "On"
            image LLH_1_colorTile5 = "B_connect_pipe_vertical.png"
            show LLH_1_colorTile5 at Position(xpos = 783, xanchor = 0, ypos = 380, yanchor = 0)
            image LLH_1_colorTile6 = "B_connect_pipe_vertical.png"
            show LLH_1_colorTile6 at Position(xpos = 783, xanchor = 0, ypos = 420, yanchor = 0)
            $LLH_1_node1 = "Blue"
            $LLH_1_node2 = "Blue"
            $LLH_1_node3 = "Blue"
        elif ifRGin4 == False: 
            hide LLH_1_colorTile1
            hide LLH_1_colorTile2
            hide LLH_1_colorTile3
            hide LLH_1_colorTile5 
            hide LLH_1_colorTile6
            
        if ifBGin4 == True:
            image LLH_1_colorTile10 = "R_vertical_ll.png"
            show LLH_1_colorTile10 at Position(xpos = 775, xanchor = 0, ypos = 300, yanchor = 0)
            image LLH_1_colorTile11 = "R_horizontal_ll.png"
            show LLH_1_colorTile11 at Position(xpos = 840, xanchor = 0, ypos = 230, yanchor = 0)
            image LLH_1_colorTile12 = "R_horizontal_ll.png"
            show LLH_1_colorTile12 at Position(xpos = 915, xanchor = 0, ypos = 230, yanchor = 0)
            $LLH_1_node1 = "Red"
        elif ifBGin4 == False: 
            hide LLH_1_colorTile10
            hide LLH_1_colorTile11
            hide LLH_1_colorTile12

        if ifRin4 == True:
            $LLH_1_node2 = "Green"
            $LLH_1_node3 = "Blue"
            
        if ifGin4 == True:
            $LLH_1_node1 = "Red"
            $LLH_1_node3 = "Blue"
            
        if ifBin4 == True:
            $LLH_1_node1 = "Red"
            $LLH_1_node2 = "Green"
            
    elif (else1in1 == False and else2in1 == False):
            hide LLH_1_colorTile1
            hide LLH_1_colorTile2
            hide LLH_1_colorTile3
            hide LLH_1_colorTile5 
            hide LLH_1_colorTile6    
            hide LLH_1_colorTile10
            hide LLH_1_colorTile11
            hide LLH_1_colorTile12
            hide LLH_1_colorTile13
            hide LLH_1_colorTile14
            hide LLH_1_colorTile16
            hide LLH_1_colorTile17
            hide LLH_1_colorTile18
            
    if ifBin1 == True and (ifRGin4 == True or ifBGin4 == True or ifRin4 == True or ifGin4 == True):
        image LLH_1_colorTile63 = "B_vertical.png"
        show LLH_1_colorTile63 at Position(xpos = 775, xanchor = 0, ypos = 300, yanchor = 0)
        image LLH_1_colorTile64 = "B_horizontal.png"
        show LLH_1_colorTile64 at Position(xpos = 840, xanchor = 0, ypos = 230, yanchor = 0)
        image LLH_1_colorTile65 = "B_horizontal.png"
        show LLH_1_colorTile65 at Position(xpos = 915, xanchor = 0, ypos = 230, yanchor = 0)
        $LLH_1_BEnd1 = "On"
        image LLH_1_colorTile67 = "B_connect_pipe_vertical.png"
        show LLH_1_colorTile67 at Position(xpos = 783, xanchor = 0, ypos = 380, yanchor = 0)
        image LLH_1_colorTile68 = "B_connect_pipe_vertical.png"
        show LLH_1_colorTile68 at Position(xpos = 783, xanchor = 0, ypos = 420, yanchor = 0)
        $LLH_1_node1 = "Blue"
        $LLH_1_node2 = "Blue"
        $LLH_1_node3 = "Blue"
    else: 
        hide LLH_1_colorTile63
        hide LLH_1_colorTile64
        hide LLH_1_colorTile65
        hide LLH_1_colorTile67
        hide LLH_1_colorTile68
        
    if ifRin1 == True and (ifRGin4 == True or ifBGin4 == True or ifGin4 == True or ifBin4 == True):
        image LLH_1_colorTile72 = "R_vertical_ll.png"
        show LLH_1_colorTile72 at Position(xpos = 775, xanchor = 0, ypos = 300, yanchor = 0)
        image LLH_1_colorTile73 = "R_horizontal_ll.png"
        show LLH_1_colorTile73 at Position(xpos = 840, xanchor = 0, ypos = 230, yanchor = 0)
        image LLH_1_colorTile74 = "R_horizontal_ll.png"
        show LLH_1_colorTile74 at Position(xpos = 915, xanchor = 0, ypos = 230, yanchor = 0)
        $LLH_1_node1 = "Red"
    else: 
        hide LLH_1_colorTile72
        hide LLH_1_colorTile73
        hide LLH_1_colorTile74
        
    if ifGin1 == True and (ifRGin4 == True or ifBGin4 == True or ifRin4 == True or ifBin4 == True):
        image LLH_1_colorTile123 = "G_vertical_ll.png"
        show LLH_1_colorTile123 at Position(xpos = 772, xanchor = 0, ypos = 300, yanchor = 0)
        image LLH_1_colorTile124 = "G_horizontal_ll.png"
        show LLH_1_colorTile124 at Position(xpos = 837, xanchor = 0, ypos = 230, yanchor = 0)
        image LLH_1_colorTile125 = "G_horizontal_ll.png"
        show LLH_1_colorTile125 at Position(xpos = 912, xanchor = 0, ypos = 230, yanchor = 0)
        image LLH_1_colorTile122 = "G_connect_pipe_vertical.png"
        show LLH_1_colorTile122 at Position(xpos = 783, xanchor = 0, ypos = 380, yanchor = 0)
        $LLH_1_node1 = "Green"
        $LLH_1_node2 = "Green"
    else: 
        hide LLH_1_colorTile122
        hide LLH_1_colorTile123
        hide LLH_1_colorTile124
        hide LLH_1_colorTile125
            
    if ifRGin4 == True:
        image LLH_1_colorTile18 = "R_horizontal_ll.png"
        show LLH_1_colorTile18 at Position(xpos = 800, xanchor = 0, ypos = 370, yanchor = 0)
        image LLH_1_colorTile19 = "G_horizontal_ll.png"
        show LLH_1_colorTile19 at Position(xpos = 800, xanchor = 0, ypos = 410, yanchor = 0)
        image LLH_1_colorTile43 = "R_horizontal_ll.png"
        show LLH_1_colorTile43 at Position(xpos = 975, xanchor = 0, ypos = 390, yanchor = 0)
        image LLH_1_colorTile44 = "G_horizontal_short.png"
        show LLH_1_colorTile44 at Position(xpos = 950, xanchor = 0, ypos = 430, yanchor = 0)
        image LLH_1_colorTile45 = "R_vertical_ll.png"
        show LLH_1_colorTile45 at Position(xpos = 1072, xanchor = 0, ypos = 438, yanchor = 0)
        image LLH_1_colorTile46 = "R_vertical_short.png"
        show LLH_1_colorTile46 at Position(xpos = 1072, xanchor = 0, ypos = 513, yanchor = 0)
        image LLH_1_colorTile47 = "G_vertical_ll.png"
        show LLH_1_colorTile47 at Position(xpos = 1019, xanchor = 0, ypos = 478, yanchor = 0)
        
        if ifRin8 == True:
            image LLH_1_colorTile48 = "R_vertical_ll.png"
            show LLH_1_colorTile48 at Position(xpos = 1072, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_1_colorTile49 = "R_vertical_ll.png"
            show LLH_1_colorTile49 at Position(xpos = 1045, xanchor = 0, ypos = 740, yanchor = 0)
            $LLH_1_REnd = "On"
            if else1in7 == True or else2in7 == True or ifGin7 == True:
                image LLH_1_colorTile54 = "G_horizontal_short.png"
                show LLH_1_colorTile54 at Position(xpos = 975, xanchor = 0, ypos = 548, yanchor = 0)
                image LLH_1_colorTile87 = "G_vertical_short.png"
                show LLH_1_colorTile87 at Position(xpos = 897, xanchor = 0, ypos = 600, yanchor = 0) 
                $LLH_1_node4 = "Green"
            else:
                hide LLH_1_colorTile54
                hide LLH_1_colorTile87
        elif ifRin8 == False:
            hide LLH_1_colorTile48
            hide LLH_1_colorTile49
            hide LLH_1_colorTile54
            hide LLH_1_colorTile87
                
        if ifGin8 == True:
            image LLH_1_colorTile51 = "G_vertical_ll.png"
            show LLH_1_colorTile51 at Position(xpos = 1019, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_1_colorTile52 = "G_vertical_ll.png"
            show LLH_1_colorTile52 at Position(xpos = 1042, xanchor = 0, ypos = 740, yanchor = 0)
            if else1in7 == True or else2in7 == True or ifRin7 == True:
                image LLH_1_colorTile55 = "R_connect_pipe.png"
                show LLH_1_colorTile55 at Position(xpos = 1037, xanchor = 0, ypos = 555, yanchor = 0)
                image LLH_1_colorTile56 = "R_vertical_short.png"
                show LLH_1_colorTile56 at Position(xpos = 900, xanchor = 0, ypos = 600, yanchor = 0)
                image LLH_1_colorTile58 = "R_horizontal_short.png"
                show LLH_1_colorTile58 at Position(xpos = 975, xanchor = 0, ypos = 548, yanchor = 0)
                $LLH_1_node4 = "Red"
                $LLH_1_node5 = "Red"
                if whileRBin6 == True:
                    image LLH_1_colorTile120 = "R_vertical_short.png"
                    show LLH_1_colorTile120 at Position(xpos = 900, xanchor = 0, ypos = 679, yanchor = 0)
                    image LLH_1_colorTile121 = "R_vertical_short.png"
                    show LLH_1_colorTile121 at Position(xpos = 900, xanchor = 0, ypos = 750, yanchor = 0)
                elif whileRBin6 == False:
                    hide LLH_1_colorTile120
                    hide LLH_1_colorTile121   
            else:
                hide LLH_1_colorTile55
                hide LLH_1_colorTile56
                hide LLH_1_colorTile58
                hide LLH_1_colorTile120
                hide LLH_1_colorTile121   
        elif ifGin8 == False:
            hide LLH_1_colorTile51
            hide LLH_1_colorTile52
            hide LLH_1_colorTile55
            hide LLH_1_colorTile56
            hide LLH_1_colorTile58 
            hide LLH_1_colorTile120
            hide LLH_1_colorTile121              
            
    elif ifRGin4 == False:
        hide LLH_1_colorTile18
        hide LLH_1_colorTile19
        hide LLH_1_colorTile43
        hide LLH_1_colorTile44
        hide LLH_1_colorTile45
        hide LLH_1_colorTile46
        hide LLH_1_colorTile47
        hide LLH_1_colorTile48
        hide LLH_1_colorTile49
        hide LLH_1_colorTile51
        hide LLH_1_colorTile52
        hide LLH_1_colorTile54
        hide LLH_1_colorTile55
        hide LLH_1_colorTile56
        hide LLH_1_colorTile58
        hide LLH_1_colorTile87
        hide LLH_1_colorTile120
        hide LLH_1_colorTile121   
        
    if ifBGin4 == True:
        image LLH_1_colorTile20 = "G_horizontal_ll.png"
        show LLH_1_colorTile20 at Position(xpos = 800, xanchor = 0, ypos = 410, yanchor = 0)        
        image LLH_1_colorTile21 = "B_horizontal.png"
        show LLH_1_colorTile21 at Position(xpos = 800, xanchor = 0, ypos = 450, yanchor = 0)
        image LLH_1_colorTile90 = "G_horizontal_ll.png"
        show LLH_1_colorTile90 at Position(xpos = 975, xanchor = 0, ypos = 390, yanchor = 0)
        image LLH_1_colorTile91 = "B_horizontal_short.png"
        show LLH_1_colorTile91 at Position(xpos = 950, xanchor = 0, ypos = 430, yanchor = 0)
        image LLH_1_colorTile92 = "G_vertical_ll.png"
        show LLH_1_colorTile92 at Position(xpos = 1069, xanchor = 0, ypos = 438, yanchor = 0)
        image LLH_1_colorTile93 = "G_vertical_short.png"
        show LLH_1_colorTile93 at Position(xpos = 1069, xanchor = 0, ypos = 513, yanchor = 0)
        image LLH_1_colorTile94 = "B_vertical.png"
        show LLH_1_colorTile94 at Position(xpos = 1022, xanchor = 0, ypos = 478, yanchor = 0)
        if ifGin8 == True:
            image LLH_1_colorTile95 = "G_vertical_ll.png"
            show LLH_1_colorTile95 at Position(xpos = 1069, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_1_colorTile96 = "G_vertical_ll.png"
            show LLH_1_colorTile96 at Position(xpos = 1042, xanchor = 0, ypos = 740, yanchor = 0)
            if else1in7 == True or else2in7 == True or ifBin7 == True:
                image LLH_1_colorTile98 = "B_horizontal_short.png"
                show LLH_1_colorTile98 at Position(xpos = 975, xanchor = 0, ypos = 548, yanchor = 0)
                image LLH_1_colorTile99 = "B_vertical_short.png"
                show LLH_1_colorTile99 at Position(xpos = 900, xanchor = 0, ypos = 600, yanchor = 0)
                $LLH_1_node4 = "Blue"
                if whileRBin6 == True:
                    image LLH_1_colorTile107 = "B_vertical_short.png"
                    show LLH_1_colorTile107 at Position(xpos = 900, xanchor = 0, ypos = 679, yanchor = 0)
                    image LLH_1_colorTile108 = "B_vertical_short.png"
                    show LLH_1_colorTile108 at Position(xpos = 900, xanchor = 0, ypos = 750, yanchor = 0)
                elif whileRBin6 == False:
                    hide LLH_1_colorTile107
                    hide LLH_1_colorTile108
            else:
                hide LLH_1_colorTile98
                hide LLH_1_colorTile99
                hide LLH_1_colorTile107
                hide LLH_1_colorTile108
        elif ifGin8 == False:
            hide LLH_1_colorTile95
            hide LLH_1_colorTile96
            hide LLH_1_colorTile98
            hide LLH_1_colorTile99
            hide LLH_1_colorTile107
            hide LLH_1_colorTile108
                
        if ifBin8 == True:
            image LLH_1_colorTile100 = "B_vertical.png"
            show LLH_1_colorTile100 at Position(xpos = 1022, xanchor = 0, ypos = 568, yanchor = 0)
            image LLH_1_colorTile101 = "B_vertical.png"
            show LLH_1_colorTile101 at Position(xpos = 1045, xanchor = 0, ypos = 740, yanchor = 0)
            if else1in7 == True or else2in7 == True or ifGin7 == True:
                image LLH_1_colorTile102 = "G_connect_pipe.png"
                show LLH_1_colorTile102 at Position(xpos = 1037, xanchor = 0, ypos = 555, yanchor = 0)
                image LLH_1_colorTile105 = "G_horizontal_short.png"
                show LLH_1_colorTile105 at Position(xpos = 975, xanchor = 0, ypos = 548, yanchor = 0)
                image LLH_1_colorTile106 = "G_vertical_short.png"
                show LLH_1_colorTile106 at Position(xpos = 897, xanchor = 0, ypos = 600, yanchor = 0)
                $LLH_1_node4 = "Green"
                $LLH_1_node5 = "Green"
            else:
                hide LLH_1_colorTile102
                hide LLH_1_colorTile105
                hide LLH_1_colorTile106
        elif ifBin8 == False:
            hide LLH_1_colorTile100
            hide LLH_1_colorTile101
            hide LLH_1_colorTile102
            hide LLH_1_colorTile105 
            hide LLH_1_colorTile106 
            
    elif ifBGin4 == False:
        hide LLH_1_colorTile20
        hide LLH_1_colorTile21
        hide LLH_1_colorTile90
        hide LLH_1_colorTile91
        hide LLH_1_colorTile92
        hide LLH_1_colorTile93
        hide LLH_1_colorTile94
        hide LLH_1_colorTile95
        hide LLH_1_colorTile96
        hide LLH_1_colorTile98
        hide LLH_1_colorTile99
        hide LLH_1_colorTile100
        hide LLH_1_colorTile101
        hide LLH_1_colorTile102
        hide LLH_1_colorTile105 
        hide LLH_1_colorTile106
        hide LLH_1_colorTile107
        hide LLH_1_colorTile108
        
    if ifRin4 == True:
        image LLH_1_colorTile22 = "R_horizontal_ll.png"
        show LLH_1_colorTile22 at Position(xpos = 800, xanchor = 0, ypos = 370, yanchor = 0)
    elif ifRin4 == False:
        hide LLH_1_colorTile22
    if ifGin4 == True:
        image LLH_1_colorTile29 = "G_horizontal_ll.png"
        show LLH_1_colorTile29 at Position(xpos = 800, xanchor = 0, ypos = 410, yanchor = 0)
    elif ifGin4 == False:
        hide LLH_1_colorTile29
    if ifBin4 == True:
        image LLH_1_colorTile30 = "B_horizontal.png"
        show LLH_1_colorTile30 at Position(xpos = 800, xanchor = 0, ypos = 450, yanchor = 0)
    elif ifBin4 == False:
        hide LLH_1_colorTile30
        
    if ifBGin3 == True:
        image LLH_1_colorTile31 = "G_horizontal_ll.png"
        show LLH_1_colorTile31 at Position(xpos = 525, xanchor = 0, ypos = 390, yanchor = 0)
        image LLH_1_colorTile32 = "B_horizontal.png"
        show LLH_1_colorTile32 at Position(xpos = 525, xanchor = 0, ypos = 430, yanchor = 0)
        
        if ifGin2 == True:
            image LLH_1_colorTile33 = "G_horizontal_ll.png"
            show LLH_1_colorTile33 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_1_colorTile34 = "G_horizontal_ll.png"
            show LLH_1_colorTile34 at Position(xpos = 190, xanchor = 0, ypos = 410, yanchor = 0)
            $LLH_1_GEnd1 = "On"
        elif ifGin2 == False:
            hide LLH_1_colorTile33
            hide LLH_1_colorTile34
        if ifBin2 == True:
            image LLH_1_colorTile36 = "B_horizontal.png"
            show LLH_1_colorTile36 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_1_colorTile37 = "B_horizontal.png"
            show LLH_1_colorTile37 at Position(xpos = 190, xanchor = 0, ypos = 410, yanchor = 0)
        elif ifBin2 == False:
            hide LLH_1_colorTile36
            hide LLH_1_colorTile37
            
        if ifGin5 == True:
            image LLH_1_colorTile38 = "G_vertical_ll.png"
            show LLH_1_colorTile38 at Position(xpos = 467, xanchor = 0, ypos = 475, yanchor = 0)
            image LLH_1_colorTile39 = "G_vertical_ll.png"
            show LLH_1_colorTile39 at Position(xpos = 467, xanchor = 0, ypos = 650, yanchor = 0)
        elif ifGin5 == False:
            hide LLH_1_colorTile38
            hide LLH_1_colorTile39
        if ifBin5 == True:
            image LLH_1_colorTile40 = "B_vertical.png"
            show LLH_1_colorTile40 at Position(xpos = 470, xanchor = 0, ypos = 475, yanchor = 0)
            image LLH_1_colorTile41 = "B_vertical.png"
            show LLH_1_colorTile41 at Position(xpos = 470, xanchor = 0, ypos = 650, yanchor = 0)
            $LLH_1_BEnd2 = "On"
        elif ifBin5 == False:
            hide LLH_1_colorTile40
            hide LLH_1_colorTile41
            
    elif ifBGin3 == False:
        hide LLH_1_colorTile31 
        hide LLH_1_colorTile32
        hide LLH_1_colorTile33
        hide LLH_1_colorTile34
        hide LLH_1_colorTile36
        hide LLH_1_colorTile37
        hide LLH_1_colorTile38
        hide LLH_1_colorTile39
        hide LLH_1_colorTile40
        hide LLH_1_colorTile41
        
    if ifRGin3 == True:
        image LLH_1_colorTile109 = "R_horizontal_ll.png"
        show LLH_1_colorTile109 at Position(xpos = 525, xanchor = 0, ypos = 390, yanchor = 0)
        image LLH_1_colorTile110 = "G_horizontal_ll.png"
        show LLH_1_colorTile110 at Position(xpos = 525, xanchor = 0, ypos = 430, yanchor = 0)
        
        if ifRin2 == True:
            image LLH_1_colorTile111 = "R_horizontal_ll.png"
            show LLH_1_colorTile111 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_1_colorTile112 = "R_horizontal_ll.png"
            show LLH_1_colorTile112 at Position(xpos = 190, xanchor = 0, ypos = 410, yanchor = 0)
        elif ifRin2 == False:
            hide LLH_1_colorTile111
            hide LLH_1_colorTile112
        if ifGin2 == True:
            image LLH_1_colorTile113 = "G_horizontal_ll.png"
            show LLH_1_colorTile113 at Position(xpos = 365, xanchor = 0, ypos = 410, yanchor = 0)
            image LLH_1_colorTile114 = "G_horizontal_ll.png"
            show LLH_1_colorTile114 at Position(xpos = 190, xanchor = 0, ypos = 410, yanchor = 0)
            $LLH_1_GEnd1 = "On"
        elif ifGin2 == False:
            hide LLH_1_colorTile113
            hide LLH_1_colorTile114
            
        if ifRin5 == True:
            image LLH_1_colorTile116 = "R_vertical_ll.png"
            show LLH_1_colorTile116 at Position(xpos = 470, xanchor = 0, ypos = 475, yanchor = 0)
            image LLH_1_colorTile117 = "R_vertical_ll.png"
            show LLH_1_colorTile117 at Position(xpos = 470, xanchor = 0, ypos = 650, yanchor = 0)
        elif ifRin5 == False:
            hide LLH_1_colorTile116
            hide LLH_1_colorTile117
        if ifGin5 == True:
            image LLH_1_colorTile118 = "G_vertical_ll.png"
            show LLH_1_colorTile118 at Position(xpos = 467, xanchor = 0, ypos = 475, yanchor = 0)
            image LLH_1_colorTile119 = "G_vertical_ll.png"
            show LLH_1_colorTile119 at Position(xpos = 467, xanchor = 0, ypos = 650, yanchor = 0)
        elif ifGin5 == False:
            hide LLH_1_colorTile118
            hide LLH_1_colorTile119
            
    elif ifBGin3 == False:
        hide LLH_1_colorTile109
        hide LLH_1_colorTile110
        hide LLH_1_colorTile111
        hide LLH_1_colorTile112
        hide LLH_1_colorTile113
        hide LLH_1_colorTile114
        hide LLH_1_colorTile116
        hide LLH_1_colorTile117
        hide LLH_1_colorTile118
        hide LLH_1_colorTile119
      
    if ifRin3 == True:
        image LLH_1_colorTile130 = "R_horizontal_ll.png"
        show LLH_1_colorTile130 at Position(xpos = 525, xanchor = 0, ypos = 390, yanchor = 0)
    else:
        hide LLH_1_colorTile130
        
    if ifGin3 == True:
        image LLH_1_colorTile131 = "G_horizontal_ll.png"
        show LLH_1_colorTile131 at Position(xpos = 525, xanchor = 0, ypos = 390, yanchor = 0)
    else:
        hide LLH_1_colorTile131
        
    if ifBin3 == True:
        image LLH_1_colorTile132 = "B_horizontal.png"
        show LLH_1_colorTile132 at Position(xpos = 525, xanchor = 0, ypos = 390, yanchor = 0)
    else:
        hide LLH_1_colorTile132
        
    if whileRBin6 == True:
        image LLH_1_colorTile59 = "B_vertical.png"
        show LLH_1_colorTile59 at Position(xpos = 620, xanchor = 0, ypos = 475, yanchor = 0)
        image LLH_1_colorTile60 = "R_vertical_ll.png"
        show LLH_1_colorTile60 at Position(xpos = 660, xanchor = 0, ypos = 475, yanchor = 0)
        image LLH_1_colorTile77 = "y_horizontal_short_on.png"
        show LLH_1_colorTile77 at Position(xpos = 680, xanchor = 0, ypos = 565, yanchor = 0)
        image LLH_1_colorTile78 = "y_horizontal_short_on.png"
        show LLH_1_colorTile78 at Position(xpos = 755, xanchor = 0, ypos = 565, yanchor = 0)
        image LLH_1_colorTile79 = "y_vertical_short_on.png"
        show LLH_1_colorTile79 at Position(xpos = 790, xanchor = 0, ypos = 595, yanchor = 0)
        image LLH_1_colorTile80 = "y_horizontal_short_on.png"
        show LLH_1_colorTile80 at Position(xpos = 800, xanchor = 0, ypos = 650, yanchor = 0)
        image LLH_1_colorTile81 = "y_horizontal_short_on.png"
        show LLH_1_colorTile81 at Position(xpos = 870, xanchor = 0, ypos = 650, yanchor = 0)
        image LLH_1_colorTile82 = "y_horizontal_short_on.png"
        show LLH_1_colorTile82 at Position(xpos = 700, xanchor = 0, ypos = 610, yanchor = 0)
        image LLH_1_colorTile83 = "y_vertical_short_on.png"
        show LLH_1_colorTile83 at Position(xpos = 760, xanchor = 0, ypos = 620, yanchor = 0)
        image LLH_1_colorTile84 = "y_vertical_short_on.png"
        show LLH_1_colorTile84 at Position(xpos = 760, xanchor = 0, ypos = 685, yanchor = 0)
        image LLH_1_colorTile85 = "y_horizontal_short_on.png"
        show LLH_1_colorTile85 at Position(xpos = 790, xanchor = 0, ypos = 720, yanchor = 0)
        image LLH_1_colorTile86 = "y_horizontal_short_on.png"
        show LLH_1_colorTile86 at Position(xpos = 860, xanchor = 0, ypos = 720, yanchor = 0)
        $LLH_1_RWhileNode = "On"
        $LLH_1_BWhileNode = "On"

    elif whileRBin6 == False: 
        hide LLH_1_colorTile59
        hide LLH_1_colorTile60
        hide LLH_1_colorTile77
        hide LLH_1_colorTile78
        hide LLH_1_colorTile79 
        hide LLH_1_colorTile80 
        hide LLH_1_colorTile81 
        hide LLH_1_colorTile82 
        hide LLH_1_colorTile83 
        hide LLH_1_colorTile84 
        hide LLH_1_colorTile85 
        hide LLH_1_colorTile86 
        
    if ifRin6 == True:
        image LLH_1_colorTile115 = "R_vertical_ll.png"
        show LLH_1_colorTile115 at Position(xpos = 620, xanchor = 0, ypos = 475, yanchor = 0)
    else:
        hide LLH_1_colorTile115
        
    if ifGin6 == True:
        image LLH_1_colorTile35 = "G_vertical_ll.png"
        show LLH_1_colorTile35 at Position(xpos = 617, xanchor = 0, ypos = 475, yanchor = 0)
    else:
        hide LLH_1_colorTile35
        
    if ifBin6 == True:
        image LLH_1_colorTile97 = "B_vertical.png"
        show LLH_1_colorTile97 at Position(xpos = 620, xanchor = 0, ypos = 475, yanchor = 0)
    else:
        hide LLH_1_colorTile97
        
    if ifRGin6 == True:
        image LLH_1_colorTile126 = "R_vertical_ll.png"
        show LLH_1_colorTile126 at Position(xpos = 620, xanchor = 0, ypos = 475, yanchor = 0)
        image LLH_1_colorTile127 = "G_vertical_ll.png"
        show LLH_1_colorTile127 at Position(xpos = 657, xanchor = 0, ypos = 475, yanchor = 0)
    else:
        hide LLH_1_colorTile126
        hide LLH_1_colorTile127     
        
    if ifBGin6 == True:
        image LLH_1_colorTile128 = "G_vertical_ll.png"
        show LLH_1_colorTile128 at Position(xpos = 617, xanchor = 0, ypos = 475, yanchor = 0)
        image LLH_1_colorTile129 = "B_vertical.png"
        show LLH_1_colorTile129 at Position(xpos = 660, xanchor = 0, ypos = 475, yanchor = 0)
    else:
        hide LLH_1_colorTile128
        hide LLH_1_colorTile129 
        
    if (whileRBin6 == True and 
            ((ifRGin4 == True and (else1in7 == True or else2in7 == True or ifGin7 == True) and ifRin8 == True) or
            (ifBGin4 == True and ifBin8 == True and (else1in7 == True or else2in7 == True or ifGin7 ==True)))):
        image LLH_1_colorTile88 = "G_vertical_short.png"
        show LLH_1_colorTile88 at Position(xpos = 897, xanchor = 0, ypos = 679, yanchor = 0)
        image LLH_1_colorTile89 = "G_vertical_short.png"
        show LLH_1_colorTile89 at Position(xpos = 897, xanchor = 0, ypos = 750, yanchor = 0)
        $LLH_1_GEnd2 = "On"
    else:
        hide LLH_1_colorTile88
        hide LLH_1_colorTile89
        
        
    #Redraw Connect Nodes *********************************************************************
    hide LLH_1_WNode1
    hide LLH_1_WNode2
    hide LLH_1_WNode3
    hide LLH_1_WNode4
    hide LLH_1_WNode5
    hide LLH_1_RNode1
    hide LLH_1_RNode2
    hide LLH_1_RNode3
    hide LLH_1_RNode4
    hide LLH_1_RNode5
    hide LLH_1_GNode1
    hide LLH_1_GNode2
    hide LLH_1_GNode3
    hide LLH_1_GNode4
    hide LLH_1_GNode5
    hide LLH_1_BNode1
    hide LLH_1_BNode2
    hide LLH_1_BNode3
    hide LLH_1_BNode4
    hide LLH_1_BNode5
    
    image LLH_1_WNode1 = "W_connect_node.png"
    image LLH_1_WNode2 = "W_connect_node.png"
    image LLH_1_WNode3 = "W_connect_node.png"
    image LLH_1_WNode4 = "W_connect_node.png"
    image LLH_1_WNode5 = "W_connect_node.png"
    image LLH_1_RNode1 = "R_connect_node.png"
    image LLH_1_RNode2 = "R_connect_node.png"
    image LLH_1_RNode3 = "R_connect_node.png"
    image LLH_1_RNode4 = "R_connect_node.png"
    image LLH_1_RNode5 = "R_connect_node.png"
    image LLH_1_GNode1 = "G_connect_node.png"
    image LLH_1_GNode2 = "G_connect_node.png"
    image LLH_1_GNode3 = "G_connect_node.png"
    image LLH_1_GNode4 = "G_connect_node.png"
    image LLH_1_GNode5 = "G_connect_node.png"
    image LLH_1_BNode1 = "B_connect_node.png"
    image LLH_1_BNode2 = "B_connect_node.png"
    image LLH_1_BNode3 = "B_connect_node.png"
    image LLH_1_BNode4 = "B_connect_node.png"
    image LLH_1_BNode5 = "B_connect_node.png"
    
    if LLH_1_node1 == "None":
        show LLH_1_WNode1 at Position(xpos = 772, xanchor = 0, ypos = 365, yanchor = 0) 
    elif LLH_1_node1 == "Red":
        show LLH_1_RNode1 at Position(xpos = 772, xanchor = 0, ypos = 365, yanchor = 0) 
    elif LLH_1_node1 == "Green":
        show LLH_1_GNode1 at Position(xpos = 772, xanchor = 0, ypos = 365, yanchor = 0) 
    elif LLH_1_node1 == "Blue":
        show LLH_1_BNode1 at Position(xpos = 772, xanchor = 0, ypos = 365, yanchor = 0) 
        
    if LLH_1_node2 == "None":
        show LLH_1_WNode2 at Position(xpos = 772, xanchor = 0, ypos = 407, yanchor = 0) 
    elif LLH_1_node2 == "Red":
        show LLH_1_RNode2 at Position(xpos = 772, xanchor = 0, ypos = 407, yanchor = 0) 
    elif LLH_1_node2 == "Green":
        show LLH_1_GNode2 at Position(xpos = 772, xanchor = 0, ypos = 407, yanchor = 0) 
    elif LLH_1_node2 == "Blue":
        show LLH_1_BNode2 at Position(xpos = 772, xanchor = 0, ypos = 407, yanchor = 0) 
        
    if LLH_1_node3 == "None":
        show LLH_1_WNode3 at Position(xpos = 772, xanchor = 0, ypos = 450, yanchor = 0) 
    elif LLH_1_node3 == "Red":
        show LLH_1_RNode3 at Position(xpos = 772, xanchor = 0, ypos = 450, yanchor = 0) 
    elif LLH_1_node3 == "Green":
        show LLH_1_GNode3 at Position(xpos = 772, xanchor = 0, ypos = 450, yanchor = 0) 
    elif LLH_1_node3 == "Blue":
        show LLH_1_BNode3 at Position(xpos = 772, xanchor = 0, ypos = 450, yanchor = 0) 
        
    if LLH_1_node4 == "None":
        show LLH_1_WNode4 at Position(xpos = 1020, xanchor = 0, ypos = 545, yanchor = 0) 
    elif LLH_1_node4 == "Red":
        show LLH_1_RNode4 at Position(xpos = 1020, xanchor = 0, ypos = 545, yanchor = 0) 
    elif LLH_1_node4 == "Green":
        show LLH_1_GNode4 at Position(xpos = 1020, xanchor = 0, ypos = 545, yanchor = 0) 
    elif LLH_1_node4 == "Blue":
        show LLH_1_BNode4 at Position(xpos = 1020, xanchor = 0, ypos = 545, yanchor = 0) 
        
    if LLH_1_node5 == "None":
        show LLH_1_WNode5 at Position(xpos = 1070, xanchor = 0, ypos = 545, yanchor = 0) 
    elif LLH_1_node5 == "Red":
        show LLH_1_RNode5 at Position(xpos = 1070, xanchor = 0, ypos = 545, yanchor = 0) 
    elif LLH_1_node5 == "Green":
        show LLH_1_GNode5 at Position(xpos = 1070, xanchor = 0, ypos = 545, yanchor = 0) 
    elif LLH_1_node5 == "Blue":
        show LLH_1_BNode5 at Position(xpos = 1070, xanchor = 0, ypos = 545, yanchor = 0) 
    
    #Redraw Ends *******************************************************************************
    hide LLH_1_BlueEnd1_Off
    hide LLH_1_BlueEnd2_Off
    hide LLH_1_GreenEnd1_Off
    hide LLH_1_GreenEnd2_Off
    hide LLH_1_RedEnd_Off
    hide LLH_1_BlueEnd1_On
    hide LLH_1_BlueEnd2_On
    hide LLH_1_GreenEnd1_On
    hide LLH_1_GreenEnd2_On
    hide LLH_1_RedEnd_On
    
    image LLH_1_BlueEnd1_Off = "B_end_off.png"
    image LLH_1_BlueEnd2_Off = "B_end_off.png"
    image LLH_1_GreenEnd1_Off = "G_end_off.png"
    image LLH_1_GreenEnd2_Off = "G_end_off.png"
    image LLH_1_RedEnd_Off = "R_end_off.png"
    image LLH_1_BlueEnd1_On = "B_end_on.png"
    image LLH_1_BlueEnd2_On = "B_end_on.png"
    image LLH_1_GreenEnd1_On = "G_end_on.png"
    image LLH_1_GreenEnd2_On = "G_end_on.png"
    image LLH_1_RedEnd_On = "R_end_on.png"
    
    if LLH_1_BEnd1 == "Off":
        show LLH_1_BlueEnd1_Off at Position(xpos = 980, xanchor = 0, ypos = 200, yanchor = 0)
    elif LLH_1_BEnd1 == "On":
        show LLH_1_BlueEnd1_On at Position(xpos = 980, xanchor = 0, ypos = 200, yanchor = 0)
        
    if LLH_1_BEnd2 == "Off":
        show LLH_1_BlueEnd2_Off at Position(xpos = 435, xanchor = 0, ypos = 725, yanchor = 0)
    elif LLH_1_BEnd2 == "On":
        show LLH_1_BlueEnd2_On at Position(xpos = 435, xanchor = 0, ypos = 725, yanchor = 0)
        
    if LLH_1_GEnd1 == "Off":
        show LLH_1_GreenEnd1_Off at Position(xpos = 100, xanchor = 0, ypos = 375, yanchor = 0)
    elif LLH_1_GEnd1 == "On":
        show LLH_1_GreenEnd1_On at Position(xpos = 100, xanchor = 0, ypos = 375, yanchor = 0)
        
    if LLH_1_GEnd2 == "Off":
        show LLH_1_GreenEnd2_Off at Position(xpos = 865, xanchor = 0, ypos = 785, yanchor = 0)
    elif LLH_1_GEnd2 == "On":
        show LLH_1_GreenEnd2_On at Position(xpos = 865, xanchor = 0, ypos = 785, yanchor = 0)
        
    if LLH_1_REnd == "Off":
        show LLH_1_RedEnd_Off at Position(xpos = 1010, xanchor = 0, ypos = 810, yanchor = 0)
    elif LLH_1_REnd == "On":
        show LLH_1_RedEnd_On at Position(xpos = 1010, xanchor = 0, ypos = 810, yanchor = 0)
    
    #Redraw While Nodes ***************************************************************************
    hide LLH_1_Red_While_Node_Off
    hide LLH_1_Red_While_Node_On
    hide LLH_1_Blue_While_Node_Off
    hide LLH_1_Blue_While_Node_On
    
    image LLH_1_Red_While_Node_Off = "r_while_off.png"
    image LLH_1_Red_While_Node_On = "r_while_on.png"
    image LLH_1_Blue_While_Node_Off = "b_while_off.png"
    image LLH_1_Blue_While_Node_On = "b_while_on.png"
    
    if LLH_1_RWhileNode == "Off":
        show LLH_1_Red_While_Node_Off at Position(xpos = 898, xanchor = 0, ypos = 648, yanchor = 0)
    elif LLH_1_RWhileNode == "On":
        show LLH_1_Red_While_Node_On at Position(xpos = 898, xanchor = 0, ypos = 648, yanchor = 0)
        
    if LLH_1_BWhileNode == "Off":
        show LLH_1_Blue_While_Node_Off at Position(xpos = 898, xanchor = 0, ypos = 719, yanchor = 0)
    elif LLH_1_BWhileNode == "On":
        show LLH_1_Blue_While_Node_On at Position(xpos = 898, xanchor = 0, ypos = 719, yanchor = 0)
    
    #*********************************************************
    #********************* redraw gates **********************
    #*********************************************************  
    hide LLH_1_tile52
    hide LLH_1_tile53
    hide LLH_1_tile54
    hide LLH_1_tile55
    hide LLH_1_tile56
    hide LLH_1_tile57
    hide LLH_1_tile58
    hide LLH_1_tile59
    show LLH_1_tile52 at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
    show LLH_1_tile53 at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
    show LLH_1_tile54 at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
    show LLH_1_tile55 at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
    show LLH_1_tile56 at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
    show LLH_1_tile57 at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
    show LLH_1_tile58 at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
    show LLH_1_tile59 at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)    

#win conditions ********
    if (else1in1 == True or else2in1 == True) and ifGin2 == True and ifBGin3 == True and ifRGin4 == True and ifBin5 == True and whileRBin6 == True and (else1in7 == True or else2in7 == True) and ifRin8 == True:
        image LLH_1_ifR = "R_if.png"
        show LLH_1_ifR at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)
        image LLH_1_ifG = "G_if.png"
        show LLH_1_ifG at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
        image LLH_1_ifB = "B_if.png"
        show LLH_1_ifB at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
        image LLH_1_ifRG = "RG_if.png"
        show LLH_1_ifRG at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
        image LLH_1_ifBG = "BG_if.png"
        show LLH_1_ifBG at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
        image LLH_1_else1 = "G_else.png"
        show LLH_1_else1 at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
        image LLH_1_else2 = "G_else.png"
        show LLH_1_else2 at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
        image LLH_1_whileRB = "RB_while.png"
        show LLH_1_whileRB at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)

        image LLH_1_ifRBorder = "placeholder3.png"
        show LLH_1_ifRBorder at Position(xpos = 1385, xanchor = 0, ypos = 635, yanchor = 0)
        image LLH_1_ifGBorder = "placeholder3.png"
        show LLH_1_ifGBorder at Position(xpos = 1515, xanchor = 0, ypos = 635, yanchor = 0)
        image LLH_1_ifBBorder = "placeholder3.png"
        show LLH_1_ifBBorder at Position(xpos = 1645, xanchor = 0, ypos = 635, yanchor = 0)
        image LLH_1_ifRGBorder = "placeholder3.png"
        show LLH_1_ifRGBorder at Position(xpos = 1435, xanchor = 0, ypos = 780, yanchor = 0)
        image LLH_1_ifBGBorder = "placeholder3.png"
        show LLH_1_ifBGBorder at Position(xpos = 1575, xanchor = 0, ypos = 780, yanchor = 0)
        image LLH_1_elseBorder = "placeholder3.png"
        show LLH_1_elseBorder at Position(xpos = 1575, xanchor = 0, ypos = 490, yanchor = 0)
        image LLH_1_whileRBBorder = "placeholder3.png"
        show LLH_1_whileRBBorder at Position(xpos = 1435, xanchor = 0, ypos = 490, yanchor = 0)
        
        "You Win!"
        jump loopLogic_hard1

#lose conditions ********
    if attempts == 0:
        hide LLH_1_colorTile1
        hide LLH_1_colorTile2
        hide LLH_1_colorTile3
        hide LLH_1_colorTile4
        hide LLH_1_colorTile5
        hide LLH_1_colorTile6
        hide LLH_1_colorTile7
        hide LLH_1_colorTile8
        hide LLH_1_colorTile9
        hide LLH_1_colorTile10
        hide LLH_1_colorTile11
        hide LLH_1_colorTile12
        hide LLH_1_colorTile13
        hide LLH_1_colorTile14
        hide LLH_1_colorTile15
        hide LLH_1_colorTile16
        hide LLH_1_colorTile17
        hide LLH_1_colorTile18
        hide LLH_1_colorTile19
        hide LLH_1_colorTile20
        hide LLH_1_colorTile21
        hide LLH_1_colorTile22
        hide LLH_1_colorTile23
        hide LLH_1_colorTile24
        hide LLH_1_colorTile25
        hide LLH_1_colorTile26
        hide LLH_1_colorTile27
        hide LLH_1_colorTile28
        hide LLH_1_colorTile29
        hide LLH_1_colorTile30
        hide LLH_1_colorTile31
        hide LLH_1_colorTile32
        hide LLH_1_colorTile33
        hide LLH_1_colorTile34
        hide LLH_1_colorTile35
        hide LLH_1_colorTile36
        hide LLH_1_colorTile37
        hide LLH_1_colorTile38
        hide LLH_1_colorTile39
        hide LLH_1_colorTile40
        hide LLH_1_colorTile41
        hide LLH_1_colorTile42
        hide LLH_1_colorTile43
        hide LLH_1_colorTile44
        hide LLH_1_colorTile45
        hide LLH_1_colorTile46
        hide LLH_1_colorTile47
        hide LLH_1_colorTile48
        hide LLH_1_colorTile49
        hide LLH_1_colorTile50
        hide LLH_1_colorTile51
        hide LLH_1_colorTile52
        hide LLH_1_colorTile53
        hide LLH_1_colorTile54
        hide LLH_1_colorTile55
        hide LLH_1_colorTile56
        hide LLH_1_colorTile57
        hide LLH_1_colorTile58
        hide LLH_1_colorTile59
        hide LLH_1_colorTile60
        hide LLH_1_colorTile61
        hide LLH_1_colorTile62
        hide LLH_1_colorTile63
        hide LLH_1_colorTile64
        hide LLH_1_colorTile65
        hide LLH_1_colorTile66
        hide LLH_1_colorTile67
        hide LLH_1_colorTile68
        hide LLH_1_colorTile69
        hide LLH_1_colorTile70
        hide LLH_1_colorTile71
        hide LLH_1_colorTile72
        hide LLH_1_colorTile73
        hide LLH_1_colorTile74
        hide LLH_1_colorTile75
        hide LLH_1_colorTile76
        hide LLH_1_colorTile77
        hide LLH_1_colorTile78
        hide LLH_1_colorTile79
        hide LLH_1_colorTile80
        hide LLH_1_colorTile81
        hide LLH_1_colorTile82
        hide LLH_1_colorTile83
        hide LLH_1_colorTile84
        hide LLH_1_colorTile85
        hide LLH_1_colorTile86
        hide LLH_1_colorTile87
        hide LLH_1_colorTile88
        hide LLH_1_colorTile89
        hide LLH_1_colorTile90
        hide LLH_1_colorTile91
        hide LLH_1_colorTile92
        hide LLH_1_colorTile93
        hide LLH_1_colorTile94
        hide LLH_1_colorTile95
        hide LLH_1_colorTile96
        hide LLH_1_colorTile97
        hide LLH_1_colorTile98
        hide LLH_1_colorTile99
        hide LLH_1_colorTile100
        hide LLH_1_colorTile101
        hide LLH_1_colorTile102
        hide LLH_1_colorTile103 
        hide LLH_1_colorTile104
        hide LLH_1_colorTile105 
        hide LLH_1_colorTile106
        hide LLH_1_colorTile107
        hide LLH_1_colorTile108
        hide LLH_1_colorTile109
        hide LLH_1_colorTile110
        hide LLH_1_colorTile111 
        hide LLH_1_colorTile112
        hide LLH_1_colorTile113
        hide LLH_1_colorTile114
        hide LLH_1_colorTile115
        hide LLH_1_colorTile116 
        hide LLH_1_colorTile117
        hide LLH_1_colorTile118
        hide LLH_1_colorTile119
        hide LLH_1_colorTile120
        hide LLH_1_colorTile121
        hide LLH_1_colorTile122
        hide LLH_1_colorTile123
        hide LLH_1_colorTile124
        hide LLH_1_colorTile125
        hide LLH_1_colorTile126
        hide LLH_1_colorTile127
        hide LLH_1_colorTile128
        hide LLH_1_colorTile129
        hide LLH_1_colorTile130
        hide LLH_1_colorTile131
        hide LLH_1_colorTile132

        hide LLH_1_WNode1
        hide LLH_1_WNode2
        hide LLH_1_WNode3
        hide LLH_1_WNode4
        hide LLH_1_WNode5
        hide LLH_1_RNode1
        hide LLH_1_RNode2
        hide LLH_1_RNode3
        hide LLH_1_RNode4
        hide LLH_1_RNode5
        hide LLH_1_GNode1
        hide LLH_1_GNode2
        hide LLH_1_GNode3
        hide LLH_1_GNode4
        hide LLH_1_GNode5
        hide LLH_1_BNode1
        hide LLH_1_BNode2
        hide LLH_1_BNode3
        hide LLH_1_BNode4
        hide LLH_1_BNode5
    
        hide LLH_1_BlueEnd1_Off
        hide LLH_1_BlueEnd2_Off
        hide LLH_1_GreenEnd1_Off
        hide LLH_1_GreenEnd2_Off
        hide LLH_1_RedEnd_Off
        hide LLH_1_BlueEnd1_On
        hide LLH_1_BlueEnd2_On
        hide LLH_1_GreenEnd1_On
        hide LLH_1_GreenEnd2_On
        hide LLH_1_RedEnd_On

        hide LLH_1_Red_While_Node_Off
        hide LLH_1_Red_While_Node_On
        hide LLH_1_Blue_While_Node_Off
        hide LLH_1_Blue_While_Node_On
    
        show LLH_1_ifR at Position(xpos = gate8x, xanchor = 0, ypos = gate8y, yanchor = 0)
        show LLH_1_ifG at Position(xpos = gate2x, xanchor = 0, ypos = gate2y, yanchor = 0)
        show LLH_1_ifB at Position(xpos = gate5x, xanchor = 0, ypos = gate5y, yanchor = 0)
        show LLH_1_ifRG at Position(xpos = gate4x, xanchor = 0, ypos = gate4y, yanchor = 0)
        show LLH_1_ifBG at Position(xpos = gate3x, xanchor = 0, ypos = gate3y, yanchor = 0)
        show LLH_1_else1 at Position(xpos = gate1x, xanchor = 0, ypos = gate1y, yanchor = 0)
        show LLH_1_else2 at Position(xpos = gate7x, xanchor = 0, ypos = gate7y, yanchor = 0)
        show LLH_1_whileRB at Position(xpos = gate6x, xanchor = 0, ypos = gate6y, yanchor = 0)
        
        show LLH_1_ifRBorder at Position(xpos = 1385, xanchor = 0, ypos = 635, yanchor = 0)
        show LLH_1_ifGBorder at Position(xpos = 1515, xanchor = 0, ypos = 635, yanchor = 0)
        show LLH_1_ifBBorder at Position(xpos = 1645, xanchor = 0, ypos = 635, yanchor = 0)
        show LLH_1_ifRGBorder at Position(xpos = 1435, xanchor = 0, ypos = 780, yanchor = 0)
        show LLH_1_ifBGBorder at Position(xpos = 1575, xanchor = 0, ypos = 780, yanchor = 0)
        show LLH_1_elseBorder at Position(xpos = 1575, xanchor = 0, ypos = 490, yanchor = 0)
        show LLH_1_whileRBBorder at Position(xpos = 1435, xanchor = 0, ypos = 490, yanchor = 0)
        
        "You lose. Try again!"
        jump loopLogic_hard1
    
    jump gamefile_llh1

screen loopLogicHard_1Scr:
    
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
                drag_name "while_RB_gate_return"
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
                drag_name "if_RG_gate_return"
                child "placeholder3.png"
                draggable False
                xpos 1435 ypos 780

            drag:
                drag_name "if_BG_gate_return"
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
                drag_name "if_RG_gate"
                child "RG_if.png"
                droppable False
                dragged gate_dragged
                xpos ifRGx ypos ifRGy
                
            drag:
                drag_name "if_BG_gate"
                child "BG_if.png"
                droppable False
                dragged gate_dragged
                xpos ifBGx ypos ifBGy       

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
                drag_name "while_RB_gate"
                child "RB_while.png"
                droppable False
                dragged gate_dragged
                xpos whileRBx ypos whileRBy  
